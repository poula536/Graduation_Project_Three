import tkinter
from tkinter import *
from tkinter import messagebox

addcourse_window = Tk()
addcourse_window.title('Add Course')
addcourse_window.geometry("925x500+300+200")
addcourse_window.config(bg="#ECF9FF")
addcourse_window.resizable(False, False)


# back forward button
def backfw_btn():
    addcourse_window.withdraw()
    import dashboard_admin
    dashboard_admin.admin_dashboard_window.deiconify()


bfw_btn = tkinter.PhotoImage(file='backfw.png', master=addcourse_window)
back_forward_btn = Button(addcourse_window, cursor='hand2', image=bfw_btn, bd=0, bg="#ECF9FF",
                          activebackground="#ECF9FF", height=80, width=80, command=backfw_btn)
back_forward_btn.place(x=10, y=5)

img_logo = tkinter.PhotoImage(file='logo.png', master=addcourse_window)
addcourse_window.iconphoto(False, img_logo)
Label(addcourse_window, image=img_logo, bg="white", background="#ECF9FF").place(x=50, y=120)
frame = Frame(addcourse_window, width=350, height=440, bg="#ECF9FF")
frame.place(x=480, y=50)

heading = Label(frame, text="اضافة مادة", fg="black", bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 25, 'bold'))
heading.place(x=100, y=-6)


def on_enter(e):
    doctorname_entry.delete(0, 'end')


def on_leave(e):
    doctor_name = doctorname_entry.get()
    if doctor_name == '':
        doctorname_entry.insert(0, 'اسم الدكتور')


doctorname_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
doctorname_entry.place(x=30, y=70)
doctorname_entry.insert(0, 'اسم الدكتور')
doctorname_entry.bind('<FocusIn>', on_enter)
doctorname_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=95)


def on_enter(e):
    email_entry.delete(0, 'end')


def on_leave(e):
    name = email_entry.get()
    if name == '':
        email_entry.insert(0, 'عنوان البريد الالكتروني')


email_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
email_entry.place(x=30, y=115)
email_entry.insert(0, 'عنوان البريد الالكتروني')
email_entry.bind('<FocusIn>', on_enter)
email_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=140)


def on_enter(e):
    password_entry.delete(0, 'end')


def on_leave(e):
    password = password_entry.get()
    if password == '':
        password_entry.insert(0, 'كلمه السر')


password_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
password_entry.place(x=30, y=150)
password_entry.insert(0, 'كلمه السر')
password_entry.bind('<FocusIn>', on_enter)
password_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=175)


def on_enter(e):
    institute_entry.delete(0, 'end')


def on_leave(e):
    institute_name = institute_entry.get()
    if institute_name == '':
        institute_entry.insert(0, 'اسم المعهد')


institute_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
institute_entry.place(x=30, y=185)
institute_entry.insert(0, 'اسم المعهد')
institute_entry.bind('<FocusIn>', on_enter)
institute_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=210)


def on_enter(e):
    department_entry.delete(0, 'end')


def on_leave(e):
    department_name = department_entry.get()
    if department_name == '':
        department_entry.insert(0, 'اسم الشعبة')


department_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
department_entry.place(x=30, y=225)
department_entry.insert(0, 'اسم الشعبة')
department_entry.bind('<FocusIn>', on_enter)
department_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=250)


def on_enter(e):
    subject_entry.delete(0, 'end')


def on_leave(e):
    material_name = subject_entry.get()
    if material_name == '':
        subject_entry.insert(0, 'اسم المادة')


subject_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
subject_entry.place(x=30, y=265)
subject_entry.insert(0, 'اسم المادة')
subject_entry.bind('<FocusIn>', on_enter)
subject_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=290)


def on_enter(e):
    academic_year_entry.delete(0, 'end')


def on_leave(e):
    year_number = academic_year_entry.get()
    if year_number == '':
        academic_year_entry.insert(0, 'العام الدراسي')


academic_year_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF",
                            font=('Microsoft YaHei UI Light ', 15))
academic_year_entry.place(x=30, y=295)
academic_year_entry.insert(0, 'العام الدراسي')
academic_year_entry.bind('<FocusIn>', on_enter)
academic_year_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=320)


def on_enter(e):
    semester_entry.delete(0, 'end')


def on_leave(e):
    semester_name = semester_entry.get()
    if semester_name == '':
        semester_entry.insert(0, 'الفصل الدراسي')


semester_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
semester_entry.place(x=30, y=330)
semester_entry.insert(0, 'الفصل الدراسي')
semester_entry.bind('<FocusIn>', on_enter)
semester_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=358)


def clear():
    email_entry.delete(0, END)
    email_entry.insert(0, 'عنوان البريد الالكتروني')
    subject_entry.delete(0, END)
    subject_entry.insert(0, 'اسم المادة')
    semester_entry.delete(0, END)
    semester_entry.insert(0, 'الفصل الدراسي')
    department_entry.delete(0, END)
    department_entry.insert(0, 'اسم الشعبة')
    doctorname_entry.delete(0, END)
    doctorname_entry.insert(0, 'اسم الدكتور')
    password_entry.delete(0, END)
    password_entry.insert(0, 'كلمه السر')
    institute_entry.delete(0, END)
    institute_entry.insert(0, 'اسم المعهد')
    academic_year_entry.delete(0, END)
    academic_year_entry.insert(0, 'العام الدراسي')


def add():
    if email_entry.get() == 'عنوان البريد الالكتروني' or subject_entry.get() == 'اسم المادة' or semester_entry.get() == 'الفصل الدراسي' or department_entry.get() == 'اسم الشعبة' or doctorname_entry.get() == 'اسم الدكتور' or password_entry.get() == 'كلمه السر' or institute_entry.get() == 'اسم المعهد' or academic_year_entry.get() == 'العام الدراسي':
        messagebox.showerror('Error', 'all fields are required')
    else:
        messagebox.showinfo('Done', 'Registration is done successfully')
        clear()


btn_login = Button(frame, width=39, pady=7, text="اضافه ", bg="#57a1f8", fg='white', border=0, command=add)
btn_login.place(x=35, y=380)

addcourse_window.mainloop()
