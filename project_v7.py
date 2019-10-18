import cx_Oracle
import datetime
from datetime import date
import random
import re
from tkinter import *
from tkinter import messagebox
#from PIL import ImageTk,Image
from tkinter import ttk

class Main_menu():
	def __init__(self,mas=''):
		if mas:
			mas.destroy()
		self.root=Tk()
		self.root.configure(background="plum")
		self.root.title("Main Menu")	
		self.root.geometry("1000x1000")
		self.Variable()
		self.Grid()
		
		self.Label()
		self.Entry()
		self.Button()
		self.gframe.place(x=250,y=250)
		#self.gframe0.pack()
		#self.gframe1.pack()
		#print("ds")
		#self.gframe2.pack()
		self.root.mainloop()	
	def Get_un_pwd(self):
		u=self.__usn.get()
		p=self.__pwd.get()
		self.New_win(u,p)
	'''def Get_usn(self):
		return self.__usn'''
	def New_win(self,u,p):
		usrn=''
		print(u[4:7])
		conn=cx_Oracle.connect('Hos','hos','XE')
		cur=conn.cursor()
		cur.execute("select * from Employee_login where E_ID=:E_ID",{'E_ID':u})
		for i in cur:
			print(i)
			pawd=i[1]
			usrn=i[0]
		cur.close()
		conn.close()
		'''data base task pending'''
		if usrn and p==pawd and u[4:7]=="Doc":
			#self.new=Toplevel(self.root)
			
			self.new_wd=Doc_menu(self.root,u)
			self.new_wd.Pack_all()
			#self.root.close()
		elif usrn and p==pawd and u[0:3]=="adm":
			
			self.new_wd=Admin_menu(self.root,u)
			self.new_wd.Pack_all()		
		elif usrn and p==pawd and u[0:3]=="cas":
			
			self.new_wd=Cash_menu(self.root,u)
			self.new_wd.Pack_all()	
		elif usrn and p==pawd and u[0:3]=="rec":
			
			self.new_wd=Info_desk_menu(self.root,u)
			self.new_wd.Pack_all()			 
		else:
			messagebox.showinfo("LoGIN", "failed")
			self.__usn.set("")
			self.__pwd.set("")
			#self.entyun.focus()
			#self.entyps.focus()
	def Exit(self):
		self.root.destroy()	

	def Variable(self):
		self.__usn=StringVar(self.root)
		self.__pwd=StringVar(self.root)
		
	def Label(self):
		self.lb1=Label(self.gframe1,text="LOG IN",font=50).grid(pady=40,columnspan=3)		
		self.lbun=Label(self.gframe1,text="User Name:", font = 40).grid(row=1,column=0,sticky=E)
		self.lbps=Label(self.gframe1,text="Password:",font=40).grid(row=2,column=0,sticky=E)	
	def Entry(self):
		self.entyun=Entry(self.gframe1,textvariable=self.__usn).grid(row=1,column=1,sticky=W)	
		self.entyps=Entry(self.gframe1,textvariable=self.__pwd,show="*").grid(row=2,column=1,sticky=W)
	def Button(self):
		self.but_login=Button(self.gframe2,text="LOG IN",width=20,bg='purple',fg ='white',command=self.Get_un_pwd).grid(row=0,column=0,sticky=W)
		#self.but_login=Button(self.gframe2,text="RESET",width=10).grid(row=0,column=1,sticky=W)
		self.but_Exit=Button(self.gframe2,text="EXIT",bg='purple',fg ='white',width=20,command=self.Exit).grid(row=0,column=2,sticky=W)
	def Grid(self):
		#self.gframe1=Frame(self.root)
		self.gframe=Frame(self.root,bg="plum",height=1000)
		#self.gframe.place(height=300,width=300)
		#self.gframe.grid(rowspan=2)	
		'''self.gframe0=LabelFrame(self.gframe,bd=12)
		self.gframe0.grid(row=0,column=3,sticky=NW)'''
		self.gframe1=LabelFrame(self.gframe,bd=12,height=100,width=100)
		self.gframe1.grid(row=0,column=1)	
		self.gframe2=LabelFrame(self.gframe,height=100,width=100,bd=12)
		self.gframe2.grid(row=1,column=1)
class com_menu():
	def __init__(self,mas="",u='0'):
		self.mas=mas
		self.nm=u
		#print(self.nm)
		mas.destroy()
		self.mas=Tk()
		self.mas.configure(background="plum")
		self.lbwl=''
		self.but=[]
		#self.r=0
		#self.c=0
		#self.__dpt=''
		#self.options=[]
		self.but_text=()
		self.but_cmmd=()

	def Grid(self):
		
		self.gframe=Canvas(self.mas,bg="plum",height=1000,width=1000)
		self.gframe1=LabelFrame(self.gframe,bd=12,height=100,width=100,bg="violet")
		self.gframe1.grid(row=0,column=1)

	def Label(self):
		self.lb1=Label(self.gframe1,text=self.lbwl+"\n"+self.nm,font=14,bg="violet",justify='center').grid(pady=40,columnspan=3)
	def Button(self):
		for i in range(len(self.but_text)-2,len(self.but_text)):

			self.but.append(Button(self.gframe1,text=self.but_text[i],width=20,bd=4,bg='purple',fg ='white',command=self.but_cmmd[i]).grid(row=i+1,column=0,columnspan=3))
#class Change_pwd_menu():

	def Change_pwd(self):
		self.new_wd=Change_pwd_menu(self.mas,self.nm)
		self.new_wd.Pack_all()             
	def Logout(self):
		self.login=Main_menu(self.mas)
class Doc_menu(com_menu):
	
	
	def Pack_all(self):
		self.but_text=("Schedule","Schedule Set","Patient Records","Patient Reports","Change Password","Log OUT")		
		self.but_cmmd=(self.Go_sch,self.Go_sch_set,self.Go_pat_rec,self.Go_pat_rep,self.Change_pwd,self.Logout)		
		self.lbwl="Welcome Doctor"
		self.mas.title("Doctor Menu")	
		self.mas.geometry("1000x700")

		self.Grid()
		self.Label()
		self.Button()
		self.Button_doc()
		self.gframe.place(x=300,y=250)
		self.mas.mainloop()
	def Go_sch(self):
		self.new_wd=Schedule_menu(self.mas,self.nm)
		self.new_wd.Pack_all(self.nm)  
	def Go_sch_set(self):
		self.new_wd=Schedule_set_menu(self.mas,self.nm)
		self.new_wd.Pack_all(self.nm)    
		#self.new_wd.Get_ID()	
	def Go_pat_rec(self):
		self.new_wd=Patient_record_menu(self.mas,self.nm)
		self.new_wd.Pack_all(self.nm)   
	def Go_pat_rep(self):
		self.new_wd=Patient_repord_menu(self.mas,self.nm)
		self.new_wd.Pack_all(self.nm)   

	def Button_doc(self):
		for i in range(len(self.but_text)-2):

			self.but.append(Button(self.gframe1,text=self.but_text[i],width=20,bd=4,bg='purple',fg ='white',command=self.but_cmmd[i]).grid(row=i+1,column=0,columnspan=3))



class Admin_menu(com_menu):
	
	
	def Pack_all(self):
		self.but_text=("Attendance","Register New Employee","Pathology Entry","Suggestion","Blood Bank","Change Password","Log OUT")
		self.but_cmmd=(self.Att_en,self.Reg_new_emp,self.patho_en,self.Advice,self.Blood,self.Change_pwd,self.Logout)	
		self.lbwl="Welcome"
		self.mas.title("Admin Menu")	
		self.mas.geometry("1000x700")

		self.Grid()
		self.Label()
		self.Button()
		self.Button_adm()
		self.gframe.pack(anchor=CENTER)
		self.mas.mainloop()
	def Button_adm(self):
		for i in range(len(self.but_text)-2):

			self.but.append(Button(self.gframe1,text=self.but_text[i],width=20,bd=4,bg='purple',fg ='white',command=self.but_cmmd[i]).grid(row=i+1,column=0,columnspan=3))
	def Reg_new_emp(self):
		self.new_wd=Data_entry_emp(self.mas,self.nm)
		self.new_wd.Pack_all()     
	        		
	def Advice(self):
		self.new_wd=Suggestion(self.mas,self.nm)
		self.new_wd.Pack_all()   
	def Blood(self):
		self.new_wd=Blood_bank_menu(self.mas,self.nm)
		self.new_wd.Pack_all()    
	def Att_en(self):
		self.new_wd=Attendance_menu(self.mas,self.nm)
		self.new_wd.Pack_all()  
	def patho_en(self):
		self.new_wd=Pathology_entry(self.mas,self.nm)
		self.new_wd.Pack_all()    

#Blood_bank_menu Attendance_menu
class Cash_menu(com_menu):
	
	def Pack_all(self):
		self.but_text=('Report Delivery','Bill Blood','Patient Discharge','Change Password','Log OUT')
		self.but_cmmd=(self.repotbill,self.Bloodbill,self.Padis,self.Change_pwd,self.Logout)
		self.lbwl="Welcome"
		self.mas.title("Cashier Menu")	
		self.mas.geometry("1000x700")

		self.Grid()
		self.Label()
		self.Button()
		self.Button_cash()
		self.gframe.pack(anchor=CENTER)
		self.mas.mainloop()
	def Button_cash(self):
		for i in range(len(self.but_text)-2):
			self.but.append(Button(self.gframe1,text=self.but_text[i],width=20,bd=4,bg='purple',fg ='white',command=self.but_cmmd[i]).grid(row=i+1,column=0,columnspan=3))
	def Bloodbill(self):
		self.new_wd=Blood_bill_menu(self.mas,self.nm)
		self.new_wd.Pack_all()    
	def repotbill(self):
		self.new_wd=Report_Del_menu(self.mas,self.nm)
		self.new_wd.Pack_all() 
	def Padis(self):
		self.new_wd=Patient_disc_menu(self.mas,self.nm)
		self.new_wd.Pack_all() 

class Info_desk_menu(com_menu):
	
	def Pack_all(self):
		self.but_text=('Patient Registration','Patient Info','Patient Advice','Blood Bank Info','Report Availability','Ambulance information','Change Password','Log OUT')
		self.but_cmmd=(self.Patient_registration,self.Go_doc_pa_rec,self.Go_doc_sug,self.Blood,self.Report_av,self.Ambu,self.Change_pwd,self.Logout)
		self.lbwl="Welcome"
		self.mas.title("Information Desk Menu")	
		self.mas.geometry("1000x700")

		self.Grid()
		self.Label()
		self.Button()
		self.Button_info()
		self.gframe.pack(anchor=CENTER)
		self.mas.mainloop()
	def Button_info(self):
		for i in range(len(self.but_text)-2):
			self.but.append(Button(self.gframe1,text=self.but_text[i],width=20,bd=4,bg='purple',fg ='white',command=self.but_cmmd[i]).grid(row=i+1,column=0,columnspan=3))
	def Blood(self):
		self.new_wd=Blood_Info_show_menu(self.mas,self.nm)
		self.new_wd.Pack_all()    
	def Ambu(self):
		self.new_wd=Ambulance_menu(self.mas,self.nm)
		self.new_wd.Pack_all()    
	def Report_av(self):
		self.new_wd=Pathology_report_av(self.mas,self.nm)
		self.new_wd.Pack_all()  
	def Patient_registration(self):
		self.new_wd=Patient_registration_menu(self.mas,self.nm)
		self.new_wd.Pack_all()  
	def Go_doc_sug(self):
		self.new_wd=Rec_doc_Suggestion(self.mas,self.nm)
		self.new_wd.Pack_all()  
	def Go_doc_pa_rec(self):
		self.new_wd=Rep_Patient_record_menu(self.mas,self.nm)
		self.new_wd.Pack_all() 		

class Change_pwd_menu(com_menu):
	def Pack_all(self):
		self.mas.title("Change Password Menu")	
		self.mas.geometry("1000x700")
		self.Variable()
		self.Grid()
		self.Label()
		self.Entry()
		self.Button()
		self.gframe.pack(anchor=CENTER)
		self.mas.mainloop()
	def Label(self):
		self.lbus=Label(self.gframe1,text='User Name:',font=14,bg="violet",justify='center').grid(row=1,column=0,sticky=E,pady=5)     
		self.lbcpw=Label(self.gframe1,text='Current Password:',font=14,bg="violet",justify='center').grid(row=2,column=0,sticky=E,pady=5)
		self.lbnpw=Label(self.gframe1,text='New Password:',font=14,bg="violet",justify='center').grid(row=3,column=0,sticky=E,pady=5)
		self.lbun=Label(self.gframe1,text=self.nm,font=14,bg="violet",justify='center').grid(row=1,column=1,sticky=W)
		self.lbm=Label(self.gframe1,text=self.message,font=14,bg="violet",justify='center').grid(row=5,columnspan=3)
	def Entry(self):
		#self.entyun=Entry(self.gframe1,text=self.nm,textvariable=self.nm).grid(row=1,column=1,sticky=W)	
		self.entycps=Entry(self.gframe1,textvariable=self.__cpw,show="*").grid(row=2,column=1,sticky=W)
		self.entynps=Entry(self.gframe1,textvariable=self.__npw,show="*").grid(row=3,column=1,sticky=W)
	def Button(self):
		self.but_chp=Button(self.gframe1,text="Change Password",width=17,bd=4,bg='purple',fg ='white',command=self.Update).grid(row=4,column=1,sticky=W,pady=5)
	def Variable(self):
		self.message=''
		self.__cpw=StringVar(self.mas)
		self.__npw=StringVar(self.mas)
	def Update(self):
		old=self.__cpw.get()
		new=self.__npw.get()
		conn=cx_Oracle.connect('Hos','hos','XE')
		cur=conn.cursor()
		cur.execute("select Password1 from Employee_login where E_id=('%s')"%self.nm)
		for i in cur:
			
			pawd=i[0]
			print(old,pawd)
	
		cur.close()
		conn.close()	
		if old==str(pawd):
			conn=cx_Oracle.connect('Hos','hos','XE')
			cur=conn.cursor()
			cur.execute('UPDATE Employee_login SET Password1 = :passw WHERE E_ID =:us',{'passw':new,'us':self.nm})
			conn.commit()
			cur.close()
			conn.close()
			self.Logout()
		else:
			self.__npw.set("")
			self.__npw.set("")
			self.message='Wrong Old Password'
			self.Label()				 	

class Data_entry_emp(com_menu):
	def Pack_all(self):
		
		self.mas.title("Employee Entry")	
		self.mas.geometry("1000x700")
		self.Variable()
		self.Grid()
		self.Label()
		self.Entry()
		self.Radio_but()
		self.Option_men()
		self.Button()

		self.gframe.pack(anchor=CENTER)
		#self.lbnm.pack(side=LEFT,anchor=NW)
		self.mas.mainloop()
	def Get_data(self):
		self.na=self.__name.get()
		self.ag=self.__age.get()
		self.j=self.__jd.get()
		self.de=self.__des.get()
		self.sa=self.__sal.get()
		self.ge = self.__gen.get()
		self.r=self.__rk.get()
		self.dp=self.__dpt.get()
		print(self.na," ",self.ag," ",self.j," ",self.de," ",self.sa," ",self.ge," ",self.r," ",self.dp)
		self.__name.set("")
		self.__age.set("")
		self.__jd.set("")
		self.__des.set("")
		self.__sal.set("")
		self.__gen.set("")
		self.__rk.set("")
		self.__dpt.set("")
		self.Give_dt()
	def Give_dt(self):
		if self.de=='Doctor':
			self.pass_dt=Doctor(self.na)
			self.pass_dt.Get_info(self.ag,self.j,self.ge,self.sa,self.de,self.r,self.dp)
			self.pass_dt.Doc_insert()
		#print(self.__name," ",self.__age," ",self.__jd," ",self.__des," ",self.__sal," ",self.__gen," ",self.__rk," ",self.__dpt)
	def Exit(self):
		self.new_wd=Admin_menu(self.mas,self.nm)
		self.new_wd.Pack_all()     		
	def Variable(self):
		self.options=["Gayanology","orthology"]
		#self.r=6
		#self.c=1
		self.__name=StringVar(self.mas)
		self.__age=StringVar(self.mas)
		self.__jd=StringVar(self.mas)
		self.__des=StringVar(self.mas)
		self.__sal=StringVar(self.mas)
		self.__gen=StringVar(self.mas)
		self.__rk=StringVar(self.mas)
		self.__dpt=StringVar(self.mas)
		self.__dpt.set(self.options[0])
	def Label(self):
		self.lb1=Label(self.gframe1,text="Enter Information",font=17,bg="violet",justify='center').grid(row=0,column=0,sticky=N,pady=5)
		self.lbnm=Label(self.gframe1,text="Name:",font=14,bg="violet",justify='center').grid(row=1,column=0,sticky=E,pady=5)
		self.lbage=Label(self.gframe1,text="Age:",font=14,bg="violet",justify='center').grid(row=2,column=0,sticky=E,pady=5)
		self.lbgen=Label(self.gframe1,text="Gender:",font=14,bg="violet",justify='center').grid(row=3,column=0,sticky=E,pady=5)
		self.lbjd=Label(self.gframe1,text="Joining Date:",font=14,bg="violet",justify='center').grid(row=4,column=0,sticky=E,pady=5)
		self.lbdes=Label(self.gframe1,text="Designation:",font=14,bg="violet",justify='center').grid(row=5,column=0,sticky=E,pady=5)
		self.lbdpt=Label(self.gframe1,text="Dept:",font=14,bg="violet",justify='center').grid(row=6,column=0,sticky=E,pady=5)
		self.lbrk=Label(self.gframe1,text="Rank:",font=14,bg="violet",justify='center').grid(row=7,column=0,sticky=E,pady=5)
		self.lbsal=Label(self.gframe1,text="Salary:",font=14,bg="violet",justify='center').grid(row=8,column=0,sticky=E,pady=5)
	
	def Entry(self):
		self.entynm=Entry(self.gframe1,textvariable=self.__name).grid(row=1,column=1,sticky=W)
		self.entyage=Entry(self.gframe1,textvariable=self.__age).grid(row=2,column=1,sticky=W)
		self.entyjd=Entry(self.gframe1,textvariable=self.__jd).grid(row=4,column=1,sticky=W)
		self.entydes=Entry(self.gframe1,textvariable=self.__des).grid(row=5,column=1,sticky=W)
		self.entysal=Entry(self.gframe1,textvariable=self.__sal).grid(row=8,column=1,sticky=W)
		self.entyrk=Entry(self.gframe1,textvariable=self.__rk).grid(row=7,column=1,sticky=W)
	def Button(self):
		self.but_info=Button(self.gframe1,text="Submit",width=17,bd=4,bg='purple',fg ='white',command=self.Get_data).grid(row=9,column=1,sticky=W,pady=5)
		self.but_info=Button(self.gframe1,text="EXIT",width=20,bd=4,bg='purple',fg ='white',command=self.Exit).grid(row=10,pady=10,columnspan=3)

	def Radio_but(self):
		self.R1 = Radiobutton(self.gframe1, text="Male", variable=self.__gen, value="male",font=14,bg="violet",justify='center',bd=0).grid(row=3,column=1,sticky=W)
		self.R2 = Radiobutton(self.gframe1, text="Female", variable=self.__gen, value="Female",font=14,bg="violet",justify='center',bd=0).grid(row=3,column=2,sticky=W)
	def Option_men(self):
		#combobox self.scldpt options
		self.scldpt = ttk.Combobox(self.gframe1,values=self.options,textvariable=self.__dpt).grid(row=6,column=1,sticky=W)
