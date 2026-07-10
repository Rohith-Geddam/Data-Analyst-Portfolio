CREATE TABLE Marketing_campaigns_cleaned_dataset AS
SELECT
  date AS campaign_date,
  channel,
  campaign_id,
  clamp_non_negative(spend) AS spend,
  clamp_non_negative(revenue) AS revenue,
  safe_divide(
    clamp_non_negative(revenue),
    clamp_non_negative(spend)
  ) AS roi,
  month_start(date) AS month
FROM Marketing_campaigns_Data_raw;
