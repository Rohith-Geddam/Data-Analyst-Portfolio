CREATE TABLE Fintech_subscriptions_cleaned_dataset AS
SELECT
  user_id,
  COALESCE(plan, 'Unknown') AS plan,
  signup_date,
  CASE
    WHEN churn_date < signup_date THEN NULL
    ELSE churn_date
  END AS churn_date,
  COALESCE(
    monthly_fee,
    MEDIAN(monthly_fee) OVER (PARTITION BY plan)
  ) AS monthly_fee,
  COALESCE(country, 'Unknown') AS country,
  CASE WHEN churn_date IS NOT NULL THEN 1 ELSE 0 END AS is_churned,
  DATEDIFF(
    day,
    signup_date,
    COALESCE(churn_date, CURRENT_DATE)
  ) AS customer_lifetime_days
FROM Fintech_Subscriptions_Data_raw;
