from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('icon creater')
root.iconbitmap("C:/Users/NAGA BABU SIGA/OneDrive/Documents/udemycourses/tkinkerpygui/NoMachine-icon-icon.ico")


my_img1=ImageTk.PhotoImage(Image.open("img1.jpeg"))
my_img2=ImageTk.PhotoImage(Image.open("img2.jpeg"))
my_img3=ImageTk.PhotoImage(Image.open("img3.jpeg"))
my_img4=ImageTk.PhotoImage(Image.open("img4.jpeg"))
my_img5=ImageTk.PhotoImage(Image.open("img5.jpeg"))


image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]

status=Label(root,text="Image 1 of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)

my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()#to delete the existing image.
    my_label=Label(image=image_list[number-1])
    button_forward=Button(root,text=">>",command=lambda:forward(number+1))
    button_back=Button(root,text="<<",command=lambda:back(number-1))
    
    if number==5:
        button_forward=Button(root,text=">>",state=DISABLED)
    
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    status=Label(root,text="Image "+str(number)+" of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

def back(number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()#to delete the existing image.
    my_label=Label(image=image_list[number-1])
    button_forward=Button(root,text=">>",command=lambda:forward(number+1))
    button_back=Button(root,text="<<",command=lambda:back(number-1))
    
    if number==1:
        button_back=Button(root,text="<<",state=DISABLED)
        
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    
    status=Label(root,text="Image "+str(number)+" of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

button_back=Button(root,text="<<",command=back,state=DISABLED)
button_exit=Button(root,text="EXIT PROGRAMME",command=root.quit)
button_forward=Button(root,text=">>",command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

root.mainloop()