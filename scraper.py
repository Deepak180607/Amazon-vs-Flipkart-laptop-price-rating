from bs4 import BeautifulSoup
import requests
import pandas as pd
from requests.exceptions import RequestException
from time import sleep

url = "https://www.flipkart.com/search?q=Gaming%20laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0',
            'Accept-Language':'en-US, en;q=0.5'})
def scrape_data():
    webpage = requests.get(url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(webpage.content, "html.parser")
        
    links = soup.find_all("a", attrs={'class':'k7wcnx'})
    link_lst = []
    for link in links:
        link_lst.append(link.get('href'))
        
    t = []
    p = []
    r = []
    cpu = []
    Storage = []
    d = {"Name": t, "Price": p, "Ratings": r, "CPU": cpu, "Storage": Storage}

    for link in link_lst:
        try:
            new_webpage = requests.get("https://flipkart.com" + link, headers=HEADERS, timeout = 10)
            new_soup = BeautifulSoup(new_webpage.content, "html.parser")
            new_webpage.raise_for_status()
        except RequestException as e:
            print("Skipping product")
            continue
        try:
            title = new_soup.find("span", attrs = {'class':"LMizgS"}).text.strip()
            title = title.split("-")
            title = title[0]
            price = new_soup.find("div",attrs={'class': "hZ3P6w bnqy13"}).text.strip()
            price = price[1::]
            price = price.split(",")
            ratings = new_soup.find("div", attrs={'class':'MKiFS6'}).text.strip()
            ratings = float(ratings.split()[0])
            x = " "
            specs = new_soup.find_all("tr", attrs = {'class':'v1Jif8 row'})
            for CPU in specs:
                processor_name = ""
                GPU = ""
                RAM = ""
                storage = ""
                spec = new_soup.find_all("tr", attrs = {"class": 'v1Jif8'})
                for row in spec:
                    key = row.find("td", attrs = {'class':'JMeybS col col-3-12'}).text.strip()
                    if key == "Processor Brand":
                        processor_name = row.find("li", attrs={'class':'DW2bnL'}).text.strip()
                    elif key == "Processor Generation":
                        processor_name = processor_name + " " + row.find("li", attrs={'class':'DW2bnL'}).text.strip()
                    elif key == "Processor Name":
                        processor_name = processor_name + " "+ row.find("li", attrs={'class':'DW2bnL'}).text.strip()
                    elif key == "Processor Generation":
                        processor_name = processor_name + " "+ row.find("li", attrs={'class':'DW2bnL'}).text.strip()
                    if key == "SSD Capacity":
                        storage = row.find("li", attrs={'class':'DW2bnL'}).text.strip()
                        break
            for i in price:
                x += i.strip()
            x = int(x)
            if x < 9999999 :
                t.append(title)
                p.append(x)
                r.append(ratings)
                cpu.append(processor_name)
                Storage.append(storage)
                print("Extracting...")
        except AttributeError:
            continue
    sleep(1.5)

    df = pd.DataFrame(d)
    df.to_csv("data/Laptop.csv", index = False)
    return df
