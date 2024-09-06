from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('icon creater')
root.iconbitmap("C:/Users/NAGA BABU SIGA/OneDrive/Documents/udemycourses/tkinkerpygui/NoMachine-icon-icon.ico")

# r=IntVar()
# r.set("2")

MODES=[
    ("pepperoni","pepperoni"),
    ("Cheesa","Cheesa"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]

pizza=StringVar()
pizza.set("pepperoni")

for text,mode in MODES:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)

def clicked(value):
    mylabel=Label(root,text=value)
    mylabel.pack()

# Radiobutton(root,text="option1",variable=r,value=1,command=lambda: clicked(r.get())).pack()
# Radiobutton(root,text="option2",variable=r,value=2,command=lambda: clicked(r.get())).pack()
# Radiobutton(root,text="option3",variable=r,value=3,command=lambda: clicked(r.get())).pack()


# mylabel=Label(root,text=pizza.get())
# mylabel.pack()

myButton=Button(root,text="Clicke Me!",command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()