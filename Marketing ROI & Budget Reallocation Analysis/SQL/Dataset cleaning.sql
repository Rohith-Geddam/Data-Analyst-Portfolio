CREATE TABLE Marketing_campaigns_cleaned_dataset AS
SELECT
  date AS campaign_date,
  channel,
  campaign_id,
  GREATEST(COALESCE(spend, 0), 0) AS spend,
  GREATEST(COALESCE(revenue, 0), 0) AS revenue,
  CASE
    WHEN spend > 0 THEN revenue / spend
    ELSE NULL
  END AS roi,
  DATE_TRUNC('month', date) AS month
FROM Marketing_campaigns_Data_raw;
