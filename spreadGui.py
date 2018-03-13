from tkinter import *
import os
import numpy as np
import datetime
import csv
import random
from dateutil.relativedelta import relativedelta
import numpy as np
from tkinter import ttk 
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from googleapiclient import discovery
import gspread
from oauth2client.service_account import ServiceAccountCredentials
now=datetime.datetime.now()
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Prajeesh").sheet1
service = discovery.build('sheets', 'v4', credentials=creds)
spreadsheet_id = '1295q1iZNmqtJhm6-byfINaMipApV2uccUGQf6TuPAms'
range= 'Sheet1!A1:H3'
value_input_option ='USER_ENTERED'
global nameEL 
global pwordL
class mainwindow(object):
    def __init__(self,parent):
        
        self.parent=parent
        parent.title=("Login")
                
        self.intruction = Label(parent, text='Please Login\n')
        self.intruction.grid(sticky=E) 

        self.nameL = Label(parent, text='Username: ')
        self.pwordL = Label(parent, text='Password: ') 
        self.nameL.grid(row=1, sticky=W)
        self.pwordL.grid(row=2, sticky=W)

        self.nameEL = Entry(parent) 
        self.pwordL = Entry(parent, show='*')
        self.nameEL.grid(row=1, column=1)
        self.pwordL.grid(row=2, column=1)

        self.loginB = tk.Button(parent, text='Login', command=self.checkaccountl) 
        self.loginB.grid(columnspan=2, sticky=W)

        self.rmuser = Button(parent, text='signin',command=self.signup)
        self.rmuser.grid(columnspan=2, sticky=W)
        
        #rootA.configure(background='blue')
        
    def checkaccountl(self):
        global nameEL
        global pwordL 
        global input1
        global input2
        global input3
        global input4
        global val
        self.input1=self.nameEL.get()

        self.input3=self.pwordL.get()
        self.cell1=sheet.find(self.input1)
        self.c=("%s " %(self.cell1.row))
        self.s=("%s" %(self.cell1.col))
        self.x=int(self.c)
        self.z=int(self.s)+3
        self.input4 = sheet.cell(self.x,self.z).value
        self.cell2=sheet.findall(self.input3)
        if(self.cell1  and self.cell2):

            self.welcome()
            
        else:
                

        
            self.pop()
    
    def signup(self):
        global nameE
        global pwordE
        global emailE
        global roots

        roots = Tk()
        self.number=tk.StringVar()
        self.k = 300 
        self.s = 150

        self.wk = roots.winfo_screenwidth() 
        self.hw = roots.winfo_screenheight()
        self.z = (self.wk/2) - (self.k/2)
        self.u = (self.hw/2) - (self.s/2) 
        roots.title('Signup') 
        self.intruction = Label(roots, text='Please Enter new Credidentials\n') 
        self.intruction.grid(row=0, column=0, sticky=E)


        self.nameL = Label(roots, text='New Username: ')
        self.emailL = Label(roots, text='EMAIL: ')
        self.pwordL = Label(roots, text='New Password: ')
        self.nameL.grid(row=1, column=0, sticky=W) 
        self.emailL.grid(row=2,column=0,sticky=W)
        self.pwordL.grid(row=3, column=0, sticky=W)

        self.nameE = Entry(roots)
        self.emailE = Entry(roots)
        self.pwordE = Entry(roots, show='*') 
        self.nameE.grid(row=1, column=1)
        self.emailE.grid(row=2,column=1)
        self.pwordE.grid(row=3, column=1) 

        self.signupButton = Button(roots, text='Signup',command=self.checkaccounts)
        self.signupButton.grid(columnspan=2, sticky=W)
        roots.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
        roots.mainloop() 
    def entryframe1(self): 
        global nameE
        global emailE
        global pwordE
        self.input1=self.nameE.get()
        self.input2=self.emailE.get()
        self.input3=self.pwordE.get()
        global input4
        self.input4=random.randint(1001,10001)

        value_range_body={
        "majorDimension":"ROWS",
        "values":[[self.input1,self.input3,self.input2,self.input4,now.strftime("%Y"),now.strftime("%m"),now.strftime("%d"),now.strftime("%H:%M")]]
            

        
        }
        request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, valueInputOption=value_input_option,range=range,  body=value_range_body)
        response = request.execute()
        self.welcome()
    def entryframe2(self): 
        global input4
        self.input1=self.incomeEL.get()
        self.input2=self.expenseEL.get()
        self.input3=self.number_chosen.get()
        self.savings=int(self.input1)-int(self.input2)

        with open( 'C:\\Users\\USER\\Untitled Folder 1\\{0}__NIGHT.csv'.format(self.input4),"a") as work:
           self.workw=csv.writer(work)
           self.workw.writerow([now.strftime("%Y"),now.strftime("%m"),now.strftime("%d"),now.strftime("%H:%M"),self.input1,self.input3,self.input2,self.savings])
           work.close()
        self.welcome()    
    def display(self):
        global input4
        print(self.input4)
        with open( 'C:\\Users\\USER\\Untitled Folder 1\\{0}__NIGHT.csv'.format(self.input4),"r") as work:
            self.hii= pd.read_csv(work)
            self.df =pd. DataFrame(self.hii)
            self.dfList1 = self.df['EXPENSE'].tolist()
            self.dfList2 = self.df['SAVINGS'].tolist()
            self.dfList3 = self.df['INCOME'].tolist()
            self.arr=[]
            self.srr=[]

            
            self.savings=0
            self.expense=0
            
            self.objects=['EXPENSE','SAVINGS']
            for p in self.dfList1: self.expense+=p
                
            for p in self.dfList2: self.savings+=p
            
            self.performance=[self.expense,self.savings]   
            self.y_pos = np.arange(len(self.objects))
            plt.bar(self.y_pos, self.performance, align='center', alpha=1)
            plt.xticks(self.y_pos, self.objects)
            plt.ylabel('INCOME')
            plt.title('REPORTS')
            plt.show()




    def entry(self):
        global nameEL
        global incomeEL
        global expenseEL
        global input4
        global number_chosen
        


        rootC = Tk() 
        rootC.title('Expense Tracker')
        self.intruction = Label(rootC, text='Add expense\n')
        self.intruction.grid(sticky=E)

        self.number=tk.StringVar()
        self.k = 250  # width for the Tk root
        self.s = 150  # height for the Tk root

        self.wk = rootC.winfo_screenwidth()  # width of the screen
        self.hw = rootC.winfo_screenheight()  # height of t 
        self.z = (self.wk/2) - (self.k/2)
        self.u = (self.hw/2) - (self.s/2)
        ttk.Label(rootC,text="category :").grid(row=1,sticky=W) 
        self.incomeL = Label(rootC, text='income : ')
        self.expenseL = Label(rootC, text='expense : ')

        self.incomeL.grid(row=2, sticky=W)
        self.expenseL.grid(row=3, sticky=W)

        self.number_chosen=ttk.Combobox(rootC,width=12,textvariable=self.number,state='readonly')
        self.number_chosen['values']=('Travel','Internet','Entertainment','Food','otherexpense')
        self.incomeEL = Entry(rootC) 
        self.expenseEL = Entry(rootC)

        self.number_chosen.grid(row=1,column=1)
        self.number_chosen.current(0)
        self.incomeEL.grid(row=2, column=1)
        self.expenseEL.grid(row=3, column=1)
        self.save = Button(rootC, text='Save',command=self.entryframe2) 
        self.save.grid(columnspan=2, sticky=W)
        rootC.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
        rootC.mainloop()        

    def welcome(self):
        global nameEL
        global pwordEL
        rootB = Tk() 
        rootB.title('Login')
        self.k = 250 # width for the Tk root
        self.s = 150 # height for the Tk root

        self.wk = rootB.winfo_screenwidth() # width of the screen
        self.hw = rootB.winfo_screenheight() # height of t 
        self.z = (self.wk/2) - (self.k/2)
        self.u = (self.hw/2) - (self.s/2)
        self.label1 = Label(rootB,text="WELCOME!")
        self.label1.grid(sticky=E)
        self.button1=Button( rootB,text="   REPORT   ",command=self.display)
        self.button1.grid(columnspan=2, sticky=W,row=1, column=1)
        self.button2=Button( rootB,text="MAKE AN ENTRY",command=self.entry)
        self.button2.grid(columnspan=2, sticky=W,row=2, column=1)
        rootB.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
        rootB.mainloop()
    def checkaccounts(self):
        global nameE
        global pwordE
        global emailE
        global input1
        global input2
        global input3
        self.input1=self.nameE.get()
        self.input2=self.emailE.get()
        self.input3=self.pwordE.get()
        if(sheet.findall(self.input1) and sheet.findall(self.input3)):
            self.popup()
        else:
             self.entryframe1()    

    

    def appe(self):
        with open("signup.csv","w") as work:
            self.workw=csv.writer(work)
            self.workw.writerow(['YEAR','MONTH','DAY','TIME','NAME','EMAIL','PASSWORD','RANDOMID'])
            work.close()


    def popup(self):
        r = Tk()
        self.k = 250 # width for the Tk root
        self.s = 100 # height for the Tk root

        self.wk = r.winfo_screenwidth() # width of the screen
        self.hw = r.winfo_screenheight() # height of t 
        self.z = (self.wk/2) - (self.k/2)
        self.u = (self.hw/2) - (self.s/2)
        r.title('Invalid USER:')
        self.rlbl = Label(r, text='\n[!] Invalid username and password')
        self.rlbl.pack()
        r.geometry('%dx%d+%d+%d' % (self.k, self.s, self.z, self.u))
        r.mainloop()
        
root=tk.Tk()
root.title("login")
w = 200 # width for the Tk root
h = 150 # height for the Tk root
ws =root.winfo_screenwidth() # width of the screen
hs =root.winfo_screenheight() # height of t 
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
my_gui=mainwindow(root)
root.mainloop()
