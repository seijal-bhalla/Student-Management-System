from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cx_Oracle
from tkinter import messagebox
class Issue_details:
 def __init__(self, root):
 self.root = root
 self.root.title("ISSUE DETAILS")
 self.root.geometry("1550x800")
 self.issueno=StringVar()
 self.issueno2=StringVar()
 self.issueno3=StringVar()
 self.bnum=StringVar()
 self.bookname=StringVar()
 self.authorname=StringVar()
 self.status=StringVar()
 self.idate=StringVar()
 self.rdate=StringVar()
 self.bleft=StringVar()
 img1 = Image.open(r"C:\Users\DELL\Downloads\\bunty.jpeg")
 img1 = img1.resize((1550,740), Image.ANTIALIAS)
 self.photoImg1 = ImageTk.PhotoImage(img1)
 lb = Label(self.root, image=self.photoImg1, bd=4, relief=RIDGE)
 lb.place(x=0, y=0, width=1550, height=740)
 cust_btn=Button(self.root,text="1.) DISPLAY DATA",command=self.fetch_data
_issue,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=10,y=150,width=200)
 cust_btn=Button(self.root,text="2.) INSERT DATA",command=self.add_data_de
tail_issue,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RI
DGE)
 cust_btn.place(x=10,y=250,width=200)
 cust_btn=Button(self.root,text="3.) DELETE DATA",command=self.del_student
_issue,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=500,y=150,width=200)
 cust_btn=Button(self.root,text="4.) SEARCH DATA",command=self.search_stud
ent_issue,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RID
GE)
 cust_btn.place(x=500,y=250,width=200)
 def fetch_data_issue(self):
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 my_cursor.execute("select * from issue_detail")
 tree=ttk.Treeview(self.root,height="60")
 tree.place(x=1295,y=650)
 tree['show']='headings'
 tree["columns"]=("issue_id","bno","bname","author","issued","issue_date",
"return_date","left")
 tree.column("issue_id",width=50,minwidth=50,anchor=CENTER)
 tree.column("bno",width=100,minwidth=100,anchor=CENTER)
 tree.column("bname",width=50,minwidth=50,anchor=CENTER)
 tree.column("author",width=150,minwidth=150,anchor=CENTER)
 tree.column("issued",width=150,minwidth=150,anchor=CENTER)
 tree.column("issue_date",width=150,minwidth=150,anchor=CENTER)
 tree.column("return_date",width=150,minwidth=150,anchor=CENTER)
 tree.column("left",width=150,minwidth=150,anchor=CENTER)
 tree.heading("issue_date",text="ISSUE ID",anchor=CENTER)
 tree.heading("bno",text="BOOK_NUM",anchor=CENTER)
 tree.heading("bname",text="BOOK NAME",anchor=CENTER)
 tree.heading("author",text="AUTHOR",anchor=CENTER)
 tree.heading("issued",text="STATUS",anchor=CENTER)
 tree.heading("issue_date",text="ISSUE DATE",anchor=CENTER)
 tree.heading("return_date",text="RETURN DATE",anchor=CENTER)
 tree.heading("left",text="LEFT",anchor=CENTER)
 count=0
 for i in my_cursor:
 tree.insert('',count,text=" ",values=(i[0],i[1] ,i[2], i[3],i[4],i[5]
,i[6],i[7]))
 count=count+1
 tree.pack(fill='x')
 def add_data_detail_issue(self):
 con = cx_Oracle.connect("system/seijal")
 self.lbl_stu_name=Label(self.root,text="Issue ID: ",font=("arial",12,"bol
d"),padx=2,pady=6)
 self.lbl_stu_name.place(x=10,y=340,width=100,height=20)
 entry_reff= ttk.Entry(self.root,textvariable=self.issueno,font=("arial",1
2,"bold"),width=29)
 entry_reff.place(x=10,y=365)
 
 self.lbl_stu_gender=Label(self.root,text="Book_num: ",font=("arial",12,"b
old"),padx=2,pady=6)
 self.lbl_stu_gender.place(x=300,y=340,width=100,height=20)
 entry_reff= ttk.Entry(self.root,textvariable=self.bnum,font=("arial",12,"
bold"),width=29)
 entry_reff.place(x=300,y=365)
 self.lbl_semes=Label(self.root,text="Book Name: ",font=("arial",12,"bold"
),padx=2,pady=6)
 self. lbl_semes.place(x=590,y=340,width=100,height=15)
 entry_reff= ttk.Entry(self.root,textvariable=self.bookname,font=("arial",
12,"bold"),width=29)
 entry_reff.place(x=590,y=365)
 self.lbl_phone=Label(self.root,text="Author: ",font=("arial",12,"bold"),p
adx=2,pady=6)
 self.lbl_phone.place(x=880,y=340,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.authorname,font=("arial
",12,"bold"),width=29)
 entry_reff.place(x=880,y=365)
 self.lbl_stu_mail=Label(self.root,text="Issue_Status: ",font=("arial",12,
"bold"),padx=2,pady=6)
 self.lbl_stu_mail.place(x=10,y=440,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.status,font=("arial",12
,"bold"),width=29)
 entry_reff.place(x=10,y=465)
 self.lbl_stu_city=Label(self.root,text="Issue Date: ",font=("arial",12,"b
old"),padx=10,pady=20)
 self.lbl_stu_city.place(x=300,y=440,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.idate,font=("arial",12,
"bold"),width=29)
 entry_reff.place(x=300,y=465)
 self.lbl_stu_dob=Label(self.root,text="Return Date: ",font=("arial",12,"b
old"),padx=10,pady=20)
 self.lbl_stu_dob.place(x=590,y=440,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.rdate,font=("arial",12,
"bold"),width=29)
 entry_reff.place(x=590,y=465)
 self.lbl_stu_father=Label(self.root,text="Left: ",font=("arial",12,"bold"
),padx=10,pady=20)
 self.lbl_stu_father.place(x=880,y=440,height=16)
 entry_reff= ttk.Entry(self.root,textvariable=self.bleft,font=("arial",12,
"bold"),width=29)
 entry_reff.place(x=880,y=465)
 cust_btn=Button(self.root,text="SAVE DETAILS",command=self.data_added_iss
ue,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=880,y=550,width=220)
 def data_added_issue(self):
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 try:
 s="insert into issue_detail (issue_id,bno,bname,author,issued,issue_d
ate,return_date,left) values(:1, :2, :3, :4 ,:5 ,:6 ,:7 , :8 )"
 my_cursor.execute(s,(self.issueno.get(),
 
 self.bnum.get(),
 
 self.bookname.get(),
 
 self.authorname.get(),
 
 self.status.get(),
 
 self.idate.get(),
 
 self.rdate.get(),
 
 self.bleft.get()
 
 )
 )
 messagebox.showinfo("message","SUCESSFULLY ADDED",parent=self.root)
 con.commit()
 con.close()
 except Exception as E:
 messagebox.showwarning(f"message","NOT ADDED:{str(E)}",parent=self.ro
ot)
 def del_student_issue(self):
 self.lbl=Label(self.root,text="ENTER ISSUE ID: ",font=("arial",12,"bold")
,padx=2,pady=6)
 self.lbl.place(x=500,y=350,width=220,height=30)
 entry_reff1= ttk.Entry(self.root,textvariable=self.issueno2,font=("arial"
,12,"bold"),width=20)
 entry_reff1.place(x=500,y=390)
 del_button=Button(self.root,text=" Delete it ",command=self.del_data_issu
e,font=("times new roman",14,"bold"),bg="black",fg="green",bd=4,relief=RIDGE)
 del_button.place(x=500,y=420,width=220)
 def del_data_issue(self):
 try:
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 s="delete from issue_detail where issue_id= :1"
 a=my_cursor.execute(s,(self.issueno2.get(),))
 con.commit()
 con.close()
 messagebox.showinfo("message","SUCESSFULLY DELETED",parent=self.root)
 except Exception as E1:
 messagebox.showwarning("Warning",f"NOT DELETED :{str(E1)} ",parent=se
lf.root)
 def search_student_issue(self):
 self.lbl=Label(self.root,text="ENTER ISSUE ID: ",font=("arial",12,"bold")
,padx=2,pady=6)
 self.lbl.place(x=500,y=400,width=350,height=20)
 entry_reff1= ttk.Entry(self.root,textvariable=self.issueno3,font=("arial"
,12,"bold"),width=29)
 entry_reff1.place(x=510,y=430)
 del_button=Button(self.root,text=" SEARCH ",command=self.search_issue,fon
t=("times new roman",14,"bold"),bg="black",fg="green",bd=4,relief=RIDGE)
 del_button.place(x=510,y=480,width=220)
 def search_issue(self):
 try:
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 s="select * from issue_detail where issue_id= :1"
 statement=my_cursor.execute(s,(self.issueno3.get(),))
 messagebox.showinfo("message","DATA FOUND",parent=self.root)
 tree=ttk.Treeview(self.root,height="60")
 tree.place(x=1500,y=750)
 tree['show']='headings'
 tree["columns"]=("issue_id","bno","bname","author","issued","issue_da
te","return_date","left")
 tree.column("issue_id",width=50,minwidth=50,anchor=CENTER)
 tree.column("bno",width=100,minwidth=100,anchor=CENTER)
 tree.column("bname",width=50,minwidth=50,anchor=CENTER)
 tree.column("author",width=150,minwidth=150,anchor=CENTER)
 tree.column("issued",width=150,minwidth=150,anchor=CENTER)
 tree.column("issue_date",width=150,minwidth=150,anchor=CENTER)
 tree.column("return_date",width=150,minwidth=150,anchor=CENTER)
 tree.column("left",width=150,minwidth=150,anchor=CENTER)
 tree.heading("issue_date",text="ISSUE DATE",anchor=CENTER)
 tree.heading("bno",text="BOOK_NUM",anchor=CENTER)
 tree.heading("bname",text="BOOK NAME",anchor=CENTER)
 tree.heading("author",text="AUTHOR",anchor=CENTER)
 tree.heading("issued",text="STATUS",anchor=CENTER)
 tree.heading("issue_date",text="ISSUE DATE",anchor=CENTER)
 tree.heading("return_date",text="RETURN DATE",anchor=CENTER)
 tree.heading("left",text="LEFT",anchor=CENTER)
 count=0
 for i in my_cursor:
 tree.insert('',count,text=" ",values=(i[0],i[1] ,i[2], i[3],i[4],
i[5],i[6],i[7]))
 count=count+1
 tree.pack(fill='x')
 con.commit()
 con.close()
 except Exception as E2:
 messagebox.showwarning("Waring",f" NOT FOUND :{str(E2)}",parent=self
.root)
if __name__ == '__main__':
 root = Tk()
 obj = Issue_details(root)
 root.mainloop()
