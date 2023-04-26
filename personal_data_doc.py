import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


doc_data=Tk()
doc_data.title('Edit course')
doc_data.geometry("925x500+300+200")
doc_data.config(bg="#ECF9FF")
doc_data.resizable(False,False)

#back forward button
def backfw_btn():
    doc_data.withdraw()
    import edit_doc_choice
    edit_doc_choice.doc_choice.deiconify()

bfw_btn = tkinter.PhotoImage(file='backfw.png',master=doc_data)
back_forward_btn = Button(doc_data,cursor='hand2',image=bfw_btn,bd=0,bg="#ECF9FF",activebackground="#ECF9FF",height=80,width=80,command=backfw_btn)
back_forward_btn.place(x=10,y=5)

img_logo = tkinter.PhotoImage(file='logo.png',master=doc_data)
doc_data.iconphoto(False,img_logo)

Label(doc_data,image=img_logo ,bg="white",background="#ECF9FF").place(x=50,y=120)
frame = Frame(doc_data,width=350,height=370,bg="#ECF9FF")
frame.place(x=480,y=50)

frame1= LabelFrame(doc_data,bd=2,bg="#ECF9FF",relief=RIDGE,text="تعديل البيانات الشخصيه", font=("times new roman",12,"bold"))
frame1.place(x=500,y=10,width=410,height=480)

e=Label(frame1,width=10,text='الاسم بالكامل',anchor="w").place(x=15,y=30)
institute_entry = Entry(frame1, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
institute_entry.place(x=120, y=20)
institute_entry.insert(0, 'osama mohamed shafiq')
Frame(frame1, width=250, height=2, bg="black").place(x=115, y=50)

e=Label(frame1,width=15,text='البريد الالكتروني',anchor="w").place(x=15,y=90)
institute_entry = Entry(frame1, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
institute_entry.place(x=120, y=80)
institute_entry.insert(0, 'osama shafiq@gmail.com')
Frame(frame1, width=250, height=2, bg="black").place(x=115, y=110)

e=Label(frame1,width=10,text='القسم',anchor="w").place(x=15,y=140)
institute_entry = Entry(frame1, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
institute_entry.place(x=120, y=140)
institute_entry.insert(0, 'علوم حاسب')
Frame(frame1, width=250, height=2, bg="black").place(x=115, y=170)

e=Label(frame1,width=10,text='كلمة السر',anchor="w").place(x=15,y=200)
institute_entry = Entry(frame1, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
institute_entry.place(x=120, y=200)
institute_entry.insert(0, '1234567')
Frame(frame1, width=250, height=2, bg="black").place(x=115, y=230)
institute_entry.config(show='*')

e=Label(frame1,width=10,text='تأكيد كلمة السر',anchor="w").place(x=15,y=260)
institute_entry = Entry(frame1, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
institute_entry.place(x=120, y=260)
institute_entry.insert(0, '123456')
Frame(frame1, width=250, height=2, bg="black").place(x=115, y=290)
institute_entry.config(show='*')

add_button = Button(frame1, width=15, height=1, text="حفظ البيانات",relief='ridge',anchor='w',bg="#0081C9", fg='white',)
add_button.place(x=170,y=320)








doc_data.mainloop()




