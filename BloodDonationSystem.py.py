import tkinter as tk
from multiprocessing import Value
from optparse import Values
from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk,messagebox
from tkinter.tix import Select
from turtle import fd
from PIL import Image,ImageTk #pip install pillow 
import pymysql #pip install pymysql
import re

#regex for email_id
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

#regex for contact 
pattern="^([+]\d{2})? \d{10}$]"

class Register:

    #def My_Func(self,root):
    def __init__(self,root):

        self.root=root
        self.root.title("Registration window")
        self.root.geometry("1266x780+100+0")
        self.root.config(bg="orange")

        #left side bg image
        self.left=ImageTk.PhotoImage(file="Images/img13.png")
        left=Label(self.root,image=self.left,bg="orange").place(x=10,y=10,width=500,height=780)
        
        #===Register Frame===
        
        frame1=Frame(self.root,bg="white",highlightbackground="black", highlightthickness=2)
        frame1.place(x=493,y=53,width=740,height=709)
        
        

        #.....title...
        title=Label(frame1,text="Blood Donation Registration Form",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=170,y=30)

        #.....row1.....

        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=85,y=105)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=85,y=140,width=250)


        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=405,y=105)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=405,y=140,width=250)

        #.....row2.....

        address=Label(frame1,text="Address",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=85,y=180)
        self.txt_address1=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_address1.place(x=85,y=215,width=570)
        self.txt_address2=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_address2.place(x=85,y=250,width=570)

        #......row3.....

        age=Label(frame1,text="Age",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=85,y=295)
        self.txt_age=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_age.place(x=85,y=330,width=250)

        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=405,y=295)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=405,y=330,width=250)


        
        #.....row 4.....

        gender=Label(frame1,text="Gender",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=85,y=365)
        
        self.cmb_gender=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=LEFT)
        self.cmb_gender['values']=("Select Your Gender","Male","Female","Trans-gender")
        self.cmb_gender.current(0)
        self.cmb_gender.place(x=85,y=400,width=250)

        bldgrp=Label(frame1,text="Blood Group",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=405,y=365)
        self.cmb_bldgrp=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=LEFT)
        self.cmb_bldgrp['values']=("Select Your Blood Group","A+","A-","B+","B-","AB+","AB-","O+","O-")
        self.cmb_bldgrp.current(0)
        self.cmb_bldgrp.place(x=405,y=400,width=250)


        #....row 5....

        email=Label(frame1,text="E-Mail Address",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=85,y=445)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=85,y=480,width=570)

        #....Terms and conditions....
        self.var_chk=IntVar()
        chk=Checkbutton(frame1, text="MY AGE IS BETWEEN 18 AND 65 YEARS OLD AND I'M ELIGIBLE FOR BLOOD DONATION...",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",11)).place(x=38,y=520)
        btn_register=Button(frame1,text="Register",font=("times new roman",16,"bold"),width=7,height=1,bg="green",fg="white",cursor="hand2",command=self.register_data).place(x=325,y=580)
        btn_register_remvbg=Button(self.root,font=("times new roman",44,"bold"),bg="white",bd=1,borderwidth=0.4,width=13,height=1,fg="white").place(x=29,y=649)
        btn_register_remvbg=Button(self.root,bg="white",bd=2,borderwidth=1,width=65,height=1,fg="white",highlightbackground="black", highlightthickness=1).place(x=29,y=738)
        btn_register=Button(self.root,text="List of Registered candidates",font=("times new roman",16,"bold"),bg="light yellow",bd=1,borderwidth=1,width=25,height=1,fg="black",cursor="hand2",command=self.show).place(x=100,y=680)
        
        btn_register_remvbg=Button(self.root,bg="orange",width=175,height=3,fg="orange").place(x=0,y=0)
        btn_register_remvbg=Button(self.root,bg="orange",width=3,height=50,fg="white").place(x=0,y=54)
        btn_register_remvbg=Button(self.root,bg="orange",width=46,height=60,fg="white").place(x=1233.3,y=0)
        btn_register_remvbg=Button(self.root,bg="orange",width=250,height=3,fg="white").place(x=0,y=762)

    #database creation
   
    def register_data(self):
        validateEmail = re.search(regex, self.txt_email.get())
        validateContact=re.search(pattern, self.txt_contact.get())

        if self.txt_fname.get()=="" or self.txt_address1.get()=="" or self.txt_age.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.txt_lname.get()=="" or self.cmb_bldgrp.get()=="Select Your Blood Group" or self.cmb_gender.get()=="Select Your Gender" :
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)

        elif not validateContact and not self.txt_contact.get().strip().isdigit():
            messagebox.showerror("Error","Please enter 10 digit phone number only.",parent=self.root)

        elif not self.txt_age.get().strip().isdigit():
            messagebox.showerror("Error","Please enter positive integers only as a Age.",parent=self.root)

        elif self.txt_age.get()<"18":
            messagebox.showerror("Error","You Are Not Eligible For Blood Donation Because Your Age is less than 18",parent=self.root)

        elif self.txt_age.get()>"65":
            messagebox.showerror("Error","You Are Not Eligible For Blood Donation Because Your Age is greater than 65",parent=self.root)

        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our Terms & Conditions",parent=self.root)

        elif not validateEmail:
            messagebox.showerror("Error","Please enter valid email id",parent=self.root)

        else:

            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="pbl 2 project")
                cur=con.cursor()
                sql ="INSERT INTO `registered candidates info`(`First Name`, `Last Name`, `Address 1`, `Address 2`, `Age`, `Contact No.`, `Gender`, `Blood Group`, `E-Mail`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (self.txt_fname.get(),self.txt_lname.get(),self.txt_address1.get(),self.txt_address1.get(),self.txt_age.get(),self.txt_contact.get(),self.cmb_gender.get(),self.cmb_bldgrp.get(),self.txt_email.get())
                cur.execute(sql, val)
                con.commit()
                con.close()

                messagebox.showinfo("Success","You Have Successfully Registered For Blood Donation",parent=self.root)
                
                self.txt_fname.delete(0, END)
                self.txt_lname.delete(0, END)
                self.txt_address1.delete(0, END)
                self.txt_address2.delete(0, END)
                self.txt_age.delete(0, END)
                self.txt_contact.delete(0, END)
                self.cmb_gender.current(0)
                self.cmb_bldgrp.current(0)
                self.txt_email.delete(0, END)
                self.var_chk.set(False)
                
                
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

    def show(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="pbl 2 project")
        cur=con.cursor()
        sql="SELECT `ID`,`First Name`,`Last Name`,`Contact No.`,`Gender`,`Blood Group` FROM `registered candidates info`"
        cur.execute(sql)
        records = cur.fetchall()
        self.label = tk.Label(self.root, text="Registered Candidates", font=("times new roman",30))
        btn_show = tk.Button(self.root,text="Finish", width=15,command = self.mainFun).grid(row=7, column=0)
        
        root.title("Registered Candidates")
        label = tk.Label(root, text="Registered Candidates", font=("times new roman",30)).grid(row=0, columnspan=2)

        cols = ('ID','First Name','Last Name','Contact No.','Gender','Blood Group')
        
        listBox = ttk.Treeview(root, columns=cols, show='headings')
        listBox.column("ID",anchor=tk.CENTER)
        listBox.column("First Name",anchor=tk.CENTER)
        listBox.column("Last Name",anchor=tk.CENTER)
        listBox.column("Contact No.",anchor=tk.CENTER)
        listBox.column("Gender",anchor=tk.CENTER)
        listBox.column("Blood Group",anchor=tk.CENTER)

        for col in cols:
            listBox.heading(col, text=col)    
            listBox.grid(row=1, column=0)

        for i, (id,firstname,lastname,contactno,gender,bloodgroup) in enumerate(records, start=1):
            listBox.insert("", "end", values=(id,firstname,lastname,contactno,gender,bloodgroup))

    def mainFun(self):
        Command = self.__init__(root)
        
root=Tk()
obj=Register(root)
root.mainloop()