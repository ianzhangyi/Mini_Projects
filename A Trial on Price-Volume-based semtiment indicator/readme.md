# QQQ Daily Data & Factor Analysis

## Overview
This notebook explores **QQQ (Invesco QQQ ETF)** daily price data and derives simple factors for analysis.  
It demonstrates data collection, preprocessing, and feature engineering for financial time series.

## Workflow
1. **Data Download**  
   - Fetch QQQ daily data (2009–2025) via `yfinance`.  
   - Save as CSV and check basic structure.

2. **Data Cleaning**  
   - Standardize column names and convert `Date` to index.  
   - Ensure numeric types for all price/volume fields.

3. **Feature Engineering**  
   - **EMA30**: 30-day exponential moving average.  
   - **Bollinger Bands**: middle = EMA30, upper/lower = ±2σ.  
   - **Factor A**: Relative deviation `(Close - EMA30) / Close`.  
   - **Factor B**: Z-score of `(Close - EMA30)` using 250-day rolling window.  

4. **Statistical Levels**  
   - Compute mean, ±1σ, ±2σ for Factor A and Factor B.  
   - Use these levels as reference bands in analysis/visualization.

5. **Visualization**  
   - Plot price with EMA30 and Bollinger Bands.  
   - Plot Factor A and Factor B with their reference levels.

## Notes
- Factor A captures the **relative distance** of price from EMA.  
- Factor B normalizes this spread by recent volatility, making it more robust across regimes.  
- This is a **mini-project for experimentation**, not an investment strategy.

## Requirements
- Python 3.x  
- `pandas`, `numpy`, `matplotlib`, `yfinance`

