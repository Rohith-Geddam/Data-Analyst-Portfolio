# Investment Performance Monitor

Investment performance is often evaluated using absolute returns, which can be misleading
without understanding the risk taken to generate those returns.

This project was designed to demonstrate how an analyst evaluates portfolio performance
from a **risk-adjusted perspective**, enabling leadership to assess performance quality,
not just headline numbers.

---

## Business Problem
Leadership needed a concise and financially correct way to answer:

- Is the portfolio performing well relative to its risk?
- Are returns consistent or volatile over time?
- Can performance be monitored at an executive level without technical overload?

---

## Dataset Overview
- Synthetic daily portfolio return data
- Includes:
  - Missing return values
  - Market noise
  - Fluctuating portfolio values

The dataset mirrors real investment data where imperfections and volatility are expected.

---

## Step-by-Step Approach

### Step 1: Data Cleaning (SQL)
- Standardized date formats
- Handled missing daily returns conservatively
- Created month-level groupings for reporting

📁 `sql/cleaning.sql`

---

### Step 2: Performance Metric Engineering
- Calculated monthly portfolio returns
- Measured volatility to quantify risk
- Used Sharpe Ratio to assess return efficiency

---

### Step 3: Analysis
- Evaluated performance trends over time
- Assessed whether higher returns were accompanied by disproportionate risk
- Avoided misleading aggregations (returns were never summed)

📁 `sql/analysis.sql`

---

### Step 4: Dashboarding
- Executive KPI cards (Return, Volatility, Sharpe Ratio)
- Monthly performance trend
- Focused on clarity over technical indicators

📁 `Dashboards/`

---

## Key Decisions Made
- Avoided summing returns to prevent aggregation bias
- Chose monthly aggregation for leadership clarity
- Prioritized risk-adjusted metrics over raw returns
- Excluded overly technical indicators not used by executives

---

## Outcome
Delivered a clear, risk-aware performance view that enables leadership to evaluate
portfolio health beyond absolute returns.