#databe insertion
class Employee():
	def __init__(self,name):

		self.name=name
		self.__age=0
		self.__j_date=''
		self.gen=''
		self.id=''
		self.__salary=0
		self.designation=''
		self.rank=''
		self.department=''
		
	def Get_info(self,age,jdate,gen,sal,designation,rank,dept):
		self.__age=age
		self.__j_date=jdate
		self.designation=designation
		self.gen=gen
		self.rank=rank
		self.department=dept		
		self.id=self.name[0:3]+'_'+self.designation[0:3]+'_'+self.__j_date[-2:]
		self.__salary=sal
		self.Insert()
	def Insert(self):
		id1=str(self.id)
		name=str(self.name)
		des=str(self.designation)
		age=float(self.__age)
		
		sal=float(self.__salary)
		dymd='YYYY/MM/DD'
		#print(id1,name,des,age,jd,sal)
		conn=cx_Oracle.connect('Hos','hos','XE')
		
		#jd=to_date(self.__j_date,'YYYY-MM-DD')
		cur=conn.cursor()

		cur.execute('insert into employee(E_ID,NAME,DESIGNATION,AGE,GENDER,J_DATE,SALARY) values(:E_ID,:NAME,:DESIGNATION,:AGE,:GENDER,:J_DATE,:SALARY)',{'E_ID':id1,'NAME':name,'DESIGNATION':des,'AGE':age,'GENDER':self.gen,'J_DATE':self.__j_date,'SALARY':sal})
		conn.commit()
		cur.close()
		cur=conn.cursor()

		cur.execute('insert into Employee_login(E_ID,PASSWORD1) values(:E_ID,:Password)',{'E_ID':id1,'Password':'123456'})
		conn.commit()
		cur.close()		
		conn.close()
		
		
	def Show(self):
		conn=cx_Oracle.connect('Hos','hos','XE')
		cur=conn.cursor()
		cur.execute('select * from employee')
		for i in cur:
			print(i)
		cur.execute('select * from Doctor')
		for i in cur:
			print(i)
		cur.close()
		conn.close()
class Doctor(Employee):
	def Doc_insert(self):
		conn=cx_Oracle.connect('Hos','hos','XE')
		
		#jd=to_date(self.__j_date,'YYYY-MM-DD')
		cur=conn.cursor()

		cur.execute('insert into Doctor(E_ID,DEPT,RANK1) values(:E_ID,:DEPT,:RANK)',{'E_ID':self.id,'DEPT':self.department,'RANK':self.rank})
		conn.commit()
		cur.close()
		conn.close()
class Suggestion(com_menu):
	def Pack_all(self):
		self.mas.title("Patient Advice")	
		self.mas.geometry("1000x700")
		self.Variable()
		self.Grid()
		self.Label()
		self.Option_men()
		self.Button()
		self.gframe.place(x=20,y=20)
		self.mas.mainloop()
	def Variable(self):
		self.options=("Gayanology","orthology")
		self.r=3
		self.__ID=''
		self.__Name=''
		self.__Rank=''
		self.__dpt=StringVar(self.mas)
		self.__dpt.set(self.options[0])
		self.lbfordoc=''
		self.lbfordoc1=''
		self.lbfordoc2=''
		self.lb4=''
	def Label(self):
		self.lbdpt=Label(self.gframe1,text="Dept:",font=17,bg="violet",justify='center').grid(row=1,column=0,sticky=N,pady=5)
	def Label1(self):
		self.lb1=Label(self.frame_1 ,text="ID",font=17,bg="orange",justify='center').grid(row=0,column=0,sticky=N,pady=5)
		self.lb2=Label(self.frame_1 ,text="Name",font=17,bg="orange",justify='center').grid(row=0,column=1,sticky=N,pady=5)
		self.lb3=Label(self.frame_1 ,text="    Rank",font=17,bg="orange",justify='center').grid(row=0,column=2,sticky=N,pady=5)
		
	def Option_men(self):
		#combobox self.scldpt options
		self.scldpt = ttk.Combobox(self.gframe1,values=self.options,textvariable=self.__dpt).grid(row=1,column=1,sticky=W)
	def Get_dt(self):
		self.dp=self.__dpt.get()
		self.__dpt.set(self.options[0])
		if self.lbfordoc!='':
			self.lbfordoc.grid_forget()
		if self.lbfordoc1!='':
			self.lbfordoc1.grid_forget()
		if self.lbfordoc2!='':
			self.lbfordoc2.grid_forget()
		if self.lb4!='':
			self.lb4.grid_forget()
		conn=cx_Oracle.connect('Hos','hos','XE')
		
		#jd=to_date(self.__j_date,'YYYY-MM-DD')
		cur=conn.cursor()

		cur.execute('select E_ID,Name,rank1 from employee natural join doctor where dept=:dp',{'dp':self.dp})
		rs = cur.fetchall()
		#print(i)
		if len(rs)!=0:
			#self.gframe=Canvas(self.mas,bg="plum",height=1000,width=1000)
			self.gframe2=Canvas(self.gframe1,bd=12,height=100,width=300,bg="orange")
			self.gframe2.grid(row=4,columnspan=3)
			self.mas.geometry("1000x700")	
			#self.gframe.configure(height=500,width=500)	
			self.gframe.place(x=80,y=80)
		 
			self.scrollbar = Scrollbar(self.gframe1,command=self.gframe2.yview)
			self.scrollbar.grid(row=4, column=3, sticky=NS)
			
			self.gframe2.configure(yscrollcommand=self.scrollbar.set)
			self.frame_1 = Frame(self.gframe2, bg="orange")
			self.frame_1.grid(row=-0,columnspan=3)
			self.gframe2.create_window((0, 0), window=self.frame_1, anchor='nw')
			count=1
			self.Label1()
			
			for i in rs:
				self.__ID=i[0]
				self.__Name=i[1]
				self.__Rank=i[2]
				self.lbfordoc=Label(self.frame_1 ,text=self.__ID,font=17,bg="orange",justify='center')
				self.lbfordoc.grid(row=count,column=0,sticky=N,pady=5)
				self.lbfordoc1=Label(self.frame_1 ,text=self.__Name,font=17,bg="orange",justify='center')
				self.lbfordoc1.grid(row=count,column=1,sticky=N,pady=5)
				self.lbfordoc2=Label(self.frame_1 ,text="    "+self.__Rank,font=17,bg="orange",justify='center')
				self.lbfordoc2.grid(row=count,column=2,sticky=N,pady=5)
				count+=1
					
				
		else:
			self.lb4=Label(self.gframe1,text="No data Found",font=17,bg="violet",justify='center').grid(row=4,sticky=N,pady=5,columnspan=3)	
		cur.close()
	
		conn.close()

		bbox = self.gframe2.bbox(ALL) 
		self.gframe1.config(row=4,height=count)
      
		self.gframe2.configure(scrollregion=bbox)

	def Exit(self):
		self.new_wd=Admin_menu(self.mas,self.nm)
		self.new_wd.Pack_all()     	
	def Button(self):
		self.but_search=Button(self.gframe1,text="Search",width=17,bd=4,bg='purple',fg ='white',command=self.Get_dt).grid(row=2,pady=5,columnspan=3)
		self.but_info=Button(self.gframe1,text="EXIT",width=20,bd=4,bg='purple',fg ='white',command=self.Exit).grid(row=self.r,pady=10,columnspan=3)
class Blood_bank_menu(com_menu):
	def Pack_all(self):
		self.mas.title("Blood Bank")	
		self.mas.geometry("1000x700")
		self.Variable()
		self.Grid()
		self.Label()
		self.Entry()
		self.Option_men()
		self.Button()
		self.gframe.place(x=100,y=80)
		self.mas.mainloop()
	def Get_blg(self):
		self.blod=self.__blood.get()
		self.__blood.set("")
		conn=cx_Oracle.connect('Hos','hos','XE')
		
		#jd=to_date(self.__j_date,'YYYY-MM-DD')
		cur=conn.cursor()

		cur.execute('select Bags,PRICE_PER_BAG from blood where B_ID=:bid',{'bid':self.blod})
		rs = cur.fetchall()
		#print(i)
		if len(rs)!=0:

			for i in rs:	
				print(i)
				self.bag_gg_g=i[0]
				self.pr__r__r=i[1]
				#if self.time=='9Am-12Noon':
		self.Labelextra()								
		cur.close()
	
		conn.close()
	def Labelextra(self):
		if self.lbBlgg!='':
			self.lbBlgg.grid_forget()
		if self.lbBlbg1!='':
			self.lbBlbg1.grid_forget()
		if self.lbBlp1!='':
			self.lbBlp1.grid_forget()
		self.lbBloodg1=Label(self.gframe1,text="Blood Group:",font=17,bg="violet",justify='center')
		self.lbBloodg1.grid(row=2,column=0,sticky=E)
		self.lbBlgg=Label(self.gframe1,text=self.blod,font=17,bg="violet",justify='center')
		self.lbBlgg.grid(row=2,column=1,sticky=W)				
		self.lbBlbg=Label(self.gframe1,text="Bags:",font=17,bg="violet",justify='center')
		self.lbBlbg.grid(row=2,column=2,sticky=E)	
		if self.bag_gg_g>=0:				
			self.lbBlbg1=Label(self.gframe1,text=self.bag_gg_g,font=17,bg="violet",justify='center')
			self.lbBlbg1.grid(row=2,column=3,sticky=W)
		else:
			self.lbBlbg1=Label(self.gframe1,text="Upadate not possible",font=17,bg="violet",justify='center')
			self.lbBlbg1.grid(row=2,column=3,sticky=W)			
		self.lbBlp=Label(self.gframe1,text="Price:",font=17,bg="violet",justify='center')
		self.lbBlp.grid(row=2,column=4,sticky=E)
		if self.pr__r__r>=0:	
			self.lbBlp1=Label(self.gframe1,text=self.pr__r__r,font=17,bg="violet",justify='center')
			self.lbBlp1.grid(row=2,column=5,sticky=W)
		else:
			self.lbBlp1=Label(self.gframe1,text='Update not possible',font=17,bg="violet",justify='center')
			self.lbBlp1.grid(row=2,column=5,sticky=W)	
	def Get_add(self):
		self.b_ggg=self.__bags.get()
		self.__bags.set("")
		conn=cx_Oracle.connect('Hos','hos','XE')
		
		#jd=to_date(self.__j_date,'YYYY-MM-DD')
		cur=conn.cursor()

		cur.execute('select Bags from blood where B_ID=:bid',{'bid':self.blod})
		rs = cur.fetchall()
		#print(i)
		if len(rs)!=0:
			if self.b_ggg>0:
				for i in rs:
					self.b_ggg=i[0]+self.b_ggg
					self.bag_gg_g=self.b_ggg
				cur=conn.cursor()
				cur.execute('UPDATE Blood SET bags = :bg WHERE B_ID =:bid',{'bg':self.b_ggg,'bid':self.blod})
				conn.commit()
				cur.close()
			else:
				self.bag_gg_g=-100
	
		conn.close()		
		self.Labelextra()
	def Get_del(self):
		self.b_ggg=self.__bags.get()
		self.__bags.set("")
		conn=cx_Oracle.connect('Hos','hos','XE')
		
		#jd=to_date(self.__j_date,'YYYY-MM-DD')
		cur=conn.cursor()

		cur.execute('select Bags from blood where B_ID=:bid',{'bid':self.blod})

		rs = cur.fetchall()
		#print(i)
		if len(rs)!=0:		
			print()
			if self.b_ggg>0:
				for i in rs:
					self.b_ggg=i[0]-self.b_ggg
					self.bag_gg_g=self.b_ggg
				if self.bag_gg_g>=0:
					cur=conn.cursor()
					cur.execute('UPDATE Blood SET bags = :bg WHERE B_ID =:bid',{'bg':self.b_ggg,'bid':self.blod})
					conn.commit()
		
					cur.close()
			else:
				self.bag_gg_g=-100
			
		conn.close()
		self.Labelextra()		
	def Change_pr(self):
		self.p__r=self.__pr.get()
		self.__pr.set("")
		conn=cx_Oracle.connect('Hos','hos','XE')
		
		#jd=to_date(self.__j_date,'YYYY-MM-DD')
		cur=conn.cursor()
		self.pr__r__r=self.p__r
		if self.pr__r__r>=0:
			cur.execute('UPDATE Blood SET PRICE_PER_BAG = :pr WHERE B_ID =:bid',{'pr':self.p__r,'bid':self.blod})
		conn.commit()
		cur.close()
	
		conn.close()	
		self.Labelextra()			
	def Label(self):
		self.lb1=Label(self.gframe1,text="SEARCH BLOOD",font=17,bg="violet",justify='center').grid(row=0,columnspan=3,sticky=W,pady=5)
		
		self.lbBloodg=Label(self.gframe1,text="Blood Group:",font=17,bg="violet",justify='center').grid(row=1,column=0,sticky=W)	
		self.lb2=Label(self.gframe1,text="UPDATE",font=17,bg="violet",justify='center').grid(row=3,columnspan=3,sticky=W,pady=5)
		self.lbbGB=Label(self.gframe1,text="Bags:",font=12,bg="violet",justify='center').grid(row=4,column=0,sticky=E,rowspan=2)		
		self.lbbGP=Label(self.gframe1,text="Price:",font=12,bg="violet",justify='center').grid(row=4,column=3,sticky=E,rowspan=2)	
		self.lb3=Label(self.gframe1,text="DONAR",font=17,bg="violet",justify='center').grid(row=6,columnspan=3,sticky=W,pady=5)	
		self.lbnm=Label(self.gframe1,text="Name:",font=12,bg="violet",justify='center').grid(row=7,column=0,sticky=E)
		self.lbcon=Label(self.gframe1,text="Contact NO:",font=12,bg="violet",justify='center').grid(row=7,column=2,sticky=E)
	def Option_men(self):
		#combobox self.scldpt options
		self.sclblood = ttk.Combobox(self.gframe1,values=self.options,textvariable=self.__blood).grid(row=1,column=1,sticky=W)
	def Variable(self):
		self.options=("A+","A-","AB+","AB-","B+","B-","O+","O-")
		self.__blood=StringVar(self.mas)
		self.__bags=IntVar(self.mas)
		self.__pr=IntVar(self.mas)	
		self.__dnm=StringVar(self.mas)
		self.__dcon=StringVar(self.mas)
		self.lbBlp1=''
		self.lbBlbg1=''
		self.lbBlgg=''
	def Entry(self):
		self.entybgb=Entry(self.gframe1,textvariable=self.__bags).grid(row=4,column=1,sticky=W,rowspan=2)
		self.entypr=Entry(self.gframe1,textvariable=self.__pr).grid(row=4,column=4,sticky=W,rowspan=2)
		self.entydnm=Entry(self.gframe1,textvariable=self.__dnm).grid(row=7,column=1,sticky=W)
		self.entydcon=Entry(self.gframe1,textvariable=self.__dcon).grid(row=7,column=3,sticky=W)
	def Add_donar(self):
		self.dddmmmnn=self.__dnm.get()
		self.dddcccconn=self.__dcon.get()
		self.__dnm.set("")
		self.__dcon.set("")
		pattern=re.compile("(01)?[0-9]{9}")
		pattern.match(self.dddcccconn)
		conn=cx_Oracle.connect('Hos','hos','XE')
		if(pattern.match(self.dddcccconn)):
			
			#jd=to_date(self.__j_date,'YYYY-MM-DD')
			cur=conn.cursor()
			cur.execute('insert into Blood_donnar(B_ID,D_ID,D_name,Contract_No) values(:b_ID,:did,:dn,:cn)',{'b_ID':self.blod,'did':self.dddmmmnn[0:3]+'_'+self.blod+'_'+self.dddcccconn,'dn':self.dddmmmnn,'cn':self.dddcccconn})
			conn.commit()
		
			rs = cur.fetchall()
			#print(i)
			if len(rs)!=0:	
				
				self.lbl=Label(self.gframe1,text="Entry success",font=17,bg="violet",justify='center').grid(row=8,columnspan=6)	
								
		
			cur.close()
	
			conn.close()	
		else:
			self.lbl=Label(self.gframe1,text="Contract No is not valid",font=17,bg="violet",justify='center').grid(row=8,columnspan=6)	
					
		
	def Button(self):
		self.but_search=Button(self.gframe1,text="Search",width=17,bd=4,bg='purple',fg ='white',command=self.Get_blg).grid(row=1,column=2,sticky=E)
		self.but_add=Button(self.gframe1,text="ADD",width=10,bd=4,bg='purple',fg ='white',command=self.Get_add).grid(row=4,column=2,sticky=W)
		self.but_del=Button(self.gframe1,text="DEL",width=10,bd=4,bg='purple',fg ='white',command=self.Get_del).grid(row=5,column=2,sticky=W)
		self.but_chn=Button(self.gframe1,text="CHANGE",width=10,bd=4,bg='purple',fg ='white',command=self.Change_pr).grid(row=4,column=5,sticky=E,rowspan=2)
		self.but_Add=Button(self.gframe1,text="ADD",width=10,bd=4,bg='purple',fg ='white',command=self.Add_donar).grid(row=7,column=4,sticky=E)
		self.but_ex=Button(self.gframe1,text="EXit",width=17,bd=4,bg='purple',fg ='white',command=self.Exit).grid(row=9,columnspan=6)
	def Exit(self):
		self.new_wd=Admin_menu(self.mas,self.nm)
		self.new_wd.Pack_all()  
