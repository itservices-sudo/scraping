import requests
from bs4 import BeautifulSoup
url = "https://tradingeconomics.com/bonds"
page = requests.get(url)
content = page.content
soup = BeautifulSoup(content, 'html.parser')

main_content = soup.find_all('div', class_='col-lg-8 col-md-9', role="main")
for th in main_content:
    Yield = th.find_all('th', 'style="text-align: center;cursor: pointer;">Yield')
    Day = th.find_all('th', 'style="text-align: center;cursor: pointer;">Day')
    Percent = th.find_all('th', 'style="text-align: center;cursor: pointer;">%')
    Weekly = th.find_all('th', 'style="text-align: center;cursor: pointer;">Weekly')
    Monthly = th.find_all('th', 'style="text-align: center;cursor: pointer;">Monthly')
    YTD = th.find_all('th', 'style="text-align: center;cursor: pointer;">YTD')
    Date = th.find_all('th', 'style="text-align: center;cursor: pointer;">Date')     
    info = [main_content]
    print(info)
