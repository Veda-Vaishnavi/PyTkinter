from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('icon creater')
root.iconbitmap("C:/Users/NAGA BABU SIGA/OneDrive/Documents/udemycourses/tkinkerpygui/NoMachine-icon-icon.ico")

my_img=ImageTk.PhotoImage(Image.open("NoMachine-icon-icon.png"))
my_label=Label(image=my_img)
my_label.pack()

button_quit=Button(root, text="exit programme", command=root.quit)
button_quit.pack()
root.mainloop()