import tkinter
from tkinter import *
import pymysql

doctor_window = Tk()
doctor_window.title('Dashboard')
doctor_window.geometry("925x500+300+200")
doctor_window.config(bg="#ECF9FF")
doctor_window.resizable(False,False)
img_logo = tkinter.PhotoImage(file='logo.png', master=doctor_window)
doctor_window.iconphoto(False, img_logo)

con_db = pymysql.connect(host='localhost', user='root', password='123456789')
mycursor = con_db.cursor()
query = 'use facerecognation_attendance_System'
mycursor.execute(query)



#back forward button

def backfw_btn():
    query = "delete from currentlogin"
    mycursor.execute(query)
    con_db.commit()
    doctor_window.withdraw()
    import main
    main.login_window.deiconify()


bfw_btn = tkinter.PhotoImage(file='logout.png',master=doctor_window)
back_forward_btn = Button(doctor_window,cursor='hand2',image=bfw_btn,bd=0,bg="#ECF9FF",activebackground="#ECF9FF",height=80,width=80,command=backfw_btn)
back_forward_btn.place(x=10,y=5)
mydata = []
def mapacounnt(row):
    global mydata
    mydata.clear()
    mydata = list(row)
    return "welcome doctor "+ str(mydata)


#print(row)
acounnent = "select distinct full_name from lecturer join currentlogin on curent = email"
mycursor.execute(acounnent)
row = mycursor.fetchone()
great_txt = "welcome doctor " + str(row)
print(row)

doct_name_labl=Label(doctor_window,text=great_txt,fg="#070A52",width=25,bg="#ECF9FF",font=('Microsoft YaHei UI Light ',30))
doct_name_labl.place(x=210,y=20)



def detals():
    doctor_window.withdraw()
    import attendence_dashboard
    attendence_dashboard.attendance_window.deiconify()


def frames (x,b,z,d,n,subject_list):
    for i, (key, value) in enumerate(subject_list.items()):
        Frame(doctor_window, width=230, height=190, bg="#0081C9").place(x=x, y=130)
        Label(doctor_window, text=value[i], bg="#0081C9", fg='white', font=('Microsoft YaHei UI Light ', 15),borderwidth=0, relief="groove").place(x=b, y=140)
        Label(doctor_window, text=key, bg="#0081C9", fg='white', font=('Microsoft YaHei UI Light ', 15)).place(x=z, y=190)
        Button(doctor_window, width=10, pady=7, text="Enter", bg="white", fg='black', border=0, command=detals).place(x=d,y=240)
        if n > 1:
            x += 240
            b += 240
            z += 240
            d += 240
            value.remove(value[i])
            frames(x, b, z, d, n - 1,subject_list)

'''''''''
subject_list = {"Computer Science":[],"Information Systems":[],"Business Administration":[]}
query = "select course_name from course join currentlogin on curent = lecturer_email"
mycursor.execute(query)
row = mycursor.fetchone()
for i in row:
    res = "".join(i)
    subject_list["Computer Science"].append(res)
for key in list(subject_list.keys()):
    if len(subject_list[key]) == 0:
        del subject_list[key]

count = len(subject_list["Computer Science"])
frames(10,60,60,90,count,subject_list)
'''''

#con_db.close()
doctor_window.mainloop()


