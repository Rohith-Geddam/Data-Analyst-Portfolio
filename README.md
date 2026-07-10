# Data Analytics Portfolio

This repository contains four end-to-end analytics projects designed to simulate
real-world workflows used in Finance, Fintech, Marketing Analytics, and Risk Management teams.

Each project follows a consistent professional pipeline:

Raw / Synthetic Data  
→ Data Cleaning & Transformation (SQL / Logic)  
→ Business Analysis  
→ Executive Dashboards (Power BI)  
→ Actionable Recommendations

## Projects Included

1. Fintech Subscription Retention & LTV Optimization
2. Investment Performance Monitor  
3. Marketing ROI & Budget Reallocation Analysis  
4. Risk Modelling & Cost Concentration Analysis

All dashboards are designed to support effective business decision-making,
with a focus on financial impact rather than technical complexity.

## Tools & Skills Demonstrated
- SQL-based data cleaning and aggregation
- KPI design and financial metric validation
- Power BI dashboard design (Executive & Analytical views)
- Business recommendations based on the data

## Shared SQL Utilities

The project SQL uses reusable DuckDB macros for common transformations:

- `clamp_non_negative` normalizes missing or negative financial values
- `month_start` creates consistent monthly reporting buckets
- `safe_divide` prevents division-by-zero errors in calculated metrics

Run `SQL/Shared Utilities.sql` once in the current database session before running
any project cleaning or analysis script.

------

# Overview of Projects

# 1.Fintech Subscription Retention & LTV Optimization

## Business Context
A mid-sized Fintech company experienced rising customer churn, creating pressure on
Monthly Recurring Revenue (MRR) and long-term unit economics. Leadership required a
clear, actionable view of churn concentration and revenue exposure to prioritize
retention initiatives.

## Problem Statement
The analysis was designed to answer three executive-level questions:
- Which customer segments are driving churn?
- Which subscription plans pose the highest revenue risk?
- Where can targeted retention efforts deliver the highest financial impact?

## Why This Matters
In subscription-based businesses, even marginal churn improvements (1–2%) can
translate into significant annual revenue protection. Without understanding churn
concentration, retention investments risk being misallocated.

## Data & Key Metrics
The analysis focuses on financially decision-relevant metrics:
- Total Users
- Monthly Recurring Revenue (MRR)
- Churn Rate
- Average Customer Lifetime
- Revenue at Risk

## Analytical Approach
1. Cleaned and standardized subscription-level data to ensure consistency in dates,
   revenue fields, and plan definitions.
2. Aggregated churn, lifetime, and revenue metrics at plan and geographic levels.
3. Designed two dashboards:
   - **Executive Overview** for leadership monitoring
   - **Deep Dive Analysis** for diagnostic investigation
4. Translated analytical findings into quantified retention opportunities.

## Dashboards
### Executive Overview
- KPI cards for Users, MRR, and Churn Rate
- Monthly churn trend to highlight directional risk
  
<img width="1293" height="732" alt="Dashboard 1 - KPI cards" src="https://github.com/user-attachments/assets/036fa337-4560-4806-a9e2-3dd146cce8ba" />

### Deep Dive Analysis
- Churn rate by subscription plan
- Average customer lifetime by plan
- Revenue at risk by plan
- Country-level churn distribution

<img width="1293" height="733" alt="Dashboard 1- deep dive" src="https://github.com/user-attachments/assets/e0f3c800-9c33-44a3-965c-fdde48ad8ffe" />

## Key Insight
Churn is disproportionately concentrated among Basic-tier subscribers, who also
represent a significant share of revenue exposure. This indicates that churn is driven
less by isolated behavior and more by structural engagement challenges within the
entry-level offering.

## Recommendation
A targeted onboarding and early engagement strategy focused on Basic-tier users
could realistically reduce churn by approximately 1–2%, protecting a meaningful
portion of annual recurring revenue.

## Assumptions & Constraints
- The analysis uses synthetic data due to lack of access to proprietary customer records.
- Churn is defined as account termination and does not distinguish between voluntary
  and involuntary churn.
- Revenue attribution assumes equal contribution across active users within a plan.
- Insights are correlation-based; causal drivers would require controlled experiments
  or A/B testing.
- Metrics are analyzed at a monthly aggregation level to prioritize executive clarity.

## Outcome
This project provides leadership with a clear prioritization framework for retention
initiatives, balancing analytical rigor with executive interpretability.

-------

# 2.Investment Performance Monitor

## Business Context
Investment performance was historically evaluated using absolute returns,
limiting leadership’s ability to assess whether returns were achieved efficiently
relative to risk.

## Problem Statement
The objective was to provide a concise, financially correct view of portfolio
performance that accounts for volatility and risk, enabling more informed
investment oversight.

## Why This Matters
Returns without risk context can be misleading. Risk-adjusted performance metrics
are essential for comparing strategies and ensuring capital is deployed efficiently.

## Data & Key Metrics
- Portfolio Return %
- Volatility %
- Sharpe Ratio
- Monthly Portfolio Returns

## Analytical Approach
1. Evaluated portfolio returns at a monthly granularity to avoid aggregation bias.
2. Incorporated volatility to contextualize performance risk.
3. Used Sharpe Ratio to assess return efficiency relative to risk.
4. Designed an executive dashboard prioritizing clarity over technical complexity.

