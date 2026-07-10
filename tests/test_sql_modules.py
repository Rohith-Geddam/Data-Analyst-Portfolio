from datetime import date
from pathlib import Path
from statistics import stdev

import duckdb
import pytest


ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def connection() -> duckdb.DuckDBPyConnection:
    database = duckdb.connect()
    yield database
    database.close()


def run_sql(
    connection: duckdb.DuckDBPyConnection, relative_path: str
) -> list[list[tuple[object, ...]]]:
    sql = (ROOT / relative_path).read_text(encoding="utf-8")
    results = []
    for statement in sql.split(";"):
        if statement.strip():
            results.append(connection.execute(statement).fetchall())
    return results


def test_fintech_cleaning_normalizes_customer_records(
    connection: duckdb.DuckDBPyConnection,
) -> None:
    connection.execute(
        """
        CREATE TABLE Fintech_Subscriptions_Data_raw (
          user_id INTEGER,
          plan VARCHAR,
          signup_date DATE,
          churn_date DATE,
          monthly_fee DOUBLE,
          country VARCHAR
        )
        """
    )
    connection.executemany(
        "INSERT INTO Fintech_Subscriptions_Data_raw VALUES (?, ?, ?, ?, ?, ?)",
        [
            (1, "Basic", date(2024, 1, 1), date(2024, 2, 1), 100, "US"),
            (2, "Basic", date(2024, 1, 10), date(2024, 1, 1), None, None),
            (3, None, date(2024, 1, 1), None, 50, "India"),
        ],
    )

    run_sql(
        connection,
        "Fintech Subscription Retention/SQL/Dataset Cleaning.sql",
    )

    rows = connection.execute(
        """
        SELECT user_id, plan, churn_date, monthly_fee, country, is_churned,
               customer_lifetime_days
        FROM Fintech_subscriptions_cleaned_dataset
        ORDER BY user_id
        """
    ).fetchall()

    assert rows[0] == (1, "Basic", date(2024, 2, 1), 100, "US", 1, 31)
    assert rows[1][:6] == (2, "Basic", None, 100, "Unknown", 0)
    assert rows[1][6] > 0
    assert rows[2][:6] == (3, "Unknown", None, 50, "India", 0)


def test_fintech_analysis_calculates_churn_and_revenue_at_risk(
    connection: duckdb.DuckDBPyConnection,
) -> None:
    connection.execute(
        """
        CREATE TABLE Fintech_subscriptions_cleaned_dataset (
          plan VARCHAR,
          monthly_fee DOUBLE,
          is_churned INTEGER
        )
        """
    )
    connection.executemany(
        "INSERT INTO Fintech_subscriptions_cleaned_dataset VALUES (?, ?, ?)",
        [
            ("Basic", 100, 1),
            ("Basic", 80, 0),
            ("Standard", 200, 1),
        ],
    )

    churn_by_plan, revenue_at_risk = run_sql(
        connection,
        "Fintech Subscription Retention/SQL/Analysis.sql",
    )

    assert sorted(churn_by_plan) == [
        ("Basic", 2, 1, 0.5),
        ("Standard", 1, 1, 1.0),
    ]
    assert sorted(revenue_at_risk) == [
        ("Basic", 100),
        ("Standard", 200),
    ]


def test_investment_cleaning_prepares_monthly_returns(
    connection: duckdb.DuckDBPyConnection,
) -> None:
    connection.execute(
        """
        CREATE TABLE Investment_returns_Data_raw (
          date DATE,
          portfolio_return DOUBLE,
          benchmark_return DOUBLE,
          portfolio_value DOUBLE
        )
        """
    )
    connection.executemany(
        "INSERT INTO Investment_returns_Data_raw VALUES (?, ?, ?, ?)",
        [
            (date(2024, 1, 5), 0.1, 0.05, 1000),
            (date(2024, 2, 5), None, -0.01, 980),
        ],
    )

    run_sql(
        connection,
        "Investment Performance Monitor/SQL/Dataset cleaning.sql",
    )

    rows = connection.execute(
        """
        SELECT trade_date, portfolio_return, month
        FROM investment_returns_cleaned_dataset
        ORDER BY trade_date
        """
    ).fetchall()

    assert rows == [
        (date(2024, 1, 5), 0.1, date(2024, 1, 1)),
        (date(2024, 2, 5), 0.0, date(2024, 2, 1)),
    ]


def test_investment_analysis_calculates_averages_and_volatility(
    connection: duckdb.DuckDBPyConnection,
) -> None:
    connection.execute(
        """
        CREATE TABLE investment_returns_cleaned_dataset (
          month DATE,
          portfolio_return DOUBLE
        )
        """
    )
    returns = [0.1, 0.0, -0.2]
    connection.executemany(
        "INSERT INTO investment_returns_cleaned_dataset VALUES (?, ?)",
        [
            (date(2024, 1, 1), returns[0]),
            (date(2024, 1, 1), returns[1]),
            (date(2024, 2, 1), returns[2]),
        ],
    )

    monthly_returns, volatility = run_sql(
        connection,
        "Investment Performance Monitor/SQL/Analysis.sql",
    )

    assert sorted(monthly_returns) == [
        (date(2024, 1, 1), 0.05),
        (date(2024, 2, 1), -0.2),
    ]
    assert volatility[0][0] == pytest.approx(stdev(returns))


