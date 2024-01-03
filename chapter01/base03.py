from tkinter import *

## 변수
window = None
canvas = None ##실제 사용하는 공간
x1,y1,x2,y2=None,None,None,None

## 함수
def mouseClick(event):
    global x1,y1,x2,y2 ## 전역변수
    x1=event.x
    y1=event.y

def mouseDrop(event):
    global x1,y1,x2,y2
    x2=event.x
    y2=event.y
    canvas.create_line(x1,y1,x2,y2, width=5, fill="red")


# 메인
window=Tk() #윈도우 창 생성
window.title("그림판")
canvas=Canvas(window, height=300, width=300) #윈도우창 안에 캔버스(작업영역) 생성
canvas.bind("<Button-1>", mouseClick)
canvas.bind("<ButtonRelease-1>", mouseDrop)    

canvas.pack() ## 출력

window.mainloop()

