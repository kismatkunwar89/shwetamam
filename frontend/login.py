from tkinter import *
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageTk
import Dashboard


class Login_Page:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg='grey')
        self.root.title(' Hotel Login Page')
        self.root.geometry('450x350')
        self.root.resizable(0, 0)
        self.image = Image.open("college.jpg")
        self.password_icon = PhotoImage(file="Password.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.Username_icon = PhotoImage(file="username.png")
        labl = Label(self.root, image=self.photo)
        labl.pack(pady=0, padx=0)
        Title = Label(self.root, text="  Softwarica Hotel Admin ", font=("arial", 20, "bold"), bg="black",
                      fg="powder blue", relief=GROOVE)
        Title.place(x=10, y=10)

        f = font.Font(size=15, slant='italic', underline=TRUE, family='arial')

        lbl_header = Label(self.root, text='  Softwarica Hotel \n Admin Login ', font=('arial', 20, 'bold'), \
                           bg='grey', fg='black')
        lbl_header.pack(side=TOP, fill=X)

        main_frame = Frame(self.root, bg='powder blue', bd=5, relief=RAISED)
        main_frame.place(x=20, y=70, width=400, height=200)

        lbl_username = Label(main_frame, image=self.Username_icon, text='  User Name:', font=('arial', 15, 'bold'), \
                             compound=LEFT, fg='Black', bg='powder blue')
        lbl_username.grid(row=0, column=0, padx=10, pady=10)

        self.ent_username = Entry(main_frame, font=('arial', 15, 'bold'))
        self.ent_username.grid(row=0, column=1)
        self.ent_username.focus_set()

        lbl_password = Label(main_frame, image=self.password_icon, text='  Password:', font=('arial', 15, 'bold'), \
                             compound=LEFT, fg='Black', bg='powder blue')

        lbl_password.grid(row=1, column=0, padx=10, pady=10)

        self.ent_password = Entry(main_frame, show="*", font=('arial', 15, 'bold'))
        self.ent_password.grid(row=1, column=1)

        btn_login = Button(main_frame, text='Login', font=('arial', 15, 'bold'), \
                           command=lambda: self.button_login(self.ent_username.get(), self.ent_password.get()))
        btn_login.place(x=150, y=120)

        btn_reset = Button(main_frame, text='Reset', font=('arial', 15, 'bold'), \
                           command=self.btn_reset_click, bd=5, relief=RAISED)
        btn_reset.place(x=250, y=120)

    def btn_reset_click(self):
        self.ent_username.delete(0, END)
        self.ent_username.insert(0, "")

        self.ent_password.delete(0, END)
        self.ent_password.insert(0, '')

    def button_login(self, username, password):
        if len(username) != 0 and len(password) != 0:
            if username == "admin" and password == "admin":
                messagebox.showinfo('Success', 'Congratulations!! login successfull')
                self.root.destroy()
                tk = Tk()
                Dashboard.Movie(tk)
                tk.mainloop()
            else:
                messagebox.showerror('Error', 'Invalid username and password')
                self.ent_password.focus()
                return
        elif (len(username) == 0):
            messagebox.showerror("Please enter username!")
            self.ent_username.focus()
            return
        else:
            messagebox.showerror("Book Store Login", "Please enter password!")
            self.ent_password.focus()
            return


if __name__ == '__main__':
    tk = Tk()
    main = Login_Page(tk)
    tk.mainloop()
