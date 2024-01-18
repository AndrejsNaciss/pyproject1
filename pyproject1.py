import requests
import bs4
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config 

def get_car_data():
    url = "https://www.ss.com/lv/transport/cars/today/" #norade uz sludinājumu servisu
    saturs = requests.get(url)

    if saturs.status_code == 200: #pārbaude vai lapa strādā
        lapa = bs4.BeautifulSoup(saturs.content, "html.parser")
        atrada = lapa.find_all(class_="msga2-o pp6") #šī klase satur auto informaciju
        return atrada
    else:
        print("Lapas ielādes kļūda.")
        return None