def test_marketing_cleaning_clamps_invalid_financial_values(
    connection: duckdb.DuckDBPyConnection,
) -> None:
    connection.execute(
        """
        CREATE TABLE Marketing_campaigns_Data_raw (
          date DATE,
          channel VARCHAR,
          spend DOUBLE,
          revenue DOUBLE,
          campaign_id INTEGER
        )
        """
    )
    connection.executemany(
        "INSERT INTO Marketing_campaigns_Data_raw VALUES (?, ?, ?, ?, ?)",
        [
            (date(2024, 1, 5), "Email", 100, 250, 1),
            (date(2024, 1, 6), "Search", -10, 50, 2),
            (date(2024, 2, 1), "Social", None, -20, 3),
        ],
    )

    run_sql(
        connection,
        "Marketing ROI & Budget Reallocation Analysis/SQL/Dataset cleaning.sql",
    )

    rows = connection.execute(
        """
        SELECT campaign_id, spend, revenue, roi, month
        FROM Marketing_campaigns_cleaned_dataset
        ORDER BY campaign_id
        """
    ).fetchall()

    assert rows == [
        (1, 100, 250, 2.5, date(2024, 1, 1)),
        (2, 0, 50, None, date(2024, 1, 1)),
        (3, 0, 0, None, date(2024, 2, 1)),
    ]


def test_marketing_analysis_uses_weighted_roi_and_handles_zero_spend(
    connection: duckdb.DuckDBPyConnection,
) -> None:
    connection.execute(
        """
        CREATE TABLE Marketing_campaigns_cleaned_dataset (
          month DATE,
          channel VARCHAR,
          spend DOUBLE,
          revenue DOUBLE
        )
        """
    )
    connection.executemany(
        "INSERT INTO Marketing_campaigns_cleaned_dataset VALUES (?, ?, ?, ?)",
        [
            (date(2024, 1, 1), "Email", 100, 200),
            (date(2024, 1, 1), "Search", 200, 100),
            (date(2024, 2, 1), "Email", 50, 150),
            (date(2024, 2, 1), "Organic", 0, 25),
        ],
    )

    monthly_roi, channel_roi = run_sql(
        connection,
        "Marketing ROI & Budget Reallocation Analysis/SQL/Analysis.sql",
    )

    assert sorted(monthly_roi) == [
        (date(2024, 1, 1), 1.0),
        (date(2024, 2, 1), 3.5),
    ]
    channel_results = dict(channel_roi)
    assert channel_results["Email"] == pytest.approx(350 / 150)
    assert channel_results["Search"] == 0.5
    assert channel_results["Organic"] is None


def test_risk_cleaning_normalizes_claim_amounts_and_years(
    connection: duckdb.DuckDBPyConnection,
) -> None:
    connection.execute(
        """
        CREATE TABLE Insurance_claims_Data_raw (
          claim_id INTEGER,
          risk_category VARCHAR,
          claim_amount DOUBLE,
          claim_date DATE,
          settled BOOLEAN
        )
        """
    )
    connection.executemany(
        "INSERT INTO Insurance_claims_Data_raw VALUES (?, ?, ?, ?, ?)",
        [
            (1, "Auto", 1000, date(2023, 12, 31), True),
            (2, "Fraud", -50, date(2024, 1, 1), False),
            (3, "Medical", None, date(2024, 6, 1), True),
        ],
    )

    run_sql(
        connection,
        "Risk Modelling & Cost Concentration Analysis/SQL/Dataset cleaning.sql",
    )

    rows = connection.execute(
        """
        SELECT claim_id, claim_amount, claim_year
        FROM Insurance_claims_cleaned_dataset
        ORDER BY claim_id
        """
    ).fetchall()

    assert rows == [(1, 1000, 2023), (2, 0, 2024), (3, 0, 2024)]


def test_risk_analysis_calculates_category_costs_and_pareto_curve(
    connection: duckdb.DuckDBPyConnection,
) -> None:
    connection.execute(
        """
        CREATE TABLE Insurance_claims_cleaned_dataset (
          risk_category VARCHAR,
          claim_amount DOUBLE
        )
        """
    )
    connection.executemany(
        "INSERT INTO Insurance_claims_cleaned_dataset VALUES (?, ?)",
        [
            ("Auto", 60),
            ("Auto", 30),
            ("Medical", 10),
        ],
    )

    category_costs, pareto_curve = run_sql(
        connection,
        "Risk Modelling & Cost Concentration Analysis/SQL/Analysis.sql",
    )

    assert sorted(category_costs) == [("Auto", 90), ("Medical", 10)]
    assert pareto_curve == [(60, 0.6), (30, 0.9), (10, 1.0)]
