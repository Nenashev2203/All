import tkinter
from tkinter import *
root = Tk()
def myClick():
    myLabel = Label(root, text="Кнопка нажата")
    myLabel.pack()
myButton = Button(root, text="Нажми на меня", command=myClick,fg="blue",bg="#ffffff")
myButton.pack()
root.mainloop()