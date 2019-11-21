import csv
import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import datetime

i = 1

URL = 'YOUR WEBPAGE URL'

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    soup1 = BeautifulSoup(soup.encode("utf-8"),"html.parser")

    title = soup1.find(id="Find this from your browser").get_text().strip()
    price = float(soup1.find(id="Find this from your browser").get_text()[4:])

    timeAndDate = datetime.fromtimestamp(datetime.timestamp(datetime.now()))

    with open('Your output file name.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow([timeAndDate, title, price])
    csvFile.close()

while(True):
    print(i)
    check_price()
    time.sleep(3600)    
    i += 1    