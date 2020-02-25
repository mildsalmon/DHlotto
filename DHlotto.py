import requests
from bs4 import BeautifulSoup
import time
import telegram

url = "https://www.dhlottery.co.kr/common.do?method=main"
my_chat_id = "*****"
my_token = "****"

print(time.strftime("%c", time.localtime(time.time())))

bot = telegram.Bot(token=my_token)
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
speetto = soup.find(id = 'speetto2000')
turning = speetto.find(class_="tit")
quantitys = speetto.select(" a > ul > li")
strong = []
span = []

print(turning.text)

for quantity in quantitys:
    strong.append(quantity.find("strong").text)
    span.append(quantity.find("em").text)

if float(span[3]) > 95:
    bot.sendMessage(chat_id= my_chat_id, text=turning.text)
    for i in range(4):
        if i == 3:
            bot.sendMessage(chat_id = my_chat_id, text = strong[i] + " 출고율 : " + span[i])
        else:
            bot.sendMessage(chat_id = my_chat_id, text = strong[i] + " 남은 수량 : " + span[i])

for i in range(4):
    if i == 3:
        print(strong[i] + " 출고율 : " + span[i])
        if float(span[3]) > 95:
            print("야 스피또 사러가 빨리 뛰어가, 뒤도 돌아보지 말고 뛰어가")
        elif float(span[3]) > 90:
            print("돈 급하냐? 그럼 지금 좀 뛰어가")
        else:
            print("아직 아니야, 기다려")
    else:
        print(strong[i] + " 남은 수량 : " + span[i])