class Attendance_menu(com_menu):
	def Pack_all(self):
		self.xdt=datetime.datetime.now()
		self.day=self.xdt.strftime("%d")
		self.mon=self.xdt.strftime("%b")
		self.year=self.xdt.strftime("%y")
		self.year=str(self.xdt.year)
		self.cdate=str(self.day)+'-'+str(self.mon)+'-'+self.year[-2:]
		print(self.cdate)
		self.mas.title("Attendance")	
		self.mas.geometry("1000x700")
		self.Variable()
		self.Grid()
		self.Label()
		self.Entry()
		self.Radio_but()
		self.Button()
		self.gframe.place(x=100,y=80)
		self.mas.mainloop()
	def Entry(self):
		self.entyid=Entry(self.gframe1,textvariable=self.__id).grid(row=0,column=1,sticky=W)
		self.entydt=Entry(self.gframe1,textvariable=self.__dt).grid(row=1,column=1,sticky=W)		
	def Variable(self):
		#self.options=("A+","A-","AB+","AB-","B+","B-","O+","O-")
		self.__id=StringVar(self.mas)
		self.__dt=StringVar(self.mas)
		self.__dt.set(self.cdate)
		self.__att=StringVar(self.mas)
	def Label(self):
		self.lbid=Label(self.gframe1,text="Employee Id:",font=12,bg="violet",justify='center').grid(row=0,column=0,sticky=E)
		self.lbdt=Label(self.gframe1,text="Date:",font=12,bg="violet",justify='center').grid(row=1,column=0,sticky=E)
		self.lbatt=Label(self.gframe1,text="Attendence:",font=12,bg="violet",justify='center').grid(row=2,column=0,sticky=E)
	def Button(self):

		self.but_add=Button(self.gframe1,text="ADD",width=10,bd=4,bg='purple',fg ='white',command=self.Get_dt).grid(row=5,column=1,columnspan=3,sticky=W)

		self.but_ex=Button(self.gframe1,text="EXit",width=17,bd=4,bg='purple',fg ='white',command=self.Exit).grid(row=7,columnspan=4)
	def Get_dt(self):
		self.idd_d=self.__id.get()
		self.dtt_t=self.__dt.get()
		self.atttt_t=self.__att.get()	
		self.__id.set("")
		self.__dt.set(self.cdate)
		self.__att.set("")
		conn=cx_Oracle.connect('Hos','hos','XE')
		cur=conn.cursor()
		cur.execute('select * from Doctor where E_ID=:eid',{'eid':self.idd_d})
		rs = cur.fetchall()
		if (len(rs)!=0):
			cur=conn.cursor()
			cur.execute('insert into Attendence(E_ID,date1,Attendence) values(:e_ID,:dt,:at)',{'e_ID':self.idd_d,'dt':self.dtt_t,'at':self.atttt_t})
			conn.commit()
		
			
				
			self.lbl=Label(self.gframe1,text="Entry success for "+self.idd_d+" Date:"+self.dtt_t,font=17,bg="violet",justify='center').grid(row=6,columnspan=4)	
			#self.mas.geometry("1000x700")
			#self.lbl=Label(self.gframe1,text="",font=17,bg="violet",justify='center').grid(row=6,columnspan=4)
								
		else: 
			self.lbl=Label(self.gframe1,text="Employee is not Available",font=17,bg="violet",justify='center').grid(row=6,columnspan=4)	
		cur.close()
	
		conn.close()
			
			
	def Exit(self):
		self.new_wd=Admin_menu(self.mas,self.nm)
		self.new_wd.Pack_all()   
	def Radio_but(self):
		self.R1 = Radiobutton(self.gframe1, text="Attend", variable=self.__att, value="A",font=14,bg="violet",justify='center',bd=0).grid(row=2,column=1,sticky=W)
		self.R2 = Radiobutton(self.gframe1, text="Not Attend", variable=self.__att, value="NA",font=14,bg="violet",justify='center',bd=0).grid(row=3,column=1,sticky=W)
		self.R3 = Radiobutton(self.gframe1, text="Vacation", variable=self.__att, value="V",font=14,bg="violet",justify='center',bd=0).grid(row=4,column=1,sticky=W)
class Schedule_set_menu(com_menu):
	def Pack_all(self,id1):
		self.xdt=datetime.datetime.now()
		self.day=self.xdt.strftime("%d")
		self.mon=self.xdt.strftime("%b")
		self.year=self.xdt.strftime("%y")
		self.year=str(self.xdt.year)
		self.cdate=str(self.day)+'-'+str(self.mon)+'-'+self.year[-2:]
		self.__id=id1
		print(self.__id)
		self.mas.title("Schedule")	
		self.mas.geometry("1000x700")
		self.Variable()
		
		self.Grid()
		self.Option_men()
		self.Label()
		self.Entry()
		self.Button()
		self.gframe.place(x=100,y=80)
		self.mas.mainloop()
	def Get_dt(self):
		self.dt=self.__dt.get()
		self.__dt.set(self.cdate)
		self.taskk1=self.__task1.get()
		self.taskk2=self.__task2.get()
		self.taskk3=self.__task3.get()
		self.taskk4=self.__task4.get()
		self.taskk5=self.__task5.get()
		self.__task1.set("")
		self.__task2.set("")
		self.__task3.set("")
		self.__task4.set("")
		self.__task5.set("")

		if self.lbw!='':
			self.lbw.grid_forget()		
		conn=cx_Oracle.connect('Hos','hos','XE')
		cur=conn.cursor()
		cur.execute('select * from Schedule where E_ID=:eid and date1=:dt',{'eid':self.__id,'dt':self.dt})
		rs = cur.fetchall()
		if(len(rs)!=0):
			if(self.taskk1!=""):
				print(self.dt)
				
				#cur.close()
				#jd=to_date(self.__j_date,'YYYY-MM-DD')
				cur=conn.cursor()

				cur.execute('select task from Schedule where time=:tt and E_ID=:eid and date1=:dt',{'eid':self.__id,'dt':self.dt,'tt':'9Am-12Noon'})
				rs1 = cur.fetchall()
				if len(rs1)!=0:

				
					for i in rs1:	
						if i[0]=="Nothing" or i[0]=="Office":
							
							cur1=conn.cursor()
							cur1.execute('UPDATE Schedule SET TASK = :ts WHERE time=:tt and E_ID=:eid and date1=:dt',{'ts':self.taskk1,'eid':self.__id,'dt':self.dt,'tt':'9Am-12Noon'})
							conn.commit()
							self.lbw=Label(self.gframe1,text='Change Success',font=12,bg="violet",justify='center')				
							self.lbw.grid(row=9,columnspan=4)
						else:
							self.lbw=Label(self.gframe1,text='op can not be changed at 9Am-12Noon ',font=12,bg="violet",justify='center')	
							self.lbw.grid(row=9,columnspan=4)											
				cur.close()
		
				#conn.close()	
			if(self.taskk2!=""):
				print(self.dt)
				
				#cur.close()
				#jd=to_date(self.__j_date,'YYYY-MM-DD')
				cur=conn.cursor()
				
				cur.execute('select task from Schedule where time=:tt and E_ID=:eid and date1=:dt',{'eid':self.__id,'dt':self.dt,'tt':'12Noon-3Pm'})
				rs1 = cur.fetchall()
				if len(rs1)!=0:
				
					for i in rs1:	
						if i[0]=="Nothing" or i[0]=="Office":
							
							cur1=conn.cursor()
							cur1.execute('UPDATE Schedule SET TASK = :ts WHERE time=:tt and E_ID=:eid and date1=:dt',{'ts':self.taskk2,'eid':self.__id,'dt':self.dt,'tt':'12Noon-3Pm'})
							conn.commit()
							self.lbw=Label(self.gframe1,text='Change Success',font=12,bg="violet",justify='center')				
							self.lbw.grid(row=9,columnspan=4)
						else:
							self.lbw=Label(self.gframe1,text='op can not be changed at 12Noon-3Pm ',font=12,bg="violet",justify='center')
							self.lbw.grid(row=9,columnspan=4)											
				cur.close()
		
				#conn.close()	
			if(self.taskk3!=""):
				print(self.dt)
				
				#cur.close()
				#jd=to_date(self.__j_date,'YYYY-MM-DD')
				cur=conn.cursor()

				cur.execute('select task from Schedule where time=:tt and E_ID=:eid and date1=:dt',{'eid':self.__id,'dt':self.dt,'tt':'3Pm-6Pm'})
				rs1 = cur.fetchall()
				if len(rs1)!=0:

				
					for i in rs1:	
						if i[0]=="Nothing" or i[0]=="Office":
							
							cur1=conn.cursor()
							cur1.execute('UPDATE Schedule SET TASK = :ts WHERE time=:tt and E_ID=:eid and date1=:dt',{'ts':self.taskk3,'eid':self.__id,'dt':self.dt,'tt':'3Pm-6Pm'})
							conn.commit()
							self.lbw=Label(self.gframe1,text='Change Success',font=12,bg="violet",justify='center')				
							self.lbw.grid(row=9,columnspan=4)
						else:
							self.lbw=Label(self.gframe1,text='op can not be changed at 3Pm-6Pm',font=12,bg="violet",justify='center')		
							self.lbw.grid(row=9,columnspan=4)										
				cur.close()
		
				#conn.close()	
			if(self.taskk4!=""):
				print(self.dt)
				
				#cur.close()
				#jd=to_date(self.__j_date,'YYYY-MM-DD')
				cur=conn.cursor()

				cur.execute('select task from Schedule where time=:tt and E_ID=:eid and date1=:dt',{'eid':self.__id,'dt':self.dt,'tt':'6Pm-9Pm'})
				rs1 = cur.fetchall()
				if len(rs1)!=0:

				
					for i in rs1:	
						if i[0]=="Nothing" or i[0]=="Office":
							
							cur1=conn.cursor()
							cur1.execute('UPDATE Schedule SET TASK = :ts WHERE time=:tt and E_ID=:eid and date1=:dt',{'ts':self.taskk4,'eid':self.__id,'dt':self.dt,'tt':'6Pm-9Pm'})
							conn.commit()
							self.lbw=Label(self.gframe1,text='Change Success',font=12,bg="violet",justify='center')				
							self.lbw.grid(row=9,columnspan=4)
						else:
							self.lbw=Label(self.gframe1,text='op can not be changed at 6Pm-9Pm',font=12,bg="violet",justify='center')
						self.lbw.grid(row=9,columnspan=4)											
				cur.close()
		
				#conn.close()		
			if(self.taskk5!=""):
				print(self.dt)
				#cur.close()
			
				#jd=to_date(self.__j_date,'YYYY-MM-DD')
				cur=conn.cursor()

				cur.execute('select task from Schedule where time=:tt and E_ID=:eid and date1=:dt',{'eid':self.__id,'dt':self.dt,'tt':'9Pm-12Midnight'})
				rs1 = cur.fetchall()
				if len(rs1)!=0:
				
					for i in rs1:	
						if i[0]=="Nothing" or i[0]=="Office":
							
							cur1=conn.cursor()
							cur1.execute('UPDATE Schedule SET TASK = :ts WHERE time=:tt and E_ID=:eid and date1=:dt',{'ts':self.taskk5,'eid':self.__id,'dt':self.dt,'tt':'9Pm-12Midnight'})
							conn.commit()
							self.lbw=Label(self.gframe1,text='Change Success',font=12,bg="violet",justify='center')				
							self.lbw.grid(row=9,columnspan=4)
						else:
							self.lbw=Label(self.gframe1,text='op can not be changed at 9Pm-12Midnight',font=12,bg="violet",justify='center')				
							self.lbw.grid(row=9,columnspan=4)
				cur.close()
	
				#conn.close()					

		else:
			cur.close()
			cur=conn.cursor()
			cur.execute('insert into Schedule(E_ID,date1,time,Task) values(:e_ID,:dt,:tt,:ts)',{'e_ID':self.__id,'dt':self.dt,'tt':'9Am-12Noon','ts':'Office'})
			conn.commit()	
			cur.execute('insert into Schedule(E_ID,date1,time,Task) values(:e_ID,:dt,:tt,:ts)',{'e_ID':self.__id,'dt':self.dt,'tt':'12Noon-3Pm','ts':'Office'})
			conn.commit()		
			cur.execute('insert into Schedule(E_ID,date1,time,Task) values(:e_ID,:dt,:tt,:ts)',{'e_ID':self.__id,'dt':self.dt,'tt':'3Pm-6Pm','ts':'Nothing'})
			conn.commit()
			cur.execute('insert into Schedule(E_ID,date1,time,Task) values(:e_ID,:dt,:tt,:ts)',{'e_ID':self.__id,'dt':self.dt,'tt':'6Pm-9Pm','ts':'Nothing'})
			conn.commit()											
			cur.execute('insert into Schedule(E_ID,date1,time,Task) values(:e_ID,:dt,:tt,:ts)',{'e_ID':self.__id,'dt':self.dt,'tt':'9Pm-12Midnight','ts':'Nothing'})
			conn.commit()
			cur.close()
	
			
			self.lbw=Label(self.gframe1,text='Please Change you schedule again',font=12,bg="violet",justify='center')				
			self.lbw.grid(row=9,columnspan=4)
		conn.close()	
		
		
	def Variable(self):	
		self.lbw=''
		self.options=("Office","Nothing")
		self.__task1=StringVar(self.mas)
		self.__task2=StringVar(self.mas)
		self.__task3=StringVar(self.mas)
		self.__task4=StringVar(self.mas)
		self.__task5=StringVar(self.mas)	
		self.__dt=StringVar(self.mas)
		self.__dt.set(self.cdate)
	def Option_men(self):
		#combobox self.scldpt options
		self.scl9_12t = ttk.Combobox(self.gframe1,values=self.options,textvariable=self.__task1).grid(row=4,column=1,sticky=E)
		self.scl12_3t = ttk.Combobox(self.gframe1,values=self.options,textvariable=self.__task2).grid(row=5,column=1,sticky=E)
		self.scl3_6t = ttk.Combobox(self.gframe1,values=self.options,textvariable=self.__task3).grid(row=6,column=1,sticky=E)
		self.scl6_9t = ttk.Combobox(self.gframe1,values=self.options,textvariable=self.__task4).grid(row=7,column=1,sticky=E)
		self.scl9_12t = ttk.Combobox(self.gframe1,values=self.options,textvariable=self.__task5).grid(row=8,column=1,sticky=E)

	def Label(self):
		self.lbnm=Label(self.gframe1,text="Name:",font=12,bg="violet",justify='center').grid(row=0,column=0,sticky=E)
		self.lbnmv=Label(self.gframe1,text=self.__id,font=12,bg="violet",justify='center').grid(row=0,column=1,sticky=W)
		self.lbdt=Label(self.gframe1,text="Date:",font=12,bg="violet",justify='center').grid(row=1,column=0,sticky=E)
		self.lbTime=Label(self.gframe1,text="Time",font=12,bg="violet",justify='center').grid(row=3,column=0,sticky=E)
		self.lbtask=Label(self.gframe1,text="Task",font=12,bg="violet",justify='center').grid(row=3,column=1,sticky=W)
		self.lb9_12=Label(self.gframe1,text="9AM-12Noon",font=12,bg="violet",justify='center').grid(row=4,column=0,sticky=E)
		self.lb12_3=Label(self.gframe1,text="12Noon-3PM",font=12,bg="violet",justify='center').grid(row=5,column=0,sticky=E)
		self.lb3_6=Label(self.gframe1,text="3PM-6PM",font=12,bg="violet",justify='center').grid(row=6,column=0,sticky=E)
		self.lb6_9=Label(self.gframe1,text="6PM-9PM",font=12,bg="violet",justify='center').grid(row=7,column=0,sticky=E)
		self.lb9_12=Label(self.gframe1,text="9PM-12Midnight",font=12,bg="violet",justify='center').grid(row=8,column=0,sticky=E)

	def Entry(self):

		self.entydt=Entry(self.gframe1,textvariable=self.__dt).grid(row=1,column=1,sticky=W)	
	def Button(self):

		self.but_add=Button(self.gframe1,text="CHANGE",width=10,bd=4,bg='purple',fg ='white',command=self.Get_dt).grid(row=2,column=1,sticky=W)

		self.but_ex=Button(self.gframe1,text="EXit",width=17,bd=4,bg='purple',fg ='white',command=self.Exit).grid(row=10,columnspan=4)
	def Exit(self):
		self.new_wd=Doc_menu(self.mas,self.nm)
		self.new_wd.Pack_all()   
class Schedule_menu(com_menu):
	def Pack_all(self,id1):
		self.xdt=datetime.datetime.now()
		self.day=self.xdt.strftime("%d")
		self.mon=self.xdt.strftime("%b")
		self.year=self.xdt.strftime("%y")
		self.year=str(self.xdt.year)
		self.cdate=str(self.day)+'-'+str(self.mon)+'-'+self.year[-2:]
		self.__id=id1
		print(self.__id)
		self.mas.title("Schedule")	
		self.mas.geometry("1000x700")
		self.Variable()
		self.Grid()
		self.Label()
		self.Entry()
		self.Button()
		self.gframe.place(x=100,y=80)
		self.mas.mainloop()
	def Get_dt(self):
		self.dt=self.__dt.get()
		self.__dt.set(self.cdate)
		if self.lbw!='':
			self.lbw.grid_forget()
		if self.lb9_12t!='':
			self.lb9_12t.grid_forget()
		if self.lb12_3t!='':
			self.lb12_3t.grid_forget()
		if self.lb3_6t!='':
			self.lb3_6.grid_forget()
		if self.lb6_9t!='':
			self.lb6_9t.grid_forget()
		if self.lb9_12t!='':
			self.lb9_12t.grid_forget()
		conn=cx_Oracle.connect('Hos','hos','XE')
		
		#jd=to_date(self.__j_date,'YYYY-MM-DD')
		cur=conn.cursor()

		cur.execute('select time,task from Schedule where E_ID=:eid and date1=:dt',{'eid':self.__id,'dt':self.dt})
		rs = cur.fetchall()
		print(rs)
		if (len(rs)!=0):

			
			for i in rs:	
				print(i)
				self.time=i[0]
				self.task=i[1]
				if self.time=='9Am-12Noon':

					self.lb9_12t=Label(self.gframe1,text=self.task,font=12,bg="violet",justify='center')
					self.lb9_12t.grid(row=4,column=1,sticky=E)
				elif self.time=='12Noon-3Pm':
					self.lb12_3t=Label(self.gframe1,text=self.task,font=12,bg="violet",justify='center')
					self.lb12_3t.grid(row=5,column=1,sticky=E)
				elif self.time=='3Pm-6Pm':
					self.lb3_6t=Label(self.gframe1,text=self.task,font=12,bg="violet",justify='center')
					self.lb3_6t.grid(row=6,column=1,sticky=E)
				elif self.time=='6Pm-9Pm':
					self.lb6_9t=Label(self.gframe1,text=self.task,font=12,bg="violet",justify='center')
					self.lb6_9t.grid(row=7,column=1,sticky=E)
				elif self.time=='9Pm-12Midnight':
					self.lb9_12t=Label(self.gframe1,text=self.task,font=12,bg="violet",justify='center')
					self.lb9_12t.grid(row=8,column=1,sticky=E)
		else:
			self.lbw=Label(self.gframe1,text='Enter Data is not a date or it is not available',font=12,bg="violet",justify='center')
			self.lbw.grid(row=9,columnspan=4)		
					
		cur.close()
	
		conn.close()
		self.__dt.set("")

	def Variable(self):		
		self.__dt=StringVar(self.mas)
		self.__dt.set(self.cdate)
		self.lbw=''
		self.lb9_12t=''
		self.lb12_3t=''
		self.lb3_6t=''
		self.lb6_9t=''
		self.lb9_12t=''
		
	def Label(self):
		self.lbnm=Label(self.gframe1,text="Name:",font=12,bg="violet",justify='center').grid(row=0,column=0,sticky=E)
		self.lbnmv=Label(self.gframe1,text=self.__id,font=12,bg="violet",justify='center').grid(row=0,column=1,sticky=W)
		self.lbdt=Label(self.gframe1,text="Date:",font=12,bg="violet",justify='center').grid(row=1,column=0,sticky=E)
		self.lbTime=Label(self.gframe1,text="Time",font=12,bg="violet",justify='center').grid(row=3,column=0,sticky=E)
		self.lbtask=Label(self.gframe1,text="Task",font=12,bg="violet",justify='center').grid(row=3,column=1,sticky=W)
		self.lb9_12=Label(self.gframe1,text="9AM-12Noon",font=12,bg="violet",justify='center').grid(row=4,column=0,sticky=E)
		self.lb12_3=Label(self.gframe1,text="12Noon-3PM",font=12,bg="violet",justify='center').grid(row=5,column=0,sticky=E)
		self.lb3_6=Label(self.gframe1,text="3PM-6PM",font=12,bg="violet",justify='center').grid(row=6,column=0,sticky=E)
		self.lb6_9=Label(self.gframe1,text="6PM-9PM",font=12,bg="violet",justify='center').grid(row=7,column=0,sticky=E)
		self.lb9_12=Label(self.gframe1,text="9PM-12Midnight",font=12,bg="violet",justify='center').grid(row=8,column=0,sticky=E)
	def Entry(self):

		self.entydt=Entry(self.gframe1,textvariable=self.__dt).grid(row=1,column=1,sticky=W)	
	def Button(self):

		self.but_add=Button(self.gframe1,text="CHECK",width=10,bd=4,bg='purple',fg ='white',command=self.Get_dt).grid(row=2,column=1,sticky=W)

		self.but_ex=Button(self.gframe1,text="EXit",width=17,bd=4,bg='purple',fg ='white',command=self.Exit).grid(row=10,columnspan=4)
	def Exit(self):
		self.new_wd=Doc_menu(self.mas,self.nm)
		self.new_wd.Pack_all()   
