import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql


new_doctor_window = Tk()
new_doctor_window.title('Add Admin')
new_doctor_window.geometry("925x500+300+200")
new_doctor_window.config(bg="#ECF9FF")
new_doctor_window.resizable(False, False)

#back forward button
def backfw_btn():
    new_doctor_window.withdraw()
    import dashboard_admin
    dashboard_admin.admin_dashboard_window.deiconify()

bfw_btn = tkinter.PhotoImage(file='backfw.png',master=new_doctor_window)
back_forward_btn = Button(new_doctor_window,cursor='hand2',image=bfw_btn,bd=0,bg="#ECF9FF",activebackground="#ECF9FF",height=80,width=80,command=backfw_btn)
back_forward_btn.place(x=10,y=5)



img_logo = tkinter.PhotoImage(file='logo.png',master=new_doctor_window)
new_doctor_window.iconphoto(False, img_logo)
Label(new_doctor_window, bg="white",image=img_logo ,background="#ECF9FF").place(x=50, y=120)
frame = Frame(new_doctor_window, width=550, height=400, bg="#ECF9FF")
frame.place(x=450, y=50)

heading = Label(frame, text="Create New Account", fg="black", bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 25, 'bold'))
heading.place(x=40, y=10)


def on_enter(e):
    newadoctor_email_entry.delete(0, 'end')


def on_leave(e):
    name = newadoctor_email_entry.get()
    if name == '':
        newadoctor_email_entry.insert(0, 'Email Address')


newadoctor_email_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
newadoctor_email_entry.place(x=30, y=95)
newadoctor_email_entry.insert(0, 'Email Address')
newadoctor_email_entry.bind('<FocusIn>', on_enter)
newadoctor_email_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=120)


def on_enter(e):
    doctor_username_entry.delete(0, 'end')


def on_leave(e):
    teacher_name = doctor_username_entry.get()
    if teacher_name == '':
        doctor_username_entry.insert(0, 'User full name')


doctor_username_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
doctor_username_entry.place(x=30, y=145)
doctor_username_entry.insert(0, 'User full name')
doctor_username_entry.bind('<FocusIn>', on_enter)
doctor_username_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=173)


def on_enter(e):
    institute_entry.delete(0, 'end')


def on_leave(e):
    institute_name = institute_entry.get()
    if institute_name == '':
        institute_entry.insert(0, 'Department')


institute_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
institute_entry.place(x=30, y=200)
institute_entry.insert(0, 'Department')
institute_entry.bind('<FocusIn>', on_enter)
institute_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=230)

#password

def on_enter(e):
    password_entry.delete(0, 'end')


def on_leave(e):
    password = password_entry.get()
    if password == '':
        password_entry.insert(0, 'Password')


password_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
password_entry.place(x=30, y=254)
password_entry.insert(0, 'Password')
password_entry.bind('<FocusIn>', on_enter)
password_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=280)


def on_enter(e):
    conf_pass_entry.delete(0, 'end')


def on_leave(e):
    confirm_password = conf_pass_entry.get()
    if confirm_password == '':
        conf_pass_entry.insert(0, 'Confirm password')


conf_pass_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
conf_pass_entry.place(x=30, y=305)
conf_pass_entry.insert(0, 'Confirm password')
conf_pass_entry.bind('<FocusIn>', on_enter)
conf_pass_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=330)
#End password

def clear():
    newadoctor_email_entry.delete(0,END)
    newadoctor_email_entry.insert(0,'Email Address')

    conf_pass_entry.delete(0, END)
    conf_pass_entry.insert(0,'Confirm password')

    password_entry.delete(0, END)
    password_entry.insert(0,'Password')

    institute_entry.delete(0, END)
    institute_entry.insert(0,'Department')

    doctor_username_entry.delete(0, END)
    doctor_username_entry.insert(0,'User full name')

#connect to database
def addDoctor():
    con_db=pymysql.connect(host='localhost',user='root',password='123456789')
    mycursor = con_db.cursor()
    query = 'use facerecognation_attendance_System'
    mycursor.execute(query)
    query = 'select * from lecturer where email=%s'
    mycursor.execute(query, (newadoctor_email_entry.get()))
    row2 = mycursor.fetchone()
    if row2 != None:
        messagebox.showerror('Error', 'Email  already exists')
    else:
        query = 'insert into lecturer(department_name,full_name,email,pass) values(%s,%s,%s,%s)'
        mycursor.execute(query, (institute_entry.get(),doctor_username_entry.get(), newadoctor_email_entry.get(), password_entry.get()))
        messagebox.showinfo('Done', 'Registration is done successfully')
        con_db.commit()
        con_db.close()


def creat_account():
    if newadoctor_email_entry.get()=='Email Address' or password_entry.get()=='Password' or conf_pass_entry.get()=='Confirm password' or institute_entry.get()=='Department' or doctor_username_entry.get()=='User full name':
        messagebox.showerror('Error', 'all fields are required')
    elif password_entry.get()!= conf_pass_entry.get():
        messagebox.showerror('Error','Password must be the same')
    else:
        addDoctor()
        clear()


btn_login = Button(frame, cursor='hand2',width=39, pady=7, text="Creat Account",
                   bg="#57a1f8", fg='white', border=0,command=creat_account)
btn_login.place(x=35, y=360)

new_doctor_window.mainloop()