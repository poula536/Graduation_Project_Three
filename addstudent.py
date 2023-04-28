import tkinter
from tkinter import *
from tkinter import messagebox
import cv2

Newstudent_window=Tk()
Newstudent_window.title('Take New Student')
Newstudent_window.geometry("925x500+300+200")
Newstudent_window.config(bg="#ECF9FF")
Newstudent_window.resizable(False,False)
img_logo = tkinter.PhotoImage(file='logo.png',master=Newstudent_window)
Newstudent_window.iconphoto(False, img_logo)
#back forward button
def backfw_btn():
    Newstudent_window.withdraw()
    import attendence_dashboard
    attendence_dashboard.attendance_window.deiconify()


bfw_btn = tkinter.PhotoImage(file='backfw.png',master=Newstudent_window)
back_forward_btn = Button(Newstudent_window,cursor='hand2',image=bfw_btn,bd=0,bg="#ECF9FF",activebackground="#ECF9FF",height=80,width=80,command=backfw_btn)
back_forward_btn.place(x=10,y=5)

frame = Frame(Newstudent_window,width=350,height=370,bg="#ECF9FF")
frame.place(x=300,y=90)

def on_enter(e):
    fuullname_entry.delete(0,'end')
def on_leave(e):
    name =fuullname_entry.get()
    if name=='':
        fuullname_entry.insert(0, 'Enter Full Name')


fuullname_entry = Entry(frame,width=35,fg='#181823',border=0,bg="#ECF9FF",font=('Microsoft YaHei UI Light ',15))
fuullname_entry.place(x=30,y=100)
fuullname_entry.insert(0,'Enter Full Name')
fuullname_entry.bind('<FocusIn>',on_enter)
fuullname_entry.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=125)

def take_attendance_manually():
    if fuullname_entry.get()=='Enter Full Name' or fuullname_entry.get()=='':
        messagebox.showerror('Error','Enter your full name')
    else:
        dataset_path = "E:/finalproject/set_images"
        cap = cv2.VideoCapture(0)
        face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        new_member_name = fuullname_entry.get()
        n = 1
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                face_image = gray[y:y + h, x:x + w]
                resized_face = cv2.resize(face_image, (100, 100))
            cv2.imwrite(f"{dataset_path}/{new_member_name}_{x}_{y}.jpg", face_image)
            messagebox.showinfo('Done', f"New member {new_member_name} added to dataset.")
            cv2.imshow('frame', frame)
            n += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if n == 2:
                break
        cv2.destroyAllWindows()


enter_btn = Button(frame,cursor='hand2',width=39,pady=7,text="Enter",
                   bg="#57a1f8",fg='white',border=0,command=take_attendance_manually)
enter_btn.place(x=35,y=250)

Newstudent_window.mainloop()