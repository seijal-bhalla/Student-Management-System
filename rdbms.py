from tkinter import *
from student import Student_Detail
from dept import Dept_Detail
from library import Library_Detail
from fee import fee_details
from PIL import Image,ImageTk
class STUDENT_MANAGMENT:
 def __init__ (self,root):
 self.root=root
 self.root.title("STUDENT MANAGEMENT SYSTEM")
 self.root.geometry("1550x800")
 img1=Image.open(r"C:\\Users\\DELL\\Downloads\\bunty.jpeg")
 img1=img1.resize((1550,740),Image.ANTIALIAS)
 self.photoImg1=ImageTk.PhotoImage(img1)
 lb=Label(self.root,image=self.photoImg1,bd=4,relief=RIDGE)
 lb.place(x=0,y=0,width=1550,height=740)
 
 lb_t= Label(self.root,text="STUDENT MANAGEMENT SYSTEM",font=("times new r
oman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 lb_t.place(x=0,y=10,width=1550,height=50)
 lb_menu= Label(self.root,text="MENU",font=("times new roman",20,"bold"),b
g="black",fg="gold",bd=4,relief=RIDGE)
 lb_menu.place(x=0,y=100,width=320)
 
 cust_btn=Button(text="STUDENT DETAILS",command=self.student,font=("times
new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=0,y=150,width=320)
 cust_btn=Button(text="DEPARTMENT DETAILS",command=self.dept,font=("times
new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=0,y=200,width=320)
 cust_btn=Button(text="LIBRARY DETAILS",command=self.library,font=("times
new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=0,y=250,width=320)
 
 cust_btn=Button(text="FEE DEPARTMENT DETAILS",command=self.fees,font=("ti
mes new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=0,y=300,width=320)
 
 def student(self):
 self.new_window=Toplevel(self.root)
 self.app=Student_Detail(self.new_window)
 def dept(self):
 self.new_window=Toplevel(self.root)
 self.app=Dept_Detail(self.new_window)
 def library(self):
 self.new_window=Toplevel(self.root)
 self.app=Library_Detail(self.new_window)
 def fees(self):
 self.new_window=Toplevel(self.root)
 self.app=fee_details(self.new_window)
if __name__ == "__main__":
 root=Tk()
 obj=STUDENT_MANAGMENT(root)
 root.mainloop(
