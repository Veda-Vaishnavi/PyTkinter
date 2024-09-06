from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt

root=Tk()
root.title('icon creater')
root.iconbitmap("C:/Users/NAGA BABU SIGA/OneDrive/Documents/udemycourses/tkinkerpygui/NoMachine-icon-icon.ico")
root.geometry("400x200")

def graph():
    house_prices=np.random.normal(2000000,25000,5000)
    # plt.hist(house_prices,200)
    plt.polar(house_prices)
    plt.show()

my_button =Button(root,text="Graph It!",command=graph)
my_button.pack()

root.mainloop()