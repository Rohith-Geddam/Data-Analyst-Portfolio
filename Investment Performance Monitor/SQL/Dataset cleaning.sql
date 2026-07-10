CREATE TABLE investment_returns_cleaned_dataset AS
SELECT
  date AS trade_date,
  portfolio_return,
  benchmark_return,
  portfolio_value,
  DATE_TRUNC('month', date) AS month
FROM Investment_returns_Data_raw;
