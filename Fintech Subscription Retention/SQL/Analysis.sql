-- Churn by plan
SELECT
  plan,
  COUNT(*) AS users,
  SUM(is_churned) AS churned_users,
  safe_divide(SUM(is_churned), COUNT(*)) AS churn_rate
FROM Fintech_subscriptions_cleaned_dataset
GROUP BY plan;

-- Revenue at risk
SELECT
  plan,
  SUM(monthly_fee) AS monthly_revenue_at_risk
FROM Fintech_subscriptions_cleaned_dataset
WHERE is_churned = 1
GROUP BY plan;
