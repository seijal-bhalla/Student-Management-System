from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cx_Oracle
from tkinter import messagebox
class Dept_Detail:
 def __init__(self, root):
 self.root = root
 self.root.title("DEPARTMENT DETAILS")
 self.root.geometry("1550x800")
 img1 = Image.open(r"C:\Users\DELL\Downloads\\bunty.jpeg")
 img1 = img1.resize((1550,740), Image.ANTIALIAS)
 self.photoImg1 = ImageTk.PhotoImage(img1)
 lb = Label(self.root, image=self.photoImg1, bd=4, relief=RIDGE)
 lb.place(x=0, y=0, width=1550, height=740)
 lb_t = Label(self.root, text="Department Details", font=(
 "times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=R
IDGE)
 lb_t.place(x=0, y=0, width=1550, height=90)
 cust_btn=Button(self.root,text="DEPARTMENT DETAILS",command=self.fetch_da
ta_dept,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE
)
 cust_btn.place(x=10,y=150,width=320)
 def fetch_data_dept(self):
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 my_cursor.execute("select * from sdept")
 tree=ttk.Treeview(self.root,height="60")
 tree.place(x=1295,y=650)
 tree['show']='headings'
 tree["columns"]=("deptno","dname","loc","hod")
 tree.column("deptno",width=50,minwidth=50,anchor=CENTER)
 tree.column("dname",width=100,minwidth=100,anchor=CENTER)
 tree.column("loc",width=50,minwidth=50,anchor=CENTER)
 tree.column("hod",width=150,minwidth=150,anchor=CENTER) 
 tree.heading("deptno",text="DEPT_NUM",anchor=CENTER)
 tree.heading("dname",text="DEPT_NAME",anchor=CENTER)
 tree.heading("loc",text="LOCATION",anchor=CENTER)
 tree.heading("hod",text="HOD",anchor=CENTER)
 count=0
 for i in my_cursor:
 tree.insert('',count,text=" ",values=(i[0],i[1] ,i[2], i[3]))
 count=count+1
 tree.pack(fill='x')
 
if __name__ == '__main__':
 root = Tk()
 obj = Dept_Detail(root)
 root.mainloop()
