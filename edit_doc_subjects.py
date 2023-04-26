import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk

doc_subject=Tk()
doc_subject.title('Edit course')
doc_subject.geometry("925x500+300+200")
doc_subject.config(bg="#ECF9FF")
doc_subject.resizable(False,False)

#back forward button
def backfw_btn():
    doc_subject.withdraw()
    import edit_doc_choice
    edit_doc_choice.doc_choice.deiconify()

bfw_btn = tkinter.PhotoImage(file='backfw.png',master=doc_subject)
back_forward_btn = Button(doc_subject,cursor='hand2',image=bfw_btn,bd=0,bg="#ECF9FF",activebackground="#ECF9FF",height=80,width=80,command=backfw_btn)
back_forward_btn.place(x=10,y=5)

img_logo = tkinter.PhotoImage(file='logo.png',master=doc_subject)
doc_subject.iconphoto(False,img_logo)

Label(doc_subject,image=img_logo ,bg="white",background="#ECF9FF").place(x=50,y=120)
frame = Frame(doc_subject,width=350,height=370,bg="#ECF9FF")
frame.place(x=480,y=50)


frame1= LabelFrame(doc_subject,bd=0,bg="#ECF9FF",relief=RIDGE,text="المواد الخاصة بالدكتور", font=("times new roman",12,"bold"))
frame1.place(x=390,y=50,width=510,height=480)

e=Label(frame1,width=15,text='اسم الماده',relief='ridge',anchor="w")
e.grid(row=1,column=0)
e=Label(frame1,width=15,text='القسم',relief='ridge',anchor="w")
e.grid(row=1,column=1)
e=Label(frame1,width=15,text='العام الدراسي',relief='ridge',anchor="w")
e.grid(row=1,column=2)
e=Label(frame1,width=15,text='الترم',relief='ridge',anchor="w")
e.grid(row=1,column=3)
#add_button = Button(frame1, width=4, height=1, text="حذف",relief='ridge',anchor='w',bg="#0081C9", fg='white',)
#add_button.grid(row=1,column=4)

e=Label(frame1,width=15,text='Data Structure',relief='ridge',anchor="w")
e.grid(row=2,column=0)
e=Label(frame1,width=15,text='Computer Science',relief='ridge',anchor="w")
e.grid(row=2,column=1)
e=Label(frame1,width=15,text='third year',relief='ridge',anchor="w")
e.grid(row=2,column=2)
e=Label(frame1,width=15,text='second',relief='ridge',anchor="w")
e.grid(row=2,column=3)
add_button = Button(frame1, width=4,height=1, text="حذف",relief='ridge',anchor='w',bg="#0081C9", fg='white',)
add_button.grid(row=2,column=4)

for i in range(4):
    for j in range(4):
        e = Label(frame1,width=15, text='from database...',
        relief='ridge', anchor="w")  
        e.grid(row=i+3, column=j) 
    add_button = Button(frame1, width=4,height=1, text="حذف",relief='ridge',anchor='w',bg="#0081C9", fg='white',)
    add_button.grid(row=i+3,column=4) 

e=Label(frame1,width=15,text='  ',bd=0)
e.grid(row=8,column=0)   
e=Label(frame1,width=15,text='اضافه ماده جديده',bg="#ECF9FF",bd=0, font=("times new roman",12,"bold"))
e.grid(row=9,column=0)   

e=Label(frame1,width=15,text='  ',bd=0)
e.grid(row=10,column=0) 

e=Label(frame1,width=10,text='اختر القسم',anchor="w")
e.grid(row=11,column=0)  

n = tk.StringVar()
monthchoosen = ttk.Combobox(frame1, width = 15, textvariable = n)
  
# Adding combobox drop down list
monthchoosen['values'] = (' علوم حاسب', 
                          ' هندسه',
                          ' نظم ومعلومات',
                          ' ادارى اعمال',
                          ' اعلام',
                          )
  
monthchoosen.grid(column = 1, row = 11)
monthchoosen.current()

##########

e=Label(frame1,width=10,text='اختر الماده',anchor="w")
e.grid(row=11,column=2)  

n = tk.StringVar()
monthchoosen = ttk.Combobox(frame1, width = 15, textvariable = n)
  
# Adding combobox drop down list
monthchoosen['values'] = ('Data Structure', 
                          ' Algrothims',
                          ' OOP ',
                          'Programming',
                          'Operating System',
                          )
  
monthchoosen.grid(column = 3, row = 11)
monthchoosen.current()

e=Label(frame1,width=15,text='',bd=0)
e.grid(row=12,column=1) 
add_button = Button(frame1, width=15, height=1, text="اضافه ماده جديده",relief='ridge',anchor='w',bg="#0081C9", fg='white',)
add_button.grid(row=13,column=2)

doc_subject.mainloop()