class Patient_record_menu(com_menu):
	def Pack_all(self,id1):
		self.__id=id1
		print(self.__id)
		self.mas.title("Patient Record")	
		self.mas.geometry("1000x700")
		self.Grid()
		
		self.Variable()
		
		self.Label()
		self.Entry()
		self.Button()
		self.gframe.place(x=100,y=80)
		self.mas.mainloop()

	def Variable(self):		
		self.lbnam_e=''
		self.lbage_e=''
		self.lbgen_e=''
		self.lbad_da=''
		self.lbsic_e=''
		self.lward_e=''
		self.lbopre_e=''
		self.lbopda_e=''
		self.lbopti_e=''
		self.lboprm_e=''
		self.lbdoc_e=''
		self.lbf=''
		self.__pid=StringVar(self.mas)
	def Label(self):
		#self.lbnm=Label(self.gframe1,text="Name:",font=12,bg="violet",justify='center').grid(row=1,column=0,sticky=E)
		self.lbid=Label(self.gframe1,text="PID:",font=12,bg="violet",justify='center').grid(row=2,column=0,sticky=E)
		self.lbnmp=Label(self.gframe1,text="Name:",font=12,bg="violet",justify='center').grid(row=3,column=0,sticky=E)
		self.lbgen=Label(self.gframe1,text="Gender:",font=12,bg="violet",justify='center').grid(row=4,column=0,sticky=E)
		self.lbage=Label(self.gframe1,text="Age:",font=12,bg="violet",justify='center').grid(row=5,column=0,sticky=E)
		self.lbadmd=Label(self.gframe1,text="Admission Date:",font=12,bg="violet",justify='center').grid(row=6,column=0,sticky=E)
		self.lbscp=Label(self.gframe1,text="Sickness:",font=12,bg="violet",justify='center').grid(row=7,column=0,sticky=E)
		self.lbnward=Label(self.gframe1,text="Ward:",font=12,bg="violet",justify='center').grid(row=8,column=0,sticky=E)
		self.lbopp=Label(self.gframe1,text="Operation:",font=12,bg="violet",justify='center').grid(row=9,column=0,sticky=E)
		self.lbopdp=Label(self.gframe1,text="operation Date:",font=12,bg="violet",justify='center').grid(row=10,column=0,sticky=E)
		self.lbopti=Label(self.gframe1,text="operation time:",font=12,bg="violet",justify='center').grid(row=11,column=0,sticky=E)
		self.lboproom=Label(self.gframe1,text="operation Room:",font=12,bg="violet",justify='center').grid(row=12,column=0,sticky=E)
		self.lbmp=Label(self.gframe1,text="Doctor:",font=12,bg="violet",justify='center').grid(row=13,column=0,sticky=E)
	
	def Entry(self):

		self.entypid=Entry(self.gframe1,textvariable=self.__pid).grid(row=2,column=1,sticky=W)	
	def Button(self):

		#self.but_lp=Button(self.gframe1,text="List Of All Patient",width=17,bd=4,bg='purple',fg ='white').grid(row=0,columnspan=3)
		self.but_src=Button(self.gframe1,text="SEARCH",width=12,bd=4,bg='purple',fg ='white',command=self.Get_info).grid(row=2,column=2)
		self.but_ex=Button(self.gframe1,text="EXit",width=17,bd=4,bg='purple',fg ='white',command=self.Exit).grid(row=16,columnspan=3)
	def Get_info(self):
		self.pidd=self.__pid.get()
		self.__pid.set("")				
		
		if self.lbnam_e!='':
			self.lbnam_e.grid_forget()
		if self.lbage_e!='':
			self.lbage_e.grid_forget()
		if self.lbgen_e!='':
			self.lbgen_e.grid_forget()
		if self.lbad_da!='':
			self.lbad_da.grid_forget()
		if self.lbsic_e!='':
			self.lbsic_e.grid_forget()
		if self.lward_e!='':
			self.lward_e.grid_forget()
		if self.lbopre_e!='':
			self.lbopre_e.grid_forget()
		if self.lbopda_e!='':
			self.lbopda_e.grid_forget()
		if self.lbopti_e!='':
			self.lbopti_e.grid_forget()
		if self.lboprm_e!='':
			self.lboprm_e.grid_forget()
		if self.lbdoc_e!='':
			self.lbdoc_e.grid_forget()		
		if self.lbf!='':
			self.lbf.grid_forget()
		pattern=re.compile("(01)?[0-9]{9}")	
		if(pattern.match(self.pidd[3:14])):
			conn=cx_Oracle.connect('Hos','hos','XE')
			cur=conn.cursor()
			cur.execute('select * from Patient where PID=:pi',{'pi':self.pidd})

			conn.commit()	
			cur1=cur
			rs = cur.fetchall()
			cur=cur1
			print(rs)
			if(len(rs)!=0):	
				print(cur)
				for i in rs:
					print(i)
					
					self.lbnam_e=Label(self.gframe1,text=i[0],font=14,bg="violet",justify='center')
					self.lbnam_e.grid(row=3,column=1,sticky=W)
					self.lbage_e=Label(self.gframe1,text=i[2],font=14,bg="violet",justify='center')
					self.lbage_e.grid(row=5,column=1,sticky=W)
					self.lbgen_e=Label(self.gframe1,text=i[3],font=14,bg="violet",justify='center')
					self.lbgen_e.grid(row=4,column=1,sticky=W)
					self.lbad_da=Label(self.gframe1,text=i[4],font=14,bg="violet",justify='center')
					self.lbad_da.grid(row=6,column=1,sticky=W)
					self.lbsic_e=Label(self.gframe1,text=i[5],font=14,bg="violet",justify='center')
					self.lbsic_e.grid(row=7,column=1,sticky=W)
					self.lward_e=Label(self.gframe1,text=i[7],font=14,bg="violet",justify='center')
					self.lward_e.grid(row=8,column=1,sticky=W)
					self.lbopre_e=Label(self.gframe1,text=i[10],font=14,bg="violet",justify='center')
					self.lbopre_e.grid(row=9,column=1,sticky=W)
					if i[9]=="Required":
						
						self.lbopda_e=Label(self.gframe1,text=i[11],font=14,bg="violet",justify='center')
						self.lbopda_e.grid(row=10,column=1,sticky=W)
						self.lbopti_e=Label(self.gframe1,text=i[12],font=14,bg="violet",justify='center')
						self.lbopti_e.grid(row=11,column=1,sticky=W)
						self.lboprm_e=Label(self.gframe1,text=i[13],font=14,bg="violet",justify='center')
						self.lboprm_e.grid(row=12,column=1,sticky=W)
					self.lbdoc_e=Label(self.gframe1,text=i[9],font=14,bg="violet",justify='center')
					self.lbdoc_e.grid(row=13,column=1,sticky=W)
				cur.close()

			else:
				self.lbf=Label(self.gframe1,text="Patient not found.",font=14,bg="violet",justify='center')
				self.lbf.grid(row=14,columnspan=3)
			conn.close()
	def Exit(self):
		self.new_wd=Doc_menu(self.mas,self.nm)
		self.new_wd.Pack_all()   	
class Patient_repord_menu(com_menu):
	def Pack_all(self,id1):
		self.__id=id1
		print(self.__id)
		self.mas.title("Patient Repord")	
		self.mas.geometry("1000x700")
		self.Grid()
		
		self.Variable()
		
		self.Label()
		self.Entry()
		self.Button()
		self.gframe.place(x=100,y=80)
		self.mas.mainloop()

	def Variable(self):	
		self.lbf=''	
		self.lbnam_e=''
		self.lbage_e=''
		self.lbgen_e=''
		self.lbbgl_e=''
		self.lbrbc_e=''
		self.lbwbc_e=''
		self.lbhsag_e=''
		self.lbheart_e=''
		self.__pid=StringVar(self.mas)
	def Label(self):
		#self.lbnm=Label(self.gframe1,text="Name:",font=12,bg="violet",justify='center').grid(row=1,column=0,sticky=E)
		self.lbid=Label(self.gframe1,text="Contact NO:",font=12,bg="violet",justify='center').grid(row=0,column=0,sticky=E)
		self.lbnmp=Label(self.gframe1,text="Name:",font=12,bg="violet",justify='center').grid(row=1,column=0,sticky=E)
		self.lbnag=Label(self.gframe1,text="Age:",font=12,bg="violet",justify='center').grid(row=2,column=0,sticky=E)
		self.lbngen=Label(self.gframe1,text="Gender:",font=12,bg="violet",justify='center').grid(row=3,column=0,sticky=E)
		#self.lbscp=Label(self.gframe1,text="Sickness:",font=12,bg="violet",justify='center').grid(row=4,column=0,sticky=E)
		self.lbnbg=Label(self.gframe1,text="Blood Group:",font=12,bg="violet",justify='center').grid(row=4,column=0,sticky=E)
		self.lbrbc=Label(self.gframe1,text="RBC:",font=12,bg="violet",justify='center').grid(row=5,column=0,sticky=E)
		self.lbwbc=Label(self.gframe1,text="WBC:",font=12,bg="violet",justify='center').grid(row=6,column=0,sticky=E)
		self.lbAg=Label(self.gframe1,text="HBsAg:",font=12,bg="violet",justify='center').grid(row=7,column=0,sticky=E)
		self.lbht=Label(self.gframe1,text="Heart:",font=12,bg="violet",justify='center').grid(row=8,column=0,sticky=E)	
	def Entry(self):

		self.entypid=Entry(self.gframe1,textvariable=self.__pid).grid(row=0,column=1,sticky=W)	
	def Button(self):

		#self.but_lp=Button(self.gframe1,text="List Of All Patient",width=17,bd=4,bg='purple',fg ='white').grid(row=0,columnspan=3)
		self.but_src=Button(self.gframe1,text="SEARCH",width=12,bd=4,bg='purple',fg ='white',command=self.Get_rp).grid(row=0,column=2)
		self.but_ex=Button(self.gframe1,text="EXit",width=17,bd=4,bg='purple',fg ='white',command=self.Exit).grid(row=10,columnspan=3)
		
	def Get_rp(self):
		self.con=self.__pid.get()
		self.__pid.set("")
		if self.lbnam_e!='':
			self.lbnam_e.grid_forget()
		if self.lbage_e!='':
			self.lbage_e.grid_forget()
		if self.lbgen_e!='':
			self.lbgen_e.grid_forget()
		if self.lbbgl_e!='':
			self.lbbgl_e.grid_forget()
		if self.lbrbc_e!='':
			self.lbrbc_e.grid_forget()
		if self.lbwbc_e!='':
			self.lbwbc_e.grid_forget()
		if self.lbhsag_e!='':
			self.lbhsag_e.grid_forget()
		if self.lbheart_e!='':
			self.lbheart_e.grid_forget()
		if self.lbf!='':
			self.lbf.grid_forget()
		pattern=re.compile("(01)?[0-9]{9}")	
		if(pattern.match(self.con)):
			conn=cx_Oracle.connect('Hos','hos','XE')
			cur=conn.cursor()
			cur.execute('select NAME,Age,Gender,BG,RBC,WBC,HBsAg,Heart from Pathology_report where Contact_No=:bco and E_ID=:dc',{'bco':self.con,'dc':self.nm})

			conn.commit()	
			cur1=cur
			rs = cur.fetchall()
			cur=cur1
			print(rs)
			if(len(rs)!=0):	
				print(cur)
				for i in rs:
					print(i)
					
					self.lbnam_e=Label(self.gframe1,text=i[0],font=14,bg="violet",justify='center')
					self.lbnam_e.grid(row=1,column=1,sticky=W)
					self.lbage_e=Label(self.gframe1,text=i[1],font=14,bg="violet",justify='center')
					self.lbage_e.grid(row=2,column=1,sticky=W)
					self.lbgen_e=Label(self.gframe1,text=i[2],font=14,bg="violet",justify='center')
					self.lbgen_e.grid(row=3,column=1,sticky=W)
					self.lbbgl_e=Label(self.gframe1,text=i[3],font=14,bg="violet",justify='center')
					self.lbbgl_e.grid(row=4,column=1,sticky=W)
					self.lbrbc_e=Label(self.gframe1,text=i[4],font=14,bg="violet",justify='center')
					self.lbrbc_e.grid(row=5,column=1,sticky=W)
					self.lbwbc_e=Label(self.gframe1,text=i[5],font=14,bg="violet",justify='center')
					self.lbwbc_e.grid(row=6,column=1,sticky=W)
					self.lbhsag_e=Label(self.gframe1,text=i[6],font=14,bg="violet",justify='center')
					self.lbhsag_e.grid(row=7,column=1,sticky=W)
					self.lbheart_e=Label(self.gframe1,text=i[7],font=14,bg="violet",justify='center')
					self.lbheart_e.grid(row=8,column=1,sticky=W)
				cur.close()

			else:
				self.lbf=Label(self.gframe1,text="Contact NO not found.",font=14,bg="violet",justify='center')
				self.lbf.grid(row=9,columnspan=3)
			conn.close()
		else:
			self.lbf=Label(self.gframe1,text="Invalid Contact NO.",font=14,bg="violet",justify='center')
			self.lbf.grid(row=9,columnspan=3)						

	def Exit(self):
		self.new_wd=Doc_menu(self.mas,self.nm)
		self.new_wd.Pack_all()   
