import tkinter
from tkinter import *

admin_dashboard_window = Tk()
admin_dashboard_window.title("Admin Dashboard")
admin_dashboard_window.geometry("925x500+300+200")
admin_dashboard_window.config(bg="#ECF9FF")
admin_dashboard_window.resizable(False, False)


def signout():
    admin_dashboard_window.withdraw()
    import adminlogin
    adminlogin.adminlogin_window.deiconify()


signout_btn = tkinter.PhotoImage(file='logout.png', master=admin_dashboard_window)
back_forward_btn = Button(admin_dashboard_window, cursor='hand2', image=signout_btn, bd=0, bg="#ECF9FF",
                          activebackground="#ECF9FF", height=80, width=80, command=signout)
back_forward_btn.place(x=10, y=5)

img_logo = tkinter.PhotoImage(file='logo.png', master=admin_dashboard_window)
admin_dashboard_window.iconphoto(False, img_logo)

Label(admin_dashboard_window, bg="white", image=img_logo, background="#ECF9FF").place(x=50, y=120)
frame = Frame(admin_dashboard_window, width=450, height=370, bg="#ECF9FF")
frame.place(x=420, y=100)

#heading = Label(frame, text="admin مرحبا محمد", fg="black", bg="#ECF9FF",font=('Microsoft YaHei UI Light ', 25, 'bold'))
#heading.place(x=100, y=-6)

def createAccount_btn():
    admin_dashboard_window.withdraw()
    import addnewDoctor
    addnewDoctor.new_doctor_window.deiconify()

def creatAdmin():
    admin_dashboard_window.withdraw()
    import addnewadmin
    addnewadmin.new_admin_window.deiconify()

def edit_data_btn():
    admin_dashboard_window.withdraw()
    import modify
    modify.modify_window.deiconify()


def add_course_btn():
    admin_dashboard_window.withdraw()
    import addcourse
    addcourse.addcourse_window.deiconify()


# create three buttons for taking attendance, adding new students, and viewing sheets
attendance_button = Button(frame, width=30, border=0, bg="#0081C9", fg='white', text="Create New Account For Lecturer",
                           command=createAccount_btn, font=("Arial", 13,'bold'),pady=8)
attendance_button.place(x=60, y=20)

attendance_button = Button(frame, width=30, border=0, bg="#0081C9", fg='white', text="Create New Account For Admin",
                           command=creatAdmin, font=("Arial", 13,'bold'),pady=8)
attendance_button.place(x=60, y=100)


add_button = Button(frame, width=30, border=0, bg="#0081C9", fg='white', text="Modify", command=edit_data_btn,
                    font=("Arial", 13,'bold'),pady=8)
add_button.place(x=60, y=180)

sheets_button = Button(frame, width=30, border=0, bg="#0081C9", fg='white', text="Add Course",
                       command=add_course_btn, font=("Arial", 13,'bold'),pady=8)
sheets_button.place(x=60, y=260)

admin_dashboard_window.mainloop()
