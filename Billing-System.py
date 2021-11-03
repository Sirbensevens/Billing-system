import tkinter as ttk
import calendar
import datetime as dt
import random
import tkinter as tk
# how to fix error tkinter has no notebook module
import tkinter.ttk as ttk
from tkinter import *
from tkinter import Toplevel, messagebox

import mysql.connector
import mysql.connector
from PIL import ImageTk, Image
from tkintertable import TableCanvas


# from final import patient
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.tint = "#09417a"
        self.root.configure(bg='#09417a')
        self.root.title("General Store Billing System")
        title = Label(self.root, text="General Store Billing System", bd=12, relief=RIDGE, font=("Arial Black", 20),
                      bg="#09417a", fg="white").pack(fill=X)
        # where admin details will be:
        Admin_btn = tk.Button(self.root, borderwidth=4, width=20, text='Administrator',
                              command=lambda: login()).place(x=20, y=20)
        # ===================================variables=======================================================================================
        self.nutella = IntVar()
        self.noodles = IntVar()
        self.lays = IntVar()
        self.oreo = IntVar()
        self.muffin = IntVar()
        self.silk = IntVar()
        self.vanilla = IntVar()
        self.cucumber = IntVar()
        self.pasta = IntVar()
        self.rice = IntVar()
        self.oil = IntVar()
        self.sugar = IntVar()
        self.ndovu = IntVar()
        self.tea = IntVar()
        self.soap = IntVar()
        self.shampoo = IntVar()
        self.lotion = IntVar()
        self.cream = IntVar()
        self.foam = IntVar()
        self.mask = IntVar()
        self.sanitizer = IntVar()
        self.total_sna = StringVar()
        self.total_gro = StringVar()
        self.total_hyg = StringVar()
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.c_name = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.phone = IntVar()

        # ==========================================customer details label frame=================================================
        global cust_entry, contact_entry, bill_entry
        details = LabelFrame(self.root, text="Customer Details", font=("Arial Black", 12), bg="#09417a", fg="white",
                             relief=GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)
        cust_name = Label(details, text="Customer Name", font=("Arial Black", 14), bg="#09417a", fg="white")
        cust_name.grid(row=0,
                       column=0,
                       padx=15)

        cust_entry = Entry(details, borderwidth=4, width=30, textvariable=self.c_name)
        cust_entry.grid(row=0, column=1, padx=8)

        contact_name = Label(details, text="Contact No.", font=("Arial Black", 14), bg="#09417a", fg="white").grid(
            row=0, column=2, padx=10)

        contact_entry = Entry(details, borderwidth=4, width=30, textvariable=self.phone)
        contact_entry.grid(row=0, column=3, padx=8)

        bill_name = Label(details, text="Bill.No.", font=("Arial Black", 14), bg="#09417a", fg="white").grid(row=0,
                                                                                                             column=4,
                                                                                                             padx=10)

        bill_entry = Entry(details, borderwidth=4, width=30, textvariable=self.bill_no)
        bill_entry.grid(row=0, column=5, padx=8)

        btnstore = Button(details, text="RECS", font=("Arial Black", 12), bg="#09417a", fg="white",
                          command=lambda: store(self)).grid(row=0, column=6, padx=5)

        def store(self):
            # also check in total function
            v1 = cust_entry.get()
            v2 = contact_entry.get()
            v3 = bill_entry.get()

            # trying to avoid saving the same record twice
            # try:
            #   con = mysql.connector.connect(host="localhost",user="root",password="wYnemanor777dfd!@",database="Admins")
            # cur = con.cursor()

            # cur.execute("select * from Customer where bill_no=%s",(self.bill_no.get()))
            # row = cur.fetchone()

            # if row==self.bill_no.get():
            #   messagebox.showerror("Error" , "Invalid User Name And Password", parent = win)

            db = mysql.connector.connect(host='127.0.0.1', user='root', password='wYnemanor777dfd!@', database='Admins')
            conn = db.cursor()

            sql = 'INSERT INTO customer (cust_name,contact_no,bill_no) VALUES(%s,%s,%s)'
            data = [v1, v2, v3]

            conn.execute(sql, data)
            db.commit()

        # =======================================snacks label frame=================================================================
        snacks = LabelFrame(self.root, text="Snacks", font=("Arial Black", 12), bg="#09417a", fg="white", relief=GROOVE,
                            bd=10)
        snacks.place(x=5, y=180, height=380, width=325)

        item1 = Label(snacks, text="Nutella Peanut Spread", font=("Arial Black", 11), bg="#09417a", fg="white").grid(
            row=0, column=0, pady=11)
        item1_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.nutella).grid(row=0, column=1, padx=10)

        item2 = Label(snacks, text="Noodles(1 Pack)", font=("Arial Black", 11), bg="#09417a", fg="white").grid(row=1,
                                                                                                               column=0,
                                                                                                               pady=11)
        item2_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.noodles).grid(row=1, column=1, padx=10)

        item3 = Label(snacks, text="Lays(10ksh)", font=("Arial Black", 11), bg="#09417a", fg="white").grid(row=2,
                                                                                                           column=0,
                                                                                                           pady=11)
        item3_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.lays).grid(row=2, column=1, padx=10)

        item4 = Label(snacks, text="Oreo(20ksh)", font=("Arial Black", 11), bg="#09417a", fg="white").grid(row=3,
                                                                                                           column=0,
                                                                                                           pady=11)
        item4_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.oreo).grid(row=3, column=1, padx=10)

        item5 = Label(snacks, text="Chocolate Muffin", font=("Arial Black", 11), bg="#09417a", fg="White").grid(row=4,
                                                                                                                column=0,
                                                                                                                pady=11)
        item5_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.muffin).grid(row=4, column=1, padx=10)

        item6 = Label(snacks, text="Dairy Milk Silk(60Ksh)", font=("Arial Black", 11), bg="#09417a", fg="white").grid(
            row=5, column=0, pady=11)
        item6_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.silk).grid(row=5, column=1, padx=10)

        item7 = Label(snacks, text="Vanilla(15Ksh)", font=("Arial Black", 11), bg="#09417a", fg="white").grid(row=6,
                                                                                                              column=0,
                                                                                                              pady=11)
        item7_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.vanilla).grid(row=6, column=1, padx=10)
        # ===================================GROCERY=====================================================================================
        grocery = LabelFrame(self.root, text="Grocery", font=("Arial Black", 12), relief=GROOVE, bd=10, bg="#09417a",
                             fg="white")
        grocery.place(x=340, y=180, height=380, width=327)

        item8 = Label(grocery, text="Canned Cucumbers(1kg)", font=("Arial Black", 11), bg="#09417a", fg="white").grid(
            row=0, column=0, pady=11)
        item8_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.cucumber).grid(row=0, column=1, padx=10)

        item9 = Label(grocery, text="Pasta(1kg)", font=("Arial Black", 11), bg="#09417a", fg="white").grid(row=1,
                                                                                                           column=0,
                                                                                                           pady=11)
        item9_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.pasta).grid(row=1, column=1, padx=10)

        item10 = Label(grocery, text="Basmathi Rice(1kg)", font=("Arial Black", 11), bg="#09417a", fg="white").grid(
            row=2, column=0, pady=11)
        item10_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.rice).grid(row=2, column=1, padx=10)

        item11 = Label(grocery, text="Sunflower Oil(1ltr)", font=("Arial Black", 11), bg="#09417a", fg="white").grid(
            row=3, column=0, pady=11)
        item11_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.oil).grid(row=3, column=1, padx=10)

        item12 = Label(grocery, text="Refined Sugar(1kg)", font=("Arial Black", 11), bg="#09417a", fg="white").grid(
            row=4, column=0, pady=11)
        item12_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.sugar).grid(row=4, column=1, padx=10)

        item13 = Label(grocery, text="Ndovu(1kg)", font=("Arial Black", 11), bg="#09417a", fg="white").grid(row=5,
                                                                                                            column=0,
                                                                                                            pady=11)
        item13_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.ndovu).grid(row=5, column=1, padx=10)

        item14 = Label(grocery, text="Tea Powder(1kg)", font=("Arial Black", 11), bg="#09417a", fg="white").grid(row=6,
                                                                                                                 column=0,
                                                                                                                 pady=11)
        item14_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.tea).grid(row=6, column=1, padx=10)
        # ========================================beauty and hygine===============================================================================
        hygine = LabelFrame(self.root, text="Beauty & Hygine", font=("Arial Black", 12), relief=GROOVE, bd=10,
                            bg="#09417a", fg="white")
        hygine.place(x=677, y=180, height=380, width=325)

        item15 = Label(hygine, text="Bathing Soap", font=("Arial Black", 11), bg="#09417a", fg="white").grid(row=0,
                                                                                                             column=0,
                                                                                                             pady=11)
        item15_entry = Entry(hygine, borderwidth=2, width=15, textvariable=self.soap).grid(row=0, column=1, padx=10)

        item16 = Label(hygine, text="Shampoo(1ltr)", font=("Arial Black", 11), bg="#09417a", fg="white").grid(row=1,
                                                                                                              column=0,
                                                                                                              pady=11)
        item16_entry = Entry(hygine, borderwidth=2, width=15, textvariable=self.shampoo).grid(row=1, column=1, padx=10)

        item17 = Label(hygine, text="Body Lotion(1ltr)", font=("Arial Black", 11), bg="#09417a", fg="white").grid(row=2,
                                                                                                                  column=0,
                                                                                                                  pady=11)
        item17_entry = Entry(hygine, borderwidth=2, width=15, textvariable=self.lotion).grid(row=2, column=1, padx=10)

        item18 = Label(hygine, text="Face Cream", font=("Arial Black", 11), bg="#09417a", fg="white").grid(row=3,
                                                                                                           column=0,
                                                                                                           pady=11)
        item18_entry = Entry(hygine, borderwidth=2, width=15, textvariable=self.cream).grid(row=3, column=1, padx=10)

        item19 = Label(hygine, text="Shaving Foam", font=("Arial Black", 11), bg="#09417a", fg="white").grid(row=4,
                                                                                                             column=0,
                                                                                                             pady=11)
        item19_entry = Entry(hygine, borderwidth=2, width=15, textvariable=self.foam).grid(row=4, column=1, padx=10)

        item20 = Label(hygine, text="Face Mask(1piece)", font=("Arial Black", 11), bg="#09417a", fg="white").grid(row=5,
                                                                                                                  column=0,
                                                                                                                  pady=11)
        item20_entry = Entry(hygine, borderwidth=2, width=15, textvariable=self.mask).grid(row=5, column=1, padx=10)

        item21 = Label(hygine, text="Hand Sanitizer(50ml)", font=("Arial Black", 11), bg="#09417a", fg="white").grid(
            row=6, column=0, pady=11)
        item21_entry = Entry(hygine, borderwidth=2, width=15, textvariable=self.sanitizer).grid(row=6, column=1,
                                                                                                padx=10)
        # =====================================================billarea==============================================================================
        billarea = Frame(self.root, bd=10, relief=GROOVE, bg="#09417a")
        billarea.place(x=1010, y=188, width=330, height=372)

        bill_title = Label(billarea, text="Bill Area", font=("Arial Black", 17), bd=7, relief=GROOVE, bg="#09417a",
                           fg="white").pack(fill=X)

        scrol_y = Scrollbar(billarea, orient=VERTICAL)
        self.txtarea = Text(billarea, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        # =================================================billing menu=========================================================================================
        billing_menu = LabelFrame(self.root, text="Billing Summery", font=("Arial Black", 12), relief=GROOVE, bd=10,
                                  bg="#09417a", fg="white")
        billing_menu.place(x=0, y=560, relwidth=1, height=137)

        total_snacks = Label(billing_menu, text="Total Snacks Price", font=("Arial Black", 11), bg="#09417a",
                             fg="white").grid(row=0, column=0)
        total_snacks_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_sna)
        total_snacks_entry.grid(row=0,
                                column=1,
                                padx=10,
                                pady=7)

        total_grocery = Label(billing_menu, text="Total Grocery Price", font=("Arial Black", 11), bg="#09417a",
                              fg="white").grid(row=1, column=0)
        total_grocery_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_gro)
        total_grocery_entry.grid(row=1,
                                 column=1,
                                 padx=10,
                                 pady=7)

        total_hygine = Label(billing_menu, text="Total Beauty & Hygine Price", font=("Arial Black", 11), bg="#09417a",
                             fg="white").grid(row=2, column=0)
        total_hygine_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_hyg)
        total_hygine_entry.grid(row=2,
                                column=1,
                                padx=10,
                                pady=7)

        tax_snacks = Label(billing_menu, text="Snacks Tax", font=("Arial Black", 11), bg="#09417a", fg="white").grid(
            row=0, column=2)
        tax_snacks_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.a).grid(row=0, column=3,
                                                                                                  padx=10, pady=7)

        tax_grocery = Label(billing_menu, text="Grocery Tax", font=("Arial Black", 11), bg="#09417a", fg="white").grid(
            row=1, column=2)
        tax_grocery_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.b).grid(row=1, column=3,
                                                                                                   padx=10, pady=7)

        tax_hygine = Label(billing_menu, text="Beauty & Hygine Tax", font=("Arial Black", 11), bg="#09417a",
                           fg="white").grid(row=2, column=2)
        tax_hygine_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.c).grid(row=2, column=3,
                                                                                                  padx=10, pady=7)

        button_frame = Frame(billing_menu, bd=7, relief=GROOVE, bg="#6C3483")
        button_frame.place(x=830, width=500, height=95)

        button_total = Button(button_frame, text="Total Bill", font=("Arial Black", 12), pady=10, bg="#09417a",
                              fg="white", command=lambda: total(self)).grid(row=0, column=0, padx=12)
        button_clear = Button(button_frame, text="Clear Field", font=("Arial Black", 12), pady=10, bg="#09417a",
                              fg="white", command=lambda: clear(self)).grid(row=0, column=2, padx=10, pady=6)
        button_exit = Button(button_frame, text="Exit", font=("Arial Black", 12), pady=10, bg="#09417a", fg="white",
                             width=8, command=lambda: exit1(self)).grid(row=0, column=6, padx=10, pady=6)

        # A FUNCTION TO RECORD ALL OF THE TRANSACTIONS
        def place(self):
            v1 = bill_entry.get()
            v2 = cust_entry.get()
            v3 = total_snacks_entry.get()
            v4 = total_grocery_entry.get()
            v5 = total_hygine_entry.get()

            db = mysql.connector.connect(host='127.0.0.1', user='root', password='wYnemanor777dfd!@', database='Admins')
            conn = db.cursor()

            sql = 'INSERT INTO history (bill_no,customer,TsnackP,TgroceryP,BandH) VALUES(%s,%s,%s,%s,%s)'
            data = [v1, v2, v3, v4, v5]

            conn.execute(sql, data)
            db.commit()

        btnstore = Button(button_frame, text="TRANS", font=("Arial Black", 12), pady=10, bg="#09417a", fg="white",
                          command=lambda: place(self)).grid(row=0, column=1, padx=10, pady=6)
        intro(self)


