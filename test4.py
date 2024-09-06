from tkinter import *
root=Tk()

e=Entry(root,width=50,bg="blue",fg="white",borderwidth=5)
e.pack()
e.insert(0,"Enter your Name: ")#default text

def myClick():
    hello="Hello "+e.get()+" !"
    myLable=Label(root,text=hello)
    myLable.pack()

# myButton=Button(root,text="Click me!",state=DISABLED)
# myButton=Button(root,text="Click me!",padx=50,pady=50)
myButton=Button(root,text="Enter your name",command=myClick,fg="blue",bg="red")# don't put paranthesis. bg="#ffffff"
myButton.pack()

root.mainloop()