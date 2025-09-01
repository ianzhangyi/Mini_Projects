# Electricity Trading Analytical Problem

## Overview
This project addresses an **electricity trading decision task**:  
At 16:54 on **2021-02-16**, a trader must decide whether to **buy**, **sell**, or **do nothing** on a delivery contract for the period **17:00–18:00 UTC**.  
The payoff depends on the sign of the **total regulation energy** during the delivery hour:

- If total regulation energy > 0 → settlement price = **90 €/MWh**  
- If total regulation energy < 0 → settlement price = **0 €/MWh**  

At 16:54, the market quotes were: **buy 1 MWh @ 30 €** or **sell 1 MWh @ 29.99 €**:contentReference[oaicite:2]{index=2}.  
The goal is to predict the sign of the upcoming regulation energy and make the optimal decision.

---

## Approach
Two directions were considered:
1. **Classification** – predict the **sign** of next hour’s total regulation energy.  
2. **Sequence forecasting** – predict the full 60-minute regulation energy path (e.g., with LSTM) and sum it.  

Due to time limits, the implemented solution focused on the **classification approach**:contentReference[oaicite:3]{index=3}.

---

## Model
- **Algorithm**: XGBoost (robust baseline for tabular features).  
- **Features (~35 total)** built at each decision time (H:54), using only past values:  
  - Rolling stats (mean, std, min, max, sum) over 5/15/30/60 minutes  
  - Ratio of positive vs nonzero values  
  - Approximate slopes from differences  
  - Short-term lags (lag1, Δ1m, Δ5m)  
  - Time features (hour sine/cosine, weekday)  
- **No hyperparameter tuning** was applied (time constraint).  

---

## Evaluation
- **Train**: until 2021-01-31  
- **Validation**: 2021-02-01 to 2021-02-07  
- **Test**: 2021-02-08 to 2021-02-16  

Performance:  
- Train: Accuracy ≈ 0.76, Macro-F1 ≈ 0.74  
- Validation: Accuracy ≈ 0.67, Macro-F1 ≈ 0.66  
- Test: Accuracy ≈ 0.65, Macro-F1 ≈ 0.64:contentReference[oaicite:4]{index=4}  

At the final decision point (**2021-02-16 14:54 UTC**), the model predicted **P(y=1)=0.687**, leading to a **BUY** recommendation.  

---

## Conclusion
- The baseline shows **predictive signal above random guessing**, but with limited generalization and some overfitting.  
- With more time, improvements would include:  
  - Implementing the LSTM sequence-forecasting version  
  - Hyperparameter tuning and model comparison  
  - Better trend/volatility features  
  - Exploring cost-aware decision thresholds  

This submission demonstrates a **complete pipeline** from raw data → feature engineering → modeling → decision, under tight time constraints:contentReference[oaicite:5]{index=5}.

