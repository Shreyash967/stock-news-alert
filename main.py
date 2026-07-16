import requests
import smtplib
from dotenv import load_dotenv
import os 


load_dotenv()  # To Load Env Variables In The Main file 

send_to_email = "kashyapshreyash85@gmail.com"
my_email = os.getenv("email")
my_password = os.getenv("password")
stock_api_key = os.getenv("stock_api_key")
news_api_key = os.getenv("news_api_key")

stock_name = "RELIANCE.BSE"
stock_parmaters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": stock_name,
    "apikey": stock_api_key
}
stock_end_point = "https://www.alphavantage.co/query"

news_name = "reliance"
news_parametrs = {
    "q" : news_name,
    "apiKey" : news_api_key
}
news_endpoint = "https://newsapi.org/v2/everything"

try :
    stock_reponse = requests.get(url=stock_end_point, params=stock_parmaters)
    stock_reponse.raise_for_status()
    stock_data = stock_reponse.json()['Time Series (Daily)']
    stock_data_list = [ value for (key,value) in stock_data.items()]
    yesterdays_stock_data_price = stock_data_list[0]['4. close']
    day_before_yesterdays_stock_data_price = stock_data_list[1]['4. close']

    difference = float(yesterdays_stock_data_price) - float(day_before_yesterdays_stock_data_price)
    symbol = None 
    if difference > 0 :
        symbol = "🔼"
    else:
        symbol ="🔽"

    diff_percentage = round((difference / float(yesterdays_stock_data_price)) * 100)

    if abs(diff_percentage) >= 5:
        news_response = requests.get(url=news_endpoint, params=news_parametrs)
        news_response.raise_for_status()
        news_data = news_response.json()["articles"]
        three_articles = news_data[:3]

        # ... (API requests stay the same) ...
        headlines = [f"STOCK NAME:{stock_name} Difference:{symbol}{diff_percentage}%\n Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
        
        # 1. Define email_msg here!
        email_msg = "\n\n".join(headlines)

        with open("stock-new-alert/news_articales.txt", "a" , encoding="utf-8") as file:
            file.write(email_msg)

        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(from_addr=my_email,to_addrs=send_to_email,msg=f"Subject:Stock Alert\n\n{email_msg}".encode('utf-8'))
    
    else:
        # 1. Define the contents string here!
        contents = f"STOCK NAME : {stock_name}\n Difference : {symbol}{diff_percentage}\n No problem At All "
        
        with open("stock-new-alert/no_issue.txt","w",encoding="utf-8") as file :
            file.write(contents)

        with smtplib.SMTP("smtp.gmail.com",port=587) as connection :
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(from_addr=my_email,to_addrs=send_to_email,msg=f"Subject:Stock Alert\n\n{contents}".encode('utf-8'))


except Exception as e:
    print(e)