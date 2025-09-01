# Powerball Numbers Exploratory Data Analysis (EDA)

## Overview
This notebook explores historical **Powerball lottery numbers** through basic exploratory data analysis (EDA).  
The goal is not to predict future results, but to practice data cleaning, visualization, and statistical summarization on real-world numeric data.

---

## Workflow
1. **Data Import & Cleaning**
   - Load historical Powerball draws (white balls and red Powerball).
   - Standardize column names and data types.
   - Remove missing or invalid rows.

2. **Frequency Distribution**
   - Count how often each number appears.
   - Compare white vs red ball distributions.
   - Plot histograms to visualize occurrence frequencies.

3. **Binning Analysis**
   - Group numbers into ranges (e.g., 1–10, 11–20).
   - Evaluate whether draws are uniformly distributed across bins.
   - Compare left–right bin symmetry.

4. **Kernel Density Estimation (KDE)**
   - Apply KDE to approximate the underlying distribution of numbers.
   - Provides a **smooth probability curve** compared to histograms.
   - Useful for spotting subtle concentration tendencies.

5. **Combination Patterns**
   - Examine common number groupings.
   - Check if certain ranges cluster more often.

6. **Visualization**
   - Histograms for white/red ball frequencies.
   - Bar plots of binned distributions.
   - KDE curves for smoothed density.
   - Comparative charts between white and red balls.

---

## Results
- Number frequencies appear broadly uniform, with minor deviations.  
- Bin-level checks suggest near-symmetry, with no strong bias.  
- KDE plots confirm distributions are generally flat, consistent with randomness.  
- No evidence of exploitable predictive patterns (as expected for a lottery).  

---

## Notes
- This project is **purely educational** — it does not provide predictive power for actual lottery outcomes.  
- It demonstrates a standard EDA workflow: **data cleaning → descriptive statistics → histograms/KDE → interpretation**.  

---

## Requirements
- Python 3.x  
- `pandas`, `numpy`, `matplotlib`, `seaborn`
