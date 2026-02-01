# Risk Modelling & Cost Concentration Analysis

In risk-heavy industries, costs are often driven by a small subset of high-impact events.
This project demonstrates how analytics can identify **cost concentration patterns**
and support **targeted risk mitigation strategies**.

---

## Business Problem
Leadership needed to understand:

- Whether claims costs were broadly distributed or highly concentrated
- Which risk categories drive the majority of losses
- What realistic savings opportunities exist without operational disruption

---

## Dataset Overview
- Synthetic insurance claims data
- Includes:
  - Missing claim amounts
  - Large cost outliers
  - Multiple risk categories

The dataset reflects real claims environments with skewed cost distributions.

---

## Step-by-Step Approach

### Step 1: Data Cleaning (SQL)
- Standardized claim amounts
- Handled missing values conservatively
- Created year-level aggregation fields

📁 `sql/cleaning.sql`

---

### Step 2: Cost Aggregation
- Aggregated claims by risk category
- Calculated total cost contribution
- Prepared data for concentration analysis

---

### Step 3: Pareto & Concentration Analysis
- Ranked claims by cost
- Calculated cumulative cost contribution
- Applied the 80/20 principle to identify high-impact segments

📁 `sql/analysis.sql`

---

### Step 4: Dashboarding
- Executive KPI cards (Total Cost, Savings Opportunity)
- Cost by risk category visualization
- Pareto curve highlighting cost concentration

📁 `Dashboards/`

---

## Key Decisions Made
- Focused on prioritization rather than exhaustive modeling
- Used conservative savings assumptions
- Avoided predictive claims modeling to maintain credibility
- Emphasized financial impact over technical complexity

---

## Outcome
Equipped leadership with a clear, financially credible framework to focus risk mitigation
efforts where they matter most.
