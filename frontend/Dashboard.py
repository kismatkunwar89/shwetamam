from tkinter import *

from tkinter import ttk
from tkinter import messagebox
import model
import backend.database
import model.model
from tkcalendar import Calendar, DateEntry
import mysql.connector

class Movie:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x820")
        self.root.title("Online Hotel Booking System")
        root.resizable(False, False)
        self.root.config(bg="orange")
        self.db=backend.database.DBConnect()

        self.name = StringVar()
        self.email = StringVar()
        self.gender = StringVar()
        self.contact = StringVar()
        self.address = StringVar()
        self.roomnumber = StringVar()
        self.search_txt = StringVar()
        self.sort = StringVar()
        self.search_by = StringVar()

        # Frames
        MainFrame = Frame(self.root, bg="light grey", width=1350, height=750)
        MainFrame.grid()

        self.TFrame = Label(MainFrame, font=('Arial', 41), text="ONLINE HOTEL BOOKING SYSTEM", bg="black", fg="orange",
                            anchor="w")
        self.TFrame.place(x=0, y=35, relwidth=1)

        frm1 = LabelFrame(self.root, text="Costumer Details", font=("times new roman", 17, "bold"),
                          fg="black", bg="powder blue")
        frm1.place(x=3, y=96, width=1183, height=125)

        f_name = Label(frm1, text="Full Name:", fg="Black", font=("times new roman", 19, "bold"))
        f_name.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        self.ef_name = Entry(frm1, textvariable=self.name, font=("times new roman", 16, "bold"), relief=GROOVE)
        self.ef_name.place(x=125, y=10)

        c_number = Label(frm1, text="Contact Number:", fg="black", font=("times new roman", 19, "bold"))
        c_number.place(x=313, y=10)

        self.e_Contact = Entry(frm1, textvariable=self.contact, font=("times new roman", 16, "bold"), relief=GROOVE)
        self.e_Contact.place(x=470, y=10)

        e_address = Label(frm1, text="Email Address:", fg="black", font=("times new roman", 19, "bold"))
        e_address.place(x=655, y=10)

        self.entry_e = Entry(frm1, textvariable=self.email, font=("times new roman", 16, "bold"), relief=GROOVE,width=30)
        self.entry_e.place(x=800, y=10)

        Gender = Label(frm1, text="Gender", fg="black", font=("times new roman", 19, "bold"))
        Gender.place(x=22, y=55)

        self.combo_gender = ttk.Combobox(frm1, textvariable=self.gender, font=("times new roman", 18, "bold"),
                                         state='readonly')
        self.combo_gender['values'] = ("Male", "Female", "Other")
        self.combo_gender.place(x=98, y=55)

        c_address = Label(frm1, text=" Address :", fg="black", font=("times new roman", 19, "bold"))
        c_address.place(x=312, y=55)

        self.e_address = Entry(frm1, textvariable=self.address, font=("times new roman", 16, "bold"), relief=GROOVE)
        self.e_address.place(x=412, y=55)

        r_number = Label(frm1, text=" Room Number :", fg="black", font=("times new roman", 19, "bold"))
        r_number.place(x=612, y=55)

        self.rno_entry = Entry(frm1, textvariable=self.roomnumber, font=("times new roman", 16, "bold"), relief=GROOVE,width=7)
        self.rno_entry.place(x=762, y=55)

        date = Label(frm1, text=" Date :", fg="black",font=("times new roman", 19, "bold"))
        date.place(x=837, y=55)

        self.cal_entry = DateEntry(frm1,width=12, background='darkblue',
                        foreground='white', borderwidth=10)
        self.cal_entry.place(x=910,y=57)


        BFrame = Frame(MainFrame, bd=2, width=1344, height=70, padx=18, pady=10, bg="orange", relief=RIDGE)
        BFrame.place(x=4, y=222)

        self.btnadd = Button(BFrame, text="Add ", font=('Arial', 18, 'bold'), width=10, height=1, bd=4, bg="orange",
                             command=self.adddata)
        self.btnadd.grid(row=0, column=0)

        self.update = Button(BFrame, text="Update", font=('Arial', 18, 'bold'), width=10, height=1, bd=4, bg="orange",
                             command=self.updata)
        self.update.grid(row=0, column=1)

        self.btnclc = Button(BFrame, text="Clear", font=('Arial', 18, 'bold'), width=10, height=1, bd=4, bg="orange",
                             command=self.clear)
        self.btnclc.grid(row=0, column=2)

        self.btndel = Button(BFrame, text="Delete", font=('Arial', 18, 'bold'), width=10, height=1, bd=4, bg="orange",
                             command=self.deletedata)
        self.btndel.grid(row=0, column=3)

        sFrame = Frame(MainFrame, bd=2, width=538, height=60, padx=18, pady=10, bg="orange", relief=RIDGE)
        sFrame.place(x=650, y=222)

        # sort
        sort_by = Label(sFrame, text=" Sort By :", fg="black", font=("times new roman", 19, "bold"))
        sort_by.place(x=3, y=1)

        self.bsort = Button(sFrame, text=" Sort ", fg="black", font=("times new roman", 18, "bold"),
                            command=self.sorted)
        self.bsort.place(x=275, y=1)

        self.combo_sort = ttk.Combobox(sFrame, textvariable=self.sort, font=("times new roman", 19, "bold"),
                                       state='readonly', width=15)
        self.combo_sort['values'] = ("Name","RoomNumber")
        self.combo_sort.place(x=93, y=1)

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="powderblue")
        Detail_Frame.place(x=5, y=289, width=1185, height=530)

        lbl_search = Label(Detail_Frame, text="Search By", bg="powderblue", fg="black",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, padx=10, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, font=("times new roman", 18, "bold"),
                                    state='readonly')
        combo_search['values'] = ( "Room Number", "Phone Number")
        combo_search.grid(row=0, column=1)

        txt_search = Entry(Detail_Frame, textvariable=self.search_txt, font=("times new roman", 17, "bold"),
                           relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        self.searchbtn = Button(Detail_Frame, text="Search ", bg="orange", fg="black", width=16, pady=5,
                                command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        self.showallbtn = Button(Detail_Frame, text="Show All",command=self.show_data, bg="orange", fg="black", width=16, pady=5).grid(row=0,
                                                                                                                column=4,
                                                                                                                padx=10,
                                                                                                                pady=10)

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="black")
        Table_Frame.place(x=10, y=70, width=1165, height=450)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.hotel_table = ttk.Treeview(Table_Frame,
                                        columns=("name", "address", "email", "gender", "number", "RoomNumber","Date"),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.hotel_table.xview)
        scroll_y.config(command=self.hotel_table.yview)

        self.hotel_table.heading("name", text="Full Name")
        self.hotel_table.heading("address", text="address")
        self.hotel_table.heading("email", text="Email")
        self.hotel_table.heading("gender", text="Gender")
        self.hotel_table.heading("number", text="Phone number")
        self.hotel_table.heading("RoomNumber", text="Room Number")
        self.hotel_table.heading("Date", text="Date")
        self.hotel_table['show'] = 'headings'

        self.hotel_table.column("name", width=100)
        self.hotel_table.column("address", width=100)
        self.hotel_table.column("email", width=100)
        self.hotel_table.column("gender", width=100)
        self.hotel_table.column("number", width=100)
        self.hotel_table.column("Date", width=100)
        self.hotel_table.pack(fill=BOTH, expand=1)

        self.fetch_data()
        self.hotel_table.bind("<ButtonRelease-1>", self.get_cursor)

    def sorted(self):
        query = ("select * from new_table")
        rows = self.db.select(query)
        myStack = []
        if len(rows) != 0:
            self.hotel_table.delete(*self.hotel_table.get_children())
            if self.sort.get() == "Name":
                for row in rows:
                    myStack.append(row[0])
                self.sorted = self.mergesort(myStack)

                for i in self.sorted:
                    for row in rows:
                        if i == row[0]:
                            self.hotel_table.insert('', END, value=row)
                            rows.remove(row)
            else:
                self.hotel_table.delete(*self.hotel_table.get_children())
                if self.sort.get() == "RoomNumber":
                    for row in rows:
                        myStack.append(row[5])
                    self.sorted = self.mergesort(myStack)

                    for i in self.sorted:
                        for row in rows:
                            if i == row[5]:
                                self.hotel_table.insert('', END, value=row)
                                rows.remove(row)


    def get_cursor(self, ev):
        curosor_row = self.hotel_table.focus()
        contents = self.hotel_table.item(curosor_row)
        row = contents['values']
        self.name.set(row[0])
        self.email.set(row[2])
        self.gender.set(row[3])
        self.contact.set(row[4])
        self.address.set(row[1])
        self.roomnumber.set(row[5])

    def show_data(self):
        self.fetch_data()

    def fetch_data(self):
        query = ("select * from new_table")

        rows = self.db.select(query)
        if len(rows) != 0:
            self.hotel_table.delete(*self.hotel_table.get_children())
            for row in rows:
                self.hotel_table.insert('', END, values=row)

    def adddata(self):
        name = self.ef_name.get()
        address = self.e_address.get()
        email = self.entry_e.get()
        gender = self.combo_gender.get()
        phone_number = self.e_Contact.get()
        room_number = self.rno_entry.get()
        date = self.cal_entry.get()
        # gender=self.cmb_gender.current()

        try:
            if name == '' or address == '' or email == '' or gender == '' or phone_number == '' or room_number == '' or date == '':
                messagebox.showerror('Error', 'plz fill the empty field')
                return
            md = model.model.User(name, address, email, gender, phone_number, room_number, date)
            query = "insert into new_table(name,phone_number,email,gender,address,room_number,date) values(%s,%s,%s,%s,%s,%s,%s)"
            values = (
            md.get_username(), md.get_pno(), md.get_email(), md.get_gender(), md.get_address(), md.get_rno(), md.get_date())

            self.db.insert(query, values)

            self.fetch_data()
            self.clear()

            query = ("select * from new_table")

            rows = self.db.select(query)
            messagebox.showinfo("congratulations", " number added succesfully")
        except mysql.connector.IntegrityError :
            messagebox.showinfo("RoomBooked","Room already booked, Please choose another room number")


    def clear(self):
        self.name.set("")
        self.email.set("")
        self.gender.set("")
        self.contact.set("")
        self.address.set("")
        self.roomnumber.set("")

    def clcdata(self):
        pass

    def deletedata(self):
        name = self.ef_name.get()
        if (name == ""):
            messagebox.showinfo("Delete Status", "ID os compolsary for delete")
        else:
            query = "delete from new_table where name=%s"
            value = (name,)
            self.db.delete(query, value)
            messagebox.showinfo("Delete Status", "Deleted Succesfuly")
            self.clear()
            self.fetch_data()

    def updata(self):
        name = self.ef_name.get()
        address = self.e_address.get()
        email = self.entry_e.get()
        gender = self.combo_gender.get()
        phone_number = self.e_Contact.get()
        room_number = self.rno_entry.get()
        date = self.cal_entry.get()
        if name == '' or address == '' or email == '' or gender == '' or phone_number == '' or room_number == '' or date == '':
            messagebox.showerror('Error', 'plz fill the empty field')

        else:
            md = model.model.User(name, address, email, gender, phone_number, room_number, date)
            query = "update new_table set name=%s,address=%s, email=%s, gender=%s, phone_number=%s, date=%s where room_number=%s"
            values = (md.get_username(),md.get_address(), md.get_email(), md.get_gender(), md.get_pno(), md.get_date(),
                      md.get_rno())
            self.db.update(query, values)
            self.fetch_data()
            self.clear()

            messagebox.showinfo("Update status", "Update Succesfuly")
    @classmethod
    def mergesort(self, alist):
        if len(alist) > 1:
            mid = len(alist) // 2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]
            self.mergesort(lefthalf)
            self.mergesort(righthalf)
            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k] = lefthalf[i]
                    i = i + 1
                else:
                    alist[k] = righthalf[j]
                    j += 1
                k += 1
            while i < len(lefthalf):
                alist[k] = lefthalf[i]
                i += 1
                k += 1
            while j < len(righthalf):
                alist[k] = righthalf[j]
                j += 1
                k += 1
        return alist
    @classmethod
    def binary_room_number(self, list, item):
        if list == []:
            return ValueError
        self.list = list
        self.item = item
        max = len(list) - 1
        min = 0
        while min <= max:
            mid = (min + max) // 2
            if self.list[mid] == self.item:
                return mid
            elif self.list[mid] > self.item:
                max = mid - 1
            else:
                min = mid + 1
        return -1

    def search_data(self):
        if self.search_by.get()=="Room Number":
            query = "select * from new_table"
            rows = self.db.select(query)
            myStack = []
            for row in rows:
                myStack.append(row[5])
            self.sorted = self.mergesort(myStack)
            item = int(self.search_txt.get())
            sorted = self.sorted
            index = self.binary_room_number(sorted, item)
            for row in rows:
                if sorted[index] == row[5]:
                    self.hotel_table.delete(*self.hotel_table.get_children())
                    self.hotel_table.insert('', END, value=row)
                    self.search_txt.set("")

        elif self.search_by.get() == "Phone Number":
            query = "select * from new_table"
            rows = self.db.select(query)
            myStack = []
            for row in rows:
                myStack.append(row[4])
            self.sorted = self.mergesort(myStack)
            item = int(self.search_txt.get())
            sorted = self.sorted
            index = self.binary_search_phone(sorted, item)
            for row in rows:
                if sorted[index] == row[4]:
                    self.hotel_table.delete(*self.hotel_table.get_children())
                    self.hotel_table.insert('', END, value=row)
                    self.search_txt.set("")
    @classmethod
    def binary_search_phone(self, list, item):
        if list == []:
            return ValueError
        self.list = list
        self.item = item
        max = len(list) - 1
        min = 0
        while min <= max:
            mid = (min + max) // 2
            if self.list[mid] == self.item:
                return mid
            elif self.list[mid] > self.item:
                max = mid - 1
            else:
                min = mid + 1
        return -1




    def btnclc(self):
        pass

    def print_sel(self):
        print(self.cal_entry.get())




if __name__=='__main__':
	root=Tk()
	datbase=Movie(root)
	root.mainloop()




