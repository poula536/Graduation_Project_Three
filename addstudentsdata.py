import tkinter
from tkinter import *
from tkinter import messagebox

addstudent_window = Tk()
addstudent_window.title('Add Student data')
addstudent_window.geometry("925x500+300+200")
addstudent_window.config(bg="#ECF9FF")
addstudent_window.resizable(False, False)


# back forward button
def backfw_btn():
    addstudent_window.withdraw()
    import dashboard_admin
    dashboard_admin.admin_dashboard_window.deiconify()


bfw_btn = tkinter.PhotoImage(file='backfw.png', master=addstudent_window)
back_forward_btn = Button(addstudent_window, cursor='hand2', image=bfw_btn, bd=0, bg="#ECF9FF",
                          activebackground="#ECF9FF", height=80, width=80, command=backfw_btn)
back_forward_btn.place(x=10, y=5)

img_logo = tkinter.PhotoImage(file='logo.png', master=addstudent_window)
addstudent_window.iconphoto(False, img_logo)
Label(addstudent_window, image=img_logo, bg="white", background="#ECF9FF").place(x=50, y=120)
frame = Frame(addstudent_window, width=350, height=440, bg="#ECF9FF")
frame.place(x=480, y=50)

heading = Label(frame, text="Add Student Data", fg="black", bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 25, 'bold'))
heading.place(x=50, y=-6)


def on_enter(e):
    studentname_entry.delete(0, 'end')


def on_leave(e):
    student_name = studentname_entry.get()
    if student_name == '':
        studentname_entry.insert(0, 'Student Name')


studentname_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
studentname_entry.place(x=30, y=70)
studentname_entry.insert(0, 'Student Name')
studentname_entry.bind('<FocusIn>', on_enter)
studentname_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=95)


def on_enter(e):
    email_entry.delete(0, 'end')

def on_leave(e):
    name = email_entry.get()
    if name == '':
        email_entry.insert(0, 'Student ID')


email_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
email_entry.place(x=30, y=115)
email_entry.insert(0, 'Student ID')
email_entry.bind('<FocusIn>', on_enter)
email_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=140)

ID = email_entry.get()
def on_enter(e):
    year_entry.delete(0, 'end')


def on_leave(e):
    year = year_entry.get()
    if year == '':
        year_entry.insert(0, 'Year of Academic')


year_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
year_entry.place(x=30, y=150)
year_entry.insert(0, 'Year of Academic')
year_entry.bind('<FocusIn>', on_enter)
year_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=175)
year = year_entry.get()

def on_enter(e):
    institute_entry.delete(0, 'end')


def on_leave(e):
    institute_name = institute_entry.get()
    if institute_name == '':
        institute_entry.insert(0, 'Institute')


institute_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
institute_entry.place(x=30, y=185)
institute_entry.insert(0, 'Institute')
institute_entry.bind('<FocusIn>', on_enter)
institute_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=210)
institute = institute_entry.get()

def on_enter(e):
    department_entry.delete(0, 'end')


def on_leave(e):
    department_name = department_entry.get()
    if department_name == '':
        department_entry.insert(0, 'Department')


department_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
department_entry.place(x=30, y=225)
department_entry.insert(0, 'Department')
department_entry.bind('<FocusIn>', on_enter)
department_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=250)
department = department_entry.get()

def on_enter(e):
    image_entry.delete(0, 'end')


def on_leave(e):
    image = image_entry.get()
    if image == '':
        image_entry.insert(0, 'Image path and Name')


image_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
image_entry.place(x=30, y=265)
image_entry.insert(0, 'Image path and Name')
image_entry.bind('<FocusIn>', on_enter)
image_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=290)


def clear():
    email_entry.delete(0, END)
    email_entry.insert(0, 'Student ID')
    image_entry.delete(0, END)
    image_entry.insert(0, 'Image path and Name')
    department_entry.delete(0, END)
    department_entry.insert(0, 'Department')
    studentname_entry.delete(0, END)
    studentname_entry.insert(0, 'Student Name')
    year_entry.delete(0, END)
    year_entry.insert(0, 'year of Academic')
    institute_entry.delete(0, END)
    institute_entry.insert(0, 'Institute')

def add():
    if email_entry.get() == 'Student ID' or image_entry.get() == 'Image path and Name' or  department_entry.get() == 'Department' or studentname_entry.get() == 'Student Name' or institute_entry.get() == 'Institute' or year_entry.get() == 'year of Academic':
        messagebox.showerror('Error', 'all fields are required')
    else:
        messagebox.showinfo('Done', 'Registration is done successfully')
        clear()


btn_login = Button(frame, width=39, pady=7, text="Done ", bg="#57a1f8", fg='white', border=0, command=add)
btn_login.place(x=35, y=380)

addstudent_window.mainloop()
