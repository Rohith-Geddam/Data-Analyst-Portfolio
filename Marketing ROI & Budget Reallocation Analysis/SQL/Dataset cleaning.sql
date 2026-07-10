CREATE TABLE Marketing_campaigns_cleaned_dataset AS
WITH normalized AS (
  SELECT
    date AS campaign_date,
    channel,
    campaign_id,
    GREATEST(COALESCE(spend, 0), 0) AS spend,
    GREATEST(COALESCE(revenue, 0), 0) AS revenue
  FROM Marketing_campaigns_Data_raw
)
SELECT
  campaign_date,
  channel,
  campaign_id,
  spend,
  revenue,
  CASE
    WHEN spend > 0 THEN revenue / spend
    ELSE NULL
  END AS roi,
  DATE_TRUNC('month', campaign_date) AS month
FROM normalized;
