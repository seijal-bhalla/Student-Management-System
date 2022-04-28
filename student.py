from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cx_Oracle
from tkinter import messagebox
class Student_Detail:
 def __init__(self, root):
 self.root = root
 self.root.title("STUDENT DETAILS")
 self.root.geometry("1550x800")
 self.university_roll=StringVar()
 self.university_roll2=StringVar()
 self.college_roll=StringVar()
 self.college_roll2=StringVar()
 self.stu_name=StringVar()
 self.stu_name2=StringVar()
 self.deptnum=StringVar()
 self.deptnum2=StringVar()
 self.gender=StringVar()
 self.student_city=StringVar()
 self.father_name=StringVar()
 self.mother_name=StringVar()
 self.semester=StringVar()
 self.classno=StringVar()
 self.mobile=StringVar()
 self.mailid=StringVar()
 self.birth=StringVar()
 self.batchno=StringVar()
 self.feeid=StringVar()
 self.hostelid=StringVar()
 img1 = Image.open(r"C:\Users\DELL\Downloads\\bunty.jpeg")
 img1 = img1.resize((1550,740), Image.ANTIALIAS)
 self.photoImg1 = ImageTk.PhotoImage(img1)
 lb = Label(self.root, image=self.photoImg1, bd=4, relief=RIDGE)
 lb.place(x=0, y=0, width=1550, height=740)
 lb_t = Label(self.root, text="Student Details", font=(
 "times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=R
IDGE)
 lb_t.place(x=0, y=0, width=1550, height=90)
 cust_btn=Button(self.root,text="ADMISTRATION DETAILS",command=self.fetch_
data_ad,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE
)
 cust_btn.place(x=10,y=150,width=320)
 cust_btn=Button(self.root,text="INSERT DATA",command=self.add_data_detail
_ad,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=350,y=150,width=200)
 cust_btn=Button(self.root,text="DELETE DATA",command=self.del_student_ad,
font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=590,y=150,width=200)
 cust_btn=Button(self.root,text="SEARCH DATA",command=self.search_student_
ad,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=820,y=150,width=200)
 cust_btn=Button(self.root,text="DEPARTMENTAL DETAILS",command=self.fetch_
data_dept,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RID
GE)
 cust_btn.place(x=10,y=250,width=320)
 cust_btn=Button(self.root,text="INSERT DATA",command=self.add_data_detail
_dept,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=350,y=250,width=200)
 cust_btn=Button(self.root,text="DELETE DATA",command=self.del_student_dep
t,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=590,y=250,width=200)
 cust_btn=Button(self.root,text="SEARCH DATA",command=self.search_student_
dept,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=820,y=250,width=200)
 def fetch_data_ad(self):
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 my_cursor.execute("select * from sta_detail")
 tree=ttk.Treeview(self.root,height="60")
 tree.place(x=1295,y=650)
 tree['show']='headings'
 tree["columns"]=("uni_roll","col_roll","name","batch","deptno","fee","hos
tel")
 tree.column("uni_roll",width=50,minwidth=50,anchor=CENTER)
 tree.column("col_roll",width=100,minwidth=100,anchor=CENTER)
 tree.column("name",width=50,minwidth=50,anchor=CENTER)
 tree.column("batch",width=150,minwidth=150,anchor=CENTER)
 tree.column("deptno",width=150,minwidth=150,anchor=CENTER)
 tree.column("fee",width=150,minwidth=150,anchor=CENTER)
 tree.column("hostel",width=150,minwidth=150,anchor=CENTER)
 tree.heading("uni_roll",text="UNI ROLL",anchor=CENTER)
 tree.heading("col_roll",text="COLLEGE ROLL",anchor=CENTER)
 tree.heading("name",text="NAME",anchor=CENTER)
 tree.heading("batch",text="BATCH",anchor=CENTER)
 tree.heading("deptno",text="DEPT NO",anchor=CENTER)
 tree.heading("fee",text="FEE ID",anchor=CENTER)
 tree.heading("hostel",text="HOSTEL ID",anchor=CENTER)
 count=0
 for i in my_cursor:
 tree.insert('',count,text=" ",values=(i[0],i[1] ,i[2], i[3],i[4],i[5]
,i[6]))
 count=count+1
 tree.pack(fill='x')
 
 def fetch_data_dept(self):
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 my_cursor.execute("select * from std_detail")
 tree=ttk.Treeview(self.root,height="60")
 tree.place(x=1295,y=650)
 tree['show']='headings'
 tree["columns"]=("uni_roll","col_roll","name","sex","sem","class","mob","
email","city","dob","father","mother","deptno")
 tree.column("uni_roll",width=10,minwidth=50,anchor=CENTER)
 tree.column("col_roll",width=10,minwidth=100,anchor=CENTER)
 tree.column("name",width=50,minwidth=50,anchor=CENTER)
 tree.column("sex",width=10,minwidth=50,anchor=CENTER)
 tree.column("sem",width=10,minwidth=50,anchor=CENTER)
 tree.column("class",width=50,minwidth=100,anchor=CENTER)
 tree.column("mob",width=20,minwidth=100,anchor=CENTER)
 tree.column("email",width=100,minwidth=100,anchor=CENTER)
 tree.column("city",width=50,minwidth=50,anchor=CENTER)
 tree.column("dob",width=150,minwidth=150,anchor=CENTER)
 tree.column("father",width=20,minwidth=100,anchor=CENTER)
 tree.column("mother",width=20,minwidth=100,anchor=CENTER)
 tree.column("deptno",width=10,minwidth=10,anchor=CENTER)
 tree.heading("uni_roll",text="UNI ROLL",anchor=CENTER)
 tree.heading("col_roll",text="COLLEGE ROLL",anchor=CENTER)
 tree.heading("name",text="NAME",anchor=CENTER)
 tree.heading("sex",text="SEX",anchor=CENTER)
 tree.heading("sem",text="SEM",anchor=CENTER)
 tree.heading("class",text="CLASS",anchor=CENTER)
 tree.heading("mob",text="MOBILE NO.",anchor=CENTER)
 tree.heading("email",text="EMAIL",anchor=CENTER)
 tree.heading("city",text="CITY",anchor=CENTER)
 tree.heading("dob",text="DOB",anchor=CENTER)
 tree.heading("father",text="FATHER NAME",anchor=CENTER)
 tree.heading("mother",text="MOTHER NAME",anchor=CENTER)
 tree.heading("deptno",text="DEPT NO",anchor=CENTER)
 
 count=0
 for i in my_cursor:
 tree.insert('',count,text=" ",values=(i[0],i[1] ,i[2], i[3],i[4],i[5]
,i[6],i[7],i[8] ,i[9], i[10],i[11],i[12]))
 count=count+1
 tree.pack(fill='x')
 def add_data_detail_dept(self):
 con = cx_Oracle.connect("system/seijal")
 self.lbl_stu_name=Label(self.root,text="Name: ",font=("arial",12,"bold"),
padx=2,pady=6)
 self.lbl_stu_name.place(x=10,y=340,width=50,height=20)
 entry_reff= ttk.Entry(self.root,textvariable=self.stu_name,font=("arial",
12,"bold"),width=29)
 entry_reff.place(x=10,y=365)
 
 self.lbl_stu_gender=Label(self.root,text="Sex: ",font=("arial",12,"bold")
,padx=2,pady=6)
 self.lbl_stu_gender.place(x=300,y=340,width=50,height=20)
 entry_reff= ttk.Entry(self.root,textvariable=self.gender,font=("arial",12
,"bold"),width=29)
 entry_reff.place(x=300,y=365)
 self.lbl_semes=Label(self.root,text="Semester: ",font=("arial",12,"bold")
,padx=2,pady=6)
 self. lbl_semes.place(x=590,y=340,width=100,height=15)
 entry_reff= ttk.Entry(self.root,textvariable=self.semester,font=("arial",
12,"bold"),width=29)
 entry_reff.place(x=590,y=365)
 self.lbl_phone=Label(self.root,text="Mobile number: ",font=("arial",12,"b
old"),padx=2,pady=6)
 self.lbl_phone.place(x=880,y=340,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.mobile,font=("arial",12
,"bold"),width=29)
 entry_reff.place(x=880,y=365)
 self.lbl_stu_mail=Label(self.root,text="Email ID: ",font=("arial",12,"bol
d"),padx=2,pady=6)
 self.lbl_stu_mail.place(x=10,y=440,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.mailid,font=("arial",12
,"bold"),width=29)
 entry_reff.place(x=10,y=465)
 self.lbl_stu_city=Label(self.root,text="City: ",font=("arial",12,"bold"),
padx=10,pady=20)
 self.lbl_stu_city.place(x=300,y=440,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.student_city,font=("ari
al",12,"bold"),width=29)
 entry_reff.place(x=300,y=465)
 self.lbl_stu_dob=Label(self.root,text="Date of Birth: ",font=("arial",12,
"bold"),padx=10,pady=20)
 self.lbl_stu_dob.place(x=590,y=440,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.birth,font=("arial",12,
"bold"),width=29)
 entry_reff.place(x=590,y=465)
 self.lbl_stu_father=Label(self.root,text="Father's Name: ",font=("arial",
12,"bold"),padx=10,pady=20)
 self.lbl_stu_father.place(x=880,y=440,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.father_name,font=("aria
l",12,"bold"),width=29)
 entry_reff.place(x=880,y=465)
 self.lbl_stu_mother=Label(self.root,text="Mother's Name: ",font=("arial",
12,"bold"),padx=10,pady=20)
 self.lbl_stu_mother.place(x=10,y=540,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.mother_name,font=("aria
l",12,"bold"),width=29)
 entry_reff.place(x=10,y=565)
 self.lbl_dept=Label(self.root,text="Dept No: ",font=("arial",12,"bold"),p
adx=6,pady=6)
 self.lbl_dept.place(x=300,y=540,height=15)
 entry_reff= ttk.Entry(self.root,textvariable=self.deptnum,font=("arial",1
2,"bold"),width=29)
 entry_reff.place(x=300,y=565)
 cust_btn=Button(self.root,text="SAVE DETAILS",command=self.data_added_dep
t,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=880,y=550,width=220)
 def data_added_dept(self):
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 try:
 s="insert into std_detail (name,sex,sem,mob,email,city,dob,father,mot
her,deptno) values(:1, :2, :3, :4 ,:5 ,:6 ,:7 , :8 , :9 , :10)"
 my_cursor.execute(s,(self.stu_name.get(),
 
 self.gender.get(),
 
 self.semester.get(),
 
 self.mobile.get(),
 
 self.mailid.get(),
 
 self.student_city.get(),
 
 self.birth.get(),
 
 self.father_name.get(),
 
 self.mother_name.get(),
 
 self.deptnum.get()
 
 )
 
 )
 messagebox.showinfo("message","SUCESSFULLY ADDED",parent=self.root)
 con.commit()
 con.close()
 except Exception as E:
 messagebox.showwarning(f"message","NOT ADDED:{str(E)}",parent=self.ro
ot)
 
 def add_data_detail_ad(self):
 con = cx_Oracle.connect("system/seijal")
 self.lbl_st_name=Label(self.root,text="Name: ",font=("arial",12,"bold"),p
adx=2,pady=6)
 self.lbl_st_name.place(x=10,y=340,width=50,height=20)
 entry_reff= ttk.Entry(self.root,textvariable=self.stu_name2,font=("arial"
,12,"bold"),width=29)
 entry_reff.place(x=10,y=365)
 
 self.lbl_batchnum=Label(self.root,text="Batch: ",font=("arial",12,"bold")
,padx=2,pady=6)
 self.lbl_batchnum.place(x=300,y=340,width=50,height=20)
 entry_reff= ttk.Entry(self.root,textvariable=self.batchno,font=("arial",1
2,"bold"),width=29)
 entry_reff.place(x=300,y=365)
 self.lbl_dept=Label(self.root,text="Dept No: ",font=("arial",12,"bold"),p
adx=6,pady=6)
 self.lbl_dept.place(x=590,y=340,height=15)
 entry_reff= ttk.Entry(self.root,textvariable=self.deptnum2,font=("arial",
12,"bold"),width=29)
 entry_reff.place(x=590,y=365)
 cust_btn=Button(self.root,text="SAVE DETAILS",command=self.data_added_ad,
font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=880,y=550,width=220)
 def data_added_ad(self):
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 try:
 s="insert into sta_detail (name,batch,deptno) values(:1, :2, :3)"
 my_cursor.execute(s,(self.stu_name2.get(),
 
 self.batchno.get(),
 
 self.deptnum2.get()
 
 )
 )
 messagebox.showinfo("message","SUCESSFULLY ADDED",parent=self.root)
 con.commit()
 con.close()
 except Exception as E:
 messagebox.showwarning(f"message","NOT ADDED:{str(E)}",parent=self.ro
ot)
 def del_student_dept(self):
 self.lbl=Label(self.root,text="ENTER STUDENT COLLEGE_ROLL: ",font=("arial
",12,"bold"),padx=2,pady=6)
 self.lbl.place(x=500,y=350,width=320,height=40)
 entry_reff1= ttk.Entry(self.root,textvariable=self.college_roll,font=("ar
ial",12,"bold"),width=20)
 entry_reff1.place(x=500,y=390)
 del_button=Button(self.root,text=" DELETE ",command=self.del_data_dept,fo
nt=("times new roman",14,"bold"),bg="black",fg="green",bd=4,relief=RIDGE)
 del_button.place(x=500,y=420,width=220)
 def del_data_dept(self):
 try:
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 s="delete from std_detail where col_roll = :1"
 a=my_cursor.execute(s,(self.college_roll.get(),))
 con.commit()
 con.close()
 messagebox.showinfo("message","SUCESSFULLY DELETED",parent=self.root)
 except Exception as E1:
 messagebox.showwarning("Warning",f"NOT DELETED :{str(E1)} ",parent=se
lf.root)
 def del_student_ad(self):
 self.lbl=Label(self.root,text="ENTER UNI_ROLL: ",font=("arial",12,"bold")
,padx=2,pady=6)
 self.lbl.place(x=500,y=350,width=220,height=30)
 entry_reff1= ttk.Entry(self.root,textvariable=self.university_roll,font=(
"arial",12,"bold"),width=20)
 entry_reff1.place(x=500,y=390)
 del_button=Button(self.root,text=" Delete it ",command=self.del_data_ad,f
ont=("times new roman",14,"bold"),bg="black",fg="green",bd=4,relief=RIDGE)
 del_button.place(x=500,y=420,width=220)
 def del_data_ad(self):
 try:
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 s="delete from sta_detail where uni_roll = :1"
 a=my_cursor.execute(s,(self.university_roll.get(),))
 con.commit()
 con.close()
 messagebox.showinfo("message","SUCESSFULLY DELETED",parent=self.root)
 except Exception as E1:
 messagebox.showwarning("Warning",f"NOT DELETED :{str(E1)} ",parent=se
lf.root)
 def search_student_ad(self):
 self.lbl=Label(self.root,text="ENTER UNIVERSITY ROLL NO: ",font=("arial",
12,"bold"),padx=2,pady=6)
 self.lbl.place(x=500,y=400,width=350,height=20)
 entry_reff1= ttk.Entry(self.root,textvariable=self.university_roll2,font=
("arial",12,"bold"),width=29)
 entry_reff1.place(x=510,y=430)
 del_button=Button(self.root,text=" SEARCH ",command=self.search_ad,font=(
"times new roman",14,"bold"),bg="black",fg="green",bd=4,relief=RIDGE)
 del_button.place(x=510,y=480,width=220)
 def search_ad(self):
 try:
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 s="select * from sta_detail where uni_roll= :1"
 statement=my_cursor.execute(s,(self.university_roll2.get(),))
 messagebox.showinfo("message","DATA FOUND",parent=self.root)
 tree=ttk.Treeview(self.root,height="60")
 tree.place(x=1500,y=750)
 tree['show']='headings'
 tree["columns"]=("uni_roll","col_roll","name","batch","deptno","fee",
"hostel")
 tree.column("uni_roll",width=50,minwidth=50,anchor=CENTER)
 tree.column("col_roll",width=100,minwidth=100,anchor=CENTER)
 tree.column("name",width=50,minwidth=50,anchor=CENTER)
 tree.column("batch",width=150,minwidth=150,anchor=CENTER)
 tree.column("deptno",width=150,minwidth=150,anchor=CENTER)
 tree.column("fee",width=150,minwidth=150,anchor=CENTER)
 tree.column("hostel",width=150,minwidth=150,anchor=CENTER)
 tree.heading("uni_roll",text="UNI ROLL",anchor=CENTER)
 tree.heading("col_roll",text="COLLEGE ROLL",anchor=CENTER)
 tree.heading("name",text="NAME",anchor=CENTER)
 tree.heading("batch",text="BATCH",anchor=CENTER)
 tree.heading("deptno",text="DEPT NO",anchor=CENTER)
 tree.heading("fee",text="FEE ID",anchor=CENTER)
 tree.heading("hostel",text="HOSTEL ID",anchor=CENTER)
 count=0
 for i in my_cursor:
 tree.insert('',count,text=" ",values=(i[0],i[1] ,i[2], i[3],i[4],
i[5],i[6]))
 count=count+1
 tree.pack(fill='x')
 con.commit()
 con.close()
 except Exception as E2:
 messagebox.showwarning("Waring",f" NOT FOUND :{str(E2)}",parent=self
.root)
 
 def search_student_dept(self):
 self.lbl=Label(self.root,text="ENTER COLLEGE ROLL NO: ",font=("arial",12,
"bold"),padx=2,pady=6)
 self.lbl.place(x=500,y=400,width=350,height=20)
 entry_reff1= ttk.Entry(self.root,textvariable=self.college_roll2,font=("a
rial",12,"bold"),width=29)
 entry_reff1.place(x=510,y=430)
 del_button=Button(self.root,text=" SEARCH ",command=self.search_dept,font
=("times new roman",14,"bold"),bg="black",fg="green",bd=4,relief=RIDGE)
 del_button.place(x=510,y=480,width=220)
 def search_dept(self):
 try:
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 s="select * from std_detail where col_roll= :1"
 statement=my_cursor.execute(s,(self.college_roll2.get(),))
 messagebox.showinfo("message","DATA FOUND",parent=self.root)
 tree=ttk.Treeview(self.root,height="60")
 tree.place(x=1500,y=750)
 tree['show']='headings'
 tree["columns"]=("uni_roll","col_roll","name","sex","sem","class","mo
b","email","city","dob","father","mother","deptno")
 tree.column("uni_roll",width=10,minwidth=50,anchor=CENTER)
 tree.column("col_roll",width=10,minwidth=100,anchor=CENTER)
 tree.column("name",width=50,minwidth=50,anchor=CENTER)
 tree.column("sex",width=10,minwidth=50,anchor=CENTER)
 tree.column("sem",width=10,minwidth=50,anchor=CENTER)
 tree.column("class",width=50,minwidth=100,anchor=CENTER)
 tree.column("mob",width=20,minwidth=100,anchor=CENTER)
 tree.column("email",width=100,minwidth=100,anchor=CENTER)
 tree.column("city",width=50,minwidth=50,anchor=CENTER)
 tree.column("dob",width=150,minwidth=150,anchor=CENTER)
 tree.column("father",width=20,minwidth=100,anchor=CENTER)
 tree.column("mother",width=20,minwidth=100,anchor=CENTER)
 tree.column("deptno",width=10,minwidth=10,anchor=CENTER)
 tree.heading("uni_roll",text="UNI ROLL",anchor=CENTER)
 tree.heading("col_roll",text="COLLEGE ROLL",anchor=CENTER)
 tree.heading("name",text="NAME",anchor=CENTER)
 tree.heading("sex",text="SEX",anchor=CENTER)
 tree.heading("sem",text="SEM",anchor=CENTER)
 tree.heading("class",text="CLASS",anchor=CENTER)
 tree.heading("mob",text="MOBILE NO.",anchor=CENTER)
 tree.heading("email",text="EMAIL",anchor=CENTER)
 tree.heading("city",text="CITY",anchor=CENTER)
 tree.heading("dob",text="DOB",anchor=CENTER)
 tree.heading("father",text="FATHER NAME",anchor=CENTER)
 tree.heading("mother",text="MOTHER NAME",anchor=CENTER)
 tree.heading("deptno",text="DEPT NO",anchor=CENTER)
 
 count=0
 for i in my_cursor:
 tree.insert('',count,text=" ",values=(i[0],i[1] ,i[2], i[3],i[4],
i[5],i[6],i[7],i[8] ,i[9], i[10],i[11],i[12]))
 count=count+1
 tree.pack(fill='x')
 con.commit()
 con.close()
 except Exception as E2:
 messagebox.showwarning("Waring",f" NOT FOUND :{str(E2)}",parent=self
.root)
 
if __name__ == '__main__':
 root = Tk()
 obj = Student_Detail(root)
 root.mainloop()
