# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 10:38:44 2022

@author: compusoft

"""
from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk

global win1
win1=Tk()

class product:
    def __init__(self,win3):
        self.win3=win3
        self.win3.title('PHARMACY MANAGMENT SYSTEM')
        width=1300
        height=600
        screenwidth=self.win3.winfo_screenwidth()
        screenheight=self.win3.winfo_screenheight()
        x=int((screenwidth-width)/2)
        y=int((screenheight-height)/2)
        self.win3.geometry(f"{width}x{height}+{x}+{y}")
        self.win3.resizable(False,False)
        self.win3.config(background='white')
        
        self.IDVar=IntVar()
        self.NameVar=StringVar()
        self.dateVar=StringVar()
        self.exdateVar=StringVar()
        self.priceVar=StringVar()
        self.conpriceVar=StringVar()
        
        self.IDVar.set('')
        
        frame3= Frame(self.win3 , width='1300',height='600',background='#2874a6')
        frame3.place(x=1,y=1)
        
        frame4= Frame(self.win3 , width='1300',height='100',background='#BDBDBD')
        frame4.place(x=1,y=1)
        
        mainlabel=Label(frame4,text='Pharmacy Managment System',background='#BDBDBD',fg='black',font=('center',30,'bold'))
        mainlabel.place(x=380,y=30)
        
        frame5= Frame(self.win3 , width='400',height='330',background='#BDBDBD')
        frame5.place(x=5,y=120)
        
        idlabel=Label(frame5,text='ID', width='12',height='1',background='#BDBDBD',font=20).place(x=1 ,y=20)
        ent1=Entry(frame5,justify='left', bg='white',fg='black',width='30',textvar=self.IDVar).place(x=150,y=20)
        
        namelabel=Label(frame5,text='Product Name', width='12',height='1',background='#BDBDBD',font=12).place(x=1 ,y=70)
        ent2=Entry(frame5,justify='left', bg='white',fg='black',width='30',textvar=self.NameVar).place(x=150,y=70)
        
        datelabel=Label(frame5,text='Product Date', width='12',height='1',background='#BDBDBD',font=12).place(x=1 ,y=120)
        ent3=Entry(frame5,justify='left', bg='white',fg='black',width='30',textvar=self.dateVar).place(x=150,y=120)
        
        explabel=Label(frame5,text='Expiration Date', width='12',height='1',background='#BDBDBD',font=12).place(x=1 ,y=170)
        ent4=Entry(frame5,justify='left', bg='white',fg='black',width='30',textvar=self.exdateVar).place(x=150,y=170)
        
        pricelabel=Label(frame5,text='Price', width='12',height='1',background='#BDBDBD',font=12).place(x=1 ,y=220)
        ent5=Entry(frame5,justify='left', bg='white',fg='black',width='30',textvar=self.priceVar).place(x=150,y=220)
        
        conlabel=Label(frame5,text='Consumer Price', width='12',height='1',background='#BDBDBD',font=12).place(x=1 ,y=270)
        ent6=Entry(frame5,justify='left', bg='white',fg='black',width='30',textvar=self.conpriceVar).place(x=150,y=270)
        
        frame6=Frame(self.win3 , width='880',height='330',background='#BDBDBD')
        frame6.place(x=412,y=120)
        
        scroll_x=Scrollbar(frame6,orient=HORIZONTAL)
        scroll_y=Scrollbar(frame6,orient=VERTICAL)
        
        self.table=ttk.Treeview(frame6,
        columns=('ID','Name','Date','Expiration Date','Price','Consumer Price'),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)
        self.table.place(x=1,y=1,width=865,height=315)
    
        '''scroll_x.pack(side='bottom',fill='x')
        scroll_y.pack(side='right',fill='y')'''
        
        scroll_x.config(command=self.table.xview)
        scroll_y.config(command=self.table.yview)

        self.table['show']='headings'
        self.table.heading('ID',text='ID')
        self.table.heading('Name',text='Name')
        self.table.heading('Date',text='Date')
        self.table.heading('Expiration Date',text='Expiration Date')
        self.table.heading('Price',text='Price')
        self.table.heading('Consumer Price',text='Consumer Price')
        
        self.table.column('ID',width=100)
        self.table.column('Name',width=100)
        self.table.column('Date',width=100)
        self.table.column('Expiration Date',width=100)
        self.table.column('Price',width=100)
        self.table.column('Consumer Price',width=100)
        self.table.bind("<ButtonRelease-1>",self.get_cursor)
        
        frame7=Frame(self.win3 , width='1280',height='130',background='#BDBDBD')
        frame7.place(x=10,y=460)
        
        bt1=Button(frame7 ,text='Add',width=15,height=3,font=20,background='white' ,fg='black',command=self.add_product )
        bt1.place(x=20, y=15)
        
        bt2=Button(frame7 ,text='Delete',width=15,height=3,font=20,background='white' ,fg='black',command=self.delete )
        bt2.place(x=220, y=15)
        
        bt3=Button(frame7 ,text='Update',width=15,height=3,font=20,background='white' ,fg='black' ,command=self.update)
        bt3.place(x=420, y=15)
        
        bt4=Button(frame7 ,text='Reset',width=15,height=3,font=20,background='white' ,fg='black',command=self.clear )
        bt4.place(x=620, y=15)
        
        bt5=Button(frame7 ,text='Exit',width=15,height=3,font=20,background='white' ,fg='black',command=win3.quit)
        bt5.place(x=820, y=15)
        
        
        self.fetch_all()
    def add_product(self):
        con=sqlite3.connect('pharmacy.db')
        with con:
            c=con.cursor()
        c.execute(''' create table if not exists product(
        pro_id integer PRIMARY KEY NOT NULL,
        pro_name text NOT NULL,
        date text NOT NULL,
        expiration_date text NOT NULL,
        price text NOT NULL,
        consumer_price text NOT NULL)''')
        c.execute('insert into product(pro_id,pro_name,date,expiration_date,price,consumer_price)values(?,?,?,?,?,?)',
        (self.IDVar.get(),self.NameVar.get(),self.dateVar.get(),self.exdateVar.get(),self.priceVar.get(),self.conpriceVar.get()))
        con.commit()
        self.fetch_all()
        self.clear()
        
    
    def fetch_all(self):
        con=sqlite3.connect('pharmacy.db')
        with con:
             c=con.cursor()
        c.execute(''' create table if not exists product(
        pro_id integer PRIMARY KEY NOT NULL,
        Pro_name text NOT NULL,
        date text NOT NULL,
        expiration_date text NOT NULL,
        price text NOT NULL,
        consumer_price text NOT NULL)''')
        c.execute('select * from product')
        rows=c.fetchall()
        if len(rows) != 0:
            self.table.delete(* self.table.get_children())
            for row in rows:
                self.table.insert("",END,value=row)
            con.commit()
            
            
    def delete(self):
        con=sqlite3.connect('pharmacy.db')
        with con:
             c=con.cursor()
        c.execute(''' create table if not exists product(
        pro_id integer PRIMARY KEY NOT NULL,
        pro_name text NOT NULL,
        date text NOT NULL,
        expiration_date text NOT NULL,
        price text NOT NULL,
        consumer_price text NOT NULL)''')
        c.execute('delete from product where pro_id=? and pro_name=? and date=? and expiration_date=? and price=? and consumer_price=?',
                  (self.IDVar.get(),self.NameVar.get(),self.dateVar.get(),self.exdateVar.get(),self.priceVar.get(),self.conpriceVar.get()))
        con.commit()
        self.fetch_all()
        self.clear()
        
        
    def clear(self):
        self.IDVar.set('')
        self.NameVar.set('')
        self.dateVar.set('')
        self.exdateVar.set('')
        self.priceVar.set('')
        self.conpriceVar.set('')
        
        
    def get_cursor(self,ev):
        cursor_row=self.table.focus()
        contents=self.table.item(cursor_row)
        row=contents['values']
        self.IDVar.set(row[0])
        self.NameVar.set(row[1])
        self.dateVar.set(row[2])
        self.exdateVar.set(row[3])
        self.priceVar.set(row[4])
        self.conpriceVar.set(row[5])
        
    
    def update(self):
        con=sqlite3.connect('pharmacy.db')
        with con:
             c=con.cursor()
        c.execute(''' create table if not exists product(
        pro_id integer PRIMARY KEY NOT NULL,
        pro_name text NOT NULL,
        date text NOT NULL,
        expiration_date text NOT NULL,
        price text NOT NULL,
        consumer_price text NOT NULL)''')
        c.execute('update product set pro_name=? , date=? , expiration_date=? , price=? , consumer_price=? where pro_id=?',
                  (self.NameVar.get(),self.dateVar.get(),self.exdateVar.get(),self.priceVar.get(),self.conpriceVar.get(),self.IDVar.get()))
        con.commit()
        self.fetch_all()
        self.clear()
        

win1.title('PHARMACY MANAGMENT SYSTEM')
width=600
height=600
screenwidth=win1.winfo_screenwidth()
screenheight=win1.winfo_screenheight()
x=int((screenwidth-width)/2)
y=int((screenheight-height)/2)
win1.geometry(f"{width}x{height}+{x}+{y}")
win1.resizable(False,False)
win1.config(background='#BDBDBD')

idVar=IntVar()
nameVar=StringVar()
usernameVar=StringVar()
passVar=StringVar()

idVar.set('')
    
def addnew():
    con=sqlite3.connect('pharmacy.db')
    with con:
        c=con.cursor()
    c.execute(''' create table if not exists doctor(
    dr_id integer PRIMARY KEY NOT NULL,
    dr_name text NOT NULL,
    username text NOT NULL,
    password text NOT NULL)''')
    count=c.execute('insert into doctor(dr_id,dr_name,username,password)values(?,?,?,?)',
                    (idVar.get(),nameVar.get(),usernameVar.get(),passVar.get()))
    if(c.rowcount>0):
        messagebox.showinfo('', 'Signup Done')
    else:
        messagebox.showinfo('', 'Signup Error')
    con.commit()
    
               
def login():
    con=sqlite3.connect('pharmacy.db')
    with con:
        c=con.cursor()
    c.execute(''' create table if not exists doctor(
    dr_id integer PRIMARY KEY NOT NULL,
    dr_name text NOT NULL,
    username text NOT NULL,
    password text NOT NULL)''')
    c.execute('Select * from doctor Where username=? AND password=?',(usernameVar.get(),passVar.get()))
    if c.fetchone() is not None:
        messagebox.showinfo('', 'Welcome')
        win3=Toplevel(win1)
        pro=product(win3)
    else:
        messagebox.showinfo('', 'Login Failed')
    con.commit()
        
       
def register():
    win2=Toplevel(win1)
    win2.title('PHARMACY MANAGMENT SYSTEM')
    width=600
    height=600
    screenwidth=win2.winfo_screenwidth()
    screenheight=win2.winfo_screenheight()
    x=int((screenwidth-width)/2)
    y=int((screenheight-height)/2)
    win2.geometry(f"{width}x{height}+{x}+{y}")
    win2.resizable(False,False)
    win2.config(background='#BDBDBD')
    frame2= Frame(win2 , width='500',height='500',background='#2874a6')
    frame2.place(x=50,y=35)
    ##283593 الازرق
    #BDBDBD الرصاصي
    label=Label(frame2,text='SIGN UP',background='#2874a6',fg='black',font=('center',24,'bold')).place(x=190,y=30)
    
    label1=Label(frame2,text='ID:',background='#2874a6',fg='black',font=('center',18,'bold')).place(x=30,y=100)
    en1=Entry(frame2,justify='left', bg='white',fg='black',width='30',textvar=idVar).place(x=200,y=108)
    
    label2=Label(frame2,text='Name:',background='#2874a6',fg='black',font=('center',18,'bold')).place(x=30,y=160)
    en2=Entry(frame2,justify='left', bg='white',fg='black',width='30',textvar=nameVar).place(x=200,y=168)
    
    label3=Label(frame2,text='User name:',background='#2874a6',fg='black',font=('center',18,'bold')).place(x=30,y=220)
    en3=Entry(frame2,justify='left', bg='white',fg='black',width='30',textvar=usernameVar).place(x=200,y=228)
    
    label4=Label(frame2,text='Password:',background='#2874a6',fg='black',font=('center',18,'bold')).place(x=30,y=280)
    en4=Entry(frame2,justify='left', bg='white',fg='black',width='30',show='*',textvar=passVar).place(x=200,y=290)

    bu1=Button(frame2 ,text=' SIGN UP ',width='15',height='2',font=('center',11,'bold'),background='white' ,fg='black',command=addnew)
    bu1.place(x=170, y=400)


frame1= Frame(win1 , width='500',height='500',background='#2874a6')
frame1.place(x=50,y=35)

lab1=Label(frame1,text='LOG IN',font=('center',24,'bold'),background='#2874a6').place(x=180 ,y=40)

lab2=Label(frame1,text='USERNAME  :', width='18',height='0',background='white',font=('center',12,'bold')).place(x=10 ,y=150)
e1=Entry(frame1,justify='left', bg='white',fg='black',width='30',textvar=usernameVar).place(x=230,y=150)

lab3=Label(frame1,text='PASSWORD  :', width='18',height='0',background='white',font=('center',12,'bold')).place(x=10 ,y=240)
e2=Entry(frame1,justify='left', bg='white',fg='black',width='30',show='*',textvar=passVar).place(x=230,y=240)

b1=Button(frame1 ,text=' LOG IN ',width='15',height='2',font=('center',12,'bold'),background='white' ,fg='black' ,command=login)
b1.place(x=40, y=400)
b2=Button(frame1 ,text=' SIGN UP ',width='15',height='2',font=('center',12,'bold'),background='white' ,fg='black' ,command=register)
b2.place(x=300, y=400)

win1.mainloop()
