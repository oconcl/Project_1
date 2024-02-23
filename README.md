# Tesla Data Oracle:
## Machine Learning Trade Cost Analysis
---
## Repository for Project 1
---
## Table of Contents 
* [Project Overview](#project-overview)
* [Data Collection](#data-collection)
* [Processing of Data](#processing-of-data)
* [Exploratory Data Analysis](#exploratory-data-analysis)
* [Statistical Analysis](#statistical-analysis)
* [Machine Learning Developments](#machine-learning-developments)
* [Resources](#resources)








## Executive Summary
  A hedge fund, Prestige Global, recently had an in-flow of $7,800,000,000 from an un-named wealthy investor. Prestige Global decided to allocate 25% of this investor's funds into TSLA US to reflect their current portfolio allocation. The traders at PG realized the 25% allocation of $1,950,000,000 into TSLA US returned an illiquid buy of 10,000,000 shares. This equated to  roughly 10% of TSLA US's 20-day ADV (average daily volume, as of 2/22/24). In order to execute this trade, PG traders knew they would need to spread the trade over a portion of the day to reduct market impact and minimize trade cost. The traders decided to run a volume analysis to identify what time of day produced the lowest Lambda levels. This ultimately would help decipher what time of day the market was able to absorb 10,000,000 shares of TSLA US with the lowest level of market impact. 

  
## Data Collection, Cleanup and Exploration
  Alpaca public API's provided data over the past five years on a 30-minute basis. The PG traders knew the more granular volume data, the more helpful the experiment would be in determining potential market impact. They first started by calling variables for objects such as volume, closing price, VWAP, date, trade count, and high and low of the day. Once they explored the data, then to make it more digestable they parsed it into specific time frames such as weekly and monthly volume data. Their goal was to determine a pattern of what days were high and low volume and what factors drove Lambda changes on those days. The traders sorted their volume data to determine the highest volume days and decided to remove earnings days given high volatility and unpredictable conditions. Once they removed earnings days they were left a smaller sample set of low Lambda days to analyze. 
  
## Approach
  PG learned the highest volume days of the past five years that were not earnings days, happened to be days of index rebalance inclusion, such as the S&P500 index changes. They decided the most opportune time to trade was on an index rebalance day. These days fell once per quarter and the next one coming up would be x. 

## Machine Learning Development

## Results and Conclusions

## Resources 
* https://github.com/quantopian
* https://frds.io/measures/kyle_lambda/
* https://alpaca.markets/data
* https://finance.yahoo.com/quote/TSLA/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAF523cXjMPfBSYf_9GiKR7BOjZzGxmMlkw428EYYxwkW7kzJDvhsk_0jiKTLMISF1RzESWiViBZrSmEIyG_zOlkPJ3xE0ADL8UIbkVipAiWlEwblr5xHOc33LT7UZcQorYaqk0-N4KsINTo9zTmIdUVasgCJztHugVaoYHOKZMfN
* https://ycharts.com/companies/TSLA/average_volume_30
* https://www.alphavantage.co/documentation/
  

  

