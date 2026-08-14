> Built under the guidance of Dr. Angela Yu from the 100 Days of Code Bootcamp on Udemy.

# Stock Trading News Alert

## Description

This Python project monitors daily stock price fluctuations for a specific ticker, such as RELIANCE.BSE. By utilizing financial data, it calculates the percentage difference between the closing prices of the two most recent trading days. If the stock price experiences an absolute change of 5% or more, the application fetches the top three relevant news articles to provide real-world context for the market movement. It then automatically logs the findings to a text file and sends an email alert to the user.

## Features

* Connects to the Alpha Vantage API (`TIME_SERIES_DAILY` endpoint) to retrieve daily time series stock data.


* Calculates the price difference and applies directional emoji indicators (🔼 or 🔽) based on positive or negative market trends.


* Integrates with the News API to fetch top headlines and brief descriptions related to the monitored company when significant volatility is detected.


* Automates email notifications using `smtplib` to send either urgent news alerts or standard status updates.


* Writes output messages locally to `stock-new-alert/news_articales.txt` or `stock-new-alert/no_issue.txt` depending on whether the price threshold was met.


* Secures sensitive information, including email credentials and API keys, using the `dotenv` library and environment variables.



## Output / Usage

* Requires a `.env` file configured with `email`, `password`, `stock_api_key`, and `news_api_key` to run successfully.


* When a significant price swing occurs, it generates and emails an alert formatted with the stock name, directional difference, headline, and a brief description of the news article.


* If the price change remains below the 5% threshold, the program generates an email and text file confirming the current difference and stating "No problem At All".
