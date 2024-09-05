from tkinter import *
import mysql.connector
import tkinter as tk
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="jeethu_pass22",
  database="farm_project"
)
def back_page():
    root.destroy()
    import demo2

if mydb.is_connected():
    print("Database is connected!")
else:
    print("Database is not connected!")
# Create a cursor object to execute SQL commands
c = mydb.cursor()
c.execute("SELECT * FROM farmer")
farmer = c.fetchall()
# Create a new Tkinter window
root = tk.Tk()
btn=Button(text='Go to main page',font=('Times 20 bold'),fg='Black',bg='lightblue',command=back_page)
btn.place(x=190,y=300)

root.geometry('600x600')

lbl = Label(root,text="AGROFARM LIST")
#lbl.grid(row=30,column=8)
# Create a Listbox widget
listbox = tk.Listbox(root,height = 10,width = 30,font='helvetica')
listbox.place(x=10,y=30)
#create loop to insert data into listbox
for farmer1 in farmer:
    id = farmer1[0]
    name = farmer1[1]
    listbox.insert(tk.END, f"{id}: {name}")
# Pack the Listbox into the window
listbox.pack()

# Run the Tkinter event loop
root.mainloop()