from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import datetime

class Application():
    products_list = []
    product_price = []
    product_quantity = []
    product_id = []

    
        
    def __init__(self, master, *args, **kwargs):
        self.master = master
         # Left Frame
        self.left = Frame(master, width=750, height=768, bg='black')
        self.left.pack(side=LEFT)
    

        # Right Frame
        self.right = Frame(master, width=500, height=500, bg='white')
        self.right.pack(side=RIGHT)

        # Labels and Entry Widgets
        self.heading = Label(self.left, text="AgroFarm", font=('Times 30 bold'), fg='White',width="20" ,bg="chartreuse3")
        self.heading.place(x=100, y=20)
        btn=Button(text='View Crop List',font=('Times 10 bold'),fg='Black',bg='white',command=next_page)
        btn.place(x=350,y=190)
       # btn=Button(text='View Crop List',font=('Times 10 bold'),fg='Black',bg='black',command=n_page)
        #btn.place(x=350,y=190)

        self.date_l = Label(self.right, text="Date: ", font=('Calibri 18 bold'), fg='RED')
        self.date_l.place(x=140, y=0)

        self.tproduct = Label(self.right, text="Products", font=('Calibri 20 bold'), fg='red')
        self.tproduct.place(x=0, y=60)

        self.tquantity = Label(self.right, text="Quantity", font=('Calibri 20 bold'), fg='red')
        self.tquantity.place(x=150, y=60)

        self.tamount = Label(self.right, text="Price", font=('Calibri 0 bold'), fg='red')
        self.tamount.place(x=300, y=63)

        self.enterid = Label(self.left, text="Enter ID: ", font=('Helvetica 20 bold'), fg='white',bg='black')
        self.enterid.place(x=50, y=223)

        self.enteride = Entry(self.left, width=20, font=('times 18 bold'), bg='white')
        self.enteride.place(x=225, y=233)
        self.enteride.focus()
       
        self.search_btn = Button(self.left, text="Check out!",font=('Times 13 bold'), width=12, height=1, bg='lightblue', command=self.ajax)
        self.search_btn.place(x=584, y=230)

        self.productname = Label(self.left, text="Name :", font=('Helvetica 27 bold'), bg='black', fg='black')
        self.productname.place(x=60, y=250)

        self.pprice = Label(self.left, text="Price:", font=('Helvetica 20 bold'), bg='black', fg='black')
        self.pprice.place(x=60, y=380)

        self.total_l = Label(self.right, text="Final Amount:", font=('Helvetica 20 bold'), bg='black', fg='red')
        self.total_l.place(x=20, y=400)

    def ajax(self, *args, **kwargs):
        try:
            self.conn = mysql.connector.connect(host='localhost', database='farm_project', user='root', password='jeethu_pass22')
            self.mycursor = self.conn.cursor()
            get_id = self.enteride.get()
            self.mycursor.execute("SELECT * FROM farmer WHERE id= %s", [get_id])
            self.pc = self.mycursor.fetchall()

            if self.pc:
                for r in self.pc:
                    self.get_id = r[0]
                    self.get_name = r[1]
                    self.get_price = r[3]
                    self.get_stock = r[2]

                # Update the displayed product's name
                self.productname.configure(text="Product Name: " + str(self.get_name), font=('Times 18 bold'),fg='white', bg='black',
                                           )
                self.productname.place(x=50, y=200)

                self.quantityl = Label(self.left, text="Quantity:", font=('Calibri 18 bold'), fg='white',
                                       bg='black')
                self.quantityl.place(x=10, y=300)

                self.quantity_e = Entry(self.left, width=10, font=('Calibri 18 bold'), bg='lightblue')
                self.quantity_e.place(x=170, y=300)
                self.quantity_e.focus()

                self.discount_l = Label(self.left, text="Discount ", font=('Calibri 20 bold'), fg='white',
                                        bg='black')
                self.discount_l.place(x=320, y=300)

                self.discount_e = Entry(self.left, text="Bill",width=10, font=('Calibri 20 bold'), fg='black', bg='lightblue')
                self.discount_e.place(x=430, y=300)
                self.discount_e.insert(END, 0)

                self.add_to_cart_btn = Button(self.left, text="Display bill receipt", width=18, height=3,
                                              bg='WHITE', command=self.add_to_cart)
                self.add_to_cart_btn.place(x=200, y=370)

                self.change_l = Label(self.left, text="Enter the paid amount", font=('Calibri 20 bold'), fg='black',
                                      bg='white')
                self.change_l.place(x=0, y=450)

                self.change_e = Entry(self.left, width=10, font=('Calibri 18 bold'), bg='lightblue')
                self.change_e.place(x=280, y=450)

                self.change_btn = Button(self.left, text="Calculate the difference", width=22, height=2, bg='lightblue',
                                          command=self.change_func)
                self.change_btn.place(x=430, y=450)

                self.bill_btn = Button(self.left, text="Create a bill of the items purchased", width=30, height=2,
                                       bg='lightgreen', fg='white', command=self.generate_bill)
                self.bill_btn.place(x=0, y=550)
            else:
                messagebox.showinfo("Product Not Found", "No product found with ID {get_id}")

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")

        finally:
            if self.conn.is_connected():
                self.mycursor.close()
                self.conn.close()

    def add_to_cart(self, *args, **kwargs):
        try:
            # Ensure these variables are defined before using them
            self.quantity_value = int(self.quantity_e.get())
            if self.quantity_value > int(self.get_stock):
                messagebox.showinfo("Error", "Not enough products in our stock.")
            else:
                # calculate the price first
                self.final_price = (float(self.quantity_value) * float(self.get_price)) - (float(self.discount_e.get()))
                Application.products_list.append(self.get_name)
                Application.product_price.append(self.final_price)
                Application.product_quantity.append(self.quantity_value)
                Application.product_id.append(self.get_id)

                self.x_index = 0
                self.y_index = 100
                self.counter = 0
                for self.p in Application.products_list:
                    self.tempname = Label(self.right, text=str(Application.products_list[self.counter]), font=('arial 18 bold'),
                                          bg='black', fg='red')
                    self.tempname.place(x=0, y=self.y_index)
                    self.tempqt = Label(self.right, text=str(Application.product_quantity[self.counter]), font=('arial 18 bold'),
                                        bg='black', fg='red')
                    self.tempqt.place(x=150, y=self.y_index)
                    self.tempprice = Label(self.right, text=str(Application.product_price[self.counter]), font=('arial 18 bold'),
                                           bg='black', fg='red')
                    self.tempprice.place(x=300, y=self.y_index)
                  
                    self.y_index += 40
                    self.counter += 1

                # total configure
                self.total_l.configure(text="Final amount=Rs. " + str(sum(Application.product_price)), bg='gray', fg='white',
                                       font=('20'))
                self.total_l.place(x=180, y=450)
                # delete
                self.quantity_e.place_forget()
                self.discount_l.place_forget()
                self.discount_e.place_forget()
                self.productname.configure(text="")
                self.pprice.configure(text="")
                self.add_to_cart_btn.destroy()
                # autofocus to the enter id
                self.enteride.focus()
                self.quantityl.focus()
                self.enteride.delete(0, END)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid quantity.")

    def change_func(self, *args, **kwargs):
        self.amount_given = float(self.change_e.get())
        self.our_total = float(sum(Application.product_price))

        self.to_give = self.amount_given - self.our_total

        # label change
        self.c_amount = Label(self.left, text="Change is Rs. " + str(self.to_give), font=('Calibri 20 bold'),
                              fg='Black', bg='white')
        self.c_amount.place(x=0, y=500)

    def generate_bill(self, *args, **kwargs):
        try:
            # Reconnect and create a new cursor
            self.conn = mysql.connector.connect(host='localhost', database='farm_project', user='root',
                                                password='jeethu_pass22')
            self.mycursor = self.conn.cursor()

            for i, product in enumerate(Application.products_list):
                for r in self.pc:
                    self.old_stock = r[2]
                    if i < len(Application.product_quantity):
                        self.new_stock = int(self.old_stock) - int(Application.product_quantity[i])
                        # updating the stock
                        self.mycursor.execute("UPDATE farmer SET stock=%s WHERE id=%s",
                                              [self.new_stock, self.get_id])
                        self.conn.commit()

                        # insert into transaction
                        self.mycursor.execute(
                            "INSERT INTO transaction (product_name, quantity, amount_per_kg, date, product_id) VALUES(%s, %s, %s, %s, %s)",
                            [self.get_name, Application.product_quantity[i], self.get_price, datetime.now(), self.get_id])
                        self.conn.commit()
                        print("Decreased")

            messagebox.showinfo("Successfully Done", "Transaction completed successfully.")

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")

        finally:
            # Close the cursor and connection in the finally block to ensure it's always closed
            if self.mycursor:
                self.mycursor.close()
            if self.conn.is_connected():
                self.conn.close()


# Create Tkinter root window
root = Tk()
def next_page():
    root.destroy()
    import demo23
#def n_page():
 #   root.destroy()
  #  import demo1


app = Application(root)


        
root.mainloop()





'''ws = Tk()
ws.geometry('400x300')
ws.title('PythonGuides')
ws['bg']='#ffbf00'

f = ("Times bold", 14)
 


def prevPage():
    ws.destroy()
    import demo1

def nextPage():
    ws.destroy()
    import page3

Button(
    ws, 
    text="Previous Page", 
    font=f,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)
Button(
    ws, 
    text="Next Page", 
    font=f,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()'''