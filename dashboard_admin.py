import tkinter
from tkinter import *

admin_dashboard_window = Tk()
admin_dashboard_window.title("Admin Dashboard")
admin_dashboard_window.geometry("1000x650+300+80")
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


def addstudent_btn():
    admin_dashboard_window.withdraw()
    import addstudentsdata
    addstudentsdata.addstudent_window.deiconify()

def attend_sheet_btn():
    admin_dashboard_window.withdraw()
    import view_attendancesheet_admin
    view_attendancesheet_admin.attendance_sheet_window.deiconify()


# create three buttons for taking attendance, adding new students, and viewing sheets
attendance_button = Button(admin_dashboard_window, width=20,height=5,padx=60 ,pady=10,border=0, bg="#0081C9", fg='white', text="Create New Account For Lecturer",
                           font=("Arial", 13,'bold'), command=createAccount_btn)
attendance_button.place(x=100, y=120)

attendance_button = Button(admin_dashboard_window, width=20,height=5, border=0,padx=60 ,pady=10,bg="#0081C9", fg='white',
                           text="Create New Account For Admin",font=("Arial", 13,'bold'),command=creatAdmin)
attendance_button.place(x=580, y=120)


add_button = Button(admin_dashboard_window, width=20,height=5, border=0,padx=60 ,pady=10,
                    bg="#0081C9", fg='white', text="Modify",
                    font=("Arial", 13,'bold'),command=edit_data_btn)
add_button.place(x=100, y=270)

sheets_button = Button(admin_dashboard_window, width=20, height=5,padx=60,pady=10,border=0, bg="#0081C9", fg='white', text="Add Course",
                       command=add_course_btn, font=("Arial", 13,'bold'))
sheets_button.place(x=580, y=270)


student_button = Button(admin_dashboard_window, width=20, height=5,padx=60,pady=10, border=0,bg="#0081C9", fg='white', text="Add New Students",
                        command=addstudent_btn,font=("Arial", 13,'bold'))
student_button.place(x=100, y=420)

student_button = Button(admin_dashboard_window, width=20, height=5,padx=60,pady=10, border=0,bg="#0081C9", fg='white', text="View Attendance Sheet",
                        command=attend_sheet_btn,font=("Arial", 13,'bold'))
student_button.place(x=580, y=420)

admin_dashboard_window.mainloop()
