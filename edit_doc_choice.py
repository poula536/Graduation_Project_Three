import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk

doc_choice=Tk()
doc_choice.title('Edit course')
doc_choice.geometry("925x500+300+200")
doc_choice.config(bg="#ECF9FF")
doc_choice.resizable(False,False)

#back forward button
def backfw_btn():
    doc_choice.withdraw()
    import editcourse
    editcourse.editcourse_window.deiconify()

bfw_btn = tkinter.PhotoImage(file='backfw.png',master=doc_choice)
back_forward_btn = Button(doc_choice,cursor='hand2',image=bfw_btn,bd=0,bg="#ECF9FF",activebackground="#ECF9FF",height=80,width=80,command=backfw_btn)
back_forward_btn.place(x=10,y=5)

img_logo = tkinter.PhotoImage(file='logo.png',master=doc_choice)
doc_choice.iconphoto(False,img_logo)

Label(doc_choice,image=img_logo ,bg="white",background="#ECF9FF").place(x=50,y=120)
frame = Frame(doc_choice,width=350,height=370,bg="#ECF9FF")
frame.place(x=480,y=50)

#frame1= LabelFrame(doc_data,bd=0,bg="#ECF9FF",relief=RIDGE,text="", font=("times new roman",12,"bold"))
#frame1.place(x=390,y=50,width=510,height=480)

def subject_btn():
    doc_choice.withdraw()
    import edit_doc_subjects
    edit_doc_subjects.doc_subject.deiconify()
add_button = Button(doc_choice, width=20, height=5,command=subject_btn,font=("times new roman",12,"bold"), text="تعديل المواد الخاصة بالدكتور",relief='ridge',anchor='w',bg="#0081C9", fg='white',)
add_button.place(x=400,y=170)

def info_btn():
    doc_choice.withdraw()
    import personal_data_doc
    personal_data_doc.doc_data.deiconify()

add_button = Button(doc_choice, width=20,command=info_btn, height=5,font=("times new roman",12,"bold"), text="تعديل البيانات الشخصية",relief='ridge',anchor='w',bg="#0081C9", fg='white',)
add_button.place(x=610,y=170)
doc_choice.mainloop()