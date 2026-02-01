## Subscription-based Fintech businesses rely heavily on recurring revenue. Even small increases in churn can materially impact Monthly Recurring Revenue (MRR) and long-term customer lifetime value.

This project is created to simulate how a data analyst would:

Diagnose churn drivers

Quantify revenue risk

Support retention decisions for leadership

## Business Problem

Leadership needed answers to three questions:

Which customers are churning?

Which subscription plans are most exposed?

How much revenue is realistically at risk?

## Dataset Overview

Synthetic subscription data (users, plans, churn, revenue)

Intentionally messy: Missing plans and countries, Invalid churn dates, Null revenue values




This reflects real production data, not curated datasets.

# Step-by-Step Approach
## Step 1: Data Cleaning (SQL)

Standardized categorical fields (plan, country)

Validated lifecycle dates

Imputed missing revenue conservatively

Preserved records to avoid bias



## Step 2: Feature Engineering

Created churn flag

Calculated customer lifetime

Derived revenue exposure

## Step 3: Analysis

Aggregated churn by plan and geography

Calculated revenue at risk

Prioritized segments by financial impact



## Step 4: Dashboarding

Executive KPI view

Diagnostic deep-dive

Focused on clarity, not metric overload



## Key Decisions Made

Avoided dropping rows with missing values

Used weighted metrics instead of averages

Focused on monthly aggregation for executive readability

Explicitly documented assumptions and limitations



## Outcome

Provided a clear, financially grounded prioritization of retention initiatives with quantified revenue impact.
