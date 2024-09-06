from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.title('icon creater')
root.iconbitmap("C:/Users/NAGA BABU SIGA/OneDrive/Documents/udemycourses/tkinkerpygui/NoMachine-icon-icon.ico")
root.geometry("400x400")
    
#Create a database or connect to one
conn=sqlite3.connect('address_book.db')

#Create cursor
c = conn.cursor()

#Databases

#create table
'''
c.execute(""" CREATE TABLE addresses(
          first_name text,
          last_name text,
          adress text,
          city text,
          state text,
          zipcode integer
          )""")
'''

#Create a function to Delete a Record
def delete():

    #Create a database or connect to one
    conn=sqlite3.connect('address_book.db')

    #Create cursor
    c = conn.cursor()

    #delete a record
    c.execute("DELETE from addresses WHERE oid="+delete_box.get())

    #commit changes
    conn.commit()

    #Close connection
    conn.close()

#Create submit function for database
def submit():
    
    #Create a database or connect to one
    conn=sqlite3.connect('address_book.db')

    #Create cursor
    c = conn.cursor()
    
    #insert into the table
    c.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:address,:city,:state,:zipcode)",
            {
               'f_name':f_name.get(),
               'l_name':l_name.get(),
               'address':address.get(),
               'city':city.get(),
               'state':state.get(),
                'zipcode':zipcode.get()
            })

    #commit changes
    conn.commit()

    #Close connection
    conn.close()


    #clear the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

def query():
    
    #Create a database or connect to one
    conn=sqlite3.connect('address_book.db')

    #Create cursor
    c = conn.cursor()
    
    #Query the database
    c.execute("SELECT *, oid FROM addresses")
    records=c.fetchall()
    # print(records)

    #loop through results
    print_records=''
    for record in records:
        print_records+=str(record[0])+" "+str(record[1])+" \t"+str(record[6])+" "+"\n"
    
    query_label=Label(root,text=print_records)
    query_label.grid(row=11,column=0,columnspan=2)

    #commit changes
    conn.commit()

    #Close connection
    conn.close()


# create text boxes
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)

address=Entry(root,width=30)
address.grid(row=2,column=1,padx=20)

city=Entry(root,width=30)
city.grid(row=3,column=1,padx=20)

state=Entry(root,width=30)
state.grid(row=4,column=1,padx=20)

zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1,padx=20)

delete_box=Entry(root,width=30)
delete_box.grid(row=9,column=1,pady=5)

#create text box labels

f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0,pady=(10,0))

l_name_label=Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)

address_label=Label(root,text="Address Name")
address_label.grid(row=2,column=0)

city_label=Label(root,text="City Name")
city_label.grid(row=3,column=0)

state_label=Label(root,text="State Name")
state_label.grid(row=4,column=0)

zipcode_label=Label(root,text="Zipcode Name")
zipcode_label.grid(row=5,column=0)

delete_box_label=Label(root,text="Delete ID")
delete_box_label.grid(row=9,column=0,pady=5)

#Create Submit button
Submit_btn=Button(root,text="Add record to database",command=submit)
Submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)


#Create a Query Button
query_btn=Button(root,text="Show Records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

#Create a delete button
delete_btn=Button(root,text="Delete Record",command=delete)
delete_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=136)

#commit changes
conn.commit()

#Close connection
conn.close()

root.mainloop()