from tkinter import *
from time import *

# 변수 선언 부분
fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif","jeju5.gif","jeju6.gif","jeju7.gif","jeju8.gif","jeju9.gif"]
photoList=[None] * 9
num=0

def clickNext():
    global num #전역변수 
    num += 1
    if num > 8: #마지막까지 이동하면
        num=0
    photo=PhotoImage(file="D:/Python/Gif/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo

def clickPrev():
    global num #전역변수
    num -= 1
    if num < 0 :  
        num = 8
    photo=PhotoImage(file="D:/Python/GIF/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo

def pageUp(event):
    clickNext()

def pageDown(event):
    clickPrev()


#메인
window=Tk()
window.geometry("700x500")
window.title("디지털 앨범")
#키보드
window.bind("<Prior>", pageUp)
window.bind("<Next>", pageDown)

btnPrev=Button(window, text="<<이전", command=clickPrev)
btnNext=Button(window, text="<<다음", command=clickNext)


photo=PhotoImage(file="D:/Python/GIF/"+fnameList[0])
pLabel=Label(window, image=photo)

btnPrev.place(x=250, y=10)
btnNext.place(x=400, y=10)
pLabel.place(x=15, y=50)

window.mainloop()


