import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql

new_admin_window = Tk()
new_admin_window.title('Add Admin')
new_admin_window.geometry("925x500+300+200")
new_admin_window.config(bg="#ECF9FF")
new_admin_window.resizable(False, False)
img_logo = tkinter.PhotoImage(file='logo.png', master=new_admin_window)
new_admin_window.iconphoto(False, img_logo)
def backfw_btn():
    new_admin_window.withdraw()
    import dashboard_admin
    dashboard_admin.admin_dashboard_window.deiconify()

bfw_btn = tkinter.PhotoImage(file='backfw.png',master=new_admin_window)
back_forward_btn = Button(new_admin_window,cursor='hand2',image=bfw_btn,bd=0,bg="#ECF9FF",activebackground="#ECF9FF",height=80,width=80,command=backfw_btn)
back_forward_btn.place(x=10,y=5)


img_logo = tkinter.PhotoImage(file='logo.png',master=new_admin_window)
Label(new_admin_window, bg="white",image=img_logo ,background="#ECF9FF").place(x=50, y=120)
frame = Frame(new_admin_window, width=350, height=400, bg="#ECF9FF")
frame.place(x=480, y=50)

heading = Label(frame, text="انشاء حساب جديد", fg="black", bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 25, 'bold'))
heading.place(x=100, y=10)


def on_enter(e):
    newadmin_fullname_entry.delete(0, 'end')


def on_leave(e):
    name = newadmin_fullname_entry.get()
    if name == '':
        newadmin_fullname_entry.insert(0, 'اسم المستخدم كامل')

newadmin_fullname_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
newadmin_fullname_entry.place(x=30, y=135)
newadmin_fullname_entry.insert(0, 'اسم المستخدم كامل')
newadmin_fullname_entry.bind('<FocusIn>', on_enter)
newadmin_fullname_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=160)


#password
def on_enter(e):
    password_entry.delete(0, 'end')


def on_leave(e):
    password = password_entry.get()
    if password == '':
        password_entry.insert(0, 'كلمه السر')


password_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
password_entry.place(x=30, y=205)
password_entry.insert(0, 'كلمه السر')
password_entry.bind('<FocusIn>', on_enter)
password_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=230)


def on_enter(e):
    conf_pass_entry.delete(0, 'end')


def on_leave(e):
    confirm_password = conf_pass_entry.get()
    if confirm_password == '':
        conf_pass_entry.insert(0, 'تاكيد كلمه السر')


conf_pass_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
conf_pass_entry.place(x=30, y=280)
conf_pass_entry.insert(0, 'تاكيد كلمه السر')
conf_pass_entry.bind('<FocusIn>', on_enter)
conf_pass_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=305)
#End password

def clear():
    newadmin_fullname_entry.delete(0,END)
    newadmin_fullname_entry.insert(0,'اسم المستخدم كامل')

    conf_pass_entry.delete(0, END)
    conf_pass_entry.insert(0,'تاكيد كلمه السر')

    password_entry.delete(0, END)
    password_entry.insert(0,'كلمه السر')


#connect to database
def addDoctor():
    con_db=pymysql.connect(host='localhost',user='root',password='123456789')
    mycursor = con_db.cursor()
    query = 'use facerecognation_attendance_System'
    mycursor.execute(query)
    query = 'select * from admin where full_name=%s'
    mycursor.execute(query, (newadmin_fullname_entry.get()))
    row2 = mycursor.fetchone()
    if row2 != None:
        messagebox.showerror('Error', 'Name already exists')
    else:
        query = 'insert into admin(full_name,pass) values(%s,%s)'
        mycursor.execute(query, (newadmin_fullname_entry.get(),password_entry.get()))
        messagebox.showinfo('Done', 'Registration is done successfully')
        con_db.commit()
        con_db.close()


def creat_account():
    if newadmin_fullname_entry.get()=='اسم المستخدم كامل' or password_entry.get()=='كلمه السر' or conf_pass_entry.get()=='تاكيد كلمه السر':
        messagebox.showerror('Error', 'all fields are required')
    elif password_entry.get()!= conf_pass_entry.get():
        messagebox.showerror('Error','Password must be the same')
    else:
        addDoctor()
        clear()


btn_login = Button(frame, cursor='hand2',width=39, pady=7, text="انشاء الحساب ",
                   bg="#57a1f8", fg='white', border=0,command=creat_account)
btn_login.place(x=35, y=360)

new_admin_window.mainloop()