# Financial Modeling: Portfolio Optimization, CAPM, and Option Pricing

## App Link
You can explore the live demo of the project here:

[Finalysis App](https://finalysis.streamlit.app/)

## Project Overview
This project applies financial models for portfolio optimization, asset pricing, and option valuation. It covers three key areas:
1. **Markowitz Portfolio Optimization**
2. **Capital Asset Pricing Model (CAPM)**
3. **Option Pricing using Binomial and Black-Scholes Models**

## 1. Markowitz Portfolio Optimization

### Objective
To construct the efficient frontier and build optimized portfolios that maximize return for a given level of risk.

### Steps:
1. **Selection of Assets:**  
   Choose 10 risky assets (stocks, bonds, or ETFs) from the market with readily available price data.
   
2. **Data Collection:**  
   Gather the closing prices of these assets for the last 3 months.
   
3. **Calculate Returns:**  
   Compute the simple or log returns for each asset over the selected period.
   
4. **Mean-Variance Optimization:**  
   Apply Markowitz’s mean-variance optimization to construct the efficient frontier.
   
5. **Construct Portfolios:**  
   Select two points on the efficient frontier representing different risk tolerance levels. Calculate the asset weights for these portfolios to maximize expected return for the given risk.

## 2. Capital Asset Pricing Model (CAPM)

### Objective
To calculate expected returns using the CAPM formula and assess portfolio performance using different risk metrics.

### Steps:
1. **Selection of Risk-Free and Risky Assets:**  
   Choose a risk-free asset (e.g., government bond yield) and 10 risky assets from the market. You can reuse the assets selected for Markowitz optimization.

2. **Expected Return Calculation:**  
   Use the CAPM formula to calculate the expected return for each risky asset.

3. **Plot the Capital Market Line (CML):**  
   Calculate the CML equation and plot it along with the efficient frontier.

4. **Identify the Tangency Point:**  
   Determine the tangency point where the CML touches the efficient frontier and discuss its significance.

5. **Security Market Lines (SML):**  
   Choose 3 risky assets and calculate their individual security market lines.

6. **Performance Measures:**  
   Compute Sharpe Ratio and Treynor Ratio for each optimized portfolio and compare them with individual assets.

7. **Bonus Comparison:**  
   Compare the portfolios constructed using the Markowitz and CAPM approaches. Discuss key insights from each method.

## 3. Option Pricing

### Objective
To price options using the Binomial and Black-Scholes models and analyze the results against actual market data.

### Steps:
1. **Selection of a Stock:**  
   Pick a stock that is traded in the derivative market. Review its option history on Yahoo Finance.

2. **Estimate Volatility:**  
   Use the past one-year data to estimate the stock’s annual volatility.

3. **Interest Rate:**  
   Use the 10-year US treasury rate as the risk-free rate.

4. **Strike Prices and Maturity:**  
   Fix different strike prices and times to maturity. Evaluate the call/put option price using the Binomial model.

5. **Black-Scholes Formula:**  
   Evaluate the option price using the Black-Scholes formula.

6. **Convergence of Binomial Model:**  
   Increase the number of steps in the Binomial model to verify that the price converges to the Black-Scholes result.

7. **Graph:**  
   Draw a graph to show the convergence in step 6.

8. **Comparison with Market Data:**  
   Compare the calculated option prices with actual market data.

9. **Delta Neutral Portfolio:**  
   Create a delta neutral portfolio to hedge against price changes.

10. **Implied Volatility:**  
    Use numerical methods to calculate implied volatility. Tools like Excel, Python, or R can be used for coding.

---

## Tools and Libraries Used
- Python
- Pandas
- NumPy
- Matplotlib

## How to Run
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/financial-modeling-project.git
2. Install the necessary Python packages:
   ```bash
    pip install -r requirements.txt
3. Run the Jupyter notebooks or scripts for each model:
     """markowitz_portfolio_optimization.ipynb
        capm_analysis.ipynb
        option_pricing_models.ipynb """


