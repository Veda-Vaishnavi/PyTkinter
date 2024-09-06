from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root=Tk()
root.title('icon creater')
root.iconbitmap("C:/Users/NAGA BABU SIGA/OneDrive/Documents/udemycourses/tkinkerpygui/NoMachine-icon-icon.ico")

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/NAGA BABU SIGA/OneDrive/Documents/udemycourses/tkinkerpygui",title="select a file",filetypes=(("jpeg files","*.jpeg"),("all files","*.*")))
    my_label=Label(root,text=root.filename).pack()
    my_image=ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label=Label(image=my_image).pack()

my_btn=Button(root,text="Open File",command=open).pack()

root.mainloop()