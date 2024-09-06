from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root=Tk()
root.title('icon creater')
root.iconbitmap("C:/Users/NAGA BABU SIGA/OneDrive/Documents/udemycourses/tkinkerpygui/NoMachine-icon-icon.ico")

#showingo ,showwarning, showerror, askquestion,askokcancel,askyesno

# def popup():
#     messagebox.showinfo("This is my Popup!","Hello world")

def popup():
    response=messagebox.askyesno("This is my Popup!","Hello world")
    # Label(root,text=response).pack
    if response==1:
        Label(root,text="Your clicked Yes!").pack()
    else:
        Label(root,text="You clikced No!").pack()

Button(root,text="Popup",command=popup).pack()

root.mainloop()