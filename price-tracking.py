import requests 
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.amazon.fr/Jabra-Bluetooth-R%C3%A9duction-Service-Int%C3%A9gr%C3%A9/dp/B07NPN3H25/ref=sr_1_2?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=11SHSCN2B5QSG&keywords=jabra+headphones&qid=1570788849&s=electronics&smid=A1X6FK5RDHNB96&sprefix=jabra+head%2Celectronics%2C222&sr=1-2'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
desiredPrice = 400


def check_price():
    page = requests.get(URL, headers=headers)


    soup = BeautifulSoup(page.content, 'html.parser') 

    title = soup.find(id="productTitle").get_text().strip()

    price = soup.find(id = 'priceblock_dealprice').get_text().strip()

    price = int(price.split(",")[0]) + 1
    print(price)

    if(price < desiredPrice):
        send_email(URL, title, price)


def send_email(URL, product_title, product_price):
    server  = smtplib.SMTP_SSL('smtp.gmail.com:465')
    server.ehlo() # self identify to another email server
    server.starttls
    

    server.login('from', 'password')
    subject = 'Price fell down'

    a = "My dream product \n\n" + product_title.encode("utf-8")+"\n\n"
    b = 'has just dropped below '+str(product_price).encode("utf-8")+'\n\n'
    c = 'The link to the rescue \n\n '+ URL.encode("utf-8")

    body = a + b + c

    msg = 'Subject: {}'.format(subject)+'\n\n {}'.format(body)

    server.sendmail(
        'from',
        'to',
        msg
    )

    print("Hey Awesome Man Email has been sent !")

    server.quit()

check_price()

