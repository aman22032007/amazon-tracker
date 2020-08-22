import requests
from bs4 import BeautifulSoup
import smtplib
url='https://www.amazon.in/Mi-Notebook-i5-10210U-Graphics-XMA1904-AR/dp/B089F5JGM1/ref=sr_1_2?dchild=1&keywords=mi+notebook&qid=1598077364&sr=8-2'
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.61'}
def check_price():
    page=requests.get(url,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title=soup.find(id='productTitle').get_text().strip()
    price=soup.find(id='priceblock_ourprice').get_text()
    price2=price[1:8].replace(",",'')
    converted_price=int(price2)
    print(converted_price)
    if converted_price<60000:
        send_mail()
def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('aman220307@gmail.com','baziafcaijkehzkg')
    subject="PRICE FELL DOWN"
    body="check the link https://www.amazon.in/Mi-Notebook-i5-10210U-Graphics-XMA1904-AR/dp/B089F5JGM1/ref=sr_1_2?dchild=1&keywords=mi+notebook&qid=1598077364&sr=8-2"
    msg=f'Subject:{subject}\n\n{body}'
    server.sendmail(
        'aman220307@gmail.com',
        'aman220307@outlook.com',
        msg
    )
    print("EMAIL HAS BEEN SENT")
    server.quit()
check_price()