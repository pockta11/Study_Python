from tkinter import *

#변수
window=None
canvas=None
XSIZE, YSIZE=256,256

#메인
window=Tk() #Tk window=new Tk();
window.title("흑백 사진 보기")
canvas=Canvas(window, height=XSIZE, width=YSIZE)

paper=PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2), image=paper, state="normal")

#파일 찍기
fp=open('D:/Python/RAW/flower.raw', 'rb')

for i in range(0,XSIZE):
    for k in range(0, YSIZE):
        data=int(ord(fp.read(1))) # 읽어온 하나의 이미지 데이터
        paper.put("#%02x%02x%02x" % (data,data,data), (k,i))  #색상 조합 만들어서 찍기

fp.close()
canvas.pack()
window.mainloop()
