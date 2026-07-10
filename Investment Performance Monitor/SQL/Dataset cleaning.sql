CREATE TABLE investment_returns_cleaned_dataset AS
SELECT
  date AS trade_date,
  COALESCE(portfolio_return, 0) AS portfolio_return,
  benchmark_return,
  portfolio_value,
  month_start(date) AS month
FROM Investment_returns_Data_raw;