def total(self):
    if (self.c_name.get == "" or self.phone.get() == ""):
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
    self.nu = self.nutella.get() * 120
    self.no = self.noodles.get() * 40
    self.la = self.lays.get() * 10
    self.ore = self.oreo.get() * 20
    self.mu = self.muffin.get() * 30
    self.si = self.silk.get() * 60
    self.na = self.vanilla.get() * 15
    total_snacks_price = (
            self.nu +
            self.no +
            self.la +
            self.ore +
            self.mu +
            self.si +
            self.na)
    self.total_sna.set(str(total_snacks_price) + " Ksh")
    self.a.set(str(round(total_snacks_price * 0.05, 3)) + " Ksh")

    self.at = self.cucumber.get() * 42
    self.pa = self.pasta.get() * 120
    self.oi = self.oil.get() * 113
    self.ri = self.rice.get() * 160
    self.su = self.sugar.get() * 55
    self.te = self.tea.get() * 480
    self.da = self.ndovu.get() * 76
    total_grocery_price = (
            self.at +
            self.pa +
            self.oi +
            self.ri +
            self.su +
            self.te +
            self.da)

    self.total_gro.set(str(total_grocery_price) + " ksh")
    self.b.set(str(round(total_grocery_price * 0.01, 3)) + " ksh")

    self.so = self.soap.get() * 30
    self.sh = self.shampoo.get() * 180
    self.cr = self.cream.get() * 130
    self.lo = self.lotion.get() * 500
    self.fo = self.foam.get() * 85
    self.ma = self.mask.get() * 100
    self.sa = self.sanitizer.get() * 20

    total_hygine_price = (
            self.so +
            self.sh +
            self.cr +
            self.lo +
            self.fo +
            self.ma +
            self.sa)

    self.total_hyg.set(str(total_hygine_price) + " Ksh")
    self.c.set(str(round(total_hygine_price * 0.10, 3)) + " Ksh")
    self.total_all_bill = (total_snacks_price +
                           total_grocery_price +
                           total_hygine_price +
                           (round(total_grocery_price * 0.01, 3)) +
                           (round(total_hygine_price * 0.10, 3)) +
                           (round(total_snacks_price * 0.05, 3)))
    self.total_all_bil = str(self.total_all_bill) + " Ksh"
    billarea(self)

    v1 = cust_entry.get()
    v2 = contact_entry.get()
    v3 = bill_entry.get()

    db = mysql.connector.connect(host='127.0.0.1', user='root', password='wYnemanor777dfd!@', database='Admins')
    conn = db.cursor()

    sql = 'INSERT INTO customer (cust_name,contact_no,bill_no) VALUES(%s,%s,%s)'
    data = [v1, v2, v3]

    conn.execute(sql, data)
    db.commit()


