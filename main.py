# By: M. Muyakwa
# 2019-07-28

import configparser
import os
import smtplib
import time
from time import gmtime, strftime
import pymysql.cursors
import requests
from bs4 import BeautifulSoup

# Connect to settings.ini
pathname = os.path.dirname(os.path.realpath(__file__))
iniFile = os.path.abspath(pathname) + '/settings.ini'
config = configparser.ConfigParser()
config.read(iniFile)

# Connect to MySQL-Server with info from settings.ini
mydb = pymysql.connect(
  host=config['DB']['host'],
  user= config['DB']['user'],
  passwd=config['DB']['passwd'], 
  database=config['DB']['database']
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM links;")
myresult = mycursor.fetchall()

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu "
                  "Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36 ",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,"
              "*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "upgrade-insecure-requests": "1",
}

# Iterating through Database
tasks = list()
for x in myresult:
    tasks.append(
        {
            'email': config['EmailTo']['email'],
            'url': '%s' % x[2],
            'alert': x[4]
        }
    )

# Set email-settings from settings.ini
mail_config = {
    'host': config['Email']['host'],
    'port': config['Email']['port'],
    'username': config['Email']['username'],
    'password': config['Email']['password'],
}

def check_price(key, url, alert, email):

    try:
        page = requests.get(url, headers=headers)

        soup = BeautifulSoup(page.content, "html.parser")

        title = soup.find(id="productTitle").get_text().strip()
        price = soup.find(id="priceblock_ourprice").get_text().strip()

        c_price = float(price[0:len(price) - 2].strip().replace(",", "."))
        delta = c_price - alert

        print(f"Title: {title}")
        print(f"Current price: {price}")
        print(f"Target price: {alert}")
        print(f"Delta: {delta}")

    except:
        print(f"Failed to fetch: {url}")
        return

    if 'informed' not in tasks[key]:
        if c_price <= alert:
            send_mail(email, title, c_price, url)
            tasks[key]['informed'] = True


def send_mail(to_addrs, title, price, url):
    # Send a price alert mail with all relevant information to a given mail address
    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    subject = f"Price alert: {title}"
    body = f"Current price: {price}\n\nProduct page: {url}\n\nDatetime: {date}"

    msg = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP(host=mail_config['host'], port=mail_config['port'])
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user=mail_config['username'], password=mail_config['password'])
        server.sendmail(from_addr=mail_config['username'], to_addrs=to_addrs, msg=msg.encode('ASCII', 'replace'))
        server.quit()

        print("Message sent")
    except:
        print(f"Failed to send message to: {to_addrs}")
        return

# Main function
if __name__ == '__main__':
    print("Amazon tracker started")

for i, task in enumerate(tasks):
    print("-----------------------------")
    check_price(i, task['url'], task['alert'], task['email'])
