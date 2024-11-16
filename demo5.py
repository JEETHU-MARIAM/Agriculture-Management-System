from tkinter import *
import mysql.connector
import tkinter as tk
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="******",
  database="farm_project"
)
'''def back_page():
    root.destroy()
    import demo2'''

if mydb.is_connected():
    print("Database is connected!")
else:
    print("Database is not connected!")
# Create a cursor object to execute SQL commands
c = mydb.cursor()
c.execute("SELECT * FROM QUANTITY_PRICE")
QUANTITY_PRICE = c.fetchall()
# Create a new Tkinter window
root = tk.Tk()
'''btn=Button(text='Go to main page',font=('Times 20 bold'),fg='Black',bg='lightblue',command=back_page)
btn.place(x=190,y=300)'''

root.geometry('600x600')

lbl = Label(root,text="AGROFARM LIST")
#lbl.grid(row=30,column=8)
# Create a Listbox widget
listbox = tk.Listbox(root,height = 10,width = 30,font='helvetica')
listbox.place(x=10,y=30)
#create loop to insert data into listbox
for farmer2 in QUANTITY_PRICE:
    PRODUCT_NAME = farmer2[1]
    T_PRICE = farmer2[3]
    listbox.insert(tk.END, f"{PRODUCT_NAME}: {T_PRICE}")
# Pack the Listbox into the window
listbox.pack()

# Run the Tkinter event loop
root.mainloop()
