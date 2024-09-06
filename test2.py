from tkinter import *
root=Tk()

#creating a label widget
myLabel1=Label(root,text="Hello World!").grid(row=0,column=0)
myLabel2=Label(root,text="My name is babu").grid(row=1,column=5)

# myLabel3=Label(root,text="    ")
# myLabel4=Label(root,text="     ")
# myLabel5=Label(root,text="     ")
#shoving it onto the screen

# myLabel1.grid(row=0,column=0)
# myLabel5.grid(row=1,column=1)
# myLabel3.grid(row=1,column=2)
# myLabel4.grid(row=1,column=3)
# myLabel2.grid(row=1,column=5)


root.mainloop()