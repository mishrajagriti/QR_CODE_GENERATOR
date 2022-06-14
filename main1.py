from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage

class QR_Generator:
    def __init__(self,root):
        self.root =root
        self.root.geometry("900x500+200+50")
        self.root.title("QR_Generator | Developed By Jagriti")
        self.root.resizable(False,False)

        title=Label(self.root,text="QR Code Generator",font=("times new roman",40),bg='#053246',fg='white',anchor='w').place(x=0,y=0,relwidth=1)

        #====Employee Details window================
        #======Variables=====
        self.var_emp_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_designation=StringVar()

        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='Sky Blue')
        emp_Frame.place(x=50,y=100,width=500,height=380)

        emp_title=Label(emp_Frame,text="Employee Details",font=("goudy old style",20),bg='#053246',fg='white').place(x=0,y=0,relwidth=1)
        
        lbl_emp_code=Label(emp_Frame,text="Employee ID",font=("times new roman",15,'bold'),bg='Sky Blue').place(x=20,y=60)
        lbl_name=Label(emp_Frame,text="Employee Name",font=("times new roman",15,'bold'),bg='Sky Blue').place(x=20,y=110)
        lbl_department=Label(emp_Frame,text="Employee Department",font=("times new roman",15,'bold'),bg='Sky Blue').place(x=20,y=160)
        lbl_designation=Label(emp_Frame,text="Employee Designation",font=("times new roman",15,'bold'),bg='Sky Blue').place(x=20,y=210)


        txt_emp_code=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_emp_code,bg='White').place(x=250,y=60)
        txt_name=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_name,bg='White').place(x=250,y=110)
        txt_department=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_department,bg='White').place(x=250,y=160)
        txt_designation=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_designation,bg='White').place(x=250,y=210)



        btn_generate=Button(emp_Frame,text='QR Generate',command=self.generate,font=("times new roman",18,'bold'),bg='#053246',fg='white').place(x=90,y=250,width=180,height=30)
        btn_Clear=Button(emp_Frame,text='Clear',command=self.clear,font=("times new roman",18,'bold'),bg='#696969',fg='white').place(x=282,y=250,width=120,height=30)


        self.msg=''
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("times new roman",20),bg='Sky Blue',fg='Dark Blue')
        self.lbl_msg.place(x=0,y=310,relwidth=1)

        #====Employee QR Code window================
        


        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='Sky Blue')
        qr_Frame.place(x=600,y=100,width=250,height=380)

        emp_title=Label(qr_Frame,text="Employee QR Code",font=("goudy old style",20),bg='#053246',fg='white').place(x=0,y=0,relwidth=1)

    
        self.qr_code=Label(qr_Frame,text='No QR\nAvailable',font=('times new roman',15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)

    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)

    def generate(self):
        if self.var_designation.get()=='' or self.var_department.get()=='' or self.var_name.get()=='' or self.var_emp_code.get()=='':
            self.msg='All Feilds are Required!!!!!!!!!'
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Employee ID: {self.var_emp_code.get()}\nEmployee Name:{self.var_name.get()}\nEmployee department:{self.var_department.get()}\nEmployee designation:{self.var_designation.get()}")
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("QR_Generator/Emp_"+str(self.var_emp_code.get())+'.png')
            #==========QR Code Image Update================
            self.im=ImageTk.PhotoImage(file="QR_Generator/Emp_"+str(self.var_emp_code.get())+'.png')
            self.qr_code.config(image=self.im)
            #============updating Notification==============
            self.msg='QR Generated Successfully!!!!!!'
            self.lbl_msg.config(text=self.msg,fg='green')



root=Tk()
obj =QR_Generator(root)
root.mainloop()