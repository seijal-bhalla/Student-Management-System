from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cx_Oracle
from tkinter import messagebox
class Library_Entries:
 def __init__(self, root):
 self.libno=StringVar()
 self.libno2=StringVar()
 self.libno3=StringVar()
 self.collroll=StringVar()
 self.deptnum=StringVar()
 self.sname=StringVar()
 self.issueno=StringVar()
 self.bookname=StringVar()
 self.root = root
 self.root.title("LIBRARY DETAILS")
 self.root.geometry("1550x800")
 img1 = Image.open(r"C:\Users\DELL\Downloads\\bunty.jpeg")
 img1 = img1.resize((1550,740), Image.ANTIALIAS)
 self.photoImg1 = ImageTk.PhotoImage(img1)
 lb = Label(self.root, image=self.photoImg1, bd=4, relief=RIDGE)
 lb.place(x=0, y=0, width=1550, height=740)
 cust_btn=Button(self.root,text="1.) DISPLAY DATA",command=self.fetch_data
_lib,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=10,y=150,width=200)
 cust_btn=Button(self.root,text="2.) INSERT DATA",command=self.add_data_de
tail_lib,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDG
E)
 cust_btn.place(x=10,y=250,width=200)
 cust_btn=Button(self.root,text="3.) DELETE DATA",command=self.del_student
_lib,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=10,y=350,width=200)
 cust_btn=Button(self.root,text="4.) SEARCH DATA",command=self.search_stud
ent_lib,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE
)
 cust_btn.place(x=10,y=450,width=200)
 def fetch_data_lib(self):
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 my_cursor.execute("select * from lib_dept")
 tree=ttk.Treeview(self.root,height="60")
 tree.place(x=1295,y=650)
 tree['show']='headings'
 tree["columns"]=("lib_id","col_roll","name","deptno","issue_id","bname")
 tree.column("lib_id",width=50,minwidth=50,anchor=CENTER)
 tree.column("col_roll",width=100,minwidth=100,anchor=CENTER)
 tree.column("name",width=50,minwidth=50,anchor=CENTER)
 tree.column("deptno",width=150,minwidth=150,anchor=CENTER)
 tree.column("issue_id",width=150,minwidth=150,anchor=CENTER)
 tree.column("bname",width=150,minwidth=150,anchor=CENTER)
 tree.heading("lib_id",text="LIBRARY ID",anchor=CENTER)
 tree.heading("col_roll",text="COL_ROLL",anchor=CENTER)
 tree.heading("name",text="STUDENT NAME",anchor=CENTER)
 tree.heading("deptno",text="DEPT_NUM",anchor=CENTER)
 tree.heading("issue_id",text="ISSUE ID",anchor=CENTER)
 tree.heading("bname",text="BOOK NAME",anchor=CENTER)
 count=0
 for i in my_cursor:
 tree.insert('',count,text=" ",values=(i[0],i[1] ,i[2], i[3],i[4],i[5]
))
 count=count+1
 tree.pack(fill='x')
 def add_data_detail_lib(self):
 con = cx_Oracle.connect("system/seijal")
 self.lbl_stu_name=Label(self.root,text="LIBRARY ID: ",font=("arial",12,"b
old"),padx=2,pady=6)
 self.lbl_stu_name.place(x=10,y=340,width=100,height=20)
 entry_reff= ttk.Entry(self.root,textvariable=self.libno3,font=("arial",12
,"bold"),width=29)
 entry_reff.place(x=10,y=365)
 
 self.lbl_stu_gender=Label(self.root,text="COLLEGE ROLL NO: ",font=("arial
",12,"bold"),padx=2,pady=6)
 self.lbl_stu_gender.place(x=300,y=340,width=100,height=20)
 entry_reff= ttk.Entry(self.root,textvariable=self.collroll,font=("arial",
12,"bold"),width=29)
 entry_reff.place(x=300,y=365)
 self.lbl_semes=Label(self.root,text="NAME: ",font=("arial",12,"bold"),pad
x=2,pady=6)
 self. lbl_semes.place(x=590,y=340,width=100,height=15)
 entry_reff= ttk.Entry(self.root,textvariable=self.sname,font=("arial",12,
"bold"),width=29)
 entry_reff.place(x=590,y=365)
 self.lbl_phone=Label(self.root,text="DEPARTMENT: ",font=("arial",12,"bold
"),padx=2,pady=6)
 self.lbl_phone.place(x=880,y=340,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.deptnum,font=("arial",1
2,"bold"),width=29)
 entry_reff.place(x=880,y=365)
 self.lbl_stu_mail=Label(self.root,text="ISSUE ID: ",font=("arial",12,"bol
d"),padx=2,pady=6)
 self.lbl_stu_mail.place(x=10,y=440,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.issueno,font=("arial",1
2,"bold"),width=29)
 entry_reff.place(x=10,y=465)
 self.lbl_stu_city=Label(self.root,text="BOOK NAME: ",font=("arial",12,"bo
ld"),padx=10,pady=20)
 self.lbl_stu_city.place(x=300,y=440,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.bookname,font=("arial",
12,"bold"),width=29)
 entry_reff.place(x=300,y=465)
 cust_btn=Button(self.root,text="SAVE DETAILS",command=self.data_added_lib
,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=880,y=550,width=220)
 def data_added_lib(self):
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 try:
 s="insert into issue_detail (lib_id,col_roll,name,deptno,issue_id,bna
me) values(:1, :2, :3, :4 ,:5 ,:6 )"
 my_cursor.execute(s,(self.libno3.get(),
 
 self.collroll.get(),
 
 self.sname.get(),
 
 self.deptnum.get(),
 
 self.issueno.get(),
 
 self.bookname.get()
 
 )
 
 )
 messagebox.showinfo("message","SUCESSFULLY ADDED",parent=self.root)
 con.commit()
 con.close()
 except Exception as E:
 messagebox.showwarning(f"message","NOT ADDED:{str(E)}",parent=self.ro
ot)
 def del_student_lib(self):
 self.lbl=Label(self.root,text="ENTER LIBRARY ID: ",font=("arial",12,"bold
"),padx=2,pady=6)
 self.lbl.place(x=500,y=350,width=220,height=30)
 entry_reff1= ttk.Entry(self.root,textvariable=self.libno,font=("arial",12
,"bold"),width=20)
 entry_reff1.place(x=500,y=390)
 del_button=Button(self.root,text=" Delete it ",command=self.del_data_lib,
font=("times new roman",14,"bold"),bg="black",fg="green",bd=4,relief=RIDGE)
 del_button.place(x=500,y=420,width=220)
 def del_data_lib(self):
 try:
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 s="delete from lib_dept where lib_id = :1"
 a=my_cursor.execute(s,(self.libno.get(),))
 con.commit()
 con.close()
 messagebox.showinfo("message","SUCESSFULLY DELETED",parent=self.root)
 except Exception as E1:
 messagebox.showwarning("Warning",f"NOT DELETED :{str(E1)} ",parent=se
lf.root)
 def search_student_lib(self):
 self.lbl=Label(self.root,text="ENTER LIBRARY ID: ",font=("arial",12,"bold
"),padx=2,pady=6)
 self.lbl.place(x=500,y=400,width=350,height=20)
 entry_reff1= ttk.Entry(self.root,textvariable=self.libno2,font=("arial",1
2,"bold"),width=29)
 entry_reff1.place(x=510,y=430)
 del_button=Button(self.root,text=" SEARCH ",command=self.search_lib,font=
("times new roman",14,"bold"),bg="black",fg="green",bd=4,relief=RIDGE)
 del_button.place(x=510,y=480,width=220)
 def search_lib(self):
 try:
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 s="select * from lib_dept where lib_id= :1"
 statement=my_cursor.execute(s,(self.libno2.get(),))
 messagebox.showinfo("message","DATA FOUND",parent=self.root)
 tree=ttk.Treeview(self.root,height="60")
 tree.place(x=1500,y=750)
 tree['show']='headings'
 tree["columns"]=("lib_id","col_roll","name","deptno","issue_id","bnam
e")
 tree.column("lib_id",width=50,minwidth=50,anchor=CENTER)
 tree.column("col_roll",width=100,minwidth=100,anchor=CENTER)
 tree.column("name",width=50,minwidth=50,anchor=CENTER)
 tree.column("deptno",width=150,minwidth=150,anchor=CENTER)
 tree.column("issue_id",width=150,minwidth=150,anchor=CENTER)
 tree.column("bname",width=150,minwidth=150,anchor=CENTER)
 tree.heading("lib_id",text="LIBRARY ID",anchor=CENTER)
 tree.heading("col_roll",text="COL_ROLL",anchor=CENTER)
 tree.heading("name",text="STUDNET NAME",anchor=CENTER)
 tree.heading("deptno",text="DEPT_NUM",anchor=CENTER)
 tree.heading("issue_id",text="ISSUE ID",anchor=CENTER)
 tree.heading("bname",text="BOOK NAME",anchor=CENTER)
 count=0
 for i in my_cursor:
 tree.insert('',count,text=" ",values=(i[0],i[1] ,i[2], i[3],i[4],
i[5]))
 count=count+1
 tree.pack(fill='x')
 con.commit()
 con.close()
 except Exception as E2:
 messagebox.showwarning("Waring",f" NOT FOUND :{str(E2)}",parent=self
.root)
if __name__ == '__main__':
 root = Tk()
 obj = Library_Entries(root)
 root.mainloop()
