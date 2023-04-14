import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import telepot

limit_date = datetime.strptime('30/04/2023', '%d/%m/%Y').date() #metti la data massima del test tolc
bot_token = "TOKEN" #bot di telegram
chat_id = "CHAT_ID" #la tua chat id
bot = telepot.Bot(token=bot_token)

def getInfo():
    url = "https://testcisia.it/calendario.php?tolc=ingegneria"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        if len(cols)>0 and cols[3] == '[email protected]' and cols[5] == 'POSTI DISPONIBILI':
                date_str = cols[4]
                test_date = datetime.strptime(date_str, '%d/%m/%Y').date()
                if test_date < limit_date:
                    print(cols)
                    message = "Tolc disponibile: {}".format(cols)
                    bot.sendMessage(chat_id, text=message)

while True:
    getInfo()
    time.sleep(10)