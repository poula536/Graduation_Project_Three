import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql

login_window=Tk()
login_window.title('Login')
login_window.geometry("925x500+300+200")
login_window.config(bg="#ECF9FF")
login_window.resizable(False,False)

#logo image
img_logo = tkinter.PhotoImage(file='logo.png',master=login_window)
Label(login_window,image=img_logo, bg="white",background="#ECF9FF").place(x=50,y=120)

frame = Frame(login_window,width=350,height=370,bg="#ECF9FF")
frame.place(x=480,y=50)
heading = Label(frame,text="تسجيل دخول",fg="black",bg="#ECF9FF",font=('Microsoft YaHei UI Light ',25,'bold'))
heading.place(x=100,y=5)

def on_enter(e):
    email_entry.delete(0,'end')
def on_leave(e):
    name =email_entry.get()
    if name=='':
        email_entry.insert(0, 'البريد الالكتروني')

email_entry = Entry(frame,width=35,fg='#181823',border=0,bg="#ECF9FF",font=('Microsoft YaHei UI Light ',15))
email_entry.place(x=30,y=100)
email_entry.insert(0,'البريد الالكتروني')
email_entry.bind('<FocusIn>',on_enter)
email_entry.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=125)

def on_enter(e):
    password_entry.delete(0,'end')
def on_leave(e):
    password =password_entry.get()
    if password=='':
        password_entry.insert(0, 'كلمه السر')

password_entry = Entry(frame,width=35,fg='#181823',border=0,bg="#ECF9FF",font=('Microsoft YaHei UI Light ',15))
password_entry.place(x=30,y=180)
password_entry.insert(0,'كلمه السر')
password_entry.bind('<FocusIn>',on_enter)
password_entry.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=205)


def hide():
    eye_img.config(file='closedeye.png')
    password_entry.config(show='*')
    openeye_btn.config(command=show)
def show():
    eye_img.config(file='openeye.png')
    password_entry.config(show='')
    openeye_btn.config(command=hide)

eye_img = tkinter.PhotoImage(file='openeye.png',master=login_window)
openeye_btn = Button(frame,bd=0,image=eye_img,activebackground="#ECF9FF",command=hide)
openeye_btn.place(x=280, y=170)

#get doctor name from database
def great_doc():
    con_db = pymysql.connect(host='localhost', user='root', password='123456789')
    mycursor = con_db.cursor()
    query = 'use facerecognation_attendance_System'
    mycursor.execute(query)
    query = 'select full_name from lecturer where email=%s'
    mycursor.execute(query, (email_entry.get()))
    row = mycursor.fetchall()[0]
    tex = "welcome doctor "
    return tex +" ".join(row)





#connect to database
def login():
    if email_entry.get() == 'البريد الالكتروني' or password_entry.get() == 'كلمه السر':
        messagebox.showerror('Error', 'all fields are required')
    else:
        con_db = pymysql.connect(host='localhost', user='root', password='123456789')
        mycursor = con_db.cursor()
        query = 'use facerecognation_attendance_System'
        mycursor.execute(query)
        query = 'select * from lecturer where email=%s and pass=%s'
        mycursor.execute(query, (email_entry.get(), password_entry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'invalid email or password')
        else:
            login_window.withdraw()
            from dashboard_doc import doctor_window
            doctor_window.withdraw()
            Label(doctor_window,text=great_doc(),fg="#070A52",width=25,bg="#ECF9FF",font=('Microsoft YaHei UI Light ',30)).place(x=210,y=20)
            doctor_window.deiconify()


def admin_login():
       login_window.withdraw()
       import adminlogin
       adminlogin.adminlogin_window.deiconify()


btn_login = Button(frame,cursor='hand2',width=39,pady=7,text="تسجيل الدخول",
                   bg="#57a1f8",fg='white',border=0,command=login)
btn_login.place(x=35,y=250)

admin_btn = Button(frame,text="Log in as admin",cursor='hand2',fg='red',bg="#ECF9FF",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',10),command=admin_login)
admin_btn.place(x=85,y=300)





login_window.mainloop()