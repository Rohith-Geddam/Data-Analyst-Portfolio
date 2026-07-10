-- Cost by risk category
SELECT
  risk_category,
  SUM(claim_amount) AS total_cost
FROM Insurance_claims_cleaned_dataset
GROUP BY risk_category;

-- Pareto preparation
SELECT
  claim_amount,
  safe_divide(
    SUM(claim_amount) OVER (ORDER BY claim_amount DESC),
    SUM(claim_amount) OVER ()
  ) AS cumulative_cost_pct
FROM Insurance_claims_cleaned_dataset;
