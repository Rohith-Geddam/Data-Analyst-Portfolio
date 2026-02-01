# Marketing ROI & Budget Reallocation Analysis

Marketing spend often increases faster than insight.
This project demonstrates how analytics can quantify marketing efficiency and guide
budget reallocation using **financially correct ROI metrics**.

---

## Business Problem
Leadership lacked clarity on:

- Which marketing channels generate the highest return
- Where spend is inefficient
- How to reallocate budget without increasing total spend

---

## Dataset Overview
- Synthetic campaign-level marketing data
- Includes:
  - Missing revenue values
  - Uneven spend distribution
  - Channel-level performance variability

This reflects real attribution and tracking challenges faced by marketing teams.

---

## Step-by-Step Approach

### Step 1: Data Cleaning (SQL)
- Handled missing and invalid spend/revenue values
- Standardized dates and campaign structure
- Preserved incomplete records to avoid channel bias

📁 `sql/cleaning.sql`

---

### Step 2: Metric Design
- Calculated **Blended ROI** using spend-weighted aggregation
- Avoided averaging ROI to maintain financial correctness
- Created channel-level efficiency metrics

---

### Step 3: Analysis
- Compared spend versus revenue by channel
- Evaluated monthly blended ROI stability
- Identified underperforming spend concentration

📁 `sql/analysis.sql`

---

### Step 4: Dashboarding
- Executive KPI summary (Spend, Revenue, Blended ROI)
- ROI by channel visualization
- Spend vs revenue comparison
- Monthly blended ROI trend

📁 `Dashboards/`

---

## Key Decisions Made
- Used blended ROI instead of simple averages
- Focused on spend-weighted performance
- Avoided complex attribution models to preserve clarity
- Translated insights into actionable budget guidance

---

## Outcome
Provided leadership with a financially grounded framework to reallocate marketing spend
and improve overall ROI without increasing total budget.

