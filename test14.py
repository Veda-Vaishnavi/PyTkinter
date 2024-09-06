from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('icon creater')
root.iconbitmap("C:/Users/NAGA BABU SIGA/OneDrive/Documents/udemycourses/tkinkerpygui/NoMachine-icon-icon.ico")
root.geometry("400x400")

vertical=Scale(root,from_=0,to=400)
vertical.pack()

def slide():
    my_label=Label(root,text=horizantal.get()).pack()
    root.geometry(str(horizantal.get())+"x"+str(vertical.get()))

horizantal=Scale(root,from_=0,to=400,orient=HORIZONTAL,command=slide)
horizantal.pack()


# my_label=Label(root,text=horizantal.get()).pack()

my_btn=Button(root,text="clickme",command=slide).pack()

root.mainloop()