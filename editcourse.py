import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


editcourse_window=Tk()
editcourse_window.title('Edit course')
editcourse_window.geometry("925x500+300+200")
editcourse_window.config(bg="#ECF9FF")
editcourse_window.resizable(False,False)

#back forward button
def backfw_btn():
    editcourse_window.withdraw()
    import dashboard_admin
    dashboard_admin.admin_dashboard_window.deiconify()

bfw_btn = tkinter.PhotoImage(file='backfw.png',master=editcourse_window)
back_forward_btn = Button(editcourse_window,cursor='hand2',image=bfw_btn,bd=0,bg="#ECF9FF",activebackground="#ECF9FF",height=80,width=80,command=backfw_btn)
back_forward_btn.place(x=10,y=5)

img_logo = tkinter.PhotoImage(file='logo.png',master=editcourse_window)
editcourse_window.iconphoto(False,img_logo)

Label(editcourse_window,image=img_logo ,bg="white",background="#ECF9FF").place(x=50,y=120)
frame = Frame(editcourse_window,width=350,height=370,bg="#ECF9FF")
frame.place(x=480,y=50)

heading = Label(frame,text="تعديل مادة",fg="black",bg="#ECF9FF",font=('Microsoft YaHei UI Light ',25,'bold'))
#heading.place(x=100,y=-6)
# create combobox
'''''''''
departments = [
    "None",
    "علوم حاسب",
    "نظم و معلومات"
]
clicked = StringVar()
clicked.set(departments[0])
dep_comp = ttk.Combobox(frame,values=departments,width=47)
dep_comp.current(0)
dep_comp.bind("<<ComboboxSelected>>")
dep_comp.place(x=25,y=110)
'''''

def on_enter(e):
    old_doctorname_entry.delete(0,'end')
def on_leave(e):
    old_name = old_doctorname_entry.get()
    if old_name=='':
        old_doctorname_entry.insert(0, 'ادخل اسم الدكتور')

old_doctorname_entry = Entry(frame,width=35,fg='#181823',border=0,bg="#ECF9FF",font=('Microsoft YaHei UI Light ',15))
old_doctorname_entry.place(x=30,y=80)
old_doctorname_entry.insert(0,'ادخل اسم الدكتور')
old_doctorname_entry.bind('<FocusIn>',on_enter)
old_doctorname_entry.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=110)




def edit():
    editcourse_window.withdraw()
    import edit_doc_choice
    edit_doc_choice.doc_choice.deiconify()
    
        

btn_login = Button(frame,width=39,pady=7,text="بحث",bg="#57a1f8",fg='white',border=0,command=edit)
btn_login.place(x=35,y=140)

editcourse_window.mainloop()