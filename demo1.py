from tkinter import *
import tkinter.messagebox
import mysql.connector
#from  tkinter import Canvas, PhotoImage, Tk

# Assuming you have a MySQL database connection
# Replace the placeholders with your actual database details
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jeethu_pass22",
    database="farm_project"
)

mycursor = conn.cursor()

class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="AgroFarm", font=('Times 40 bold'),width="20" ,fg='white',bg="chartreuse3")
        self.heading.place(x=300, y=0)
        #window=Tk()
        #root.configure(bg=PhotoImage(file="screenshot(75).png"))
        #bgimg=tk.PhotoImage(file="screenshot(75).png")
        #bg=PhotoImage(file="screenshot(75).png")
        #window.mainloop
        # labels for the window
        self.name_l = Label(master, text="Crop Name: ", font=('Helvetica 20 bold'), fg='darkolivegreen4')
        self.name_l.place(x=120, y=100)
        btn=Button(text='Customer',font=('Times 15 bold'),fg='Red',bg='white',command=news_page)
        btn.place(x=480,y=470)

        self.stock_l = Label(master, text="Quantity(in Kg):", font=('Helvetica 20 bold'), fg='darkolivegreen4')
        self.stock_l.place(x=120, y=180)

        self.cp_l = Label(master, text="Price ", font=('Helvetica 20 bold'), fg='darkolivegreen4')
        self.cp_l.place(x=120, y=260)

        # entries for window
        self.name_e = Entry(master, width=25, font=('Calibri 20 bold'))
        self.name_e.place(x=380, y=100)

        self.stock_e = Entry(master, width=25, font=('Calibri 20 bold'))
        self.stock_e.place(x=380, y=180)

        self.cp_e = Entry(master, width=25, font=('Calibri 20 bold'))
        self.cp_e.place(x=380, y=260)

        # button to add to the database
        self.btn_add = Button(master, text='Update', width=0, height=0, fg='Black',
                              command=self.get_items, font=2)
        self.btn_add.place(x=400, y=400)

        self.btn_clear = Button(master, text="Reset", width=0, height=0, fg='Black',
                                command=self.clear_all, font=2)
        self.btn_clear.place(x=600, y=400)

        # text box for the log
        self.tbBox = Text(master, width=20, height=10, )
        self.tbBox.place(x=900, y=120)

        # Initialize ID number
        self.id = 1

        # Set up event bindings
        self.master.bind('<Return>', self.get_items)
        self.master.bind('<Up>', self.clear_all)

    def get_items(self, event=None):
        # get from entries
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()

        # dynamic entries
        if self.name == '' or self.stock == '' or self.cp == '':
            tkinter.messagebox.showinfo("Error", "Please Fill all the entries.")
        else:
            mycursor.execute("INSERT INTO farmer(name, stock, price) VALUES(%s,%s,%s)",
                             [self.name, self.stock, self.cp])
            conn.commit()
            # textbox insert
            self.tbBox.insert(END, "\n\nInserted " + str(self.name) + " into the database with the quantity of " + str(
                self.stock))
            tkinter.messagebox.showinfo("Success", "Successfully added to the database")

    def clear_all(self, event=None):
        num = self.id + 1
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)


# Create the Tkinter window
root = Tk()
root.title("Product Database")

# Set the window size
root.geometry("1200x600")

backgroundImage = PhotoImage(file=r"C:\Users\91790\OneDrive\Desktop\demo_farm\Screenshot (75).png",width=1024,height=683)
backgroundLabel = Label(root, image=backgroundImage)
backgroundLabel.place(x=110,y=0)
def news_page():
    root.destroy()
    import demo2

# Create an instance of the Database class
db = Database(root)

# Run the Tkinter event loop
root.mainloop()

