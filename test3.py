from tkinter import *
root=Tk()

def myClick():
    myLable=Label(root,text="Look! I Clicked a Button!")
    myLable.pack()

# myButton=Button(root,text="Click me!",state=DISABLED)
# myButton=Button(root,text="Click me!",padx=50,pady=50)
myButton=Button(root,text="Click me!",command=myClick,fg="blue",bg="red")# don't put paranthesis. bg="#ffffff"
myButton.pack()

root.mainloop()