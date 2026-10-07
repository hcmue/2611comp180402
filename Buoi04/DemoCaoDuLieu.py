import requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup
import schedule
import time

def scrape_data():
    rs = requests.get("https://giavang.org/trong-nuoc/", verify=False)
    if rs.status_code == 200:
        # print(rs.text)
        soup = BeautifulSoup(rs.text)
        # print(soup.prettify())
        list_tr = soup.find_all("tr")
        for item in list_tr:
            print(item)
            # list_td = item.find_all("td")
            # for td_item in list_td:
            #     print(td_item)
            gias = soup.css.select("td.text-right")
            for gia in gias:
                print(gia, gia.text)
    else:
        print(rs.status_code)


# Define lặp
schedule.every(30).seconds.do(scrape_data)

while True:
    schedule.run_pending()
    time.sleep(1)