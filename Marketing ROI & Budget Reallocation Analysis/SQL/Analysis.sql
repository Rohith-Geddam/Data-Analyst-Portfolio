-- Blended ROI
SELECT
  month,
  SUM(revenue) / NULLIF(SUM(spend), 0) AS blended_roi
FROM Marketing_campaigns_cleaned_dataset
GROUP BY month;

-- ROI by channel
SELECT
  channel,
  SUM(revenue) / NULLIF(SUM(spend), 0) AS channel_roi
FROM Marketing_campaigns_cleaned_dataset
GROUP BY channel;
