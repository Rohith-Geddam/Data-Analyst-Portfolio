-- Monthly returns
SELECT
  month,
  AVG(portfolio_return) AS avg_return
FROM investment_returns_cleaned_dataset
GROUP BY month;

-- Volatility
SELECT
  STDDEV(portfolio_return) AS volatility
FROM investment_returns_cleaned_dataset
