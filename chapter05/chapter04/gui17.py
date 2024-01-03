from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import *

def func_open():
    filname=askopenfilename(parent=window, filetypes=(("GIF 파일","*.gif"), ("모든 파일", "*.*")))
    photo=PhotoImage(file=filname)
    pLabel.configure(image=photo)
    pLabel.image=photo

def func_exit():
    window.quit()
    window.destroy()


# 메인
window=Tk()
window.geometry("400x400")
window.title("명화감상하기")

photo=PhotoImage()
pLabel=Label(window, image=photo)
pLabel.pack(expand=1, anchor=CENTER)

mainManu=Menu(window)
window.config(menu=mainManu)

fileMenu=Menu(mainManu)
mainManu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기", command=func_open)

fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)

window.mainloop()