class Ambulance_menu(com_menu):	
	def Pack_all(self):
		#self.m=-1
		self.xdt=datetime.datetime.now()
		self.day=self.xdt.strftime("%d")
		self.mon=self.xdt.strftime("%b")
		self.year=self.xdt.strftime("%y")
		self.year=str(self.xdt.year)
		self.cdate=str(self.day)+'-'+str(self.mon)+'-'+self.year[-2:]
		print(self.cdate)
		self.mas.title("Ambulance")	
		self.mas.geometry("1000x700")
		self.Variable()
		self.Avaibility()
		self.NotAvaibility()
		self.Grid()
		self.Label()
		self.Option_men()
		self.Entry()	
		self.Button()
		self.Button_am_re()
		self.gframe.configure(bd=5)
		self.gframe.place(x=100,y=80)
		self.mas.mainloop()
	def Label(self):
		self.lb1=Label(self.gframe1,text="Ambulance Reserve",font=17,bg="violet",justify='center').grid(row=0,columnspan=3,sticky=W,pady=5)
		
		self.lbAmbu1=Label(self.gframe1,text="Ambulance:",font=17,bg="violet",justify='center').grid(row=1,column=0,sticky=E)
		self.lbAmb1=Label(self.gframe1,text=self.__am1,font=17,bg="violet",justify='center')
		self.lbAmb1.grid(row=1,column=1,sticky=W)
		if self.__am1!='':
			self.lbus=Label(self.gframe1,text="Name:",font=17,pady=5,bg="violet",justify='center')
			self.lbus.grid(row=2,column=0,sticky=E)	
			self.lbcon=Label(self.gframe1,text="Contact No:",font=17,pady=5,bg="violet",justify='center')
			self.lbcon.grid(row=3,column=0,sticky=E)
			self.lbadd=Label(self.gframe1,text="Address:",font=17,pady=5,bg="violet",justify='center')
			self.lbadd.grid(row=4,column=0,sticky=E)
		else:
			if self.lbus!='':
				self.lbus.grid_forget()
				self.lbcon.grid_forget()
				self.lbadd.grid_forget()		
		self.lb2=Label(self.gframe2,text="Ambulance Reset",font=17,bg="violet",justify='center').grid(row=0,columnspan=3,sticky=W,pady=5)
		self.lbAmbu2=Label(self.gframe2,text="Ambulance:",font=17,bg="violet",justify='center').grid(row=1,column=0,sticky=E)
	def Variable(self):
		self.options1=[]
		self.options2=[]
		self.__am1=''
		self.lbus=''
		self.lbconf=''
		self.lbcon=''
		self.lbadd=''
		self.entynm=''
		self.entycon=''
		self.entyadd=''
		self.but_Reserve=''
		self.but_ch=''
		self.__am2=StringVar(self.mas)
		self.__name=StringVar(self.mas)
		self.__con=StringVar(self.mas)
		self.__add=StringVar(self.mas)
		#self.__blood=StringVar(self.mas)
		#self.__bags=IntVar(self.mas)	
	def Avaibility(self):
			conn=cx_Oracle.connect('Hos','hos','XE')
			cur=conn.cursor()
			cur.execute('select A_ID,Cost from Ambulance where Avaibility=:av',{'av':'Yes'})
			for i in cur:	
				self.options1.append(i[0])
				self.costc=i[1]

			conn.commit()	
			cur.close()
			conn.close()
			self.__am1=random.choice(self.options1)	
	def NotAvaibility(self):
			conn=cx_Oracle.connect('Hos','hos','XE')
			cur=conn.cursor()
			cur.execute('select A_ID from Ambulance where Avaibility=:av',{'av':'No'})
			for i in cur:	
				self.options2.append(i[0])
				#self.costc=i[1]

			conn.commit()	
			cur.close()
			conn.close()
			#self.__am1=random.choice(self.options1)
	def Change_dt(self):
		self.amc=self.__am2.get()	
		self.__am2.set("")
		conn=cx_Oracle.connect('Hos','hos','XE')
		cur=conn.cursor()
			
		cur.execute('UPDATE Ambulance SET Avaibility = :av WHERE A_ID=:ai',{'av':'Yes','ai':self.amc})
		conn.commit()
		cur.close()
		conn.close()
		self.Reeset()
				
	def Entry(self):
		if self.__am1!='':
			self.entynm=Entry(self.gframe1,textvariable=self.__name)
			self.entynm.grid(row=2,column=1,sticky=W)
			self.entycon=Entry(self.gframe1,textvariable=self.__con)
			self.entycon.grid(row=3,column=1,sticky=W)	
			self.entyadd=Entry(self.gframe1,textvariable=self.__add)
			self.entyadd.grid(row=4,column=1,sticky=W)	
		else:
			if self.lbus!='':
				self.entynm.grid_forget()
				self.entycon.grid_forget()
				self.entyadd.grid_forget()
	def Option_men(self):
		#combobox self.scldpt options
		#self.sclAmbu = ttk.Combobox(self.gframe1,values=self.options1,textvariable=self.__am1).grid(row=1,column=1,sticky=W)
		self.sclAmbu1 = ttk.Combobox(self.gframe2,values=self.options2,textvariable=self.__am2).grid(row=1,column=1,sticky=W)
	def Get_dt(self):
		self.nam=self.__name.get()
		self.cont=self.__con.get()
		self.addr=self.__add.get()
		self.__name.set("")
		self.__con.set("")
		self.__add.set("")
		pattern=re.compile("(01)?[0-9]{9}")
		if self.lbconf!='':
			self.lbconf.grid_forget()
		if (pattern.match(self.cont)):
			

			conn=cx_Oracle.connect('Hos','hos','XE')
			cur1=conn.cursor()
			print(self.nam,' ',self.cont,' ',self.__am1,' ',self.cdate,' ',self.costc,' ',self.addr)
			#cur.execute('insert into Doctor(E_ID,DEPT,RANK1) values(:E_ID,:DEPT,:RANK)',{'E_ID':self.id,'DEPT':self.department,'RANK':self.rank})
			cur1.execute('insert into Ambulance_reserve(Name,Contact,A_ID,Date1,Cost,Address) values(:n_ame,:contr,:aii,:dt,:cc,:adr)',{'n_ame':self.nam,'contr':self.cont,'aii':self.__am1,'dt':self.cdate,'cc':self.costc,'adr':self.addr})
			conn.commit()	
			cur1.close()
			conn.close()
			conn=cx_Oracle.connect('Hos','hos','XE')
			cur=conn.cursor()
			
			cur.execute('UPDATE Ambulance SET Avaibility = :av WHERE A_ID=:ai',{'av':'No','ai':self.__am1})
			conn.commit()
			cur.close()
			conn.close()
			self.lbconf=Label(self.gframe1,text="Reserve Success",font=17,pady=5,bg="violet",justify='center')
			self.lbconf.grid(row=6,columnspan=3)		
		else:
			self.lbconf=Label(self.gframe1,text="Invalid Password",font=17,pady=5,bg="violet",justify='center')
			self.lbconf.grid(row=6,columnspan=3)
					
	def Grid(self):
		
		self.gframe=Canvas(self.mas,bg="plum",height=1000,width=1000)
		self.gframe1=LabelFrame(self.gframe,bd=12,height=100,width=100,bg="violet")
		self.gframe1.grid(row=0,column=1)
		self.gframe2=LabelFrame(self.gframe,height=100,width=100,bd=12,bg="violet")
		self.gframe2.grid(row=1,column=1)
		self.gframe3=LabelFrame(self.gframe,height=100,width=100,bd=12,bg="violet")
		self.gframe3.grid(row=2,column=1)
	def Reeset(self):
		if self.lbconf!='':
			self.lbconf.grid_forget()
		if self.but_ch!='':
			self.but_ch.grid_forget()
		self.Variable()
		self.Avaibility()
		self.NotAvaibility()
		self.Label()
		self.Option_men()
		self.Entry()	
		self.Button()
		self.Button_am_re()		
	def Button(self):
		if self.__am1!='':
			self.but_Reserve=Button(self.gframe1,text="Reserve",width=17,bd=4,bg='purple',fg ='white',command=self.Get_dt)
			self.but_Reserve.grid(row=5,column=1,sticky=W)
		else:
			if self.lbus!='':
				self.but_Reserve.grid_forget()
		self.but_Reset=Button(self.gframe3,text="Reset",width=30,bd=4,bg='purple',fg ='white',command=self.Reeset)
		self.but_Reset.grid(row=0,columnspan=3)
		self.but_ex=Button(self.gframe3,text="Exit",width=30,bd=4,bg='purple',fg ='white',command=self.Exit)
		self.but_ex.grid(row=1,columnspan=3)		
	def Exit(self):
		self.new_wd=Info_desk_menu(self.mas,self.nm)
		self.new_wd.Pack_all() 		
	def Button_am_re(self):
		if len(self.options2)!=0:
			self.but_ch=Button(self.gframe2,text="Change",width=17,bd=4,bg='purple',fg ='white',command=self.Change_dt)
			self.but_ch.grid(row=2,column=1,sticky=W)	
		else:
			if self.but_ch!='':
				self.but_ch.grid_forget()					
class Blood_Info_show_menu(com_menu):	
	def Pack_all(self):
		self.m=-1

		self.mas.title("Blood Bank")	
		self.mas.geometry("1000x700")
		self.Variable()
		self.Grid()
		self.Label()
		#self.Entry()
		self.Option_men()
		self.Button()
		self.gframe.place(x=100,y=80)
		self.mas.mainloop()
	def Get_blg(self):
		self.mas.geometry("1000x700")
		self.blod=self.__blood.get()
		self.__blood.set("")
		if(self.lbBloodg2!=''):
			self.lbBloodg2.grid_forget()
		if(self.lbBlbg1!=''):
			self.lbBlbg1.grid_forget()
		if(self.lbBlp1!=''):
			self.lbBlp1.grid_forget()
		if(self.lbf!=''):
			self.lbf.grid_forget()	
		conn=cx_Oracle.connect('Hos','hos','XE')
		
		#jd=to_date(self.__j_date,'YYYY-MM-DD')
		cur=conn.cursor()

		cur.execute('select Bags,PRICE_PER_BAG from blood where B_ID=:bid',{'bid':self.blod})
		rs = cur.fetchall()
		print(rs)
		if(len(rs)!=0):
			
			for i in rs:	
				print(i)
				self.bag_gg_g=i[0]
				self.pr__r__r=i[1]
				#if self.time=='9Am-12Noon':
		if(self.m!=-1):
			i=self.m-6
			self.m-=1
			while i>-1:
				print(i)

				self.lbnmd[i].grid_forget()	
				self.lbncon[i].grid_forget()	
				i-=1
		self.Labelextra()	
		self.List_of_don()							
		cur.close()
	
		conn.close()
	def Labelextra(self):
		self.lbBloodg1=Label(self.gframe1,text="Blood Group:",font=17,bg="violet",justify='center').grid(row=2,column=0,sticky=E)
		self.lbBloodg2=Label(self.gframe1,text=self.blod,font=17,bg="violet",justify='center')
		self.lbBloodg2.grid(row=2,column=1,sticky=W)				
		self.lbBlbg=Label(self.gframe1,text="Bags:",font=17,bg="violet",justify='center').grid(row=2,column=2,sticky=E)					
		self.lbBlbg1=Label(self.gframe1,text=self.bag_gg_g,font=17,bg="violet",justify='center')
		self.lbBlbg1.grid(row=2,column=3,sticky=W)
		self.lbBlp=Label(self.gframe1,text="Price:",font=17,bg="violet",justify='center').grid(row=2,column=4,sticky=E)	
		self.lbBlp1=Label(self.gframe1,text=self.pr__r__r,font=17,bg="violet",justify='center')
		self.lbBlp1.grid(row=2,column=5,sticky=W)
		self.lbnmd=Label(self.gframe1,text="Name",font=17,bg="violet",justify='center').grid(row=4,column=0)	
		self.lbncon=Label(self.gframe1,text="Contact No",font=17,bg="violet",justify='center').grid(row=4,column=2)
		self.lbBloodpur=Label(self.gframe1,text="BLOOD PURCHASE:",font=20,pady=8,bg="violet",justify='center').grid(row=9,columnspan=6,sticky=W)
		self.lbbnmm=Label(self.gframe1,text="Name:",font=17,bg="violet",justify='center').grid(row=10,column=0,sticky=E)	
		self.lbbconn=Label(self.gframe1,text="Contact No:",font=17,bg="violet",justify='center').grid(row=10,column=2,sticky=E)	
		self.lbbuybag=Label(self.gframe1,text="Bags:",font=17,pady=8,bg="violet",justify='center').grid(row=10,column=4,sticky=E)
		self.Entry()
		self.Button_order()	
	def List_of_don(self):
		conn=cx_Oracle.connect('Hos','hos','XE')
		
		#jd=to_date(self.__j_date,'YYYY-MM-DD')
		cur=conn.cursor()

		cur.execute('select D_name,Contract_No from Blood_donnar where B_ID=:bid',{'bid':self.blod})	
		rs = cur.fetchall()
		print(rs)
		if(len(rs)!=0):		
		
			self.m=5

			self.lbnmd=[]
			self.lbncon=[]
			for i in rs:
				self.lbnmd.append(Label(self.gframe1,text=i[0],font=17,bg="violet",justify='center'))	
				self.lbnmd[self.m-5].grid(row=self.m,column=0)
				self.lbncon.append(Label(self.gframe1,text=i[1],font=17,bg="violet",justify='center'))	
				self.lbncon[self.m-5].grid(row=self.m,column=2)
				self.m+=1
		conn.commit()		
		
				
	def Label(self):
		self.lb1=Label(self.gframe1,text="SEARCH BLOOD",font=17,bg="violet",justify='center').grid(row=0,columnspan=3,sticky=W,pady=5)
		
		self.lbBloodg=Label(self.gframe1,text="Blood Group:",font=17,bg="violet",justify='center').grid(row=1,column=0,sticky=W)	
		self.lb2=Label(self.gframe1,text="LIST OF DONNERS:",font=17,bg="violet",justify='center').grid(row=3,columnspan=3,sticky=W,pady=5)
		
	def Option_men(self):
		#combobox self.scldpt options
		self.sclblood = ttk.Combobox(self.gframe1,values=self.options,textvariable=self.__blood).grid(row=1,column=1,sticky=W)
	def Variable(self):
		self.options=("A+","A-","AB+","AB-","B+","B-","O+","O-")
		self.lbBloodg2=''
		self.lbBlbg1=''
		self.lbBlp1=''
		self.lbf=''
		self.__blood=StringVar(self.mas)
		self.__bags=IntVar(self.mas)
		self.__pr=IntVar(self.mas)	
		self.__dnm=StringVar(self.mas)
		self.__dcon=StringVar(self.mas)
		self.__bname=StringVar(self.mas)
		self.__bcon=StringVar(self.mas)
		self.__buybag=IntVar(self.mas)	

	def Entry(self):
		self.entyname=Entry(self.gframe1,textvariable=self.__bname).grid(row=10,column=1,sticky=W)
		self.entycon=Entry(self.gframe1,textvariable=self.__bcon).grid(row=10,column=3,sticky=W)
		self.entybag=Entry(self.gframe1,textvariable=self.__buybag).grid(row=10,column=5,sticky=W)		
	def Button(self):
		self.but_search=Button(self.gframe1,text="Search",width=17,bd=4,bg='purple',fg ='white',command=self.Get_blg).grid(row=1,column=2,sticky=E)
	
		self.but_ex=Button(self.gframe1,text="EXit",width=17,bd=4,bg='purple',fg ='white',command=self.Exit).grid(row=13,columnspan=6)
	def Button_order(self):
		self.but_order=Button(self.gframe1,text="Order",width=17,bd=4,pady=10,bg='purple',fg ='white',command=self.Buyer_get_dt).grid(row=11,columnspan=6,sticky=E)
	def Buyer_get_dt(self):
		self.buyer_name=self.__bname.get()
		self.buyer_con=self.__bcon.get()
		self.buyer_bag=self.__buybag.get()
		self.__bname.set("")
		self.__bcon.set("")
		self.__buybag.set("")
		if(self.lbf!=''):
			self.lbf.grid_forget()	
		pattern=re.compile("(01)?[0-9]{9}")
		if pattern.match(self.buyer_con) and self.buyer_bag<=self.bag_gg_g and self.bag_gg_g!=0:
			conn=cx_Oracle.connect('Hos','hos','XE')
			cur=conn.cursor()
			cur.execute('insert into Blood_order(buyer_name,bcontact,B_ID,bag,Total_price,Bill) values(:bname,:bcon,:bid,:bg,:ttp,:b)',{'bname':self.buyer_name,'bcon':self.buyer_con,'bid':self.blod,'bg':self.buyer_bag,'ttp':self.buyer_bag*self.pr__r__r,'b':'Pending'})
			conn.commit()	
			cur.close()
	
			conn.close()		
			self.lbf=Label(self.gframe1,text="Entry Success",font=17,bg="violet",justify='center')
			self.lbf.grid(row=12,columnspan=6)	
		elif self.buyer_bag>self.bag_gg_g:
			self.lbf=Label(self.gframe1,text="Entry Fail, Order bag is larger",font=17,bg="violet",justify='center')
			self.lbf.grid(row=12,columnspan=6)	
		else:
			self.lbf=Label(self.gframe1,text="Entry Fail, Contact no is not a Contact no",font=17,bg="violet",justify='center')
			self.lbf.grid(row=12,columnspan=6)								
	def Exit(self):
		self.new_wd=Info_desk_menu(self.mas,self.nm)
		self.new_wd.Pack_all() 
class Blood_bill_menu(com_menu):	
	def Pack_all(self):
		#self.m=-1

		self.mas.title("Blood Bill")	
		self.mas.geometry("1000x700")
		self.Variable()
		self.Grid()
		self.Label()
		self.Entry()	
		self.Button()
		self.gframe.place(x=100,y=80)
		self.mas.mainloop()
	def Entry(self):
		#self.entyname=Entry(self.gframe1,textvariable=self.__bname).grid(row=10,column=1,sticky=W)
		self.entycon=Entry(self.gframe1,textvariable=self.__bcon).grid(row=0,column=1,sticky=W)
		#self.entybag=Entry(self.gframe1,textvariable=self.__buybag).grid(row=10,column=5,sticky=W)
	def Button(self):
		self.but_pay=Button(self.gframe1,text="Search",width=17,bd=4,bg='purple',fg ='white',command=self.get_bl_dt).grid(row=0,column=2,sticky=W)
		self.but_ex=Button(self.gframe1,text="EXit",width=17,bd=4,bg='purple',fg ='white',command=self.Exit).grid(row=6,columnspan=3)
	def Label(self):
		self.lbcon=Label(self.gframe1,text="Contact NO:",font=17,bg="violet",justify='center').grid(row=0,column=0,sticky=W,pady=5)
		
	def get_bl_dt(self):
		self.buyer_con=self.__bcon.get()
		self.__bcon.set("")
		if(self.lbcf!=''):
			self.lbcf.grid_forget()	
		if self.lbbgr!='':
			self.lbbgr.grid_forget()
		if self.lbdyw!='':
			self.lbdyw.grid_forget()
		if self.but_yes!='':
			self.but_yes.grid_forget()
		if self.but_no!='':
			self.but_no.grid_forget()
		pattern=re.compile("(01)?[0-9]{9}")	
		if(pattern.match(self.buyer_con)):
			conn=cx_Oracle.connect('Hos','hos','XE')
			cur=conn.cursor()
			cur.execute('select B_ID,bag,Bill from Blood_order where bcontact=:bco',{'bco':self.buyer_con})

			conn.commit()	
			rs = cur.fetchall()
			print(rs)
			if(len(rs)!=0):
				for i in rs:	
					#print(i)
					self.bill_c=i[2]
					self.bag_buyer=i[1]
					self.bgroup=i[0]
					print(self.bill_c)
				cur.close()
				cur=conn.cursor()
				cur.execute('select Bags,Price_per_bag from Blood where B_ID=:bi',{'bi':self.bgroup})
				for i in cur:	
					#print(i)
					self.bag_remain=i[0]
					self.pr_ice=i[1]
					print(self.bag_remain)
				cur.close()
				if self.bill_c=='Pending':
					if self.bag_remain==0:
						self.lbbgr=Label(self.gframe1,text="No bags Available",font=17,bg="violet",justify='center')
						self.lbbgr.grid(row=2,columnspan=3)
						self.lbdyw=Label(self.gframe1,text="Do you want to cancel order?",font=17,bg="violet",justify='center')
						self.lbdyw.grid(row=3,columnspan=3)	
						
						self.but_yes=Button(self.gframe1,text="Yes",width=17,bd=4,bg='purple',fg ='white',command=self.Bill_pay)
						self.but_yes.grid(row=4,column=0)													
						self.but_no=Button(self.gframe1,text="No",width=17,bd=4,bg='purple',fg ='white',command=self.Exit)
						self.but_no.grid(row=4,column=1)
					elif self.bag_remain>self.bag_buyer:
						self.lbbgr=Label(self.gframe1,text="Contact No:"+str(self.buyer_con)+", Bags:"+str(self.bag_buyer)+", Price:"+str(self.bag_buyer*self.pr_ice),font=17,bg="violet",justify='center')
						self.lbbgr.grid(row=2,columnspan=3)
						self.but_yes=Button(self.gframe1,text="Pay",width=17,bd=4,bg='purple',fg ='white',command=self.Bill_pay)
						self.but_yes.grid(row=4,column=0)
						'''cur=conn.cursor()
						cur.execute('UPDATE Blood_order SET TASK = :ts WHERE time=:tt and E_ID=:eid and date1=:dt',{'ts':self.taskk5,'eid':self.__id,'dt':self.dt,'tt':'9Pm-12Midnight'})	'''
					else:
						self.lbbgr=Label(self.gframe1,text="Contact No:"+str(self.buyer_con)+", Bags: avilable "+str(self.bag_remain)+" but wanted "+str(self.bag_buyer)+", Price:"+str(self.bag_remain*self.pr_ice),font=17,bg="violet",justify='center')
						self.lbbgr.grid(row=2,columnspan=3)
						self.but_yes=Button(self.gframe1,text="Pay",width=17,bd=4,bg='purple',fg ='white',command=self.Bill_pay)
						self.but_yes.grid(row=4,column=0)
						self.but_no=Button(self.gframe1,text="Cancel",width=17,bd=4,bg='purple',fg ='white',command=self.Exit)
						self.but_no.grid(row=4,column=1)	
				else:
						self.lbbgr=Label(self.gframe1,text="Bill is already paid",font=17,bg="violet",justify='center')
						self.lbbgr.grid(row=2,columnspan=3)	
			else:
				cur.close()
				self.lbcf=Label(self.gframe1,text="Contact No is not Available",font=17,bg="violet",justify='center')
				self.lbcf.grid(row=1,columnspan=3)
																
			conn.close()
		else:
			self.lbcf=Label(self.gframe1,text="Invalid Contact NO",font=17,bg="violet",justify='center')
			self.lbcf.grid(row=1,columnspan=3)
	def Bill_pay(self):
		if self.bag_remain==0:	
			conn=cx_Oracle.connect('Hos','hos','XE')
			cur=conn.cursor()
			cur=conn.cursor()
			cur.execute('delete from Blood_order where bcontact=:bco',{'bco':self.buyer_con})
			conn.commit()
			cur.close()
			conn.close()	
		elif self.bag_remain>self.bag_buyer:
			conn=cx_Oracle.connect('Hos','hos','XE')
			cur=conn.cursor()
			cur=conn.cursor()
			cur.execute('UPDATE Blood_order SET Bill = :bl WHERE bcontact=:bco',{'bco':self.buyer_con,'bl':'Paid'})	
			conn.commit()		
			cur=conn.cursor()
			cur.execute('UPDATE Blood SET bags = :bg WHERE B_ID =:bid',{'bg':self.bag_remain-self.bag_buyer,'bid':self.bgroup})	
			conn.commit()
			cur.close()
			conn.close()	
		else:
			conn=cx_Oracle.connect('Hos','hos','XE')
			cur=conn.cursor()
			cur=conn.cursor()
			cur.execute('UPDATE Blood_order SET Bill = :bl WHERE bcontact=:bco',{'bco':self.buyer_con,'bl':'Paid'})	
			conn.commit()		
			cur=conn.cursor()
			cur.execute('UPDATE Blood SET bags = :bg WHERE B_ID =:bid',{'bg':self.bag_remain-self.bag_remain,'bid':self.bgroup})	
			conn.commit()
			cur.close()
			conn.close()											
	def Exit(self):
		self.new_wd=Cash_menu(self.mas,self.nm)
		self.new_wd.Pack_all() 	
	def Variable(self):
		self.lbbgr=''
		self.lbcf=''
		self.lbdyw=''
		self.but_yes=''
		self.but_no=''
		self.__bcon=StringVar(self.mas)

