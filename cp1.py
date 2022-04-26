import cx_Oracle
from tkinter import messagebox
from tkinter import *
from tkinter import scrolledtext
import matplotlib.pyplot as plt 
import numpy as np
import time
import socket
import requests
import bs4
import os.path
import os
import tkinter as tk      #importing stuffs
from PIL import Image, ImageTk
global data

root=Tk()
root.title("Student Management System")
root.geometry("500x200+500+300")
root.resizable(True, True)
#root.iconbitmap('.ico')
root.configure(background="sky blue")

def login():
		root.withdraw()
		login.deiconify()			

def register():
		root.withdraw()
		register.deiconify()

btnLog=Button(root, text="Login", font=("Times new Roman Bold", 20), command=login)
btnReg=Button(root,text="Register",  font=("Times new Roman Bold", 20),command=register)
btnLog.pack(side=LEFT, padx=20)
btnReg.pack(side=LEFT, padx=20)
 

login=Toplevel(master=root)
login.title("Login")
login.geometry("500x200+500+300")
login.resizable(True, True)
#login.iconbitmap('.ico')
login.configure(background="sky blue")
login.withdraw() #To not open at start of prog

def splash():
	login.withdraw()
	try:
		url='https://www.brainyquote.com/quote_of_the_day'
		res=requests.get(url)
		soup=bs4.BeautifulSoup(res.text,'html.parser') #html parser cause its lit
		quote=str(soup.find("a",{"class":"oncl_q"}))
		
		mid=quote.find("src")+5 #+14 cause we dont want  ' data-img-url:" ' to pop up as well
	
		val=mid+quote[mid:].find(".jpg")+4 #+4 cause we want to inlclude .jpg as well in the string
		final='https://www.brainyquote.com'+str(quote[mid:val]) #using the string manipulation to get the desired o/p
		r=requests.get(final) #fetches image
		if os.path.exists('image1.jpg')==True:
			os.remove("image1.jpg")
			print("File deleted")
		else:
			print("Chill maar, file nai hai")
		with open("image1.jpg", 'wb') as f:
			f.write(r.content)
		print(final)

		hi=Toplevel(login)
		#hi.pack()
		image1 = Image.open("./image1.jpg")
		photo_image = ImageTk.PhotoImage(image1) #usingTk photo image to size as image
		label = tk.Label(hi, image = photo_image) 
		label.pack()

		def temp():
			hi.destroy()
			sms.deiconify()
	
		login.after(5000, temp)
		hi.mainloop()
	except Exception as e:
		messagebox.showerror("ERROR",e)

con=None
cursor=None

def log():
	try:
		temp=1
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		username=[]
		password=[]
		query="select * from login"
		cursor.execute(query)
		con.commit()
		for i in cursor:
			a=username.append(i[0])
			b=password.append(i[1])
		if len(entunn.get())==0 and len(entpww.get())==0:
				messagebox.showerror("ERROR", "Enter credentials")
				temp=2
		elif len(entunn.get())==0:
				messagebox.showerror("ERROR", "Enter username")
				entpww.delete(0,END)
				temp=2
		elif len(entpww.get())==0:
				messagebox.showerror("ERROR","Enter password")
				temp=2
		for i in range(len(password)):
			'''if len(entunn.get())==0 and len(entpww.get())==0:
				messagebox.showerror("ERROR", "Enter credentials")
				temp=2
			elif len(entunn.get())==0:
				messagebox.showerror("ERROR", "Enter username")
				entpww.delete(0,END)
				temp=2
			elif len(entpww.get())==0:
				messagebox.showerror("ERROR","Enter password")
				entunn.delete(0,END)
				temp=2'''
			if username[i]==entunn.get():
				print("un found")
				if password[i]==int(entpww.get()):
					print("pw found")
					temp=3
					entunn.delete(0,END)
					entpww.delete(0,END)	
					break
		if temp==3:
			print("Entered loop")
			splash()
			print("Execute nahin ho rha")
		elif temp==1:
			messagebox.showerror("ERROR","Enter valid Credentials")
			entunn.delete(0,END)
			entpww.delete(0,END)
		cursor.close()
		con.close()
	except Exception as e:
        	print("Issue:", e)

        
