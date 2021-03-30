from tkinter import *

win = Tk()
win.geometry("600x100")
win.title("Lottery Finder")
win.option_add("*Font", "맑은고딕 8")

ent = Entry(win)
ent.pack()
def ent_p():
    a = ent.get()
    print(a)

btn = Button(win)
btn.config(text="로또 당첨 번호 확인")
btn.config(command=ent_p)
btn.pack()
win.mainloop()

# div class ="win_result"
import requests
from bs4 import BeautifulSoup

n = input()
url = "https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(n)
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

#당첨번호 추출하기
txt1 = soup.find('div', attrs={"class", "win_result"}).get_text()
print("txt1= ", txt1)

num1 = txt1.split()
print(num1)
print("num1 인덱싱 수 : ", len(num1))

numlist1 = num1[7:13]
print("당첨번호 ", numlist1)

bonus = num1[14]
print("보너스 번호 ", bonus)
