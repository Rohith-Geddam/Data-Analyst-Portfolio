CREATE OR REPLACE MACRO clamp_non_negative(input_value) AS
  GREATEST(COALESCE(input_value, 0), 0);

CREATE OR REPLACE MACRO month_start(input_date) AS
  DATE_TRUNC('month', input_date);

CREATE OR REPLACE MACRO safe_divide(numerator, denominator) AS
  numerator * 1.0 / NULLIF(denominator, 0);