class Pathology_entry(com_menu):
	def Pack_all(self):
		
		self.mas.title("Pathology Entry")	
		self.mas.geometry("1000x700")
		self.Variable()
		self.Grid()
		self.Label()
		self.Entry()
		self.Radio_but()
		self.Option_men()
		self.Button()

		self.gframe.pack(anchor=CENTER)
		#self.lbnm.pack(side=LEFT,anchor=NW)
		self.mas.mainloop()
	def Get_data(self):
		self.na=self.__name.get()
		self.ag=self.__age.get()
		self.doctor=self.__dc.get()
		self.co=self.__con.get()
		self.wb=self.__wbc.get()
		
		self.ge = self.__gen.get()
		self.r=self.__rbc.get()

		self.bl=self.__blo.get()
		self.hhhgg=self.__hg.get()

		self.heart=self.__hear.get()

		#print(self.na," ",self.ag," ",self.j," ",self.de," ",self.sa," ",self.ge," ",self.r," ",self.dp)
		self.__name.set("")
		self.__age.set(0)
		self.__dc.set("")
		self.__con.set("")
		self.__wbc.set(0)
		self.__gen.set("")
		self.__rbc.set(0)
		self.__blo.set(self.options[0])
		self.__hg.set(self.option_hg[0])
		self.__hear.set(self.option_heart[0])
		pattern=re.compile("(01)?[0-9]{9}")
		if self.lbf!='':
			self.lbf.grid_forget()
		if (pattern.match(self.co)):
			
			conn=cx_Oracle.connect('Hos','hos','XE')
			cur=conn.cursor()
			cur.execute('select E_ID from Doctor where E_ID=:ei',{'ei':self.doctor})
			rs = cur.fetchall()
				#print(i)
			if len(rs)!=0:
				#print(self.na,' ',self.ag,' ',self.doctor,' ',self.co,' ',self.wb,' ',self.ge,' ',self.r,' ',self.bl,' ',self.hhhgg,' ',self.heart)
				cur1=conn.cursor()

				cur1.execute('insert into Pathology_report(Name,Age,Gender,Contact_No,E_ID,BG,RBC,WBC,HBsAg,Heart) values(:n_ame,:ag,:gn,:contr,:eidi,:b_g,:r_bc,:w_bc,:hb_ag,:ht)',{'n_ame':self.na,'ag':self.ag,'gn':self.ge,'contr':self.co,'eidi':self.doctor,'b_g':self.bl,'r_bc':self.r,'w_bc':self.wb,'hb_ag':self.hhhgg,'ht':self.heart})
				conn.commit()
				cur1.close()
				cur1=conn.cursor()
				cur1.execute('insert into Pathology_report_deliver(Contact_No,Availability,Deliver) values(:contr,:av,:dl)',{'contr':self.co,'av':'Available','dl':'No'})
				conn.commit()
				cur1.close()
					#Pathology_report_deliver
				self.lbf=Label(self.gframe1,text="Suceess",font=14,bg="violet",justify='center')
				self.lbf.grid(row=12,columnspan=3)
			else:
				self.lbf=Label(self.gframe1,text="Doc is not here",font=14,bg="violet",justify='center')
				self.lbf.grid(row=12,columnspan=3)
			cur.close()
			conn.close()
		else:
			self.lbf=Label(self.gframe1,text="Invalid Contact NO.",font=14,bg="violet",justify='center')
			self.lbf.grid(row=12,columnspan=3)

	def Exit(self):
		self.new_wd=Admin_menu(self.mas,self.nm)
		self.new_wd.Pack_all()     		
	def Variable(self):
		self.options=("A+","A-","AB+","AB-","B+","B-","O+","O-")
		self.option_hg=("Posative","Negative","Nothing")
		self.option_heart=("Normal","Block","Nothing")
		#self.r=6
		#self.c=1
		self.lbf=''
		self.__name=StringVar(self.mas)
		self.__age=IntVar(self.mas)
		self.__dc=StringVar(self.mas)
		self.__con=StringVar(self.mas)
		self.__wbc=IntVar(self.mas)
		self.__gen=StringVar(self.mas)
		self.__rbc=IntVar(self.mas)
		self.__blo=StringVar(self.mas)
		self.__blo.set(self.options[0])
		self.__hg=StringVar(self.mas)
		self.__hg.set(self.option_hg[0])
		self.__hear=StringVar(self.mas)
		self.__hear.set(self.option_heart[0])
		
	def Label(self):
		self.lb1=Label(self.gframe1,text="Enter Information",font=17,bg="violet",justify='center').grid(row=0,column=0,sticky=N,pady=5)
		self.lbnm=Label(self.gframe1,text="Name:",font=14,bg="violet",justify='center').grid(row=1,column=0,sticky=E,pady=5)
		self.lbage=Label(self.gframe1,text="Age:",font=14,bg="violet",justify='center').grid(row=2,column=0,sticky=E,pady=5)
		self.lbgen=Label(self.gframe1,text="Gender:",font=14,bg="violet",justify='center').grid(row=3,column=0,sticky=E,pady=5)
		self.lbdoc=Label(self.gframe1,text="Reference Doctor ID:",font=14,bg="violet",justify='center').grid(row=4,column=0,sticky=E,pady=5)
		self.lbcon=Label(self.gframe1,text="Contact No:",font=14,bg="violet",justify='center').grid(row=5,column=0,sticky=E,pady=5)
		self.lbblo=Label(self.gframe1,text="Blood Group:",font=14,bg="violet",justify='center').grid(row=6,column=0,sticky=E,pady=5)
		self.lbrbc=Label(self.gframe1,text="RBC:",font=14,bg="violet",justify='center').grid(row=7,column=0,sticky=E,pady=5)
		self.lbrbc1=Label(self.gframe1,text="millions/cmm",font=14,bg="violet",justify='center').grid(row=7,column=2,sticky=W,pady=5)
		self.lbwbc=Label(self.gframe1,text="WBC:",font=14,bg="violet",justify='center').grid(row=8,column=0,sticky=E,pady=5)
		self.lbwbc1=Label(self.gframe1,text="/cmm",font=14,bg="violet",justify='center').grid(row=8,column=2,sticky=W,pady=5)
		self.lbhbag=Label(self.gframe1,text="HBsAg:",font=14,bg="violet",justify='center').grid(row=9,column=0,sticky=E,pady=5)	
		self.lbhecg=Label(self.gframe1,text="Heart:",font=14,bg="violet",justify='center').grid(row=10,column=0,sticky=E,pady=5)
	def Entry(self):
		self.entynm=Entry(self.gframe1,textvariable=self.__name).grid(row=1,column=1,sticky=W)
		self.entyage=Entry(self.gframe1,textvariable=self.__age).grid(row=2,column=1,sticky=W)
		self.entydoc=Entry(self.gframe1,textvariable=self.__dc).grid(row=4,column=1,sticky=W)
		self.entycons=Entry(self.gframe1,textvariable=self.__con).grid(row=5,column=1,sticky=W)
		self.entywbc=Entry(self.gframe1,textvariable=self.__wbc).grid(row=8,column=1,sticky=W)
		self.entyrbc=Entry(self.gframe1,textvariable=self.__rbc).grid(row=7,column=1,sticky=W)

	def Button(self):
		self.but_info=Button(self.gframe1,text="Submit",width=17,bd=4,bg='purple',fg ='white',command=self.Get_data).grid(row=11,column=1,sticky=W,pady=5)
		self.but_ex=Button(self.gframe1,text="EXIT",width=20,bd=4,bg='purple',fg ='white',command=self.Exit).grid(row=13,pady=10,columnspan=3)

	def Radio_but(self):
		self.R1 = Radiobutton(self.gframe1, text="Male", variable=self.__gen, value="male",font=14,bg="violet",justify='center',bd=0).grid(row=3,column=1,sticky=W)
		self.R2 = Radiobutton(self.gframe1, text="Female", variable=self.__gen, value="Female",font=14,bg="violet",justify='center',bd=0).grid(row=3,column=2,sticky=W)
	def Option_men(self):
		#combobox self.scldpt options
		self.sclblo = ttk.Combobox(self.gframe1,values=self.options,textvariable=self.__blo).grid(row=6,column=1,sticky=W)
		self.sclhg = ttk.Combobox(self.gframe1,values=self.option_hg,textvariable=self.__hg).grid(row=9,column=1,sticky=W)
		self.sclecg = ttk.Combobox(self.gframe1,values=self.option_heart,textvariable=self.__hear).grid(row=10,column=1,sticky=W)
class Pathology_report_av(com_menu):
	def Pack_all(self):
		
		self.mas.title("Report Avaibility")	
		self.mas.geometry("1000x700")
		self.Variable()
		self.Grid()
		self.Label()
		self.Entry()
		self.Button()

		self.gframe.pack(anchor=CENTER)
		#self.lbnm.pack(side=LEFT,anchor=NW)
		self.mas.mainloop()
	def Label(self):
	
		self.lbcon=Label(self.gframe1,text="Contact No:",font=14,bg="violet",justify='center').grid(row=0,column=0,sticky=E,pady=5)
	def Entry(self):
		self.entycon=Entry(self.gframe1,textvariable=self.__con).grid(row=0,column=1,sticky=W)
	def Variable(self):
		self.lbf=''
		self.__con=StringVar(self.mas)
	def Get_data(self):
		self.c=self.__con.get()
		self.__con.set("")
		pattern=re.compile("(01)?[0-9]{9}")
		if self.lbf!='':
			self.lbf.grid_forget()
		if (pattern.match(self.c)):
			conn=cx_Oracle.connect('Hos','hos','XE')
			cur=conn.cursor()
			cur.execute('select Availability from Pathology_report_deliver where Contact_No=:ci',{'ci':self.c})
			rs = cur.fetchall()
			print(rs)
			if(len(rs)!=0):
				self.lbf=Label(self.gframe1,text="Available",font=14,bg="violet",justify='center')
				self.lbf.grid(row=1,columnspan=3)
			else:
				self.lbf=Label(self.gframe1,text="Not Available",font=14,bg="violet",justify='center')
				self.lbf.grid(row=1,columnspan=3)					
		else:
			self.lbf=Label(self.gframe1,text="Invalid Contact NO.",font=14,bg="violet",justify='center')
			self.lbf.grid(row=1,columnspan=3)				

	def Button(self):
		self.but_info=Button(self.gframe1,text="Submit",width=17,bd=4,bg='purple',fg ='white',command=self.Get_data).grid(row=0,column=2,sticky=W,pady=5)
		self.but_ex=Button(self.gframe1,text="EXIT",width=20,bd=4,bg='purple',fg ='white',command=self.Exit).grid(row=2,pady=10,columnspan=3)
	def Exit(self):
		self.new_wd=Info_desk_menu(self.mas,self.nm)
		self.new_wd.Pack_all()   

class Report_Del_menu(com_menu):
	def Pack_all(self):
		#self.__id=id1
		#print(self.__id)
		self.mas.title("Repord Delivery")	
		self.mas.geometry("1000x700")
		self.Grid()
		
		self.Variable()
		
		self.Label()
		self.Entry()
		self.Button()
		self.gframe.place(x=100,y=80)
		self.mas.mainloop()

	def Variable(self):	
		self.lbf=''	
		self.lbnam_e=''
		self.lbage_e=''
		self.lbgen_e=''
		self.lbbgl_e=''
		self.lbrbc_e=''
		self.lbwbc_e=''
		self.lbhsag_e=''
		self.lbheart_e=''
		self.lbrbc_e1=''
		self.lbhsag_e1=''
		self.lbheart_e1=''
		self.lbbill1=''
		self.but_pay=''
		self.__pid=StringVar(self.mas)
	def Label(self):
		#self.lbnm=Label(self.gframe1,text="Name:",font=12,bg="violet",justify='center').grid(row=1,column=0,sticky=E)
		self.lbid=Label(self.gframe1,text="Contact NO:",font=12,bg="violet",justify='center').grid(row=0,column=0,sticky=E)
		self.lbnmp=Label(self.gframe1,text="Name:",font=12,bg="violet",justify='center').grid(row=1,column=0,sticky=E)
		self.lbnag=Label(self.gframe1,text="Age:",font=12,bg="violet",justify='center').grid(row=2,column=0,sticky=E)
		self.lbngen=Label(self.gframe1,text="Gender:",font=12,bg="violet",justify='center').grid(row=3,column=0,sticky=E)
		self.lbtotal=Label(self.gframe1,text="Cost",font=12,bg="violet",justify='center').grid(row=4,column=2,sticky=W)
		#self.lbscp=Label(self.gframe1,text="Sickness:",font=12,bg="violet",justify='center').grid(row=4,column=0,sticky=E)
		self.lbnbg=Label(self.gframe1,text="Blood Group:",font=12,bg="violet",justify='center').grid(row=5,column=0,sticky=E)
		self.lbrbc=Label(self.gframe1,text="RBC:",font=12,bg="violet",justify='center').grid(row=6,column=0,sticky=E)
		self.lbwbc=Label(self.gframe1,text="WBC:",font=12,bg="violet",justify='center').grid(row=7,column=0,sticky=E)
		self.lbAg=Label(self.gframe1,text="HBsAg:",font=12,bg="violet",justify='center').grid(row=8,column=0,sticky=E)
		self.lbht=Label(self.gframe1,text="Heart:",font=12,bg="violet",justify='center').grid(row=9,column=0,sticky=E)
		self.lbbill=Label(self.gframe1,text="Bill:",font=12,bg="violet",justify='center').grid(row=10,column=0,sticky=E)	
	def Entry(self):

		self.entypid=Entry(self.gframe1,textvariable=self.__pid).grid(row=0,column=1,sticky=W)	
	def Button(self):

		#self.but_lp=Button(self.gframe1,text="List Of All Patient",width=17,bd=4,bg='purple',fg ='white').grid(row=0,columnspan=3)
		self.but_src=Button(self.gframe1,text="SEARCH",width=12,bd=4,bg='purple',fg ='white',command=self.Get_rp).grid(row=0,column=2)
		self.but_ex=Button(self.gframe1,text="EXit",width=17,bd=4,bg='purple',fg ='white',command=self.Exit).grid(row=14,columnspan=3)
		
	def Get_rp(self):
		self.con=self.__pid.get()
		self.__pid.set("")
		self.blood_pr=0
		self.hg_pr=0
		self.heart_pr=0
		if self.lbnam_e!='':
			self.lbnam_e.grid_forget()
		if self.lbage_e!='':
			self.lbage_e.grid_forget()
		if self.lbgen_e!='':
			self.lbgen_e.grid_forget()
		if self.lbbgl_e!='':
			self.lbbgl_e.grid_forget()
		if self.lbrbc_e!='':
			self.lbrbc_e.grid_forget()
		if self.lbrbc_e1!='':
			self.lbrbc_e1.grid_forget()
		if self.lbwbc_e!='':
			self.lbwbc_e.grid_forget()
		if self.lbhsag_e!='':
			self.lbhsag_e.grid_forget()
		if self.lbhsag_e1!='':
			self.lbhsag_e1.grid_forget()
		if self.lbheart_e!='':
			self.lbheart_e.grid_forget()
		if self.lbheart_e1!='':
			self.lbheart_e1.grid_forget()
		if self.lbf!='':
			self.lbf.grid_forget()
		if self.lbbill1!='':
			self.lbbill1.grid_forget()
		if self.but_pay!='':
			self.but_pay.grid_forget()
		pattern=re.compile("(01)?[0-9]{9}")	
		if(pattern.match(self.con)):
			conn=cx_Oracle.connect('Hos','hos','XE')
			cur=conn.cursor()
			cur.execute('select NAME,Age,Gender,BG,RBC,WBC,HBsAg,Heart from Pathology_report where Contact_No=:bco',{'bco':self.con})

			conn.commit()	
			cur1=cur
			rs = cur.fetchall()
			cur=cur1
			print(rs)
			if(len(rs)!=0):	
				print(cur)
				for i in rs:
					print(i)
					
					self.lbnam_e=Label(self.gframe1,text=i[0],font=14,bg="violet",justify='center')
					self.lbnam_e.grid(row=1,column=1,sticky=W)
					self.lbage_e=Label(self.gframe1,text=i[1],font=14,bg="violet",justify='center')
					self.lbage_e.grid(row=2,column=1,sticky=W)
					self.lbgen_e=Label(self.gframe1,text=i[2],font=14,bg="violet",justify='center')
					self.lbgen_e.grid(row=3,column=1,sticky=W)
					self.lbbgl_e=Label(self.gframe1,text=i[3],font=14,bg="violet",justify='center')
					self.lbbgl_e.grid(row=5,column=1,sticky=W)
					self.lbrbc_e=Label(self.gframe1,text=i[4],font=14,bg="violet",justify='center')
					self.lbrbc_e.grid(row=6,column=1,sticky=W)
					if i[4]!=None:
						self.lbrbc_e1=Label(self.gframe1,text='200',font=14,bg="violet",justify='center')
						self.lbrbc_e1.grid(row=6,column=2,sticky=W)						
						self.blood_pr=200
					self.lbwbc_e=Label(self.gframe1,text=i[5],font=14,bg="violet",justify='center')
					self.lbwbc_e.grid(row=7,column=1,sticky=W)
					self.lbhsag_e=Label(self.gframe1,text=i[6],font=14,bg="violet",justify='center')
					self.lbhsag_e.grid(row=8,column=1,sticky=W)
					if i[6]!=None:
						self.lbhsag_e1=Label(self.gframe1,text='200',font=14,bg="violet",justify='center')
						self.lbhsag_e1.grid(row=8,column=2,sticky=W)						
						self.hg_pr=200
					self.lbheart_e=Label(self.gframe1,text=i[7],font=14,bg="violet",justify='center')
					self.lbheart_e.grid(row=9,column=1,sticky=W)
					if i[7]!=None:
						self.lbheart_e1=Label(self.gframe1,text='600',font=14,bg="violet",justify='center')
						self.lbheart_e1.grid(row=9,column=2,sticky=W)						
						self.heart_pr=600
				self.lbbill1=Label(self.gframe1,text=self.blood_pr+self.hg_pr+self.heart_pr,font=12,bg="violet",justify='center')
				self.lbbill1.grid(row=10,column=2,sticky=W)	
				cur.close()
				self.but_pay=Button(self.gframe1,text="Paid",width=12,bd=4,bg='purple',fg ='white',command=self.Pay)
				self.but_pay.grid(row=11,column=2)

			else:
					self.lbf=Label(self.gframe1,text="Contact NO not found.",font=14,bg="violet",justify='center')
					self.lbf.grid(row=12,columnspan=3)
			conn.close()
		else:
			self.lbf=Label(self.gframe1,text="Invalid Contact NO.",font=14,bg="violet",justify='center')
			self.lbf.grid(row=12,columnspan=3)						
	def Pay(self):
		if self.lbf!='':
			self.lbf.grid_forget()
		conn=cx_Oracle.connect('Hos','hos','XE')
		cur=conn.cursor()
		cur.execute('UPDATE Pathology_report_deliver SET Deliver = :dv WHERE Contact_No =:bco',{'dv':'Yes','bco':self.con})
		self.lbf=Label(self.gframe1,text="Successfuly Paid",font=14,bg="violet",justify='center')
		self.lbf.grid(row=12,columnspan=3)	
		conn.commit()	
		cur.close()
		conn.close()		
	def Exit(self):
		self.new_wd=Cash_menu(self.mas,self.nm)
		self.new_wd.Pack_all() 
