import requests as req
from bs4 import BeautifulSoup 
import time, csv
import mailsender
from datetime import date 

urls = ["https://finance.yahoo.com/quote/AAPL/", 
        "https://finance.yahoo.com/quote/BAC/", 
        "https://finance.yahoo.com/quote/TTWO/"]

headers = {'User-Agent':
'YOUR USER AGENT INFO HERE (GOOGLE SEARCH: "MY USER AGENT")'}

today = str(date.today()) + ".csv"
csv_creator = open(today, 'w')
csv_writer = csv.writer(csv_creator)
csv_writer.writerow(['Stock Name', 'Current Price', 'Previous Close', 'Open', 'Bid', 
                     'Ask', "Day's Range", "52 Week Range", "Volume", "Avg. Volume"])

for url in urls:
    stock = []
    html_page = req.get(url, headers=headers)
    soup = BeautifulSoup(html_page.content, "lxml")

    header_info = soup.find_all("section", class_="container yf-ltlfr9")[0]
    stock_title = header_info.find("div", class_="hdr yf-ltlfr9").get_text()
    cur_price = header_info.find("span", class_="price yf-1n64cj base").get_text()
    table_info = soup.find("div", class_="content yf-13o2two").find_all("li")

    stock.append(stock_title)
    stock.append(cur_price)

    for i in range(0,8):
        value_num = table_info[i].find_all("span")[2].get_text()
        stock.append(value_num)
    
    csv_writer.writerow(stock)
    time.sleep(5) # waiting for 5 secs because we don't want to  
                  # send too many requests in a sec
csv_creator.close()

mailsender.send(filename=today)
