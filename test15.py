from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('icon creater')
root.iconbitmap("C:/Users/NAGA BABU SIGA/OneDrive/Documents/udemycourses/tkinkerpygui/NoMachine-icon-icon.ico")
root.geometry("400x400")

def show():
    mylabel=Label(root,text=var.get()).pack()

var=StringVar() #StringVar for strings
c=Checkbutton(root,text="Would u like to supersize your order",variable=var,onvalue="Supersize",offvalue="regular")
c.deselect()
c.pack()


myButton=Button(root,text="show Selection",command=show).pack()

root.mainloop()