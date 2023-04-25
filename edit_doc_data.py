import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
edit_doc = Tk()
edit_doc.title("Edit Doctor Information")
edit_doc.geometry("925x500+300+200")
edit_doc.config(bg="#ECF9FF")
edit_doc.resizable(False, False)

def backfw_btn():
    edit_doc.withdraw()
    import dashboard_admin
    dashboard_admin.admin_dashboard_window.deiconify()


bfw_btn = tkinter.PhotoImage(file='backfw.png',master=edit_doc)
back_forward_btn = Button(edit_doc,cursor='hand2',image=bfw_btn,bd=0,bg="#ECF9FF",activebackground="#ECF9FF",height=80,width=80,command=backfw_btn)
back_forward_btn.place(x=10,y=5)

for i in range (5):
    e=Label(edit_doc,width=0,text='',fg='#ECF9FF')
    e.grid(row=i,column=22)

x=10
e=Label(edit_doc,width=20,text=' المواد الخاصه بالدكتور',anchor="w")
#e.grid(row=8,column=0)


e=Label(edit_doc,width=15,text='اسم الماده',relief='ridge',anchor="w")
e.grid(row=0+x,column=0)
e=Label(edit_doc,width=15,text='القسم',relief='ridge',anchor="w")
e.grid(row=0+x,column=1)
e=Label(edit_doc,width=15,text='العام الدراسي',relief='ridge',anchor="w")
e.grid(row=0+x,column=2)
e=Label(edit_doc,width=15,text='الترم',relief='ridge',anchor="w")
e.grid(row=0+x,column=3)
add_button = Button(edit_doc, width=4, height=1, text="حذف",relief='ridge',anchor='w',bg="#0081C9", fg='white',)
add_button.grid(row=0+x,column=4)
#############
e=Label(edit_doc,width=15,text='Data Structure',relief='ridge',anchor="w")
e.grid(row=1+x,column=0)
e=Label(edit_doc,width=15,text='Computer Science',relief='ridge',anchor="w")
e.grid(row=1+x,column=1)
e=Label(edit_doc,width=15,text='third year',relief='ridge',anchor="w")
e.grid(row=1+x,column=2)
e=Label(edit_doc,width=15,text='second',relief='ridge',anchor="w")
e.grid(row=1+x,column=3)
add_button = Button(edit_doc, width=4,height=1, text="حذف",relief='ridge',anchor='w',bg="#0081C9", fg='white',)
add_button.grid(row=1+x,column=4)
for i in range(4):
    for j in range(4):
        e = Label(edit_doc,width=15, text='abdoo',
        relief='ridge', anchor="w")  
        e.grid(row=x+i+2, column=j) 
    add_button = Button(edit_doc, width=4,height=1, text="حذف",relief='ridge',anchor='w',bg="#0081C9", fg='white',)
    add_button.grid(row=x+i+2,column=4) 

e=Label(edit_doc,width=15,text='')
e.grid(row=6+x,column=1)   
e=Label(edit_doc,width=15,text='اضافه ماده جديده',anchor="w")
e.grid(row=7+x,column=0)   

e=Label(edit_doc,width=15,text='  ')
e.grid(row=8+x,column=1) 
e=Label(edit_doc,width=10,text='اختر القسم',anchor="w")
e.grid(row=9+x,column=0)  

n = tk.StringVar()
monthchoosen = ttk.Combobox(edit_doc, width = 15, textvariable = n)
  
# Adding combobox drop down list
monthchoosen['values'] = (' علوم حاسب', 
                          ' هندسه',
                          ' نظم ومعلومات',
                          ' ادارى اعمال',
                          ' اعلام',
                          )
  
monthchoosen.grid(column = 1, row = 9+x)
monthchoosen.current()

##########

e=Label(edit_doc,width=10,text='اختر الماده',anchor="w")
e.grid(row=9+x,column=2)  

n = tk.StringVar()
monthchoosen = ttk.Combobox(edit_doc, width = 15, textvariable = n)
  
# Adding combobox drop down list
monthchoosen['values'] = ('Data Structure', 
                          ' Algrothims',
                          ' OOP ',
                          'Programming',
                          'Operating System',
                          )
  
monthchoosen.grid(column = 3, row = 9+x)
monthchoosen.current()

e=Label(edit_doc,width=15,text='')
e.grid(row=10+x,column=1) 
add_button = Button(edit_doc, width=15, height=1, text="اضافه ماده جديده",relief='ridge',anchor='w',bg="#0081C9", fg='white',)
add_button.grid(row=11+x,column=2)

##################### تعديل البيانات الشخصيه 

frame1= LabelFrame(edit_doc,bd=2,bg="#ECF9FF",relief=RIDGE,text="تعديل البيانات الشخصيه", font=("times new roman",12,"bold"))
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








edit_doc.mainloop()


