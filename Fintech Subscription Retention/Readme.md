# Fintech Subscription Retention & LTV Optimization

Subscription-based Fintech businesses rely heavily on recurring revenue.
Even small increases in customer churn can materially impact Monthly Recurring Revenue
(MRR) and long-term customer lifetime value.

This project was created to simulate how a data analyst would diagnose churn drivers,
quantify revenue risk, and support retention decisions for leadership.

---

## Business Problem
Leadership needed clear, actionable answers to the following questions:

- Which customer segments are driving churn?
- Which subscription plans pose the highest revenue risk?
- Where can targeted retention efforts deliver the greatest financial impact?

---

## Dataset Overview
- Synthetic subscription-level customer data
- Includes:
  - Missing plan and country values
  - Invalid or incomplete churn dates
  - Null revenue fields

The dataset intentionally reflects real-world data imperfections rather than
idealized academic examples.

---

## Step-by-Step Approach

### Step 1: Data Cleaning (SQL)
- Standardized plan and country fields
- Validated customer lifecycle dates
- Handled missing revenue values conservatively
- Preserved records to avoid introducing bias

📁 `sql/cleaning.sql`

---

### Step 2: Feature Engineering
- Created churn flag
- Calculated customer lifetime in days
- Derived revenue exposure for churned customers

---

### Step 3: Analysis
- Aggregated churn metrics by plan and geography
- Estimated revenue at risk from churned users
- Prioritized customer segments by financial impact

📁 `sql/analysis.sql`

---

### Step 4: Dashboarding
- Executive overview dashboard with core KPIs
- Deep-dive dashboard for diagnostic analysis
- Designed for clarity and executive decision-making

📁 `Dashboards/`

---

## Key Decisions Made
- Avoided dropping records solely due to missing values
- Used weighted financial metrics instead of simple averages
- Focused on monthly aggregation for executive interpretability
- Explicitly documented assumptions and analytical constraints

---

## Outcome
Provided leadership with a clear, financially grounded framework to prioritize
retention initiatives, balancing analytical rigor with business usability.
