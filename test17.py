from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.title('icon creater')
root.iconbitmap("C:/Users/NAGA BABU SIGA/OneDrive/Documents/udemycourses/tkinkerpygui/NoMachine-icon-icon.ico")
root.geometry("400x400")

#Databases

#Create a database or connect to one
conn=sqlite3.connect('address_book.db')

#Create cursor
c = conn.cursor()

#create table
c.execute(""" CREATE TABLE addresses(
          first_name text,
          last_name text,
          adress text,
          city text,
          state text,
          zipcode integer
          )""")

#commit changes
conn.commit()

#Close connection
conn.close()

root.mainloop()