## Dashboard Overview
- KPI cards for portfolio return, volatility, and Sharpe ratio
- Monthly portfolio returns trend (non-aggregated)

<img width="1137" height="642" alt="Screenshot 2026-01-29 120148" src="https://github.com/user-attachments/assets/bc1dbf2a-7485-403c-b88b-cc4ec0a6b8d3" />

## Key Insight
The portfolio demonstrates strong risk-adjusted performance, with a Sharpe ratio
above 1.5, indicating efficient return generation relative to observed volatility.

## Assumptions & Constraints
- Returns are analyzed at a monthly frequency, limiting visibility into intramonth volatility.
- Sharpe Ratio assumes normally distributed returns and does not capture tail risk.
- No benchmark index comparison was included due to data availability constraints.
- Transaction costs, taxes, and liquidity constraints were not modeled.

## Outcome
Provides leadership with a financially sound, interpretable view of portfolio health,
supporting informed performance evaluation rather than raw return comparisons.

-----

# 3.Marketing ROI & Budget Reallocation Analysis

## Business Context
Marketing expenditure was increasing, but leadership lacked visibility into which
channels were driving meaningful returns versus inefficient spend.

## Problem Statement
The objective was to evaluate marketing efficiency using correctly weighted ROI
metrics and identify data-backed budget reallocation opportunities.

## Solves-
Misallocated marketing budgets can silently erode profitability.
Accurate ROI measurement is critical for scaling growth efficiently.

## Data & Key Metrics
- Total Marketing Spend
- Revenue Attributed to Marketing
- Blended ROI (Revenue / Spend)
- Channel-Level ROI

## Analytical Approach
1. Calculated blended ROI to ensure spend-weighted performance assessment.
2. Compared spend versus revenue to identify misalignment across channels.
3. Analyzed monthly blended ROI trends to assess stability over time.
4. Translated insights into actionable budget optimization recommendations.

## Dashboard Overview
- Executive KPI summary (Spend, Revenue, Blended ROI)
- ROI by marketing channel
- Spend versus revenue comparison
- Monthly blended ROI trend

<img width="1297" height="737" alt="Screenshot 2026-01-29 172948" src="https://github.com/user-attachments/assets/75d7ba9d-194a-44d7-8f38-a2319b411d4d" />

## Key Insight
Email and Affiliate channels deliver materially higher ROI at lower spend.
Underperforming paid channels consume a disproportionate share of budget relative
to their revenue contribution.

## Recommendation
Reallocating approximately 15–20% of budget from lower-performing paid channels
to higher-ROI channels could improve blended ROI by ~0.3.

## Assumptions & Constraints
- Attribution assumes simplified last-touch logic and does not model multi-touch journeys.
- Channel overlap and cannibalization effects were not evaluated.
- ROI calculations assume linear scalability and do not account for diminishing returns.
- Insights indicate correlation rather than causal lift.

## Outcome
Delivers a clear, financially grounded framework for marketing budget optimization.

-----

# 4.Risk Modelling & Cost Concentration Analysis

## Business Context
Claims costs were rising, but leadership lacked clarity on whether losses were broadly
distributed or concentrated among a small subset of risks.

## Problem Statement
The objective was to assess cost concentration patterns and estimate a realistic
savings opportunity through targeted risk mitigation.

## Solves-
In insurance and risk-heavy environments, a small percentage of claims often drive
the majority of losses. Identifying these patterns enables focused intervention.

## Data & Key Metrics
- Total Annual Claims Cost
- Cost by Risk Category
- Pareto (80/20) Cost Concentration
- Estimated Savings Opportunity

## Analytical Approach
1. Aggregated claims costs by risk category.
2. Applied Pareto analysis to assess concentration of losses.
3. Estimated potential savings using conservative, defensible assumptions.
4. Designed an executive dashboard emphasizing prioritization over exhaustiveness.

## Dashboard Overview
- Executive KPIs for total cost and savings opportunity
- Cost by risk category visualization
- Pareto curve highlighting concentration

<img width="1362" height="773" alt="Screenshot 2026-01-29 172710" src="https://github.com/user-attachments/assets/1f8d30bf-a998-4846-b015-3cc7c3252369" />

## Key Insight
Approximately 10–15% of claims account for the majority of losses,
indicating a strong opportunity for targeted risk controls.

## Recommendation
Focusing mitigation efforts on high-cost claim categories could realistically reduce
annual costs by ~$1.6–$1.8M without broad-based operational disruption.

## Assumptions & Constraints
- Claims data is aggregated and does not capture individual lifecycle complexity.
- Cost concentration assumes historical patterns remain relatively stable.
- Savings estimates are illustrative and conservative, not predictive.
- Regulatory and behavioral responses were not modeled.

## Outcome
Provides leadership with a focused, financially credible risk prioritization framework.

---

## Portfolio Takeaway

Across all four projects, the focus is on decision-supporting analytics rather than
tool demonstration. The portfolio build based on how analytics is practiced in real
organizations: working with imperfect data, making defensible assumptions, and
communicating insights clearly.
