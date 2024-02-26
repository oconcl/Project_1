# Project 1: Tesla Data Oracle
##  Using Kyle's Lambda to identify times of the day where market impact is lowest in TSLA US
---
## Table of Contents 
* [Executive Summary](#executive-summary)
* [Installation and Usage Instructions](#installation-and-usage-instructions)
* [Data Collection, Cleanup and Exploration](#data-collection-cleanup-and-exploration)
* [Approach](#approach)
* [Results and Conclusions](#results-and-conclusions)
* [Future Delevopments](#future-developments)
* [Collaboration and Version Control](#collaboration-and-version-control)
* [Resources](#resources)
* [Presentation-Project 1- Tesla Data Oracle](#presentation-project-1-tesla-data-oracle)
* 

## Executive Summary
  A hedge fund, Prestige Global, recently had an in-flow of $7,800,000,000 from an un-named wealthy investor. Prestige Global decided to allocate 25% of this investor's funds into TSLA US to reflect their current portfolio allocation. The traders at PG realized the 25% allocation of $1,950,000,000 into TSLA US returned an illiquid buy of 10,000,000 shares. This equated to  roughly 10% of TSLA US's 20-day ADV (average daily volume, as of 2/22/24). In order to execute this trade, PG traders knew they would need to spread the trade over a portion of the day to reduct market impact and minimize trade cost. The traders decided to run a volume analysis to identify what time of day produced the lowest Lambda levels. This ultimately would help decipher what time of day the market was able to absorb 10,000,000 shares of TSLA US with the lowest level of market impact. 

## Installation and Usage Instructions
  This section covers how to get your project up and running on a local machine for development and testing purposes.Prerequisites
  Before installing, ensure you have the following installed:
  * Python 3.8 or later
  * pip (Python package manager)

  The project depends on several Python libraries, including Alpaca Trade API, Pandas, Matplotlib, and others. To install all required dependencies, navigate to your project directory and run: `pip install alpaca-trade-api matplotlib pandas hvplot python-dotenv numpy requests`

  1. Create a file named api_keys.env in the root directory of your project.
  2. Add your Alpaca API Key and Secret Key to the .env file as follows:

  ```
  ALPACA_API_KEY=your_alpaca_api_key_here
  ALPACA_SECRET_KEY=your_alpaca_secret_key_here
  ```

  Make sure to replace your_alpaca_api_key_here and your_alpaca_secret_key_here with your actual Alpaca API and Secret keys

## Data Collection, Cleanup and Exploration
  Alpaca public API's provided data over the past five years on a 30-minute basis. The PG traders knew the more granular volume data, the more helpful the experiment would be in determining potential market impact. They first started by calling variables for objects such as volume, closing price, VWAP, date, trade count, and high and low of the day. Once they explored the data, then to make it more digestable they parsed it into specific time frames such as weekly and monthly volume data. Their goal was to determine a pattern of what days were high and low volume and what factors drove Lambda changes on those days. The traders sorted their volume data to determine the highest volume days and decided to remove earnings days given high volatility and unpredictable conditions. Once they removed earnings days they were left a smaller sample set of low Lambda days to analyze. 
  
## Approach
  PG traders used visualizations in MatPlotLib to view and identify volume spikes through visualizations and statistical analysis that identifies any volume days which have greater than 2-standard deviation move. 
  
  learned the highest volume days of the past five years that were not earnings days, happened to be days of index rebalance inclusion, such as the S&P500 index changes. They decided the most opportune time to trade was on an index rebalance day. These days fell once per quarter and the next one coming up would be x. 

## Results and Conclusions
  - handful of dates when there are high standard deviation volume moves, and why there was such high spikes in volumes
    
## Future Developments and Alternative Processes
* Machine Learning Development:
Model Selection: Experiment with different models suitable for time series forecasting, like ARIMA (Autoregressive Integrated Moving Average), LSTM (Long Short-Term Memory networks), or Gated Recurrent Units (GRUs).

* Feature Engineering: Incorporate lag features, moving averages, and RSI (Relative Strength Index).

* Training and Testing: Employ scikit-learn and deep learning libraries like tensorflow or keras for model training. Use a rolling forecast origin for more accurate time series forecasting.

Machine learning or alternative process
Data Collection:

* Relevant data is collected from various sources. This can include historical records, sensor data, user interactions, or any other information pertinent to the problem at hand.
Data Cleaning and Preprocessing:

* Raw data often contains noise, missing values, outliers, or inconsistencies. Data cleaning involves handling these issues to ensure the dataset is suitable for analysis.
Preprocessing involves transforming the data into a format suitable for machine learning algorithms. This may include normalization, standardization, encoding categorical variables, and handling imbalanced data.


## Collaboration and Version Control
* Version Control: Use git for version control and platforms like GitHub for collaboration, code sharing, and tracking changes.
* Project Management: Consider tools like Jupyter Notebooks for sharing code and results in a readable format or Trello for task management.

## Resources 
* [Quantopian](https://github.com/quantopian)
* [Kyle's Lambda](https://frds.io/measures/kyle_lambda/)
* [Alpaca](https://alpaca.markets/data)
* [Yahoo Finance](https://finance.yahoo.com/quote/TSLA/?   guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAF523cXjMPfBSYf_9GiKR7BOjZzGxmMlkw428EYYxwkW7kzJDvhsk_0jiKTLMISF1RzESWiViBZrSmEIyG_zOlkPJ3xE0ADL8UIbkVipAiWlEwblr5xHOc33LT7UZcQorYaqk0-N4KsINTo9zTmIdUVasgCJztHugVaoYHOKZMfN)
* [Volume Analysis](https://ycharts.com/companies/TSLA/average_volume_30)
* [AlphaVantage](https://www.alphavantage.co/documentation/)

## Presentation- Project 1- Tesla Data Oracle


  