def intro(self):
    self.txtarea.delete(1.0, END)
    self.txtarea.insert(END, "\tWELCOME TO SUPER MARKET\n\tPhone-No.739275410")
    self.txtarea.insert(END, f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END, f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END, "\n====================================\n")
    self.txtarea.insert(END, "\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END, "\n====================================\n")


def billarea(self):
    intro(self)
    if self.nutella.get() != 0:
        self.txtarea.insert(END, f"Nutella\t\t {self.nutella.get()}\t{self.nu}\n")
    if self.noodles.get() != 0:
        self.txtarea.insert(END, f"Noodles\t\t {self.noodles.get()}\t{self.no}\n")
    if self.lays.get() != 0:
        self.txtarea.insert(END, f"Lays\t\t {self.lays.get()}\t{self.la}\n")
    if self.oreo.get() != 0:
        self.txtarea.insert(END, f"Oreo\t\t {self.oreo.get()}\t{self.ore}\n")
    if self.muffin.get() != 0:
        self.txtarea.insert(END, f"Muffins\t\t {self.muffin.get()}\t{self.mu}\n")
    if self.silk.get() != 0:
        self.txtarea.insert(END, f"Silk\t\t {self.silk.get()}\t{self.si}\n")
    if self.vanilla.get() != 0:
        self.txtarea.insert(END, f"Vanilla\t\t {self.vanilla.get()}\t{self.na}\n")
    if self.cucumber.get() != 0:
        self.txtarea.insert(END, f"Cucumber\t\t {self.cucumber.get()}\t{self.at}\n")
    if self.pasta.get() != 0:
        self.txtarea.insert(END, f"Pasta\t\t {self.pasta.get()}\t{self.pa}\n")
    if self.rice.get() != 0:
        self.txtarea.insert(END, f"Rice\t\t {self.rice.get()}\t{self.ri}\n")
    if self.oil.get() != 0:
        self.txtarea.insert(END, f"Oil\t\t {self.oil.get()}\t{self.oi}\n")
    if self.sugar.get() != 0:
        self.txtarea.insert(END, f"Sugar\t\t {self.sugar.get()}\t{self.su}\n")
    if self.ndovu.get() != 0:
        self.txtarea.insert(END, f"Ndovu\t\t {self.ndovu.get()}\t{self.da}\n")
    if self.tea.get() != 0:
        self.txtarea.insert(END, f"Tea\t\t {self.tea.get()}\t{self.te}\n")
    if self.soap.get() != 0:
        self.txtarea.insert(END, f"Soap\t\t {self.soap.get()}\t{self.so}\n")
    if self.shampoo.get() != 0:
        self.txtarea.insert(END, f"Shampoo\t\t {self.shampoo.get()}\t{self.sh}\n")
    if self.lotion.get() != 0:
        self.txtarea.insert(END, f"Lotion\t\t {self.lotion.get()}\t{self.lo}\n")
    if self.cream.get() != 0:
        self.txtarea.insert(END, f"Cream\t\t {self.cream.get()}\t{self.cr}\n")
    if self.foam.get() != 0:
        self.txtarea.insert(END, f"Foam\t\t {self.foam.get()}\t{self.fo}\n")
    if self.mask.get() != 0:
        self.txtarea.insert(END, f"Mask\t\t {self.mask.get()}\t{self.ma}\n")
    if self.sanitizer.get() != 0:
        self.txtarea.insert(END, f"Sanitizer\t\t {self.sanitizer.get()}\t{self.sa}\n")

    self.txtarea.insert(END, f"------------------------------------\n")
    if self.a.get() != "0.0 Ksh":
        self.txtarea.insert(END, f"Total Snacks Tax : {self.a.get()}\n")
    if self.b.get() != "0.0 Ksh":
        self.txtarea.insert(END, f"Total Grocery Tax : {self.b.get()}\n")
    if self.c.get() != "0.0 Ksh":
        self.txtarea.insert(END, f"Total Beauty&Hygine Tax : {self.c.get()}\n")
    self.txtarea.insert(END, f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(END, f"------------------------------------\n")


def clear(self):
    self.txtarea.delete(1.0, END)
    self.nutella.set(0)
    self.noodles.set(0)
    self.lays.set(0)
    self.oreo.set(0)
    self.muffin.set(0)
    self.silk.set(0)
    self.vanilla.set(0)
    self.cucumber.set(0)
    self.pasta.set(0)
    self.rice.set(0)
    self.oil.set(0)
    self.sugar.set(0)
    self.ndovu.set(0)
    self.tea.set(0)
    self.soap.set(0)
    self.shampoo.set(0)
    self.lotion.set(0)
    self.cream.set(0)
    self.foam.set(0)
    self.mask.set(0)
    self.sanitizer.set(0)
    self.total_sna.set(0)
    self.total_gro.set(0)
    self.total_hyg.set(0)
    self.a.set(0)
    self.b.set(0)
    self.c.set(0)
    self.c_name.set(0)
    self.bill_no.set(0)
    self.bill_no.set(0)
    self.phone.set(0)


def exit1(self):
    self.root.destroy()


# =======================
root = tk.Tk()


# =======================


def administrator():
    admin = tk.Toplevel()
    admin.title("admin dashboard")
    admin.geometry("1350x700+0+0")
    admin.configure(bg="#343a40")

    # main label
    lbl = tk.Label(admin, text="Welcome Admin", font=("Poppins", 35), fg='blue', bg='#343a40').pack()
    w = Label(admin, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="#33cc00", bg="#343a40",
              font=("helvetica", 35)).pack()

    # w.place(x=450,y=100)

    def exit():
        admin.destroy()

    def show():
        conn = mysql.connector.connect(host="localhost", user="root", password="wYnemanor777dfd!@", database="Admins")
        dbc = conn.cursor()
        dbc.execute("SELECT invoice_no,itemcode,itemname,quantity,total FROM invoice")
        rows = dbc.fetchall()
        data = {}
        for row in rows:
            item = {len(data) + 1: {'Invoice No': row[0], 'Item Code': row[1], 'Item Name': row[2],
                                    'quantity': row[3], 'Total': row[4]}
                    }
            data.update(item)
        table = TableCanvas(userFrame, data=data)
        table.show()

    def showstock():
        conn = mysql.connector.connect(host="localhost", user="root", password="wYnemanor777dfd!@", database="Admins")
        dbc = conn.cursor()
        dbc.execute("SELECT invoice_no,item_name,quantity,description,vendor_name FROM stock")
        rows = dbc.fetchall()
        data = {}
        for row in rows:
            item = {len(data) + 1: {'Invoice No': row[0], 'Item Name': row[1], 'Quantity': row[2],
                                    'description': row[3], 'Supplier': row[4]}
                    }
            data.update(item)
        table = TableCanvas(userFrame, data=data)
        table.show()

    def showcust():
        conn = mysql.connector.connect(host="localhost", user="root", password="wYnemanor777dfd!@", database="Admins")
        dbc = conn.cursor()
        dbc.execute("SELECT cust_name,cust_add,contact_no,bill_no FROM customer")
        rows = dbc.fetchall()
        data = {}
        for row in rows:
            item = {len(data) + 1: {'Customer Name': row[0], 'Customer Address': row[1], 'Contacts': row[2],
                                    'Bill_No': row[3]}
                    }
            data.update(item)
        table = TableCanvas(userFrame, data=data)
        table.show()

    def showven():
        conn = mysql.connector.connect(host="localhost", user="root", password="wYnemanor777dfd!@", database="Admins")
        dbc = conn.cursor()
        dbc.execute("SELECT vendor_name,address,city,account_no,telephone FROM vendor")
        rows = dbc.fetchall()
        data = {}
        for row in rows:
            item = {len(data) + 1: {'Vendor name': row[0], 'Address': row[1], 'City': row[2],
                                    'Account': row[3], 'Telephone': row[4]}
                    }
            data.update(item)
        table = TableCanvas(userFrame, data=data)
        table.show()

    # =================================== special buttons =====================================
    # ======================= frame containing the calender ===================================
    root = LabelFrame(admin, width=240, height=200)
    root.place(x=1070, y=450)

    # defining funtion
    def days():
        a = int(spin1.get())
        b = int(spin2.get())

        cal = calendar.month(b, a)  # pass the year and the month here

        txt.delete(0.0, END)
        txt.insert(INSERT, cal)

    # creating label
    lb1 = Label(root, text="Month", font=("arial", 9, 'bold')).place(x=15, y=0)

    lb2 = Label(root, text="year", font=("arial", 9, 'bold')).place(x=115, y=0)

    # creating spinbox

    spin1 = Spinbox(root, values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), width=4)
    spin1.place(x=60, y=0)

    spin2 = Spinbox(root, from_=1999, to_=2100, width=4)
    spin2.place(x=150, y=0)

    # creating a button
    btn = Button(root, text="show", font=("arial", 9, 'bold'), command=days).place(x=100, y=30)

    # creating textbox
    txt = Text(root, width=24, height=8)
    txt.place(x=20, y=57)

    # ======================== end of frame holding the calender ==================================

    btnlog = tk.Button(admin, text='LOG OUT', width=20, height=2, command=exit).place(x=1200, y=30)
    btnBak = tk.Button(admin, text='BACK', width=20, height=2).place(x=1200, y=100)
    invoices = tk.Button(admin, text='INVOICES', width=40, height=2, command=show).place(x=1050, y=200)
    stock = tk.Button(admin, text='STOCK', width=40, height=2, command=showstock).place(x=1050, y=250)
    customer = tk.Button(admin, text='CUSTOMERS', width=40, height=2, command=showcust).place(x=1050, y=300)
    vendors = tk.Button(admin, text='VENDORS', width=40, height=2, command=showven).place(x=1050, y=350)

    userFrame = Frame(admin)
    userFrame.place(x=330, y=450, width=730, height=200)
    # ========================================== end ===========================================

    # ==========================================================================================
    frame = tk.LabelFrame(admin, bg='royal blue', text="my profile", font=("helvatica", 11, 'bold'), width=320,
                          height=690)
    frame.place(x=0, y=15)

    btn1 = tk.Button(frame, text='My Profile', width=20).place(x=70, y=570)

    canvas = Canvas(frame, width=300, height=250, bg='royalblue')
    canvas.place(x=0, y=0)
    img = ImageTk.PhotoImage(Image.open("user.png"))
    canvas.create_image(9, 5, anchor=NW, image=img)

    lblUY = tk.Label(frame, text='UserRequierments', width=20, bg='royalblue', fg='white', font=("times", 15)).place(
        x=50, y=270)

    # labels
    lbl1 = tk.Label(frame, text='Firstname', width=10, bg='royalblue', fg='white', font=("times", 13)).place(x=100,
                                                                                                             y=300)
    lbl2 = tk.Label(frame, text='Lastname', width=10, bg='royalblue', fg='white', font=("times", 13)).place(x=100,
                                                                                                            y=340)
    lbl3 = tk.Label(frame, text='Email', width=10, bg='royalblue', fg='white', font=("times", 13)).place(x=100, y=380)
    lbl4 = tk.Label(frame, text='Telephone', width=10, bg='royalblue', fg='white', font=("times", 13)).place(x=100,
                                                                                                             y=420)
    lbl5 = tk.Label(frame, text='Store_name', width=10, bg='royalblue', fg='white', font=("times", 13)).place(x=100,
                                                                                                              y=460)
    lbl6 = tk.Label(frame, text='Username', width=10, bg='royalblue', fg='white', font=("times", 13)).place(x=100,
                                                                                                            y=500)

    # entries
    # ent1 = tk.Entry(frame, width=30)
    # ent1.place(x=90, y=300)
    # ent2 = tk.Entry(frame, width=30)
    # ent2.place(x=90, y=340)
    # ent3 = tk.Entry(frame, width=30)
    # ent3.place(x=90, y=380)
    # ent4 = tk.Entry(frame, width=30)
    # ent4.place(x=90, y=420)
    # ent5 = tk.Entry(frame, width=30)
    # ent5.place(x=90, y=460)
    # ent6 = tk.Entry(frame, width=30)
    # ent6.place(x=90, y=500)

    # ==========================================================================================

    def add_stock():
        # remember i changed checked_by with username and supplier with vendor name
        stock = tk.Tk()
        stock.title('Adding stock')
        stock.geometry('870x300')
        stock.configure(bg='#343a40')
        c1 = "#343a40"
        c2 = "white"

        lblm = tk.Label(stock, text='ADDING STOCK', bg=c1, fg='yellow', font=("Times", 20, 'bold'), width=20).pack()

        # labels
        lbl1 = tk.Label(stock, text='Item Name', bg=c1, fg=c2, font=("helvatica", 15), width=10).place(x=0, y=50)
        lbl2 = tk.Label(stock, text='Quantity', bg=c1, fg=c2, font=("helvatica", 15), width=10).place(x=0, y=90)
        lbl3 = tk.Label(stock, text='Description', bg=c1, fg=c2, font=("helvatica", 15), width=10).place(x=0, y=130)
        lbl4 = tk.Label(stock, text='Item Price', bg=c1, fg=c2, font=("helvatica", 15), width=10).place(x=0, y=170)
        lbl5 = tk.Label(stock, text='Supplier', bg=c1, fg=c2, font=("helvatica", 15), width=10).place(x=400, y=50)
        lbl6 = tk.Label(stock, text='Remark', bg=c1, fg=c2, font=("helvatica", 15), width=10).place(x=400, y=90)
        lbl7 = tk.Label(stock, text='Checked By', bg=c1, fg=c2, font=("helvatica", 15), width=10).place(x=400, y=130)

        # Entries
        ent1 = tk.Entry(stock, width=40)
        ent1.place(x=150, y=54)
        ent2 = tk.Entry(stock, width=40)
        ent2.place(x=150, y=94)
        ent3 = tk.Entry(stock, width=40)
        ent3.place(x=150, y=134)
        ent4 = tk.Entry(stock, width=40)
        ent4.place(x=150, y=174)
        ent5 = tk.Entry(stock, width=40)
        ent5.place(x=550, y=54)
        ent6 = tk.Entry(stock, width=40)
        ent6.place(x=550, y=94)
        ent7 = tk.Entry(stock, width=40)
        ent7.place(x=550, y=134)

        # functions
        def store():
            # get the entries
            v1 = ent1.get()
            v2 = ent2.get()
            v3 = ent3.get()
            v4 = ent4.get()
            v5 = ent5.get()
            v6 = ent6.get()
            v7 = ent7.get()
            db = mysql.connector.connect(host='127.0.0.1',
                                         user='root',
                                         passwd='wYnemanor777dfd!@',
                                         database='Admins'
                                         )

            conn = db.cursor()
            sql = "INSERT INTO stock (item_name,quantity,description,item_price,vendor_name,remarks,username) " \
                  "VALUES (%s,%s,%s,%s,%s,%s,%s) "
            data = [v1, v2, v3, v4, v5, v6, v7]

            conn.execute(sql, data)
            db.commit()
            messagebox.showinfo("information", "New item added", parent=stock)

        def clear():
            v1 = ent1.delete(0, END)
            v2 = ent2.delete(0, END)
            v3 = ent3.delete(0, END)
            v4 = ent4.delete(0, END)
            v6 = ent5.delete(0, END)
            v7 = ent6.delete(0, END)
            v8 = ent7.delete(0, END)

        def exit():
            stock.destroy()

        # buttons
        btn1 = tk.Button(stock, text='Add Item', bg='green', fg=c2, width=10, font=("helvetica", 10, 'bold'),
                         command=store).place(x=70, y=250)
        btn2 = tk.Button(stock, text='Clear', bg='blue', fg=c2, width=10, font=("helvetica", 10, 'bold'),
                         command=clear).place(x=170, y=250)
        btn3 = tk.Button(stock, text='Exit', bg='red', fg=c2, width=10, font=("helvetica", 10, 'bold'),
                         command=exit).place(x=270, y=250)
        btn3 = tk.Button(stock, text='Available Stock', bg='red', fg=c2, width=13, font=("helvetica", 10, 'bold'),
                         command=display_stock).place(x=270, y=250)
        stock.mainloop()

    def add_cust():
        root = tk.Tk()
        root.title("Adding customer")
        root.geometry("360x300")
        root.configure(bg="gray")

        # labels
        lbl1 = tk.Label(root, text='Customer Name', bg='gray', fg='white', width=12,
                        font=("helvetica", 10, 'bold')).place(x=0, y=10)
        lbl2 = tk.Label(root, text='Address', bg='gray', fg='white', width=12, font=("helvetica", 10, 'bold')).place(
            x=0, y=50)
        lbl3 = tk.Label(root, text='Phone Number', bg='gray', fg='white', width=12,
                        font=("helvetica", 10, 'bold')).place(x=0, y=90)
        lbl4 = tk.Label(root, text='bill_no', bg='gray', fg='white', width=12, font=("helvetica", 10, 'bold')).place(
            x=0, y=130)

        # Entries
        ent1 = tk.Entry(root, width=30)
        ent1.place(x=130, y=10)

        ent2 = tk.Entry(root, width=30)
        ent2.place(x=130, y=50)

        ent3 = tk.Entry(root, width=30)
        ent3.place(x=130, y=90)

        ent4 = tk.Entry(root, width=30)
        ent4.place(x=130, y=130)

        def add():
            # get the entry data using.get
            # connect with db
            # clear the entries

            v1 = ent1.get()
            v2 = ent2.get()
            v3 = ent3.get()
            v4 = ent4.get()

            db = mysql.connector.connect(host='127.0.0.1', user='root', database='Admins', password='wYnemanor777dfd!@')
            conn = db.cursor()

            sql = "INSERT INTO customer (cust_name,cust_add,contact_no,bill_no) VALUES (%s,%s,%s,%s)"
            data = [v1, v2, v3, v4]

            conn.execute(sql, data)
            db.commit()
            messagebox.showinfo('customers', 'New Customer Added Successfully', parent=root)

        def clear():
            v1 = ent1.delete(0, END)
            v2 = ent2.delete(0, END)
            v3 = ent3.delete(0, END)
            v4 = ent4.delete(0, END)

        def exit():
            root.destroy()

        # button to clear the entries
        btn_add = tk.Button(root, text="Add New", bg='green', fg='white', width=10, command=add).place(x=0, y=200)
        btn_clear = tk.Button(root, text="Clear", bg='blue', fg='white', width=10, command=clear).place(x=100, y=200)
        btn_exit = tk.Button(root, text="Exit", bg='red', fg='white', width=10, command=exit).place(x=200, y=200)
        btn_view = tk.Button(root, text="All customers", bg='red', fg='white', width=16,
                             command=display_customer).place(x=90, y=250)
        root.mainloop()

    def add_vend():
        monty = tk.Tk()
        monty.title("vendor data")
        monty.geometry('350x450')
        monty.configure(bg='white')

        wrapper3 = tk.LabelFrame(monty, text='Adding a new vendor', font=("Poppins", 20, 'bold'), bg='#9999ff',
                                 width=350, height=450)
        wrapper3.place(x=0, y=0)

        # lbl = tk.Label(wrapper3, text='New Suppliers/ vendors', font=("helvetica", 20, 'bold'), bg='#00bfff').place(x=0,y=0)

        # user data section
        lbl1 = Label(wrapper3, text='Vendor Name', width=10, font=("helvetica", 10), bg='#00ffbf', fg='black').place(
            x=0, y=20)
        ent1 = Entry(wrapper3, width=20)
        ent1.place(x=100, y=24)
        lbl2 = Label(wrapper3, text='Address', width=10, font=("helvetica", 10), bg='#00ffbf', fg='white').place(x=0,
                                                                                                                 y=60)
        ent2 = Entry(wrapper3, width=20)
        ent2.place(x=100, y=64)
        lbl3 = Label(wrapper3, text='City', width=10, font=("helvetica", 10), bg='#00ffbf', fg='white').place(x=0,
                                                                                                              y=100)
        ent3 = Entry(wrapper3, width=20)
        ent3.place(x=100, y=104)
        lbl4 = Label(wrapper3, text='Date', width=10, font=("helvetica", 10), bg='#00ffbf', fg='white').place(x=0,
                                                                                                              y=140)
        ent4 = Entry(wrapper3, width=20)
        ent4.place(x=100, y=144)
        lbl5 = Label(wrapper3, text='Amount', width=10, font=("helvetica", 10), bg='#00ffbf', fg='white').place(x=0,
                                                                                                                y=180)
        ent5 = Entry(wrapper3, width=20)
        ent5.place(x=100, y=184)
        lbl6 = Label(wrapper3, text='Account', width=10, font=("helvetica", 10), bg='#00ffbf', fg='white').place(x=0,
                                                                                                                 y=220)
        ent6 = Entry(wrapper3, width=20)
        ent6.place(x=100, y=224)
        lbl7 = Label(wrapper3, text='Telephone', width=10, font=("helvetica", 10), bg='#00ffbf', fg='white').place(x=0,
                                                                                                                   y=260)
        ent7 = Entry(wrapper3, width=20)
        ent7.place(x=100, y=264)

        def store():
            tree = ttk.Treeview()
            v1 = ent1.get()
            v2 = ent2.get()
            v3 = ent3.get()
            v4 = ent4.get()
            v5 = ent5.get()
            v6 = ent6.get()
            v7 = ent7.get()
            db = mysql.connector.connect(host='localhost', user='root', passwd='wYnemanor777dfd!@', database='Admins')
            conn = db.cursor()

            sql = "insert into vendor (vendor_name,address,city,date,amount,account_no,telephone) values(%s,%s,%s,%s," \
                  "%s,%s,%s) "
            data = [v1, v2, v3, v4, v5, v6, v7]

            conn.execute(sql, data)
            db.commit()
            print(conn.lastrowid)
            tree.insert('', 'end', text='', values=(conn.lastrowid, v1, v2, v3, v4, v5, v6))
            messagebox.showinfo('information', 'successfully added a new vendor!!', parent=monty)

        def clear():
            v1 = ent1.delete(0, END)
            v2 = ent2.delete(0, END)
            v3 = ent3.delete(0, END)
            v4 = ent4.delete(0, END)
            v5 = ent5.delete(0, END)
            v6 = ent6.delete(0, END)
            v7 = ent7.delete(0, END)

        def exit():
            monty.destroy()

        btnAdd = Button(wrapper3, text='Add Vendor', bg='green', fg='white', width=10, command=store).place(x=0, y=300)
        btnxt = Button(wrapper3, text='Exit', width=10, bg='red', fg='white', command=exit).place(x=100, y=300)
        btnclear = Button(wrapper3, text='Clear', width=10, bg='blue', fg='white', command=clear).place(x=140, y=350)
        btnall = Button(wrapper3, text='All Vendors', width=15, bg='blue', fg='white', command=display_vendor).place(
            x=0, y=350)
        monty.mainloop()

    def add_user():
        win = tk.Tk()
        win.title("Adding a new user")
        win.geometry("300x380")
        win.configure(bg="white")

        lbl = tk.Label(win, text='REGISTER USER', font=("Times", 20, "bold"), fg='Green', bg='gray')
        lbl.pack()

        frame = ttk.Labelframe(win, width=300, height=400)
        frame.place(x=0, y=40)

        s = ttk.Style(win)
        s.theme_use('clam')
        lbl1 = Label(frame, text='Firstname', bg='red', fg='blue').place(x=0, y=0)
        ent1 = Entry(frame, width=20)
        ent1.place(x=70, y=0)
        lbl2 = Label(frame, text='Lastname').place(x=0, y=30)
        ent2 = Entry(frame, width=20)
        ent2.place(x=70, y=30)
        lbl3 = Label(frame, text='Email').place(x=0, y=60)
        ent3 = Entry(frame, width=20)
        ent3.place(x=70, y=60)
        lbl4 = Label(frame, text='telephone').place(x=0, y=90)
        ent4 = Entry(frame, width=20)
        ent4.place(x=70, y=90)
        lbl5 = Label(frame, text='password').place(x=0, y=120)
        ent5 = Entry(frame, width=20)
        ent5.place(x=70, y=120)
        lbl6 = Label(frame, text='confirm').place(x=0, y=150)
        ent6 = Entry(frame, width=20)
        ent6.place(x=70, y=150)
        lbl7 = Label(frame, text='username').place(x=0, y=180)
        ent7 = Entry(frame, width=20)
        ent7.place(x=70, y=180)

        def store_user():
            tree = ttk.Treeview()
            v1 = ent1.get()
            v2 = ent2.get()
            v3 = ent3.get()
            v4 = ent4.get()
            v5 = ent5.get()
            v6 = ent6.get()
            v7 = ent7.get()
            db = mysql.connector.connect(host='localhost', user='root', passwd='wYnemanor777dfd!@',
                                         database='Admins')
            conn = db.cursor()

            sql = "INSERT INTO user (firstname,lastname,email,telephone,user_pass,confirm,username) VALUES(%s,%s,%s,%s," \
                  "%s,%s,%s) "
            data = [v1, v2, v3, v4, v5, v6, v7]

            conn.execute(sql, data)
            db.commit()
            print(conn.lastrowid)
            tree.insert('', 'end', text='', values=(conn.lastrowid, v1, v2, v3, v4, v5, v6))
            messagebox.showinfo('information', 'successfully added a new User!', parent=win)

        def clear():
            v1 = ent1.delete(0, END)
            v2 = ent2.delete(0, END)
            v3 = ent3.delete(0, END)
            v4 = ent4.delete(0, END)
            v5 = ent5.delete(0, END)
            v6 = ent6.delete(0, END)
            v7 = ent7.delete(0, END)

        def exit():
            win.destroy()

        btn = Button(frame, text='Add User', width=10, bg='green', fg='white', command=store_user).place(x=0, y=240)
        btnE = Button(frame, text='Exit', width=10, bg='red', fg='white', command=exit).place(x=200, y=240)
        btnC = Button(frame, text='Clear', width=10, bg='blue', fg='white', command=clear).place(x=100, y=240)
        btnA = Button(frame, text='All Users', width=25, bg='#99ccff', fg='black', command=display_user).place(x=0,
                                                                                                               y=280)
        win.mainloop()

    def add_invoice():
        prime = tk.Tk()
        prime.title("invoice data")
        prime.geometry("350x380")
        prime.configure(bg='#8080ff')

        lblp = tk.Label(prime, text='Iserting Invoices', bg="#8080ff", font=("Poppins", 20, 'bold')).pack()

        root = tk.LabelFrame(prime, width=350, height=380, bg="#8080ff")
        root.place(x=0, y=50)
        # labels
        lbl1 = tk.Label(root, text='Invoice NO', bg='gray', fg='white', width=12, font=("helvatica", 10, 'bold')).place(
            x=0, y=10)
        lbl2 = tk.Label(root, text='Date', bg='gray', fg='white', width=12, font=("helvatica", 10, 'bold')).place(x=0,
                                                                                                                  y=50)
        lbl3 = tk.Label(root, text='Item Code', bg='gray', fg='white', width=12, font=("helvatica", 10, 'bold')).place(
            x=0, y=90)
        lbl4 = tk.Label(root, text='Quantity', bg='gray', fg='white', width=12, font=("helvatica", 10, 'bold')).place(
            x=0, y=130)
        lbl5 = tk.Label(root, text='Total', bg='gray', fg='white', width=12, font=("helvatica", 10, 'bold')).place(x=0,
                                                                                                                   y=170)

        # Entries
        ent1 = tk.Entry(root, width=30)
        ent1.place(x=130, y=10)

        ent2 = tk.Entry(root, width=30)
        ent2.place(x=130, y=50)

        ent3 = tk.Entry(root, width=30)
        ent3.place(x=130, y=90)

        ent4 = tk.Entry(root, width=30)
        ent4.place(x=130, y=130)

        ent5 = tk.Entry(root, width=30)
        ent5.place(x=130, y=170)

        def add():
            # get the entry data using.get
            # connect with db
            # clear the entries

            v1 = ent1.get()
            v2 = ent2.get()
            v3 = ent3.get()
            v4 = ent4.get()
            v5 = ent5.get()

            db = mysql.connector.connect(host='127.0.0.1', user='root', database='Admins', password='wYnemanor777dfd!@')
            conn = db.cursor()

            sql = "INSERT INTO invoice (invoice_no,invoice_date,itemcode,quantity,total) VALUES (%s,%s,%s,%s,%s)"
            data = [v1, v2, v3, v4, v5]

            conn.execute(sql, data)
            db.commit()
            messagebox.showinfo('Invoices', 'Successfully added a new Invoice', parent=prime)

        def clear():
            v1 = ent1.delete(0, END)
            v2 = ent2.delete(0, END)
            v3 = ent3.delete(0, END)
            v4 = ent4.delete(0, END)
            v5 = ent5.delete(0, END)

        def exit():
            prime.destroy()

            # button to clear the entries

        btn_add = tk.Button(root, text="Add New", bg='green', fg='white', width=10, command=add).place(x=30, y=220)
        btn_clear = tk.Button(root, text="Clear", bg='blue', fg='white', width=10, command=clear).place(x=130, y=220)
        btn_exit = tk.Button(root, text="Exit", bg='red', fg='white', width=10, command=exit).place(x=230, y=220)
        btn_invc = tk.Button(root, text="All Invoices", bg="#00264d", fg='white', width=15,
                             command=display_invoice).place(x=30, y=270)
        prime.mainloop()

    def add_bill():
        star = tk.Tk()
        star.title("Enter Bills")
        star.geometry('340x360')
        c1 = '#9999ff'
        tree = ttk.Treeview()
        star.configure(bg=c1)
        lblx = tk.Label(star, text='BILLS', bg=c1, fg='Gold', font=("poppins", 20, 'bold'), width=10).pack()
        cover = tk.LabelFrame(star, bg=c1, width=360, height=360)
        cover.place(x=0, y=40)
        lblb = Label(cover, text='Bill_No', bg=c1, width=10).place(x=0, y=0)
        entb = Entry(cover, width=20)
        entb.place(x=70, y=0)
        lbl1 = Label(cover, text='Vendor', bg=c1, width=10).place(x=0, y=20)
        ent1 = Entry(cover, width=20)
        ent1.place(x=70, y=20)
        lbl2 = Label(cover, text='Address', bg=c1, width=10).place(x=0, y=40)
        ent2 = Entry(cover, width=20)
        ent2.place(x=70, y=40)
        lbl3 = Label(cover, text='Date', bg=c1, width=10).place(x=0, y=60)
        ent3 = Entry(cover, width=20)
        ent3.place(x=70, y=60)
        lbl4 = Label(cover, text='Amount', bg=c1, width=10).place(x=0, y=80)
        ent4 = Entry(cover, width=20)
        ent4.place(x=70, y=80)
        lbl5 = Label(cover, text='Account', bg=c1, width=10).place(x=0, y=100)
        ent5 = Entry(cover, width=20)
        ent5.place(x=70, y=100)
        lbl6 = Label(cover, text='Customer', bg=c1, width=10).place(x=0, y=120)
        ent6 = Entry(cover, width=20)
        ent6.place(x=70, y=120)

        def new_bill():
            vb = entb.get()
            v1 = ent1.get()
            v2 = ent2.get()
            v3 = ent3.get()
            v4 = ent4.get()
            v5 = ent5.get()
            v6 = ent6.get()
            db = mysql.connector.connect(host='localhost', user='root', passwd='wYnemanor777dfd!@',
                                         database='Admins')
            conn = db.cursor()

            sql = "insert into bill (bill_no,vendor_name,address,date,amount,account,customer) values(%s,%s,%s,%s,%s," \
                  "%s,%s) "
            data = [vb, v1, v2, v3, v4, v5, v6]

            conn.execute(sql, data)
            db.commit()
            print(conn.lastrowid)
            tree.insert('', 'end', text='', values=(conn.lastrowid, v1, v2, v3, v4, v5, v6))
            messagebox.showinfo('information', 'successfully added a new bill!!', parent=star)

        def clear():
            v1 = ent1.delete(0, END)
            v2 = ent2.delete(0, END)
            v3 = ent3.delete(0, END)
            v4 = ent4.delete(0, END)
            v5 = ent5.delete(0, END)
            v6 = ent6.delete(0, END)

        def exit():
            star.destroy()

        btn1 = tk.Button(cover, text='New Bill', width=10, command=new_bill).place(x=220, y=0)
        btn2 = tk.Button(cover, text='Exit Bill', width=10, command=exit).place(x=220, y=30)
        btn3 = tk.Button(cover, text='Clear', width=10, command=clear).place(x=220, y=60)
        btn4 = tk.Button(cover, text='Show Bills', width=10, command=display_bill).place(x=220, y=90)

        star.mainloop()

    # first column -- add
    btnstock = tk.Button(admin, text='Stock', width=20, command=add_stock).place(x=400, y=200)
    btncust = tk.Button(admin, text='Customer', width=20, command=add_cust).place(x=400, y=250)
    btnvendor = tk.Button(admin, text='Vendor', width=20, command=add_vend).place(x=400, y=300)
    btnuser = tk.Button(admin, text='Users', width=20, command=add_user).place(x=400, y=350)
    btninvoice = tk.Button(admin, text='Invoice', width=20, command=add_invoice).place(x=400, y=400)

    def display_stock():
        win = tk.Tk()
        win.title("vendor info")
        win.geometry("1100x400")
        c1 = 'blue'

        framex = tk.LabelFrame(win, width=1100, height=500)
        framex.place(x=0, y=30)

        lbla = tk.Label(win, text='Viewing Available Stock', font=("poppins", 20, 'bold'), width=20).pack()

        entx = tk.Entry(framex, width=30)
        entx.place(x=10, y=10)

        btnx = tk.Button(framex, text='Search', bg="#bfff00", fg='black', width=10).place(x=200, y=10)

        def getrow(event):
            return True

        def update(rows):
            tree.delete(*tree.get_children())
            for x in rows:
                tree.insert('', 'end', values=x)

        # search option code
        def search():
            q2 = entx.get()
            sql = "SELECT * FROM stock WHERE item_name LIKE '%" + q2 + "%' "  # OR lname '%"+q2+"%'"
            conn.execute(sql)
            rows = conn.fetchall()
            update(rows)

        def clearx():
            sql = "select * from stock"
            conn.execute(sql)
            rows = conn.fetchall()
            update(rows)

        btnx = tk.Button(framex, text='Search', bg="#bfff00", fg='black', width=10, command=search).place(x=200, y=10)
        btny = tk.Button(framex, text='clear', bg="#bfff00", fg='black', width=10, command=clearx).place(x=500, y=10)
        # end of search option

        db = mysql.connector.connect(host='localhost', user='root', passwd='wYnemanor777dfd!@', database='Admins')
        conn = db.cursor()

        tree = ttk.Treeview(framex, column=(1, 2, 3, 4, 5, 6, 7, 8), show='headings', height='12', selectmode='browse')
        tree.column("1", minwidth=40, width=100, stretch=NO)
        tree.column("2", minwidth=40, width=100, stretch=NO)
        tree.column("3", minwidth=40, width=200, stretch=NO)
        tree.column("4", minwidth=40, width=100, stretch=NO)
        tree.column("5", minwidth=40, width=100, stretch=NO)
        tree.column("6", minwidth=40, width=170, stretch=NO)
        tree.column("7", minwidth=40, width=150, stretch=NO)
        tree.column("8", minwidth=40, width=100, stretch=NO)

        tree.place(x=0, y=70)

        s = ttk.Style(win)
        s.theme_use('classic')  # clam, winnative, alt, xpnative, classic, vista

        s.configure('.', font=('Helvetica', 10))
        s.configure('Treeview.Heading', foreground='#004d00', font=('Helvetica', 10, 'bold'))

        tree.heading(1, text='Item Name')
        tree.heading(2, text='Quantity')
        tree.heading(3, text='Description')
        tree.heading(4, text='Item Price')
        tree.heading(5, text='Invoice No')
        tree.heading(6, text='Supplier')
        tree.heading(7, text='Remarks')
        tree.heading(8, text='Checked By')

        tree.bind('<Double 1>', getrow)

        sql = 'SELECT item_name,quantity,description,item_price,invoice_no,vendor_name,remarks,username FROM stock'
        conn.execute(sql)
        rows = conn.fetchall()
        update(rows)

        # vsb = ttk.Scrollbar(framex,orient='vertical')
        # vsb.configure(command=tree.yview)
        # tree.configure(yscrollcommand=vsb.set)
        # vsb.place(x=1070,y=70)

        vsb = ttk.Scrollbar(framex, orient="vertical", command=tree.yview)
        vsb.place(x=30 + 1010 + 2, y=70, height=120 + 20)
        tree.configure(yscrollcommand=vsb.set)

        def delete_data():
            db = mysql.connector.connect(host='localhost', user='root', passwd='wYnemanor777dfd!@', database='Admins')
            conn = db.cursor()
            selected_item = tree.selection()[0]
            print(tree.item(selected_item)['values'])
            invent = tree.item(selected_item)['values'][0]
            del_query = "DELETE FROM stock where item_name = %s"
            sel_data = (invent,)
            conn.execute(del_query, sel_data)
            db.commit()
            tree.delete(selected_item)
            messagebox.showinfo('Success', 'Stock data removed successfully !', parent=win)

        def exit():
            win.destroy()

        free = tk.Button(framex, text='Remove Stock', width=10, fg='white', bg='red', command=delete_data).place(x=300,
                                                                                                                 y=10)
        # btnD = Button(framex, text='Update', width=10, bg='#bf4080', fg='white', command=update(rows)).place(x=150,
        #                                                                                                     y=270)
        free2 = tk.Button(framex, text='Back', width=10, fg='white', bg='black', command=exit).place(x=400, y=10)
        win.mainloop()

    def display_customer():
        win = tk.Tk()
        win.title("All customers present")
        win.geometry("600x500")
        win.configure(bg="#ff4d4d")

        c1 = '#ff4d4d'

        framez = tk.LabelFrame(win, bg=c1, width=600, height=500)
        framez.place(x=0, y=30)

        s = ttk.Style(win)

        lbla = tk.Label(win, text='Viewing customers', font=("poppins", 15, 'bold'), bg=c1, width=20).pack()

        entx = tk.Entry(framez, width=30)
        entx.place(x=10, y=10)

        def getrow(event):
            return True

        def update(rows):
            tree.delete(*tree.get_children())
            for x in rows:
                tree.insert('', 'end', values=x)

        # search option code
        def search():
            q2 = entx.get()
            sql = "SELECT * FROM customer WHERE cust_name LIKE '%" + q2 + "%'"  # OR lname '%"+q2+"%'"
            conn.execute(sql)
            rows = conn.fetchall()
            update(rows)

        def clearx():
            sql = "select * from customer"
            conn.execute(sql)
            rows = conn.fetchall()
            update(rows)

        btnx = tk.Button(framez, text='Search', bg="#bfff00", fg='black', width=10, command=search).place(x=200, y=10)
        btny = tk.Button(framez, text='clear', bg="#bfff00", fg='black', width=10, command=clearx).place(x=500, y=10)

        db = mysql.connector.connect(host='localhost', user='root', passwd='wYnemanor777dfd!@', database='Admins')
        conn = db.cursor()

        tree = ttk.Treeview(framez, columns=(1, 2, 3, 4), show='headings', height='13')
        tree.place(x=0, y=70)

        s = ttk.Style(framez)
        s.theme_use('vista')  # clam, winnative, alt, xpnative, classic, vista

        s.configure('.', font=('Helvetica', 10))
        s.configure('Treeview.Heading', foreground='#8000ff', font=('Helvetica', 10, 'bold'))

        tree.column("1", minwidth=40, width=120, stretch=NO)
        tree.column("2", minwidth=40, width=120, stretch=NO)
        tree.column("3", minwidth=40, width=120, stretch=NO)
        tree.column("4", minwidth=40, width=120, stretch=NO)

        tree.heading(1, text='Customer Name')
        tree.heading(2, text='Address')
        tree.heading(3, text='Contact No')
        tree.heading(4, text='Bill No')

        tree.bind('<Double 1>', getrow)

        sql = 'SELECT cust_name,cust_add,contact_no,bill_no FROM customer'
        conn.execute(sql)
        rows = conn.fetchall()
        update(rows)

        vsb = ttk.Scrollbar(framez, orient="vertical", command=tree.yview)
        vsb.place(x=500, y=70, height=70 + 20)
        tree.configure(yscrollcommand=vsb.set)

        def delete_data():
            selected_item = tree.selection()[0]
            print(tree.item(selected_item)['values'])
            customer = tree.item(selected_item)['values'][0]
            del_query = "DELETE FROM customer where cust_name = %s"
            sel_data = (customer,)
            conn.execute(del_query, sel_data)
            db.commit()
            tree.delete(selected_item)
            messagebox.showinfo('Success', 'Customer Removed successfully !', parent=win)

        def exit():
            win.destroy()

        btnd = tk.Button(framez, text="Delete", width=10, bg='red', fg='white', command=delete_data).place(x=300, y=10)
        # btnb = tk.Button(framez, text="update", width=10, bg='black', fg='white', command=update(rows)).place(x=500,
        #                                                                                                     y=120)
        btne = tk.Button(framez, text="Exit", width=10, bg='#bf4080', fg='white', command=exit).place(x=400, y=10)

        win.mainloop()

    def display_vendor():
        win = tk.Tk()
        win.title("vendor info")
        win.geometry("900x300")
        win.configure(bg="#6666cc")
        c1 = 'blue'
        c2 = "#6666cc"

        s = ttk.Style(win)

        framez = tk.LabelFrame(win, text="vendor data", bg=c2, width=900, height=300)
        framez.place(x=0, y=70)

        lbla = tk.Label(win, text='Viewing Vendors', font=("poppins", 15, 'bold'), bg=c2, width=20).pack()

        entx = tk.Entry(win, width=30)
        entx.place(x=0, y=40)

        # btnx = tk.Button(win, text='Search', bg="#bfff00", fg='black', width=10).place(x=200, y=40)

        def getrow(event):
            return True

        def update(rows):
            tree.delete(*tree.get_children())
            for x in rows:
                tree.insert('', 'end', values=x)

        # search option code
        def search():
            q2 = entx.get()
            sql = "SELECT * FROM vendor WHERE vendor_name LIKE '%" + q2 + "%'"  # OR lname '%"+q2+"%'"
            conn.execute(sql)
            rows = conn.fetchall()
            update(rows)

        def clearx():
            sql = "select * from vendor"
            conn.execute(sql)
            rows = conn.fetchall()
            update(rows)

        btnx = tk.Button(win, text='Search', bg="#bfff00", fg='black', width=10, command=search).place(x=200, y=40)
        btny = tk.Button(win, text='clear', bg="#bfff00", fg='black', width=10, command=clearx).place(x=500, y=40)

        db = mysql.connector.connect(host='localhost', user='root', passwd='wYnemanor777dfd!@', database='Admins')
        conn = db.cursor()

        tree = ttk.Treeview(framez, columns=(1, 2, 3, 4, 5, 6, 7), show='headings', height='12')
        tree.place(x=0, y=0)

        s = ttk.Style(framez)
        s.theme_use('vista')  # clam, winnative, alt, xpnative, classic, vista

        s.configure('.', font=('Helvetica', 10))
        s.configure('Treeview.Heading', foreground='#8000ff', font=('Helvetica', 10, 'bold'))

        tree.column("1", minwidth=40, width=120, stretch=NO)
        tree.column("2", minwidth=40, width=120, stretch=NO)
        tree.column("3", minwidth=40, width=120, stretch=NO)
        tree.column("4", minwidth=40, width=120, stretch=NO)
        tree.column("5", minwidth=40, width=120, stretch=NO)
        tree.column("6", minwidth=40, width=120, stretch=NO)
        tree.column("7", minwidth=40, width=120, stretch=NO)

        tree.heading(1, text='Vendor name')
        tree.heading(2, text='Address')
        tree.heading(3, text='City')
        tree.heading(4, text='Date')
        tree.heading(5, text='Balance')
        tree.heading(6, text='Account')
        tree.heading(7, text='Telephone')

        tree.bind('<Double 1>', getrow)

        sql = 'SELECT vendor_name,address,city,date,amount,account_no,telephone FROM vendor'
        conn.execute(sql)
        rows = conn.fetchall()
        update(rows)

        # adding vsroll bar
        vsb = ttk.Scrollbar(framez, orient="vertical", command=tree.yview)
        vsb.place(x=20 + 850 + 2, y=0, height=70 + 20)
        tree.configure(yscrollcommand=vsb.set)

        def delete_data():
            selected_item = tree.selection()[0]
            print(tree.item(selected_item)['values'])
            vendor = tree.item(selected_item)['values'][0]
            del_query = "DELETE FROM vendor where vendor_name = %s"
            sel_data = (vendor,)
            conn.execute(del_query, sel_data)
            db.commit()
            tree.delete(selected_item)
            messagebox.showinfo('Success', 'Vendor deactivated successfully !', parent=win)

        def exit():
            win.destroy()

        btnd = tk.Button(win, text="Delete", width=10, bg='red', fg='white', command=delete_data).place(x=300, y=40)
        btnb = tk.Button(win, text="Back", width=10, bg='black', fg='white', command=exit).place(x=400, y=40)
        win.mainloop()

    def display_user():
        sun = tk.Tk()
        sun.title("all users")
        sun.geometry("1000x350")

        frame2 = ttk.Labelframe(sun, text='All Users', width=1000, height=350)
        frame2.place(x=0, y=70)

        lbl = tk.Label(sun, text='Viewing Users', font=("poppins", 15, 'bold'), width=20).pack()

        entx = tk.Entry(sun, width=30)
        entx.place(x=10, y=40)

        # btnx = tk.Button(sun, text='Search', bg="#bfff00", fg='black', width=10).place(x=200, y=40)

        def getrow(event):
            return True

        def update(rows):
            tree.delete(*tree.get_children())
            for x in rows:
                tree.insert('', 'end', values=x)

        # search option code
        def search():
            q2 = entx.get()
            sql = "SELECT * FROM user WHERE username LIKE '%" + q2 + "%'"  # OR lname '%"+q2+"%'"
            conn.execute(sql)
            rows = conn.fetchall()
            update(rows)

        def clearx():
            sql = "select * from user"
            conn.execute(sql)
            rows = conn.fetchall()
            update(rows)

        btnx = tk.Button(sun, text='Search', bg="#bfff00", fg='black', width=10, command=search).place(x=200, y=40)
        btny = tk.Button(sun, text='clear', bg="#bfff00", fg='black', width=10, command=clearx).place(x=500, y=40)

        db = mysql.connector.connect(host='localhost', user='root', passwd='wYnemanor777dfd!@', database='Admins')
        conn = db.cursor()

        tree = ttk.Treeview(frame2, column=(1, 2, 3, 4, 5, 6, 7), show='headings', height='12')
        tree.column("1", minwidth=40, width=120, stretch=NO)
        tree.column("2", minwidth=40, width=120, stretch=NO)
        tree.column("3", minwidth=40, width=120, stretch=NO)
        tree.column("4", minwidth=40, width=170, stretch=NO)
        tree.column("5", minwidth=40, width=120, stretch=NO)
        tree.column("6", minwidth=40, width=120, stretch=NO)
        tree.column("7", minwidth=40, width=120, stretch=NO)
        tree.place(x=0, y=0)

        s = ttk.Style(frame2)
        s.theme_use('clam')  # clam, winnative, alt, xpnative, classic, vista

        s.configure('.', font=('Helvetica', 10))
        s.configure('Treeview.Heading', foreground='blue', font=('Helvetica', 10, 'bold'))

        tree.heading(1, text='user_ID')
        tree.heading(2, text='Firstname')
        tree.heading(3, text='Lastname')
        tree.heading(4, text='Email')
        tree.heading(5, text='Telephone')
        tree.heading(6, text='User_Password')
        tree.heading(7, text='Username')

        tree.bind('<Double 1>', getrow)

        sql = 'select user_id,firstname,lastname,email,telephone,user_pass,username from user'
        conn.execute(sql)
        rows = conn.fetchall()
        update(rows)

        vsb = ttk.Scrollbar(frame2, orient="vertical", command=tree.yview)
        vsb.place(x=0 + 900 + 20, y=0, height=70 + 6)
        tree.configure(yscrollcommand=vsb.set)

        def delete_data():
            selected_item = tree.selection()[0]
            print(tree.item(selected_item)['values'])
            vendor = tree.item(selected_item)['values'][0]
            del_query = "DELETE FROM user where user_id = %s"
            sel_data = (vendor,)
            conn.execute(del_query, sel_data)
            db.commit()
            tree.delete(selected_item)
            messagebox.showinfo('Success', 'User removed successfully !', parent=sun)

        def exit():
            sun.destroy()

        btnD = Button(sun, text='Delete User', width=10, bg='red', fg='white', command=delete_data).place(x=300,
                                                                                                          y=40)
        btnD = Button(sun, text='Back', width=10, bg='blue', fg='white', command=exit).place(x=400, y=40)

        sun.mainloop()

    def display_invoice():
        win = tk.Tk()
        win.title("All invoices present")
        win.geometry("800x350")

        c1 = '#262673'

        win.configure(bg=c1)

        framez = tk.LabelFrame(win, bg=c1, width=800, height=380)
        framez.place(x=0, y=30)

        s = ttk.Style(win)

        lbla = tk.Label(win, text='INVOICES', font=("poppins", 15, 'bold'), bg=c1, fg="#ace600", width=20).pack()

        entx = tk.Entry(framez, width=30)
        entx.place(x=10, y=35)

        # btnx = tk.Button(framez, text='Search', bg="#bfff00", fg='black', width=10).place(x=200, y=30)

        def getrow(event):
            return True

        def update(rows):
            tree.delete(*tree.get_children())
            for x in rows:
                tree.insert('', 'end', values=x)

        # search option code
        def search():
            q2 = entx.get()
            sql = "SELECT * FROM invoice WHERE itemname LIKE '%" + q2 + "%'"  # OR lname '%"+q2+"%'"
            conn.execute(sql)
            rows = conn.fetchall()
            update(rows)

        def clearx():
            sql = "select * from invoice"
            conn.execute(sql)
            rows = conn.fetchall()
            update(rows)

        btnx = tk.Button(framez, text='Search', bg="#bfff00", fg='black', width=10, command=search).place(x=200, y=30)
        btny = tk.Button(framez, text='clear', bg="#bfff00", fg='black', width=10, command=clearx).place(x=500, y=30)

        db = mysql.connector.connect(host='localhost', user='root', passwd='wYnemanor777dfd!@', database='Admins')
        conn = db.cursor()

        tree = ttk.Treeview(framez, columns=(1, 2, 3, 4, 5, 6), show='headings', height='10')
        tree.place(x=0, y=70)

        s = ttk.Style(framez)
        s.theme_use('vista')  # clam, winnative, alt, xpnative, classic, vista

        s.configure('.', font=('Helvetica', 10))
        s.configure('Treeview.Heading', foreground='#8000ff', font=('Helvetica', 10, 'bold'))

        tree.column("1", minwidth=40, width=120, stretch=NO)
        tree.column("2", minwidth=40, width=120, stretch=NO)
        tree.column("3", minwidth=40, width=120, stretch=NO)
        tree.column("4", minwidth=40, width=120, stretch=NO)
        tree.column("5", minwidth=40, width=120, stretch=NO)
        tree.column("6", minwidth=40, width=120, stretch=NO)

        tree.heading(1, text='Invoice No')
        tree.heading(2, text='Date')
        tree.heading(3, text='Item Code')
        tree.heading(4, text='item Name')
        tree.heading(5, text='Quantity')
        tree.heading(6, text='Total Amount')

        tree.bind('<Double 1>', getrow)

        sql = 'SELECT invoice_no,invoice_date,itemcode,itemname,quantity,total FROM invoice'
        conn.execute(sql)
        rows = conn.fetchall()
        update(rows)

        vsb = ttk.Scrollbar(framez, orient="vertical", command=tree.yview)
        vsb.place(x=750, y=70, height=70 + 20)
        tree.configure(yscrollcommand=vsb.set)

        def delete_data():
            selected_item = tree.selection()[0]
            print(tree.item(selected_item)['values'])
            invoice = tree.item(selected_item)['values'][0]
            del_query = "DELETE FROM invoice where invoice_no = %s"
            sel_data = (invoice,)
            conn.execute(del_query, sel_data)
            db.commit()
            tree.delete(selected_item)
            messagebox.showinfo('Success', 'invoice Removed successfully !', parent=win)

        def exit():
            win.destroy()

        btnd = tk.Button(framez, text="Delete", width=10, bg='red', fg='white', command=delete_data).place(x=300, y=30)
        btne = tk.Button(framez, text="Exit", width=10, bg='black', fg='white', command=exit).place(x=400, y=30)

        win.mainloop()

    # second column -- display and update
    btnstock2 = tk.Button(admin, text='View Stock', width=20, command=display_stock).place(x=600, y=200)
    btncust2 = tk.Button(admin, text='View Customer', width=20, command=display_customer).place(x=600, y=250)
    btnvendor2 = tk.Button(admin, text='View Vendor', width=20, command=display_vendor).place(x=600, y=300)
    btnuser2 = tk.Button(admin, text='View Users', width=20, command=display_user).place(x=600, y=350)
    btninvoice2 = tk.Button(admin, text='View Invoices', width=20, command=display_invoice).place(x=600, y=400)

    def display_bill():
        win = tk.Tk()
        win.title("All invoices present")
        win.geometry("800x400")

        c1 = '#6666ff'
        win.configure(bg=c1)

        label = tk.Label(win, text='List of All Bills', font=("times", 16, 'bold'), bg=c1, fg="black").pack()
        framez = tk.LabelFrame(win, width=800, height=400, bg=c1)
        framez.place(x=0, y=50)

        entx = tk.Entry(framez, width=30)
        entx.place(x=10, y=20)

        btnx = tk.Button(framez, text='Search', bg="#bfff00", fg='black', width=10).place(x=200, y=20)

        def getrow(event):
            return True

        def update(rows):
            tree.delete(*tree.get_children())
            for x in rows:
                tree.insert('', 'end', values=x)

        # search option code
        def search():
            q2 = entx.get()
            sql = "SELECT * FROM bill WHERE bill_no LIKE '%" + q2 + "%'"  # OR lname '%"+q2+"%'"
            conn.execute(sql)
            rows = conn.fetchall()
            update(rows)

        def clearx():
            sql = "select * from bill"
            conn.execute(sql)
            rows = conn.fetchall()
            update(rows)

        btnx = tk.Button(framez, text='Search', bg="#bfff00", fg='black', width=10, command=search).place(x=200, y=20)
        btny = tk.Button(framez, text='clear', bg="#bfff00", fg='black', width=10, command=clearx).place(x=500, y=20)

        db = mysql.connector.connect(host='localhost', user='root', passwd='wYnemanor777dfd!@', database='Admins')
        conn = db.cursor()

        tree = ttk.Treeview(framez, column=(1, 2, 3, 4, 5, 6, 7), show='headings', height='12')
        tree.column("1", minwidth=40, width=90, stretch=NO)
        tree.column("2", minwidth=40, width=90, stretch=NO)
        tree.column("3", minwidth=40, width=90, stretch=NO)
        tree.column("4", minwidth=40, width=90, stretch=NO)
        tree.column("5", minwidth=40, width=90, stretch=NO)
        tree.column("6", minwidth=40, width=90, stretch=NO)
        tree.column("6", minwidth=40, width=90, stretch=NO)

        tree.place(x=0, y=70)

        s = ttk.Style(framez)
        s.theme_use('xpnative')  # clam, winnative, alt, xpnative, classic, vista

        s.configure('.', font=('Helvetica', 10))
        s.configure('Treeview.Heading', foreground='#0d1a00', font=('Helvetica', 10, 'bold'))

        tree.heading(1, text='Bill No')
        tree.heading(2, text='Vendor name')
        tree.heading(3, text='Address')
        tree.heading(4, text='Date')
        tree.heading(5, text='Amount')
        tree.heading(6, text='Account')
        tree.heading(7, text='Customer')

        tree.bind('<Double 1>', getrow)

        sql = 'select bill_no,vendor_name,address,date,amount,account,customer from bill'
        conn.execute(sql)
        rows = conn.fetchall()
        update(rows)

        vsb = ttk.Scrollbar(framez, orient="vertical", command=tree.yview)
        vsb.place(x=30 + 720 + 2, y=70, height=130 + 20)
        tree.configure(yscrollcommand=vsb.set)

        def del_bill():
            db = mysql.connector.connect(host='localhost', user='root', passwd='wYnemanor777dfd!@', database='Admins')
            conn = db.cursor()
            selected_item = tree.selection()[0]
            print(tree.item(selected_item)['values'])
            vendor = tree.item(selected_item)['values'][0]
            del_query = "DELETE FROM bill where vendor_name = %s"
            sel_data = (vendor,)
            conn.execute(del_query, sel_data)
            db.commit()
            tree.delete(selected_item)
            messagebox.showinfo('Success', 'Bill deleted successfully !', parent=win)

        def exit():
            win.destroy()

        free = tk.Button(framez, text='Delete Bill', fg='white', bg='red', command=del_bill, width=10).place(x=300,
                                                                                                             y=20)
        btnb = tk.Button(framez, text="Back", width=10, bg='black', fg='white', command=exit).place(x=400, y=20)
        win.mainloop()

    def display_history():
        win = tk.Tk()
        win.title("All daily Transaction")
        win.geometry("900x400")
        c1 = 'blue'

        s = ttk.Style(win)

        framez = tk.LabelFrame(win, text="Transactions", width=900, height=330)
        framez.place(x=0, y=70)

        lbla = tk.Label(win, text='Viewing Transactions', font=("poppins", 15, 'bold'), width=20).pack()

        entx = tk.Entry(win, width=30)
        entx.place(x=10, y=45)

        btnx = tk.Button(win, text='Search', bg="#bfff00", fg='black', width=10).place(x=200, y=40)

        def getrow(event):
            return True

        def update(rows):
            tree.delete(*tree.get_children())
            for x in rows:
                tree.insert('', 'end', values=x)

        # search option code
        def search():
            q2 = entx.get()
            sql = "SELECT * FROM history WHERE customer LIKE '%" + q2 + "%'"  # OR lname '%"+q2+"%'"
            conn.execute(sql)
            rows = conn.fetchall()
            update(rows)

        def clearx():
            sql = "select customer,TsnackP,TgroceryP,BandH,bill_no from history"
            conn.execute(sql)
            rows = conn.fetchall()
            update(rows)

        btnx = tk.Button(win, text='Search', bg="#bfff00", fg='black', width=10, command=search).place(x=200, y=40)
        btny = tk.Button(win, text='clear', bg="#bfff00", fg='black', width=10, command=clearx).place(x=500, y=40)

        db = mysql.connector.connect(host='localhost', user='root', passwd='wYnemanor777dfd!@', database='Admins')
        conn = db.cursor()

        tree = ttk.Treeview(framez, columns=(1, 2, 3, 4, 5), show='headings', height='12')
        tree.place(x=0, y=0)

        s = ttk.Style(framez)
        s.theme_use('vista')  # clam, winnative, alt, xpnative, classic, vista

        s.configure('.', font=('Helvetica', 10))
        s.configure('Treeview.Heading', foreground='#8000ff', font=('Helvetica', 10, 'bold'))

        tree.column("1", minwidth=40, width=170, stretch=NO)
        tree.column("2", minwidth=40, width=170, stretch=NO)
        tree.column("3", minwidth=40, width=170, stretch=NO)
        tree.column("4", minwidth=40, width=170, stretch=NO)
        tree.column("5", minwidth=40, width=170, stretch=NO)

        tree.heading(1, text='Customer Name')
        tree.heading(2, text='Total Snack Price')
        tree.heading(3, text='Total Grocery Price')
        tree.heading(4, text='Beauty And Hygine')
        tree.heading(5, text='Bill No')

        tree.bind('<Double 1>', getrow)

        sql = 'SELECT customer,TsnackP,TgroceryP,BandH,bill_no FROM history'
        conn.execute(sql)
        rows = conn.fetchall()
        update(rows)

        vsb = ttk.Scrollbar(framez, orient="vertical", command=tree.yview)
        vsb.place(x=30 + 830 + 2, y=0, height=70 + 20)
        tree.configure(yscrollcommand=vsb.set)

        def delete_data():
            selected_item = tree.selection()[0]
            print(tree.item(selected_item)['values'])
            hist = tree.item(selected_item)['values'][0]
            del_query = "DELETE FROM history where bill_no = %s"
            sel_data = (hist,)
            conn.execute(del_query, sel_data)
            db.commit()
            tree.delete(selected_item)
            messagebox.showinfo('Success', 'Transaction(s) deleted successfully !', parent=win)

        def exit():
            win.destroy()

        btnd = tk.Button(win, text="Delete", width=10, bg='red', fg='white', command=delete_data).place(x=300, y=40)
        btnb = tk.Button(win, text="Back", width=10, bg='black', fg='white', command=exit).place(x=400, y=40)
        win.mainloop()

    def display_assets():
        win = tk.Tk()
        win.title("Reports")
        win.geometry("900x570")
        c1 = '#9999ff'
        win.configure(bg=c1)

        def add_asset():
            root = tk.Tk()
            root.title("Asset Enter Window")
            root.geometry("400x300")
            framez = tk.LabelFrame(root, width=400, height=300)
            framez.place(x=0, y=0)
            # labels
            lbl1 = tk.Label(root, text='Asset Name', width=10, font=("helvetica", 10)).place(x=0, y=5)
            lbl2 = tk.Label(root, text='Description', width=10, font=("helvetica", 10)).place(x=0, y=30)
            lbl3 = tk.Label(root, text='Buying price', width=10, font=("helvetica", 10)).place(x=0, y=60)
            lbl4 = tk.Label(root, text='Depreciation', width=10, font=("helvetica", 10)).place(x=0, y=90)
            lbl5 = tk.Label(root, text='Record Number', width=10, font=("helvetica", 10)).place(x=0, y=120)

            # entries
            ent1 = tk.Entry(root, width=30)
            ent1.place(x=100, y=5)
            ent2 = tk.Entry(root, width=30)
            ent2.place(x=100, y=30)
            ent3 = tk.Entry(root, width=30)
            ent3.place(x=100, y=60)
            ent4 = tk.Entry(root, width=30)
            ent4.place(x=100, y=90)
            ent5 = tk.Entry(root, width=30)
            ent5.place(x=100, y=120)

            def add():
                # get the entry data using.get
                # connect with db
                # clear the entries

                v1 = ent1.get()
                v2 = ent2.get()
                v3 = ent3.get()
                v4 = ent4.get()
                v5 = ent5.get()

                db = mysql.connector.connect(host='127.0.0.1', user='root', database='Admins',
                                             password='wYnemanor777dfd!@')
                conn = db.cursor()

                sql = "INSERT INTO assets (asset_name,description,buying,depreciation,rec_no) VALUES (%s,%s,%s,%s,%s)"
                data = [v1, v2, v3, v4, v5]

                conn.execute(sql, data)
                db.commit()
                messagebox.showinfo('Assets', 'New asset added ', parent=root)

            def clear():
                v1 = ent1.delete(0, END)
                v2 = ent2.delete(0, END)
                v3 = ent3.delete(0, END)
                v4 = ent4.delete(0, END)
                v5 = ent5.delete(0, END)

            btnA = tk.Button(root, width=10, text='Add', bg='green', command=add).place(x=50, y=250)
            btnB = tk.Button(root, width=10, text='clear', bg='red', command=clear).place(x=150, y=250)
            btnview = tk.Button(root, width=10, text="back", bg='black', fg="white", command=display_assets).place(
                x=250, y=250)
            root.mainloop()

        btn = tk.Button(win, text='Add An Asset', width=15, command=add_asset).place(x=0, y=20)

        T = Text(win, height=30, width=100)
        T.place(x=50, y=50)
        T.insert(END, "\t \t \t \t STEVAH GENERAL STORE REPORT\n\t \t \t \t Phone-No.745597321")
        T.insert(END, "\n \t \t \t \t All of Available Assets")
        T.insert(END, "\n ============================================================================================")
        T.insert(END, "\n \t Name \t \t \t Description")
        T.insert(END,
                 "\n ============================================================================================\n")
        T.insert(END, "\n \t computer \t \t \t the Hardware for containing the system. ")
        T.insert(END, "\n \t Van \t \t \t For recieving inventory in huge bulk ")
        T.insert(END, "\n \t Shelves Structure \t \t \t the shelves for display")
        T.insert(END, "\n \t Box Sealers \t \t \t Box sealers for picketing services")
        T.insert(END, "\n \t Desk \t \t \t  The client servicing Desk to the teller")
        T.insert(END, "\n \t Room \t \t \t The building where the store is hosted")
        T.insert(END, "\n \t Kitchen \t \t \t The kitchen for serving lunch to employees")
        T.insert(END, "\n \t Stationary tool \t \t \t Tools used by employees to document things")
        T.insert(END, "\n \t Receipt books \t \t \t Books that will hold the hard copy receipts")
        T.insert(END, "\n \t Receipt machine \t \t \t The tool used to generate hard copy receipts for transaction")
        T.insert(END, "\n \t Mini Fridge \t \t \t For cooling drinks and water")
        T.insert(END, "\n \t Milk Atm \t \t \t For measuring affordable milk product to consumers")
        T.insert(END, "\n \t Cooking Oil Atm \t \t \t For Measuring affordable cooking oil to customers")
        T.insert(END, "\n \t Motor Bike \t \t \t For delivering goods and services to customers")
        T.insert(END, "\n \t Paper Sealers \t \t \t For sealing fragile goods")
        T.insert(END, "\n \t LandLine Telephone \t \t \t For communicating with the other store_users")
        T.insert(END, "\n \t Overalls \t \t \t For uniformity and professionalism of employees")
        T.insert(END, "\n \t Cooking Gas \t \t \t it also offers exchange of empty cooking gas Cans")

        win.mainloop()

    # third column -- search
    btnstock3 = tk.Button(admin, text='Transactions', width=20, command=display_history).place(x=800, y=200)
    btncust3 = tk.Button(admin, text='Bills', width=20, command=add_bill).place(x=800, y=250)
    btnvendor3 = tk.Button(admin, text='View Bills', width=20, command=display_bill).place(x=800, y=300)
    btnuser3 = tk.Button(admin, text='Assets and Reports', width=20, command=display_assets).place(x=800, y=350)

    # adding a menu bar
    def menu_callback():
        print("I'm in the menu callback!")

    def submenu_callback():
        print("I'm in the submenu callback!")

    menu_widget = tk.Menu(admin)
    submenu_widget1 = tk.Menu(admin, tearoff=False)
    submenu_widget2 = tk.Menu(admin, tearoff=False)
    submenu_widget3 = tk.Menu(admin, tearoff=False)
    submenu_widget4 = tk.Menu(admin, tearoff=False)
    submenu_widget5 = tk.Menu(admin, tearoff=False)
    submenu_widget6 = tk.Menu(admin, tearoff=False)

    submenu_widget1.add_command(label="List Stock", command=display_stock)
    submenu_widget1.add_command(label="Enter Stock", command=add_stock)
    submenu_widget1.add_command(label="Assets", command=display_assets)
    menu_widget.add_cascade(label="Stock", menu=submenu_widget1)

    submenu_widget2.add_command(label="List customers", command=display_customer)
    submenu_widget2.add_command(label="Enter New Customer", command=add_cust)
    menu_widget.add_cascade(label="Customer", menu=submenu_widget2)

    submenu_widget3.add_command(label="List Vendors", command=display_vendor)
    submenu_widget3.add_command(label="Enter New Vendor", command=add_vend)
    menu_widget.add_cascade(label="Vendor", menu=submenu_widget3)

    submenu_widget4.add_command(label="List Invoices", command=display_invoice)
    submenu_widget4.add_command(label="Enter New Invoice", command=add_invoice)
    menu_widget.add_cascade(label="Invoice", menu=submenu_widget4)

    submenu_widget5.add_command(label="List Of Users", command=display_user)
    submenu_widget5.add_command(label="Enter New User", command=add_user)
    menu_widget.add_cascade(label="User", menu=submenu_widget5)

    submenu_widget6.add_command(label="List Bills", command=display_bill)
    submenu_widget6.add_command(label="Enter New Bill", command=add_bill)
    menu_widget.add_cascade(label="Bills", menu=submenu_widget6)

    admin.config(menu=menu_widget)
    # end of menu bar
    # fourth column top
    # log out button

    admin.mainloop()


def log_in1():
    win = Toplevel()
    win.title("Log in window")
    win.configure(bg="#001133")
    win.geometry("400x560")

    c1 = '#001133'

    wrapper = tk.LabelFrame(win, text='CLIENT LOGIN DETAILS', bg=c1, fg='white', font=("Helvetica", 12, 'bold'),
                            width=400, height=560)
    wrapper.place(x=0, y=0)

    canvas = Canvas(wrapper, width=300, height=250, bg=c1)
    canvas.place(x=50, y=50)
    img = ImageTk.PhotoImage(Image.open("general.png"))
    canvas.create_image(20, 20, anchor=NW, image=img)

    lbl1 = tk.Label(wrapper, text='Store name:', fg="white", bg=c1, font=("Aerial black", 15)).place(x=50, y=317)

    # combo box
    n = tk.StringVar()
    cbo = ttk.Combobox(wrapper, width=27, textvariable=n)
    cbo['values'] = ('Stevah Store I',
                     'Stevah Store II',
                     'Stevah-Supermarket',
                     'Stevah-Minimart'
                     )
    cbo.place(x=170, y=320)
    lbl3 = tk.Label(wrapper, text='Username:', bg=c1, fg="white", font=("Aerial black", 15)).place(x=50, y=380)
    ent3 = tk.Entry(wrapper, width=30)
    ent3.place(x=170, y=385)

    lbl4 = tk.Label(wrapper, text='Password:', bg=c1, fg="white", font=("Aerial black", 15)).place(x=50, y=430)
    ent4 = tk.Entry(wrapper, width=30, show='*')
    ent4.place(x=170, y=435)

    def verify():
        def exit():
            win.destroy()

        if ent3.get() == "" or ent4.get() == "":
            messagebox.showerror("Error", "Enter User Name And Password", parent=win)
        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="wYnemanor777dfd!@",
                                              database="Admins")
                cur = con.cursor()

                cur.execute("select * from user where username=%s and user_pass = %s", (ent3.get(), ent4.get()))
                row = cur.fetchone()

                if row == None:
                    messagebox.showerror("Error", "Invalid User Name And Password", parent=win)

                else:

                    messagebox.showinfo("Success", "Successfully Login", parent=win)
                    exit()
                    # administrator()
                    # watch here #######################################################################!!!
                    # root = Tk()
                    obj = Bill_App(root)
                    root.mainloop()
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=win)

    def user():
        win.destroy()
        user = tk.Toplevel()
        user.title("New User signup details")
        user.geometry("300x300")
        user.configure(bg="#161219")

        frame = tk.LabelFrame(user, text='Enter Your details', font=("Poppins", 16, 'bold'), bg="#d24dff", width=300,
                              height=300)
        frame.pack(side='left')

        # canvas = Canvas(user, width=350, height=300, bg='#161219')
        # canvas.place(x=10, y=10)
        # img = ImageTk.PhotoImage(Image.open("dollar.png"))
        # canvas.create_image(20, 20, anchor=NW, image=img)

        lbl1 = Label(frame, text='Firstname', bg='royal blue', fg='white', width=10).place(x=0, y=0)
        ent1 = Entry(frame, width=30)
        ent1.place(x=100, y=0)
        lbl2 = Label(frame, text='Lastname', bg='royal blue', fg='white', width=10).place(x=0, y=30)
        ent2 = Entry(frame, width=30)
        ent2.place(x=100, y=30)
        lbl3 = Label(frame, text='Email', bg='royal blue', fg='white', width=10).place(x=0, y=60)
        ent3 = Entry(frame, width=30)
        ent3.place(x=100, y=60)
        lbl4 = Label(frame, text='telephone', bg='royal blue', fg='white', width=10).place(x=0, y=90)
        ent4 = Entry(frame, width=30)
        ent4.place(x=100, y=90)
        lbl5 = Label(frame, text='password', bg='royal blue', fg='white', width=10).place(x=0, y=120)
        ent5 = Entry(frame, width=30, show="*")
        ent5.place(x=100, y=120)
        lbl6 = Label(frame, text='confirm', bg='royal blue', fg='white', width=10).place(x=0, y=150)
        ent6 = Entry(frame, width=30, show="*")
        ent6.place(x=100, y=150)
        lbl7 = Label(frame, text='username', bg='royal blue', fg='white', width=10).place(x=0, y=180)
        ent7 = Entry(frame, width=30)
        ent7.place(x=100, y=180)

        def action():
            if ent1.get() == "" or ent2.get() == "" or ent3.get() == "" or ent4.get() == "" or ent5.get() == "" or ent6.get() == "" or ent7.get() == "":
                messagebox.showerror("Error", "All Fields Are Required", parent=user)
            if ent5.get() != ent6.get():
                messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=user)
            else:
                try:

                    def exit():
                        user.destroy()

                    # db = mysql.connector.connect(host="localhost", user="root", password="wYnemanor777dfd!@", database="admins")
                    # cur = db.cursor()
                    # cur.execute("SELECT * FROM user WHERE username=%s" % ent7.get())
                    # row = cur.fetchone()
                    # if row!=None:
                    #    messagebox.showerror("Error", "User Name Already Exits", parent=user)

                    # get the entry elements
                    v1 = ent1.get()
                    v2 = ent2.get()
                    v3 = ent3.get()
                    v4 = ent4.get()
                    v5 = ent5.get()
                    v6 = ent6.get()
                    v7 = ent7.get()

                    # connect to the db and perform operations
                    db = mysql.connector.connect(host='localhost', user='root', password='wYnemanor777dfd!@',
                                                 database='Admins')
                    conn = db.cursor()

                    sql = "INSERT INTO user (firstname,lastname,email,telephone,user_pass,confirm,username) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    data = [v1, v2, v3, v4, v5, v6, v7]

                    conn.execute(sql, data)
                    db.commit()
                    print(conn.lastrowid)
                    messagebox.showinfo("Success", "Registration Successful", parent=user)
                    clear()
                    # switch()

                except Exception as es:
                    messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=user)

        def clear():
            v1 = ent1.delete(0, END)
            v2 = ent2.delete(0, END)
            v3 = ent3.delete(0, END)
            v4 = ent4.delete(0, END)
            v5 = ent5.delete(0, END)
            v6 = ent6.delete(0, END)
            v7 = ent7.delete(0, END)

        btn = Button(frame, text='Add User', width=10, bg='green', fg='white', command=action).place(x=20, y=220)
        btnC = Button(frame, text='Clear', width=10, bg='blue', fg='white', command=clear).place(x=120, y=220)
        btnE = Button(frame, text='Exit', width=20, bg='blue', fg='white', command=exit).place(x=80, y=250)
        back = Button(frame, text='Back', width=7, bg='black', fg='white', font=("Poppins", 10), command=log_in1).place(
            x=220, y=220)

        user.mainloop()

    def new_password():
        pas = tk.Tk()
        pas.title('Change password')
        pas.geometry('500x300')
        pas.configure(bg='#00b3b3')

        security = tk.Label(pas, text="security question!", font=("times", 20, "bold"), bg="#00b3b3").pack()

        query = tk.Label(pas, text="What is the Name of your Pet ?", bg='#00b3b3', fg='#ffff00',
                         font=("times", 12, "bold")).place(x=30, y=50)
        qent = tk.Entry(pas, width=20, show="X")
        qent.place(x=250, y=50)

        def passwordchange():
            def new_user():
                win = tk.Tk()
                win.title("Update Password")
                win.geometry("400x350")
                win.configure(bg="gray")

                Lab = tk.Label(win, text="UPDATE NEW  PASSWORD HERE !! ", font=("times", 12, "bold"), bg="gray",
                               fg="white").pack()

                new = tk.Label(win, text='User_Name', font=("times", 12, "bold"), bg='#00b3b3', fg='#ffff00',
                               width=13).place(x=30, y=50)
                nent = tk.Entry(win, width=20)
                nent.place(x=200, y=50)

                newp = tk.Label(win, text='New Password', font=("times", 12, "bold"), bg='#00b3b3', fg='#ffff00',
                                width=13).place(x=30, y=100)
                nentp = tk.Entry(win, width=20, show="x")
                nentp.place(x=200, y=100)

                new = tk.Label(win, text='Confirm Password', font=("times", 12, "bold"), bg='#00b3b3', fg='#ffff00',
                               width=13).place(x=30, y=150)
                nentc = tk.Entry(win, width=20, show="x")
                nentc.place(x=200, y=150)

                def verify():
                    if nentp.get() == "" or nentc.get() == "" or nent.get() == "":
                        messagebox.showwarning("Warning", "All fields are required", parent=win)

                    if nentp.get() != nentc.get():
                        messagebox.showwarning("Warning", "Passwords dont Match", parent=win)
                    else:
                        v5 = nent.get()
                        v6 = nentp.get()
                        v7 = nentc.get()
                        # connect to the db and perform operations
                        db = mysql.connector.connect(host='127.0.0.1', user='root', password='wYnemanor777dfd!@',
                                                     database='Admins')
                        conn = db.cursor()

                        sql = "INSERT INTO user (username,user_pass,confirm) VALUES (%s,%s,%s)"
                        data = [v5, v6, v7]
                        conn.execute(sql, data)
                        messagebox.showinfo("Information", "Success Update !", parent=win)
                        print("Updating User in the database")

                        db.commit()

                def exit():
                    win.destroy()

                btn = tk.Button(win, text='CHANGE', fg='#ffff00', font=("Helvetica", 12, "bold"), width=15, bg='blue',
                                command=verify).place(x=30, y=250)
                btncl = tk.Button(win, text='EXIT', fg='#ffff00', font=("Helvetica", 12, "bold"), width=10, bg='blue',
                                  command=exit).place(x=200, y=250)

                win.mainloop()

            if qent.get() == "seven" or qent.get() == "Bones":
                # messagebox.showwarning("Warning","inCorrect Pet Name!! Failure to change password ",parent=pas)

                messagebox.showinfo("Information", "correct pet name! ", parent=pas)
                new_user()

            else:
                messagebox.showwarning("Warning", "Incorrect Pet Name Failure to change password!", parent=pas)

        def exit():
            pas.destroy()

        btn = tk.Button(pas, text='Change', fg='#ffff00', font=("Helvetica", 12, "bold"), width=10, bg='blue',
                        command=passwordchange).place(x=30, y=100)
        btncl = tk.Button(pas, text='close', fg='#ffff00', font=("Helvetica", 12, "bold"), width=10, bg='blue',
                          command=exit).place(x=200, y=100)

        pas.mainloop()

    btn = tk.Button(wrapper, text='Log_in', fg="white", bg='green', width=9, font=("Aerial black", 10),
                    command=verify).place(x=260, y=490)

    btn2 = tk.Button(wrapper, text='New User!', bg='#cc0066', fg='white', width=10, font=("Poppins", 15),
                     command=user).place(x=240, y=0)

    btnf = tk.Button(wrapper, text='Forgot your password?', fg="white", bg=c1, width=20, command=new_password).place(
        x=50, y=490)

    win.mainloop()


def login():
    log = tk.Tk()
    log.title("Log in to admin window verification")
    log.geometry("350x250")
    Label(log, text="Accessing the Admin Panel", bg="royalblue", width="300", height="2", font=("calibri", 16)).pack()
    l1 = Label(log, text="Enter Password! ", font=("times", 12, "bold"), fg="black").place(x=10, y=80)
    e1 = tk.Entry(log, width=30, show="*")
    e1.place(x=130, y=80)

    def Access():
        if e1.get() == "Admin" or e1.get() == "admin":
            administrator()
            print("success Log into the admin panel!! ")

        else:
            messagebox.showwarning("Warning", "Wrong Password! :) ", parent=log)

        # print("Login session started")

    Button(log, text="Enter", width="30", height="2", command=Access).place(x=70, y=120)

    log.mainloop()


log_in1()
# administrator()