class Patient_registration_menu(com_menu):
	def Pack_all(self):
		
		self.mas.title("Registration")	
		self.mas.geometry("1000x700")
		self.Variable()
		self.Grid()
		self.Label()
		self.Entry()
		self.Radio_but()
		self.Option_men()
		self.Button()

		self.gframe.place(x=100,y=100)
		#self.lbnm.pack(side=LEFT,anchor=NW)
		self.mas.mainloop()
	def Get_data(self):
		self.name1=self.__name.get()
		self.age1=self.__age.get()
		self.ad1=self.__ad.get()
		self.dis1=self.__dis.get()
		self.wrd1=self.__wrd.get()
		self.depart1=self.__dpt.get()
		self.gender1=self.__gen.get()
		self.contract=self.__con.get()
		self.doctor=self.__doc.get()
		if self.oper=="Required":
			self.ti=self.__time.get()
			self.__time.set(self.options1[0])
			self.rm1=self.__room.get()
			self.__room.set('')
			self.date1=self.__date.get()
			self.__date.set('')
		else:
			self.ti=''
			self.date1=''
			self.rm1=''
				
		self.__name.set("")
		self.__age.set(0)
		self.__ad.set(self.cdate)
		self.__dis.set("")
		#self.__sal.set("")
		self.__gen.set("")
		self.__wrd.set(self.options2[0])
		self.__dpt.set(self.options[0])
		self.__con.set("")
		self.__doc.set("")
		pattern=re.compile("(01)?[0-9]{9}")
		if self.lbf!='':
			self.lbf.grid_forget()
		if (pattern.match(self.contract)):
			conn=cx_Oracle.connect('Hos','hos','XE')
			cur=conn.cursor()
			cur.execute('select E_ID from Doctor where E_ID=:ei',{'ei':self.doctor})
			rs = cur.fetchall()
				#print(i)
			if len(rs)!=0:
				cur.close()
				if self.date1!='':
					
					cur=conn.cursor()
					cur.execute('select * from Attendence where E_ID=:ei and Date1=:dt and Attendence=:att',{'ei':self.doctor,'dt':self.date1,'att':'A'})
					rs1 = cur.fetchall()
					if len(rs1)!=0:
						cur.close()
						cur=conn.cursor()
						cur.execute('select Task from Schedule where E_ID=:ei and Date1=:dt and Time=:tt and Task in (:tas,:tas1)',{'ei':self.doctor,'dt':self.date1,'tt':self.ti,'tas':'Office','tas1':'Nothing'})
						rs2 = cur.fetchall()
						if len(rs2)==0:
							self.lbf=Label(self.gframe1,text="Time not Available",font=14,bg="violet",justify='center')
							self.lbf.grid(row=15,columnspan=3)
								
						else:
							cur.close()
							cur=conn.cursor()
							cur.execute('insert into Patient(Name,pid,Age,Gender,ADate,Disease,Department,Ward,Contact_No,Supervisor,Op,Dateop,Timeop,Roomop) values(:nm,:id,:ag,:gn,:adt,:dis,:dpt,:wd,:con,:sup,:oper,:odt,:ott,:orr)',{'nm':self.name1,'id':self.name1[0:2]+'_'+self.contract,'ag':self.age1,'gn':self.gender1,'adt':self.ad1,'dis':self.dis1,'dpt':self.depart1,'wd':self.wrd1,'con':self.contract,'sup':self.doctor,'oper':'Required','odt':self.date1,'ott':self.ti,'orr':self.rm1})

							conn.commit()						
							cur.close()
							cur=conn.cursor()
							cur.execute('UPDATE Schedule SET TASK = :ts WHERE time=:tt and E_ID=:eid and date1=:dt',{'ts':'Op,room-'+self.rm1,'eid':self.doctor,'dt':self.date1,'tt':self.ti})
							conn.commit()
								
					else:
						self.lbf=Label(self.gframe1,text="Doctor is not available on that day",font=14,bg="violet",justify='center')
						self.lbf.grid(row=15,columnspan=3)
				else:
					#conn=cx_Oracle.connect('Hos','hos','XE')
					cur=conn.cursor()
					print('no')	
					cur.execute('insert into Patient(Name,pid,Age,Gender,ADate,Disease,Department,Ward,Contact_No,Supervisor,Op) values(:nm,:id,:ag,:gn,:adt,:dis,:dpt,:wd,:con,:sup,:oper)',{'nm':self.name1,'id':self.name1[0:2]+'_'+self.contract,'ag':self.age1,'gn':self.gender1,'adt':self.ad1,'dis':self.dis1,'dpt':self.depart1,'wd':self.wrd1,'con':self.contract,'sup':self.doctor,'oper':'Not Required'})
					conn.commit()					
					cur.close()
							
			else:
				self.lbf=Label(self.gframe1,text="No Doctor available",font=14,bg="violet",justify='center')
				self.lbf.grid(row=15,columnspan=3)				
			
		else:
			
			self.lbf=Label(self.gframe1,text="Invalid Contact NO.",font=14,bg="violet",justify='center')
			self.lbf.grid(row=15,columnspan=3)			
		#self.Give_dt()
	'''def Give_dt(self):
		if self.de=='Doctor':
			self.pass_dt=Doctor(self.na)
			self.pass_dt.Get_info(self.ag,self.j,self.ge,self.sa,self.de,self.r,self.dp)
			self.pass_dt.Doc_insert()
		#print(self.__name," ",self.__age," ",self.__jd," ",self.__des," ",self.__sal," ",self.__gen," ",self.__rk," ",self.__dpt)'''
	def Exit(self):
		self.new_wd=Info_desk_menu(self.mas,self.nm)
		self.new_wd.Pack_all()     		
	def Variable(self):
		self.xdt=datetime.datetime.now()
		self.day=self.xdt.strftime("%d")
		self.mon=self.xdt.strftime("%b")
		self.year=self.xdt.strftime("%y")
		self.year=str(self.xdt.year)
		self.cdate=str(self.day)+'-'+str(self.mon)+'-'+self.year[-2:]
		self.options=["Gayanology","orthology"]
		self.oper=''
		self.options1=['3Pm-6Pm','6Pm-9Pm','9Pm-12Midnight']
		self.options2=['ward1','ward2','ward3','ward4']
		self.__name=StringVar(self.mas)
		self.__age=IntVar(self.mas)
		self.__ad=StringVar(self.mas)
		self.__ad.set(self.cdate)
		self.__dis=StringVar(self.mas)
		self.__wrd=StringVar(self.mas)
		self.__dpt=StringVar(self.mas)
		self.__gen=StringVar(self.mas)
		self.__con=StringVar(self.mas)
		self.__dpt.set(self.options[0])
		self.__doc=StringVar(self.mas)
		self.__op=StringVar(self.mas)
		self.__time=StringVar(self.mas)
		self.__room=StringVar(self.mas)
		self.__date=StringVar(self.mas)
		#self.__date.set(self.cdate)
		self.lbdt=''
		self.lbtm=''
		self.lbrm=''
		self.entydt=''
		self.scltm=''
		self.entyrm=''
		self.lbf=''
		self.__wrd.set(self.options2[0])
		self.__time.set(self.options1[0])
	def Label(self):
		self.lb1=Label(self.gframe1,text="Enter Patient Information",font=12,bg="violet",justify='center',padx=7).grid(row=0,column=0,sticky=N)
		self.lbnm=Label(self.gframe1,text="Name :",font=12,bg="violet",justify='center',padx=7).grid(row=1,column=0,sticky=E)
		self.lbage=Label(self.gframe1,text="Age :",font=12,bg="violet",justify='center',padx=7).grid(row=2,column=0,sticky=E)
		self.lbgen=Label(self.gframe1,text="Gender :",font=12,bg="violet",justify='center',padx=7).grid(row=3,column=0,sticky=E)
		self.lbad=Label(self.gframe1,text="Admission Date :",font=12,bg="violet",justify='center',padx=7).grid(row=4,column=0,sticky=E)
		self.lbdes=Label(self.gframe1,text="Disease :",font=12,bg="violet",justify='center',padx=7).grid(row=5,column=0,sticky=E)
		self.lbdpt=Label(self.gframe1,text="Department :",font=12,bg="violet",justify='center',padx=7).grid(row=6,column=0,sticky=E)
		self.lbward=Label(self.gframe1,text="Ward Number :",font=12,bg="violet",justify='center',padx=7).grid(row=7,column=0,sticky=E)
		self.lbcon=Label(self.gframe1,text="Contract No :",font=12,bg="violet",justify='center',padx=7).grid(row=8,column=0,sticky=E)
		self.lbsup=Label(self.gframe1,text="Supervisor Doctor :",font=12,bg="violet",justify='center',padx=7).grid(row=9,column=0,sticky=E)
		self.lboper=Label(self.gframe1,text="Operation :",font=12,bg="violet",justify='center',padx=7).grid(row=10,column=0,sticky=E)	
	def Entry(self):
		self.entynm=Entry(self.gframe1,textvariable=self.__name).grid(row=1,column=1,sticky=W)
		self.entyage=Entry(self.gframe1,textvariable=self.__age).grid(row=2,column=1,sticky=W)
		self.entyad=Entry(self.gframe1,textvariable=self.__ad).grid(row=4,column=1,sticky=W)
		self.entydis=Entry(self.gframe1,textvariable=self.__dis).grid(row=5,column=1,sticky=W)
		
		self.entycon=Entry(self.gframe1,textvariable=self.__con).grid(row=8,column=1,sticky=W)
		self.entydoc=Entry(self.gframe1,textvariable=self.__doc).grid(row=9,column=1,sticky=W)
	def Button(self):
		self.but_info=Button(self.gframe1,text="Submit",command=self.Get_data,width=17,bd=4,bg='purple',fg ='white').grid(row=14,column=1,columnspan=2)
		self.but_exit=Button(self.gframe1,text="Exit",width=17,bd=4,bg='purple',fg ='white',command=self.Exit).grid(row=16,columnspan=3)
	def Radio_but(self):
		self.R1 = Radiobutton(self.gframe1, text="Male", variable=self.__gen, value="male",font=14,bg="violet",justify='center',bd=0).grid(row=3,column=1,sticky=W)
		self.R2 = Radiobutton(self.gframe1, text="Female", variable=self.__gen, value="Female",font=14,bg="violet",justify='center',bd=0).grid(row=3,column=2,sticky=W)

		self.Ro1 = Radiobutton(self.gframe1, text="Required", variable=self.__op, value="Required",font=14,bg="violet",justify='center',bd=0,command=self.get_op).grid(row=10,column=1,sticky=W)
		self.Ro2 = Radiobutton(self.gframe1, text="Not Required", variable=self.__op, value="Not Required",font=14,bg="violet",justify='center',bd=0,command=self.get_op).grid(row=10,column=2,sticky=W)
	def get_op(self):
		self.oper=self.__op.get()
		
		self.__op.set('')
		if self.oper=="Required":
			self.Labelextra()
			self.Optionextra()
			self.Entry_extra()
			self.mas.geometry("1000x700")
		else:
			if self.lbdt!='':
				self.lbdt.grid_forget()
				self.lbtm.grid_forget()
				self.lbrm.grid_forget()
				self.scltm.grid_forget()
				self.entyrm.grid_forget()
				self.entydt.grid_forget()
			self.mas.geometry("1000x700")
			
	def Labelextra(self):
		self.lbdt=Label(self.gframe1,text="Date :",font=12,bg="violet",justify='center',padx=7)
		self.lbdt.grid(row=11,column=0,sticky=E)
		self.lbtm=Label(self.gframe1,text="Time :",font=12,bg="violet",justify='center',padx=7)
		self.lbtm.grid(row=12,column=0,sticky=E)
		self.lbrm=Label(self.gframe1,text="Room :",font=12,bg="violet",justify='center',padx=7)
		self.lbrm.grid(row=13,column=0,sticky=E)
	def Optionextra(self):	
		self.scltm = ttk.Combobox(self.gframe1,values=self.options1,textvariable=self.__time)
		self.scltm .grid(row=12,column=1,sticky=W)
	def Entry_extra(self):
		self.entydt=Entry(self.gframe1,textvariable=self.__date)
		self.entydt.grid(row=11,column=1,sticky=W)
		self.entyrm=Entry(self.gframe1,textvariable=self.__room)
		self.entyrm.grid(row=13,column=1,sticky=W)									
	def Option_men(self):
		self.sclwrd=ttk.Combobox(self.gframe1,values=self.options2,textvariable=self.__wrd).grid(row=7,column=1,sticky=W)
		#combobox self.scldpt options
		self.scldpt = ttk.Combobox(self.gframe1,values=self.options,textvariable=self.__dpt).grid(row=6,column=1,sticky=W)

class Rec_doc_Suggestion(com_menu):
	def Pack_all(self):
		self.mas.title("Patient Advice")	
		self.mas.geometry("1000x700")
		self.Variable()
		self.Grid()
		self.Label()
		self.Option_men()
		self.Button()
		self.gframe.place(x=20,y=20)
		self.mas.mainloop()
	def Variable(self):
		self.options=("Gayanology","orthology")
		self.r=3
		self.__ID=''
		self.__Name=''
		self.__Rank=''
		self.__dpt=StringVar(self.mas)
		self.__dpt.set(self.options[0])
		self.lbfordoc=''
		self.lbfordoc1=''
		self.lbfordoc2=''
		self.lb4=''
	def Label(self):
		self.lbdpt=Label(self.gframe1,text="Dept:",font=17,bg="violet",justify='center').grid(row=1,column=0,sticky=N,pady=5)
	def Label1(self):
		self.lb1=Label(self.frame_1 ,text="ID",font=17,bg="orange",justify='center').grid(row=0,column=0,sticky=N,pady=5)
		self.lb2=Label(self.frame_1 ,text="Name",font=17,bg="orange",justify='center').grid(row=0,column=1,sticky=N,pady=5)
		self.lb3=Label(self.frame_1 ,text="    Rank",font=17,bg="orange",justify='center').grid(row=0,column=2,sticky=N,pady=5)
		
	def Option_men(self):
		#combobox self.scldpt options
		self.scldpt = ttk.Combobox(self.gframe1,values=self.options,textvariable=self.__dpt).grid(row=1,column=1,sticky=W)
	def Get_dt(self):
		self.dp=self.__dpt.get()
		self.__dpt.set(self.options[0])
		if self.lbfordoc!='':
			self.lbfordoc.grid_forget()
		if self.lbfordoc1!='':
			self.lbfordoc1.grid_forget()
		if self.lbfordoc2!='':
			self.lbfordoc2.grid_forget()
		if self.lb4!='':
			self.lb4.grid_forget()
		conn=cx_Oracle.connect('Hos','hos','XE')
		
		#jd=to_date(self.__j_date,'YYYY-MM-DD')
		cur=conn.cursor()

		cur.execute('select E_ID,Name,rank1 from employee natural join doctor where dept=:dp',{'dp':self.dp})
		rs = cur.fetchall()
		#print(i)
		if len(rs)!=0:
			#self.gframe=Canvas(self.mas,bg="plum",height=1000,width=1000)
			self.gframe2=Canvas(self.gframe1,bd=12,height=100,width=300,bg="orange")
			self.gframe2.grid(row=4,columnspan=3)
			self.mas.geometry("1000x700")	
			#self.gframe.configure(height=500,width=500)	
			self.gframe.place(x=80,y=80)
		 
			self.scrollbar = Scrollbar(self.gframe1,command=self.gframe2.yview)
			self.scrollbar.grid(row=4, column=3, sticky=NS)
			
			self.gframe2.configure(yscrollcommand=self.scrollbar.set)
			self.frame_1 = Frame(self.gframe2, bg="orange")
			self.frame_1.grid(row=-0,columnspan=3)
			self.gframe2.create_window((0, 0), window=self.frame_1, anchor='nw')
			count=1
			self.Label1()
			
			for i in rs:
				self.__ID=i[0]
				self.__Name=i[1]
				self.__Rank=i[2]
				self.lbfordoc=Label(self.frame_1 ,text=self.__ID,font=17,bg="orange",justify='center')
				self.lbfordoc.grid(row=count,column=0,sticky=N,pady=5)
				self.lbfordoc1=Label(self.frame_1 ,text=self.__Name,font=17,bg="orange",justify='center')
				self.lbfordoc1.grid(row=count,column=1,sticky=N,pady=5)
				self.lbfordoc2=Label(self.frame_1 ,text="    "+self.__Rank,font=17,bg="orange",justify='center')
				self.lbfordoc2.grid(row=count,column=2,sticky=N,pady=5)
				count+=1
					
				
		else:
			self.lb4=Label(self.gframe1,text="No data Found",font=17,bg="violet",justify='center').grid(row=4,sticky=N,pady=5,columnspan=3)	
		cur.close()
	
		conn.close()

		bbox = self.gframe2.bbox(ALL) 
		self.gframe1.config(row=4,height=count)
      
		self.gframe2.configure(scrollregion=bbox)

	def Exit(self):
		self.new_wd=Info_desk_menu(self.mas,self.nm)
		self.new_wd.Pack_all()     	
	def Button(self):
		self.but_search=Button(self.gframe1,text="Search",width=17,bd=4,bg='purple',fg ='white',command=self.Get_dt).grid(row=2,pady=5,columnspan=3)
		self.but_info=Button(self.gframe1,text="EXIT",width=20,bd=4,bg='purple',fg ='white',command=self.Exit).grid(row=self.r,pady=10,columnspan=3)

