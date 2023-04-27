import tkinter
from tkinter import *

import pymysql

doctor_window = Tk()
doctor_window.title('Dashboard')
doctor_window.geometry("925x500+300+200")
doctor_window.config(bg="#ECF9FF")
doctor_window.resizable(False,False)


#back forward button
def backfw_btn():
    doctor_window.withdraw()
    import main
    main.login_window.deiconify()

bfw_btn = tkinter.PhotoImage(file='logout.png',master=doctor_window)
back_forward_btn = Button(doctor_window,cursor='hand2',image=bfw_btn,bd=0,bg="#ECF9FF",activebackground="#ECF9FF",height=80,width=80,command=backfw_btn)
back_forward_btn.place(x=10,y=5)




#frame for subjects
fram_one=Frame(doctor_window,width=250,height=230,bg="#0081C9").place(x=30,y=130)
fram_two=Frame(doctor_window,width=250,height=230,bg="#0081C9").place(x=320,y=130)
fram_three=Frame(doctor_window,width=250,height=230,bg="#0081C9").place(x=620,y=130)

#frames for subjects
Label(doctor_window,text="Data Structure",bg="#0081C9",fg='white',font=('Microsoft YaHei UI Light ',15)).place(x=80,y=140)
Label(doctor_window,text="Database",bg="#0081C9",fg='white',font=('Microsoft YaHei UI Light ',15)).place(x=390,y=140)
Label(doctor_window,text="Structure Programming",bg="#0081C9",fg='white',font=('Microsoft YaHei UI Light ',15)).place(x=635,y=140)

#frame one
Label(doctor_window,text="قسم حاسبات",bg="#0081C9",fg='white',font=('Microsoft YaHei UI Light ',15)).place(x=110,y=190)
Label(doctor_window,text="شعبه علوم حاسب",bg="#0081C9",fg='white',font=('Microsoft YaHei UI Light ',15)).place(x=90,y=240)

#frame two
Label(doctor_window,text="قسم حاسبات",bg="#0081C9",fg='white',font=('Microsoft YaHei UI Light ',15)).place(x=400,y=190)
Label(doctor_window,text="شعبه علوم حاسب",bg="#0081C9",fg='white',font=('Microsoft YaHei UI Light ',15)).place(x=380,y=240)

#frame three
Label(doctor_window,text="قسم حاسبات",bg="#0081C9",fg='white',font=('Microsoft YaHei UI Light ',15)).place(x=700,y=190)
Label(doctor_window,text="شعبه علوم حاسب",bg="#0081C9",fg='white',font=('Microsoft YaHei UI Light ',15)).place(x=680,y=240)

def detals():
    doctor_window.withdraw()
    import attendence_dashboard
    attendence_dashboard.attendance_window.deiconify()

Button(doctor_window,width=10,pady=7,text="الدخول",bg="white",fg='black',border=0,command=detals).place(x=110,y=310)
Button(doctor_window,width=10,pady=7,text="الدخول",bg="white",fg='black',border=0,command=detals).place(x=405,y=310)
Button(doctor_window,width=10,pady=7,text="الدخول",bg="white",fg='black',border=0,command=detals).place(x=710,y=310)

doctor_window.mainloop()
