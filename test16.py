from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('icon creater')
root.iconbitmap("C:/Users/NAGA BABU SIGA/OneDrive/Documents/udemycourses/tkinkerpygui/NoMachine-icon-icon.ico")
root.geometry("400x400")

#Drop down boxes

def show():
    myLabel=Label(root,text=Clicked.get()).pack()

options=[
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

Clicked=StringVar()
Clicked.set(options[0])

drop=OptionMenu(root,Clicked,*options)
drop.pack()

MyButton=Button(root,text="Show Selection",command=show).pack()

root.mainloop()