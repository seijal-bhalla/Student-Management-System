from sublibrary3 import Book_details
from sublibrary2 import Issue_details
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cx_Oracle
from tkinter import messagebox
from sublibrary import Library_Entries
from sublibrary2 import Issue_details
from sublibrary3 import Book_details
class Library_Detail:
 def __init__(self, root):
 self.root = root
 self.root.title("LIBRARY DETAILS")
 self.root.geometry("1550x800")
 img1 = Image.open(r"C:\Users\DELL\Downloads\\bunty.jpeg")
 img1 = img1.resize((1550,740), Image.ANTIALIAS)
 self.photoImg1 = ImageTk.PhotoImage(img1)
 lb = Label(self.root, image=self.photoImg1, bd=4, relief=RIDGE)
 lb.place(x=0, y=0, width=1550, height=740)
 lb_t = Label(self.root, text="Library Details", font=(
 "times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=R
IDGE)
 lb_t.place(x=0, y=0, width=1550, height=90)
 cust_btn=Button(self.root,text="LIBRARY ENTRIES",command=self.library,fon
t=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=10,y=150,width=320)
 cust_btn=Button(self.root,text="ISSUED BOOKS",command=self.issue,font=("t
imes new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=10,y=250,width=320)
 cust_btn=Button(self.root,text="BOOK DETAILS",command=self.book,font=("ti
mes new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=10,y=350,width=320)
 def library(self):
 self.new_window=Toplevel(self.root)
 self.app=Library_Entries(self.new_window)
 def issue(self):
 self.new_window=Toplevel(self.root)
 self.app=Issue_details(self.new_window)
 def book(self):
 self.new_window=Toplevel(self.root)
 self.app=Book_details(self.new_window)
if __name__ == '__main__':
 root = Tk()
 obj = Library_Detail(root)
 root.mainloop()
