CREATE TABLE Insurance_claims_cleaned_dataset AS
SELECT
  claim_id,
  risk_category,
  claim_date,
  GREATEST(COALESCE(claim_amount, 0), 0) AS claim_amount,
  settled,
  EXTRACT(year FROM claim_date) AS claim_year
FROM Insurance_claims_Data_raw;
