import tkinter
from tkinter import *
import cv2
from tkinter import messagebox

attendance_window=Tk()
attendance_window.title("Attendance System")
attendance_window.geometry("925x500+300+200")
attendance_window.config(bg="#ECF9FF")
attendance_window.resizable(False,False)

#back forward button
def backfw_btn():
    attendance_window.withdraw()
    import dashboard_doc
    dashboard_doc.doctor_window.deiconify()


bfw_btn = tkinter.PhotoImage(file='backfw.png',master=attendance_window)
back_forward_btn = Button(attendance_window,cursor='hand2',image=bfw_btn,bd=0,bg="#ECF9FF",activebackground="#ECF9FF",height=80,width=80,command=backfw_btn)
back_forward_btn.place(x=10,y=5)



img_logo = tkinter.PhotoImage(file='logo.png',master=attendance_window)
attendance_window.iconphoto(False,img_logo)

Label(attendance_window,image=img_logo, bg="white",background="#ECF9FF").place(x=50,y=120)
frame = Frame(attendance_window,width=350,height=370,bg="#ECF9FF")
frame.place(x=480,y=100)


def take_attendance():
    print("Window will be added soon")


def take_attendance_manually():
    attendance_window.withdraw()
    import addstudent
    addstudent.Newstudent_window.deiconify()

def view_sheets():
    print("Viewing attendance sheets...")


# create three buttons for taking attendance, adding new students, and viewing sheets
attendance_button = Button(frame,width=15,border=0 ,bg="#0081C9",fg='white',text="اخذ الحضور",
                           command=take_attendance, font=("Arial", 14))
attendance_button.place(x=140,y=80)


add_button = Button(frame, width=15,border=0,bg="#0081C9",fg='white',text="اخذ الحضور يدويا",
                    command=take_attendance_manually, font=("Arial", 14))
add_button.place(x=140,y=150)

sheets_button = Button(frame,width=15,border=0 ,bg="#0081C9",fg='white',text="اظهار كشف الحضور",
                       command=view_sheets, font=("Arial", 14))
sheets_button.place(x=140,y=220)

attendance_window.mainloop()