class Rep_Patient_record_menu(com_menu):
	def Pack_all(self):
		
		self.mas.title("Patient Record")	
		self.mas.geometry("1000x700")
		self.Grid()
		
		self.Variable()
		
		self.Label()
		self.Entry()
		self.Button()
		self.gframe.place(x=100,y=80)
		self.mas.mainloop()

	def Variable(self):		
		self.lbnam_e=''
		self.lbage_e=''
		self.lbgen_e=''
		self.lbad_da=''
		self.lbsic_e=''
		self.lward_e=''
		self.lbopre_e=''
		self.lbopda_e=''
		self.lbopti_e=''
		self.lboprm_e=''
		self.lbdoc_e=''
		self.lbf=''
		self.__pid=StringVar(self.mas)
	def Label(self):
		#self.lbnm=Label(self.gframe1,text="Name:",font=12,bg="violet",justify='center').grid(row=1,column=0,sticky=E)
		self.lbid=Label(self.gframe1,text="PID:",font=12,bg="violet",justify='center').grid(row=2,column=0,sticky=E)
		self.lbnmp=Label(self.gframe1,text="Name:",font=12,bg="violet",justify='center').grid(row=3,column=0,sticky=E)
		self.lbgen=Label(self.gframe1,text="Gender:",font=12,bg="violet",justify='center').grid(row=4,column=0,sticky=E)
		self.lbage=Label(self.gframe1,text="Age:",font=12,bg="violet",justify='center').grid(row=5,column=0,sticky=E)
		self.lbadmd=Label(self.gframe1,text="Admission Date:",font=12,bg="violet",justify='center').grid(row=6,column=0,sticky=E)
		self.lbscp=Label(self.gframe1,text="Sickness:",font=12,bg="violet",justify='center').grid(row=7,column=0,sticky=E)
		self.lbnward=Label(self.gframe1,text="Ward:",font=12,bg="violet",justify='center').grid(row=8,column=0,sticky=E)
		self.lbopp=Label(self.gframe1,text="Operation:",font=12,bg="violet",justify='center').grid(row=9,column=0,sticky=E)
		self.lbopdp=Label(self.gframe1,text="operation Date:",font=12,bg="violet",justify='center').grid(row=10,column=0,sticky=E)
		self.lbopti=Label(self.gframe1,text="operation time:",font=12,bg="violet",justify='center').grid(row=11,column=0,sticky=E)
		self.lboproom=Label(self.gframe1,text="operation Room:",font=12,bg="violet",justify='center').grid(row=12,column=0,sticky=E)
		self.lbmp=Label(self.gframe1,text="Doctor:",font=12,bg="violet",justify='center').grid(row=13,column=0,sticky=E)
	
	def Entry(self):

		self.entypid=Entry(self.gframe1,textvariable=self.__pid).grid(row=2,column=1,sticky=W)	
	def Button(self):

		#self.but_lp=Button(self.gframe1,text="List Of All Patient",width=17,bd=4,bg='purple',fg ='white').grid(row=0,columnspan=3)
		self.but_src=Button(self.gframe1,text="SEARCH",width=12,bd=4,bg='purple',fg ='white',command=self.Get_info).grid(row=2,column=2)
		self.but_ex=Button(self.gframe1,text="EXit",width=17,bd=4,bg='purple',fg ='white',command=self.Exit).grid(row=16,columnspan=3)
	def Get_info(self):
		self.pidd=self.__pid.get()
		self.__pid.set("")				
		
		if self.lbnam_e!='':
			self.lbnam_e.grid_forget()
		if self.lbage_e!='':
			self.lbage_e.grid_forget()
		if self.lbgen_e!='':
			self.lbgen_e.grid_forget()
		if self.lbad_da!='':
			self.lbad_da.grid_forget()
		if self.lbsic_e!='':
			self.lbsic_e.grid_forget()
		if self.lward_e!='':
			self.lward_e.grid_forget()
		if self.lbopre_e!='':
			self.lbopre_e.grid_forget()
		if self.lbopda_e!='':
			self.lbopda_e.grid_forget()
		if self.lbopti_e!='':
			self.lbopti_e.grid_forget()
		if self.lboprm_e!='':
			self.lboprm_e.grid_forget()
		if self.lbdoc_e!='':
			self.lbdoc_e.grid_forget()		
		if self.lbf!='':
			self.lbf.grid_forget()
		pattern=re.compile("(01)?[0-9]{9}")	
		if(pattern.match(self.pidd[3:14])):
			conn=cx_Oracle.connect('Hos','hos','XE')
			cur=conn.cursor()
			cur.execute('select * from Patient where PID=:pi',{'pi':self.pidd})

			conn.commit()	
			cur1=cur
			rs = cur.fetchall()
			cur=cur1
			print(rs)
			if(len(rs)!=0):	
				print(cur)
				for i in rs:
					print(i)
					
					self.lbnam_e=Label(self.gframe1,text=i[0],font=14,bg="violet",justify='center')
					self.lbnam_e.grid(row=3,column=1,sticky=W)
					self.lbage_e=Label(self.gframe1,text=i[2],font=14,bg="violet",justify='center')
					self.lbage_e.grid(row=5,column=1,sticky=W)
					self.lbgen_e=Label(self.gframe1,text=i[3],font=14,bg="violet",justify='center')
					self.lbgen_e.grid(row=4,column=1,sticky=W)
					self.lbad_da=Label(self.gframe1,text=i[4],font=14,bg="violet",justify='center')
					self.lbad_da.grid(row=6,column=1,sticky=W)
					self.lbsic_e=Label(self.gframe1,text=i[5],font=14,bg="violet",justify='center')
					self.lbsic_e.grid(row=7,column=1,sticky=W)
					self.lward_e=Label(self.gframe1,text=i[7],font=14,bg="violet",justify='center')
					self.lward_e.grid(row=8,column=1,sticky=W)
					self.lbopre_e=Label(self.gframe1,text=i[10],font=14,bg="violet",justify='center')
					self.lbopre_e.grid(row=9,column=1,sticky=W)
					if i[9]=="Required":
						
						self.lbopda_e=Label(self.gframe1,text=i[11],font=14,bg="violet",justify='center')
						self.lbopda_e.grid(row=10,column=1,sticky=W)
						self.lbopti_e=Label(self.gframe1,text=i[12],font=14,bg="violet",justify='center')
						self.lbopti_e.grid(row=11,column=1,sticky=W)
						self.lboprm_e=Label(self.gframe1,text=i[13],font=14,bg="violet",justify='center')
						self.lboprm_e.grid(row=12,column=1,sticky=W)
					self.lbdoc_e=Label(self.gframe1,text=i[9],font=14,bg="violet",justify='center')
					self.lbdoc_e.grid(row=13,column=1,sticky=W)
				cur.close()

			else:
				self.lbf=Label(self.gframe1,text="Patient not found.",font=14,bg="violet",justify='center')
				self.lbf.grid(row=14,columnspan=3)
			conn.close()
	def Exit(self):
		self.new_wd=Info_desk_menu(self.mas,self.nm)
		self.new_wd.Pack_all()   

class Patient_disc_menu(com_menu):
	def Pack_all(self):
		#self.__id=id1
		#print(self.__id)
		self.mas.title("Patient Discharge")	
		self.mas.geometry("1000x700")
		self.Grid()
		
		self.Variable()
		
		self.Label()
		self.Entry()
		self.Button()
		self.gframe.place(x=100,y=80)
		self.mas.mainloop()

	def Variable(self):	
		self.lbf=''	
		self.lbnam_e=''
		self.lbage_e=''
		self.lbgen_e=''
		self.lbad_da=''
		self.lbsic_e=''
		self.lbsic_e=''
		self.lward_e=''
		self.ltreat_e=''
		self.lbopre_e=''
		self.lbbill1=''
		self.but_pay=''
		self.lbnmp=''
		self.lbnag=''
		self.lbtotal=''
		self.lbngen=''
		self.wardcost=''
		self.lbOPcost=''
		self.lbbill=''
		self.addate=''
		self.treatment_cost=''
		self.sicness=''
		self.super=''
		self.lbdoc_e=''
		self.__pid=StringVar(self.mas)
	def Label(self):
		#self.lbnm=Label(self.gframe1,text="Name:",font=12,bg="violet",justify='center').grid(row=1,column=0,sticky=E)
		self.lbid=Label(self.gframe1,text="PID:",font=12,bg="violet",justify='center').grid(row=0,column=0,sticky=E)
		
	def Label_extra(self):
		self.lbnmp=Label(self.gframe1,text="Name:",font=12,bg="violet",justify='center')
		self.lbnmp.grid(row=1,column=0,sticky=E)
		self.lbnag=Label(self.gframe1,text="Age:",font=12,bg="violet",justify='center')
		self.lbnag.grid(row=2,column=0,sticky=E)
		self.lbngen=Label(self.gframe1,text="Gender:",font=12,bg="violet",justify='center')
		self.lbngen.grid(row=3,column=0,sticky=E)
		self.addate=Label(self.gframe1,text="Admission Date:",font=12,bg="violet",justify='center')
		self.addate.grid(row=4,column=0,sticky=E)
		self.super=Label(self.gframe1,text="Doctor:",font=12,bg="violet",justify='center')
		self.super.grid(row=5,column=0,sticky=E)
		self.sicness=Label(self.gframe1,text="Sickness:",font=12,bg="violet",justify='center')
		self.sicness.grid(row=6,column=0,sticky=E)
		self.lbtotal=Label(self.gframe1,text="Cost",font=12,bg="violet",justify='center')
		self.lbtotal.grid(row=7,column=2,sticky=W)
		#self.lbscp=Label(self.gframe1,text="Sickness:",font=12,bg="violet",justify='center').grid(row=4,column=0,sticky=E)
		self.wardcost=Label(self.gframe1,text="Ward Cost:",font=12,bg="violet",justify='center')
		self.wardcost.grid(row=8,column=0,sticky=E)
		self.treatment_cost=Label(self.gframe1,text="Treatment Cost:",font=12,bg="violet",justify='center')
		self.treatment_cost.grid(row=9,column=0,sticky=E)
		self.lbOPcost=Label(self.gframe1,text="Operation Cost:",font=12,bg="violet",justify='center')
		self.lbOPcost.grid(row=10,column=0,sticky=E)		
		self.lbbill=Label(self.gframe1,text="Bill:",font=12,bg="violet",justify='center')
		self.lbbill.grid(row=11,column=0,sticky=E)			
		
	def Entry(self):

		self.entypid=Entry(self.gframe1,textvariable=self.__pid).grid(row=0,column=1,sticky=W)	
	def Button(self):

		#self.but_lp=Button(self.gframe1,text="List Of All Patient",width=17,bd=4,bg='purple',fg ='white').grid(row=0,columnspan=3)
		self.but_src=Button(self.gframe1,text="SEARCH",width=12,bd=4,bg='purple',fg ='white',command=self.Get_rp).grid(row=0,column=2)
		self.but_ex=Button(self.gframe1,text="EXit",width=17,bd=4,bg='purple',fg ='white',command=self.Exit).grid(row=14,columnspan=3)
		
	def Get_rp(self):
		self.mas.geometry("1000x700")
		self.pidd=self.__pid.get()
		self.__pid.set("")
		#self.blood_pr=0
		#self.hg_pr=0
		self.op=0
		if self.lbnam_e!='':
			self.lbnam_e.grid_forget()
			self.lbnmp.grid_forget()
		if self.lbage_e!='':
			self.lbage_e.grid_forget()
			self.lbnag.grid_forget()
		if self.lbgen_e!='':
			self.lbgen_e.grid_forget()
			self.lbngen.grid_forget()
		if self.addate!='':
			self.addate.grid_forget()
		if self.super!='':
			self.super.grid_forget()
		if self.lbdoc_e!='':
			self.lbdoc_e.grid_forget()
		if self.sicness!='':
			self.sicness.grid_forget()
		if self.lbad_da!='':
			self.lbad_da.grid_forget()
		if self.lbsic_e!='':
			self.lbsic_e.grid_forget()
		if self.lbtotal!='':
			self.lbtotal.grid_forget()
		if self.wardcost!='':
			self.wardcost.grid_forget()
		if self.treatment_cost!='':
			self.treatment_cost.grid_forget()
		if self.lbOPcost!='':
			self.lbOPcost.grid_forget()
		if self.lbf!='':
			self.lbf.grid_forget()
		if self.lbbill1!='':
			self.lbbill1.grid_forget()
		if self.but_pay!='':
			self.but_pay.grid_forget()
		pattern=re.compile("(01)?[0-9]{9}")	
		if(pattern.match(self.pidd[3:14])):
			self.Label_extra()
			self.xdt=datetime.datetime.now()
			self.day=self.xdt.strftime("%d")
			self.mon=self.xdt.strftime("%b")
			self.year=self.xdt.strftime("%y")
			self.year=str(self.xdt.year)
			self.cdate=str(self.day)+'-'+str(self.mon)+'-'+self.year[-2:]
			conn=cx_Oracle.connect('Hos','hos','XE')
			cur=conn.cursor()
			cur.execute('select * from Patient where PID=:pi',{'pi':self.pidd})

			conn.commit()	
			cur1=cur
			rs = cur.fetchall()
			cur=cur1
			print(rs)
			
			if(len(rs)!=0):	
				self.b_i_l=rs[len(rs)-1]
				print(cur)
				for i in rs:
					print(i)
					
					self.lbnam_e=Label(self.gframe1,text=i[0],font=14,bg="violet",justify='center')
					self.lbnam_e.grid(row=1,column=1,sticky=W)
					self.lbage_e=Label(self.gframe1,text=i[2],font=14,bg="violet",justify='center')
					self.lbage_e.grid(row=2,column=1,sticky=W)
					self.lbgen_e=Label(self.gframe1,text=i[3],font=14,bg="violet",justify='center')
					self.lbgen_e.grid(row=3,column=1,sticky=W)
					self.lbad_da=Label(self.gframe1,text=i[4],font=14,bg="violet",justify='center')
					self.lbad_da.grid(row=4,column=1,sticky=W)
					self.lbdoc_e=Label(self.gframe1,text=i[9],font=14,bg="violet",justify='center')
					self.lbdoc_e.grid(row=5,column=1,sticky=W)
					self.lbsic_e=Label(self.gframe1,text=i[5],font=14,bg="violet",justify='center')
					self.lbsic_e.grid(row=6,column=1,sticky=W)
					cd1=datetime.datetime.strptime(self.cdate, '%d-%b-%y').strftime('%d/%m/%Y')
					admis_date=str(i[4])
					addd=admis_date[0:10]
					dddt=int(cd1[0:2])
					mmmo=int(cd1[3:5])
					yyr=int(cd1[6:])
					dddt1=int(addd[9:])
					mmmo1=int(addd[5:7])
					yyr1=int(addd[0:4])
					days_s=date(yyr,mmmo,dddt)-date(yyr1,mmmo1,dddt1)
					days_s1=int(days_s.days)
					self.cccostward=days_s1*500
					self.treaatcost=days_s1*1200
					print(days_s1)
					self.lward_e=Label(self.gframe1,text=self.cccostward,font=14,bg="violet",justify='center')
					self.lward_e.grid(row=8,column=2,sticky=W)
					self.ltreat_e=Label(self.gframe1,text=self.treaatcost,font=14,bg="violet",justify='center')
					self.ltreat_e.grid(row=9,column=2,sticky=W)				
			
					if i[10]=='Required':
						self.op=random.randint(10000,20000)
					self.lbopre_e=Label(self.gframe1,text=self.op,font=14,bg="violet",justify='center')
					self.lbopre_e.grid(row=10,column=2,sticky=W)
										
						
				self.lbbill1=Label(self.gframe1,text=self.cccostward+self.treaatcost+self.op,font=12,bg="violet",justify='center')
				self.lbbill1.grid(row=11,column=2,sticky=W)	
				cur.close()
				self.but_pay=Button(self.gframe1,text="Paid",width=12,bd=4,bg='purple',fg ='white',command=self.Pay)
				self.but_pay.grid(row=12,column=2)

			else:
					self.lbf=Label(self.gframe1,text="PID not found.",font=14,bg="violet",justify='center')
					self.lbf.grid(row=13,columnspan=3)
			conn.close()
		else:
			self.lbf=Label(self.gframe1,text="Invalid PID.",font=14,bg="violet",justify='center')
			self.lbf.grid(row=13,columnspan=3)						
	def Pay(self):

		if self.lbf!='':

			self.lbf.grid_forget()
		if self.b_i_l==None:
			conn=cx_Oracle.connect('Hos','hos','XE')
			cur=conn.cursor()
			cur.execute('UPDATE Patient SET Bill = :bl WHERE Pid =:bco',{'bl':self.cccostward+self.treaatcost+self.op,'bco':self.pidd})
			
			conn.commit()	
			cur.close()
			conn.close()	
			self.lbf=Label(self.gframe1,text="Successfuly Paid",font=14,bg="violet",justify='center')
			self.lbf.grid(row=13,columnspan=3)
		else:
			self.lbf=Label(self.gframe1,text="Bill is already Paid",font=14,bg="violet",justify='center')
			self.lbf.grid(row=13,columnspan=3)			
	
				
	def Exit(self):
		self.new_wd=Cash_menu(self.mas,self.nm)
		self.new_wd.Pack_all() 
a=Main_menu()
		
