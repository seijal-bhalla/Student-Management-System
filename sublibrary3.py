from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cx_Oracle
from tkinter import messagebox
class Book_details:
 def __init__(self, root):
 self.root = root
 self.root.title("BOOK DETAILS")
 self.root.geometry("1550x800")
 img1 = Image.open(r"C:\Users\DELL\Downloads\\bunty.jpeg")
 img1 = img1.resize((1550,740), Image.ANTIALIAS)
 self.photoImg1 = ImageTk.PhotoImage(img1)
 lb = Label(self.root, image=self.photoImg1, bd=4, relief=RIDGE)
 lb.place(x=0, y=0, width=1550, height=740)
 cust_btn=Button(self.root,text="DISPLAY DATA",command=self.fetch_data_boo
k,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
 cust_btn.place(x=10,y=150,width=200)
 def fetch_data_book(self):
 con=cx_Oracle.connect("system/seijal")
 my_cursor = con.cursor()
 my_cursor.execute("select * from book_detail")
 tree=ttk.Treeview(self.root,height="60")
 tree.place(x=1295,y=650)
 tree['show']='headings'
 tree["columns"]=("bno","bname","author","qnty")
 tree.column("bno",width=50,minwidth=50,anchor=CENTER)
 tree.column("bname",width=100,minwidth=100,anchor=CENTER)
 tree.column("author",width=50,minwidth=50,anchor=CENTER)
 tree.column("qnty",width=150,minwidth=150,anchor=CENTER) 
 tree.heading("bno",text="DBOOK_NUM",anchor=CENTER)
 tree.heading("bname",text="BOOK_NAME",anchor=CENTER)
 tree.heading("author",text="AUTHOR",anchor=CENTER)
 tree.heading("qnty",text="QUANTITY",anchor=CENTER)
 count=0
 for i in my_cursor:
 tree.insert('',count,text=" ",values=(i[0],i[1] ,i[2], i[3]))
 count=count+1
 tree.pack(fill='x')
if __name__ == '__main__':
 root = Tk()
 obj = Book_details(root)
 root.mainloop()
