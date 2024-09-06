from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('icon creater')
root.iconbitmap("C:/Users/NAGA BABU SIGA/OneDrive/Documents/udemycourses/tkinkerpygui/NoMachine-icon-icon.ico")

def open():
    global my_img
    top=Toplevel()
    my_img=ImageTk.PhotoImage(Image.open("img1.jpeg"))
    my_label=Label(top,image=my_img).pack()
    top.title('MY second window')
    top.iconbitmap("C:/Users/NAGA BABU SIGA/OneDrive/Documents/udemycourses/tkinkerpygui/NoMachine-icon-icon.ico")
    btn2=Button(top,text="close window",command=top.destroy).pack()


btn=Button(root,text="Open second window",command=open).pack()

root.mainloop()