-- Blended ROI
SELECT
  month,
  SUM(revenue) / SUM(spend) AS blended_roi
FROM Marketing_campaigns_cleaned_dataset
GROUP BY month;

-- ROI by channel
SELECT
  channel,
  SUM(revenue) / SUM(spend) AS channel_roi
FROM Marketing_campaigns_cleaned_dataset
GROUP BY channel;
