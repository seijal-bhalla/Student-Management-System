from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cx_Oracle
from tkinter import messagebox
class fee_details:
 def __init__(self, root):
 self.root = root
 self.root.title("FEE DETAILS")
 self.root.geometry("1550x800")
 self.feeno=StringVar()
 self.feeno2=StringVar()
 self.feeno3=StringVar()
 self.uniroll=StringVar()
 self.colroll=StringVar()
 self.sname=StringVar()
 self.deptnum=StringVar()
 self.tfees=StringVar()
 self.tstatus=StringVar()
 self.hostelno=StringVar()
 self.hfees=StringVar()
 self.hstatus=StringVar()
 img1 = Image.open(r"C:\Users\DELL\Downloads\\bunty.jpeg")
 img1 = img1.resize((1550,740), Image.ANTIALIAS)
 self.photoImg1 = ImageTk.PhotoImage(img1)
 lb = Label(self.root, image=self.photoImg1, bd=4, relief=RIDGE)
 lb.place(x=0, y=0, width=1550, height=740)
 cust_btn=Button(self.root,text="1.) DISPLAY DATA",command=self.fetch_data
_fee,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=10,y=150,width=200)
 cust_btn=Button(self.root,text="2.) INSERT DATA",command=self.add_data_de
tail_fee,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDG
E)
 cust_btn.place(x=10,y=250,width=200)
 cust_btn=Button(self.root,text="3.) DELETE DATA",command=self.del_student
_fee,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=500,y=150,width=200)
 cust_btn=Button(self.root,text="4.) SEARCH DATA",command=self.search_stud
ent_fee,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE
)
 cust_btn.place(x=500,y=250,width=200)
 def fetch_data_fee(self):
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 my_cursor.execute("select * from fee_dept")
 tree=ttk.Treeview(self.root,height="60")
 tree.place(x=1295,y=650)
 tree['show']='headings'
 tree["columns"]=("fee","uni_roll","col_roll","name","deptno","t_fees","t_
status","hostel","h_fees","h_status")
 tree.column("fee",width=50,minwidth=50,anchor=CENTER)
 tree.column("uni_roll",width=100,minwidth=100,anchor=CENTER)
 tree.column("col_roll",width=50,minwidth=50,anchor=CENTER)
 tree.column("name",width=150,minwidth=150,anchor=CENTER)
 tree.column("deptno",width=150,minwidth=150,anchor=CENTER)
 tree.column("t_fees",width=150,minwidth=150,anchor=CENTER)
 tree.column("t_status",width=150,minwidth=150,anchor=CENTER)
 tree.column("hostel",width=150,minwidth=150,anchor=CENTER)
 tree.column("h_fees",width=150,minwidth=150,anchor=CENTER)
 tree.column("h_status",width=150,minwidth=150,anchor=CENTER)
 tree.heading("fee",text="FEE ID",anchor=CENTER)
 tree.heading("uni_roll",text="UNI_ROLL",anchor=CENTER)
 tree.heading("col_roll",text="COL_ROLL",anchor=CENTER)
 tree.heading("name",text="STUDENT NAME",anchor=CENTER)
 tree.heading("deptno",text="DEPT_NUM",anchor=CENTER)
 tree.heading("t_fees",text="TUITION FEE",anchor=CENTER)
 tree.heading("t_status",text="T_FEE STATUS",anchor=CENTER)
 tree.heading("hostel",text="HOSTEL ID",anchor=CENTER)
 tree.heading("h_fees",text="HOSTEL FEE",anchor=CENTER)
 tree.heading("h_status",text="H_FEE STATUS",anchor=CENTER)
 count=0
 for i in my_cursor:
 tree.insert('',count,text=" ",values=(i[0],i[1] ,i[2], i[3],i[4],i[5]
,i[6],i[7],i[8],i[9]))
 count=count+1
 tree.pack(fill='x')
 def add_data_detail_fee(self):
 con = cx_Oracle.connect("system/seijal")
 self.lbl_stu_name=Label(self.root,text="Fee Reciept ID: ",font=("arial",1
2,"bold"),padx=2,pady=6)
 self.lbl_stu_name.place(x=10,y=340,width=200,height=20)
 entry_reff= ttk.Entry(self.root,textvariable=self.feeno,font=("arial",12,
"bold"),width=29)
 entry_reff.place(x=10,y=365)
 
 self.lbl_stu_gender=Label(self.root,text="Uni_roll no: ",font=("arial",12
,"bold"),padx=2,pady=6)
 self.lbl_stu_gender.place(x=300,y=340,width=100,height=20)
 entry_reff= ttk.Entry(self.root,textvariable=self.uniroll,font=("arial",1
2,"bold"),width=29)
 entry_reff.place(x=300,y=365)
 self.lbl_semes=Label(self.root,text="Col_roll no: ",font=("arial",12,"bol
d"),padx=2,pady=6)
 self. lbl_semes.place(x=590,y=340,width=100,height=15)
 entry_reff= ttk.Entry(self.root,textvariable=self.colroll,font=("arial",1
2,"bold"),width=29)
 entry_reff.place(x=590,y=365)
 self.lbl_phone=Label(self.root,text="Name: ",font=("arial",12,"bold"),pad
x=2,pady=6)
 self.lbl_phone.place(x=880,y=340,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.sname,font=("arial",12,
"bold"),width=29)
 entry_reff.place(x=880,y=365)
 self.lbl_stu_father=Label(self.root,text="Dept_num: ",font=("arial",12,"b
old"),padx=10,pady=20)
 self.lbl_stu_father.place(x=10,y=440,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.deptnum,font=("arial",1
2,"bold"),width=29)
 entry_reff.place(x=10,y=465)
 self.lbl_stu_mail=Label(self.root,text="Tuition Fee: ",font=("arial",12,"
bold"),padx=2,pady=6)
 self.lbl_stu_mail.place(x=300,y=440,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.tfees,font=("arial",12,
"bold"),width=29)
 entry_reff.place(x=300,y=465)
 self.lbl_stu_city=Label(self.root,text="T_fee Status: ",font=("arial",12,
"bold"),padx=10,pady=20)
 self.lbl_stu_city.place(x=590,y=440,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.tstatus,font=("arial",1
2,"bold"),width=29)
 entry_reff.place(x=590,y=465)
 self.lbl_stu_dob=Label(self.root,text="Hostel ID: ",font=("arial",12,"bol
d"),padx=10,pady=20)
 self.lbl_stu_dob.place(x=880,y=440,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.hostelno,font=("arial",
12,"bold"),width=29)
 entry_reff.place(x=800,y=465)
 self.lbl_stu_father=Label(self.root,text="Hostel Fee: ",font=("arial",12,
"bold"),padx=10,pady=20)
 self.lbl_stu_father.place(x=10,y=540,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.hfees,font=("arial",12,
"bold"),width=29)
 entry_reff.place(x=10,y=565)
 self.lbl_stu_father=Label(self.root,text="H_Fee Status: ",font=("arial",1
2,"bold"),padx=10,pady=20)
 self.lbl_stu_father.place(x=300,y=540,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.hstatus,font=("arial",1
2,"bold"),width=29)
 entry_reff.place(x=300,y=565)
 cust_btn=Button(self.root,text="SAVE DETAILS",command=self.data_added_fee
,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=880,y=650,width=220)
 def data_added_fee(self):
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 try:
 s="insert into lib_dept (fee,uni_roll,col_roll,name,deptno,t_fees,t_s
tatus,hostel,h_fees,h_status) values(:1, :2, :3, :4 ,:5 ,:6 ,:7 , :8 , :9, :10 )"
 my_cursor.execute(s,(self.feeno.get(),
 
 self.uniroll.get(),
 
 self.colroll.get(),
 
 self.sname.get(),
 
 self.deptnum.get(),
 
 self.tfees.get(),
 
 self.tstatus.get(),
 
 self.hostelno.get(),
 
 self.hfees.get(),
 
 self.hstatus.get()
 
 )
 )
 messagebox.showinfo("message","SUCESSFULLY ADDED",parent=self.root)
 con.commit()
 con.close()
 except Exception as E:
 messagebox.showwarning(f"message","NOT ADDED:{str(E)}",parent=self.ro
ot)
 def del_student_fee(self):
 self.lbl=Label(self.root,text="ENTER FEE ID: ",font=("arial",12,"bold"),p
adx=2,pady=6)
 self.lbl.place(x=500,y=350,width=220,height=30)
 entry_reff1= ttk.Entry(self.root,textvariable=self.feeno2,font=("arial",1
2,"bold"),width=20)
 entry_reff1.place(x=500,y=390)
 del_button=Button(self.root,text=" Delete it ",command=self.del_data_fee,
font=("times new roman",14,"bold"),bg="black",fg="green",bd=4,relief=RIDGE)
 del_button.place(x=500,y=420,width=220)
 def del_data_fee(self):
 try:
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 s="delete from fee_dept where fee= :1"
 a=my_cursor.execute(s,(self.feeno2.get(),))
 con.commit()
 con.close()
 messagebox.showinfo("message","SUCESSFULLY DELETED",parent=self.root)
 except Exception as E1:
 messagebox.showwarning("Warning",f"NOT DELETED :{str(E1)} ",parent=se
lf.root)
 def search_student_fee(self):
 self.lbl=Label(self.root,text="ENTER FEE ID: ",font=("arial",12,"bold"),p
adx=2,pady=6)
 self.lbl.place(x=500,y=400,width=350,height=20)
 entry_reff1= ttk.Entry(self.root,textvariable=self.feeno3,font=("arial",1
2,"bold"),width=29)
 entry_reff1.place(x=510,y=430)
 del_button=Button(self.root,text=" SEARCH ",command=self.search_fee,font=
("times new roman",14,"bold"),bg="black",fg="green",bd=4,relief=RIDGE)
 del_button.place(x=510,y=480,width=220)
 def search_fee(self):
 try:
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 s="select * from fee_dept where fee= :1"
 statement=my_cursor.execute(s,(self.feeno3.get(),))
 messagebox.showinfo("message","DATA FOUND",parent=self.root)
 tree=ttk.Treeview(self.root,height="60")
 tree.place(x=1500,y=750)
 tree['show']='headings'
 tree["columns"]=("fee","uni_roll","col_roll","name","deptno","t_fees"
,"t_status","hostel","h_fees","h_status")
 tree.column("fee",width=50,minwidth=50,anchor=CENTER)
 tree.column("uni_roll",width=100,minwidth=100,anchor=CENTER)
 tree.column("col_roll",width=50,minwidth=50,anchor=CENTER)
 tree.column("name",width=150,minwidth=150,anchor=CENTER)
 tree.column("deptno",width=150,minwidth=150,anchor=CENTER)
 tree.column("t_fees",width=150,minwidth=150,anchor=CENTER)
 tree.column("t_status",width=150,minwidth=150,anchor=CENTER)
 tree.column("hostel",width=150,minwidth=150,anchor=CENTER)
 tree.column("h_fees",width=150,minwidth=150,anchor=CENTER)
 tree.column("h_status",width=150,minwidth=150,anchor=CENTER)
 tree.heading("fee",text="FEE ID",anchor=CENTER)
 tree.heading("uni_roll",text="UNI_ROLL",anchor=CENTER)
 tree.heading("col_roll",text="COL_ROLL",anchor=CENTER)
 tree.heading("name",text="STUDENT NAME",anchor=CENTER)
 tree.heading("deptno",text="DEPT_NUM",anchor=CENTER)
 tree.heading("t_fees",text="TUITION FEE",anchor=CENTER)
 tree.heading("t_status",text="T_FEE STTAUS",anchor=CENTER)
 tree.heading("hostel",text="HOSTEL ID",anchor=CENTER)
 tree.heading("h_fees",text="HOSTEL FEE",anchor=CENTER)
 tree.heading("h_status",text="H_FEE STATUS",anchor=CENTER)
 count=0
 for i in my_cursor:
 tree.insert('',count,text=" ",values=(i[0],i[1] ,i[2], i[3],i[4],
i[5],i[6],i[7],i[8],i[9]))
 count=count+1
 tree.pack(fill='x')
 con.commit()
 con.close()
 except Exception as E2:
 messagebox.showwarning("Waring",f" NOT FOUND :{str(E2)}",parent=self
.root)
if __name__ == '__main__':
 root = Tk()
 obj = fee_details(root)
 root.mainloop()