def backlog():
	entunn.delete(0,END)
	entpww.delete(0, END)
	root.deiconify()
	login.withdraw()
    
lblunn=Label(login, text="Username:",font=("Times new Roman Bold", 12))
lblunn.place(x=100, y=10)

entunn=Entry(login,bd=10)
entunn.place(x=200, y=10)

lblpww=Label(login,text="Password:",font=("Times new Roman Bold", 12))
lblpww.place(x=100, y=50)

entpww=Entry(login, bd=10, show='*')
entpww.place(x=200, y=50)

btnlog=Button(login, text='LOGIN',font=("Times new Roman Bold", 12), command=log)
btnlog.place(x=220,y=100)
btnbacklog=Button(login, text='BACK',font=("Times new Roman Bold", 12), command=backlog)
btnbacklog.place(x=290,y=100 )



#REGISTER PAGE

register=Toplevel(master=root)
register.title("Register")
register.geometry("500x200+500+300")
register.resizable(True, True)
#register.iconbitmap('.ico')
register.configure(background="sky blue")
register.withdraw()

def reg():
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		username=[]
		password=[]
		query1='insert into register(fn, ln,username,password) values(\'{0}\',\'{1}\',\'{2}\',\'{3}\')'.format(entfn.get(),entln.get(),entun.get(),entpw.get())
		cursor.execute(query1)
		con.commit()
		query2='insert into login (username, password) values(\'{0}\',\'{1}\')'.format(entun.get(), entpw.get())
		cursor.execute(query2)
		con.commit()
		query1='select * from login'
		print("Query intialize ho gayi lol")
		cursor.execute(query1)
		print("Query execute ho gayi lol")
		con.commit()
		for i in cursor:
			username.append(i[0])
			password.append(i[1])
		for i in range(len(password)):
			if len(entun.get())==0 or len(entpw.get())==0 or len(entfn.get())==0 or len(entln.get())==0:
				pass #messagebox.showerror("ERROR", "Enter credentials")
	
			else:
				if entun.get()==username[i]:
					print("un already exists")
					messagebox.showinfo("Error", "Username exists")
					entun.delete(0,END)
				else:
					for i in username:
						if i==entun.get():
							print('Username Found')
					for j in password:
						if str(j) == entpw.get():
							print('Password found')
							entun.delete(0,END)
							entpw.delete(0,END)
							entfn.delete(0,END)
							entln.delete(0,END)
							messagebox.showinfo("Registration", "Registration successful!")
							#register.withdraw()
							#login.deiconify()
						'''else:
							messagebox.showerror("Error", "Enter valid char only")
							entun.delete(0,END)
							entpw.delete(0,END)
							entfn.delete(0,END)
							entln.delete(0,END)'''
				#  importlib.import_module('next mod.py')
	except Exception as e:
		print("Issue:", e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

def back():
	entun.delete(0,END)
	entpw.delete(0,END)
	entfn.delete(0,END)
	entln.delete(0,END)
	root.deiconify()
	register.withdraw()

lbldet = Label(register, text="Please enter registration details", font=("Arial Bold", 10))
lbldet.place(x=0, y=0)

lblfn = Label(register, text="First Name:")
lblfn.place(x=0, y=20)

entfn = Entry(register,width=10)
entfn.place(x=60, y=20 )
entfn.focus()

lblln = Label(register, text="Last Name:")
lblln.place(x=0, y=45)

entln = Entry(register, width=10)
entln.place(x=60, y=45)

lblun = Label(register, text="Username:")
lblun.place(x=00, y=70)

entun= Entry(register,width= 10)
entun.place(x=60, y=70)

lblpw=Label(register,text="Password:")
lblpw.place(x=00, y=95)

entpw=Entry(register, width="10", show='*')
entpw.place(x=60, y=95)

btnreg = Button(register, text="Register", bg="blue", fg="white", width=10, command=reg)
btnreg.place(x=130, y=125)

btnback = Button(register, text="Back", bg="blue", fg="white", width=10, command=back)
btnback.place(x=230, y=125)

lblinfo=Label(register, text="Password should not contain more than 10 characters (numbers).")
lblinfo.place(x=120, y=150)

sms=Toplevel(master=login)
sms.title("S.M.S.")
sms.geometry("500x400+500+400")
sms.resizable(True, True)
#sms.iconbitmap('.ico')
sms.configure(background="sky blue")
sms.withdraw()

def f1():
	adSt.deiconify()
	sms.withdraw()

def f9():
	sms.withdraw()
	deSt.deiconify()

def f6():
	upSt.deiconify()
	sms.withdraw()
	

def f3():
	viSt.deiconify()
	sms.withdraw()

	try:
		global data
		global msg
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		query="select * from student"
		cursor.execute(query)
		data=cursor.fetchall()
		msg=''
		for d in data:
                	msg=msg+"RNo: "+str(d[0])+" Name:"+str(d[1])+" Marks:"+str(d[2]) +"\n"
		stData.insert(INSERT,msg)	
		
	except cx_Oracle.DatabaseError as e:
		print ("Select issue", e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

def f4():
	stData.delete('1.0',END)
	viSt.withdraw()
	sms.deiconify()         
	
def f11():
	try:
		                                             
		con=cx_Oracle.connect("system/abc123")
		rno=int(entAddRno2.get())
		cursor=con.cursor()
		sql="delete from student where rno=('%d')"
		args=(rno)
		cursor.execute(sql%args)
		con.commit()
		msg=str (cursor.rowcount) + "Rows sucesssfully updated"
		messagebox.showinfo("", msg)
		entAddRno2.delete(0,END)

	except Exception as e:
		con.rollback()
		messagebox.showerror("Failure",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()	 
		

def f12():
        try:
                con=cx_Oracle.connect("system/abc123")	
                cursor=con.cursor()
                l1=[]
                l2=[]
                sql1="select * from student"
                cursor.execute(sql1)
                row=cursor.fetchall()
                for r in row:
                        plt.bar(r[1],r[2],width=0.5)
                plt.title('Exam score',fontsize=20)
                plt.legend(loc="upper right",shadow=True)
                plt.xlabel('Subjects',fontsize=15)
                plt.ylabel('Marks',fontsize=15)
                plt.show()

        except Exception as e:
                messagebox.showerror("Failure",e)
                
                
		
	
def f13():
    sms.withdraw()
    root.deiconify()

btnAdd=Button(sms,text="Add", font=("arial", 16, 'bold'), width=10,command=f1)
btnView=Button(sms,text="View", font=("arial", 16, 'bold'), width=10, command=f3)
btnUpdate=Button(sms,text="Update", font=("arial", 16, 'bold'), width=10,command=f6)
btnDelete=Button(sms,text="Delete", font=("arial", 16, 'bold'), width=10, command=f9)
btnGraph=Button(sms,text="Graph", font=("arial", 16, 'bold'), width=10,command=f12)
btnexit=Button(sms,text="LogOut", font=("arial", 16, 'bold'), width=10,command=f13)

btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnGraph.pack(pady=10)
btnexit.pack(pady=10)

adSt=Toplevel(sms)
adSt.title("Add student")
adSt.geometry("400x400+200+200")
adSt.withdraw()

upSt=Toplevel(sms)
upSt.title("Add student")
upSt.geometry("400x400+200+200")
upSt.withdraw()

deSt=Toplevel(sms)
deSt.title("Delete student")
deSt.geometry("400x400+200+200")
deSt.withdraw()



def f2():
	sms.deiconify()
	adSt.withdraw()



def f5():
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		rno=int(entAddRno.get())
		name=entAddName.get()
		marks=int(entAddMarks.get())

		cursor=con.cursor()
		sql="insert into student values('%d', '%s', '%d')"
		args=(rno,name, marks)
		cursor.execute(sql % args)
		con.commit()
		msg=str (cursor.rowcount) + "Rows inserted"
		messagebox.showinfo("Success", msg)
		entAddRno.delete(0,END)
		entAddMarks.delete(0,END)
               # entAddName.delete(0,END)

	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("Failure",e)
		entAddRno.delete(0,END)
		entAddMarks.delete(0,END)
		#entAddName.delete(0,END)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

def f8():
	sms.deiconify()
	upSt.withdraw()

def f10():
	sms.deiconify()
	deSt.withdraw()

def f7():
	con=None
	cursor=None
	try:
		
		con=cx_Oracle.connect("system/abc123")
		rno=int(entAddRno1.get())
		name=entAddName1.get()
		marks=int(entAddMarks1.get())
		cursor=con.cursor()
		sql="update student set name=('%s'),marks=('%d') where rno= ('%d')"
		args=(name, marks,rno)
		cursor.execute(sql%args)
		con.commit()
		msg=str (cursor.rowcount) + "Rows sucesssfully updated"
		messagebox.showinfo("", msg)
		entAddRno1.delete(0,END)
		entAddMarks1.delete(0,END)
		entAddName1.delete(0,END)
	except Exception as e:
		con.rollback()
		messagebox.showerror("Failure",e)
		entAddRno1.delete(0,END)
		entAddMarks1.delete(0,END)
		entAddName1.delete(0,END)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()






lblAddRno=Label(adSt,text="Enter rno")
lblAddName=Label(adSt,text="Enter name")
lblAddMarks=Label(adSt,text="Enter marks")
entAddRno=Entry(adSt, bd=5)
entAddName=Entry(adSt, bd=5)
entAddMarks=Entry(adSt, bd=5)
btnAddSave=Button(adSt, text="Save", command=f5)
btnAddBack=Button(adSt, text="Back", command=f2)

lblAddRno.pack(pady=10)
entAddRno.pack(pady=10)
lblAddName.pack(pady=10)
entAddName.pack(pady=10)
lblAddMarks.pack(pady=10)
entAddMarks.pack(pady=10)
btnAddSave.pack(pady=10)
btnAddBack.pack(pady=10)

lblAddRno1=Label(upSt,text="Enter rno to be updated")
lblAddName1=Label(upSt,text="Enter name")
lblAddMarks1=Label(upSt,text="Enter marks")
entAddRno1=Entry(upSt, bd=5)
entAddName1=Entry(upSt, bd=5)
entAddMarks1=Entry(upSt, bd=5)
btnAddSave1=Button(upSt, text="Save",command=f7)
btnAddBack1=Button(upSt, text="Back", command=f8)
lblAddRno1.pack(pady=10)
entAddRno1.pack(pady=10)
lblAddName1.pack(pady=10)
entAddName1.pack(pady=10)
lblAddMarks1.pack(pady=10)
entAddMarks1.pack(pady=10)
btnAddSave1.pack(pady=10)
btnAddBack1.pack(pady=10)

lblAddRno2=Label(deSt,text="Enter rno to be deleted")
entAddRno2=Entry(deSt, bd=5)
btnAddSave2=Button(deSt, text="delete",command=f11)
btnAddBack2=Button(deSt, text="Back",command=f10)
lblAddRno2.pack(pady=10)
entAddRno2.pack(pady=10)
btnAddSave2.pack(pady=10)
btnAddBack2.pack(pady=10)





	
        

viSt=Toplevel(sms)
viSt.title("view students")
viSt.geometry("400x400+200+200")
viSt.withdraw()

stData=scrolledtext.ScrolledText(viSt,width=30,height=10)
btnViewBack=Button(viSt,text="back",command=f4)
stData.pack(pady=10)
btnViewBack.pack(pady=10)

root.mainloop()