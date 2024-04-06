import tkinter
from tkinter import *
root = Tk()
e=Entry(root, width=50, bg="blue", fg="white", borderwidth=5)
e.pack()
e.insert(0, "Введи своё имя: ")
def myClick():
    hello ="Hello "+e.get()
    MyLabel =Label(root,text=hello)
    MyLabel.pack()
MyButton=Button(root, text="Введи своё имя", command=myClick,fg="blue",bg="#ffffff")
MyButton.pack()

root.mainloop()