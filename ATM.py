from tkinter import *
from tkinter import messagebox
from mysql import connector

db=connector.connect(user='root',host='localhost',database='atm')
if db:
    print("Databse Connected Successfully")

#Trigger code--------------------------------------
##try:
##    cur=db.cursor()
##    cur.execute("drop trigger if exists after_update_account_holder;")
##    cur.execute("""create trigger after_update_account_holder
##    after update on account_holder
##    for each row
##    begin
##    IF new.last_status = 'withdraw' THEN
##    INSERT into transaction(account_number,current_balance,withdraw_amount) values(old.account_number,new.total_balance,new.last_withdraw);
##    ELSEIF new.last_status = 'deposit' THEN
##    INSERT into transaction(account_number,current_balance,deposit_amount) values(old.account_number,new.total_balance,new.last_deposit);
##    END IF;
##    end
##    """)
##    cur.close()
##    db.close()
##    print("successfull created trigger")
##except Exception as e:
##    messagebox.showwarning('Warning',e)
    


class ATM:
    def __init__(self):
        #-------------root configuration--------------------
        root = Tk()
        screen_width=root.winfo_screenwidth()
        screen_height=root.winfo_screenheight()
        print(screen_width,"*",screen_height)
        root.geometry('{0}x{1}+{2}+{3}'.format((screen_width//2)- 50 ,screen_height//2,screen_width//4,(screen_height//4)-50))
        root.title('ATM')
        root.resizable(width=False, height=False)
        self.root =  root
        ##----------------Database Connection--------------------
        self.db=connector.connect(user='root',host='localhost',database='atm')
        self.cur=self.db.cursor()
        self.name_user      = None
        self.user_ac_number = None
        self.mobile_no_user = None
        self.total_amount   = None
        self.user_pin       = None


        #-------------Heading and fucntion calling----------------
        heading = Label(self.root,text="ATM",font=( 'aria' ,30, 'bold' ),fg='green')
        heading.pack()
        hr=Frame(self.root,height=3,width=screen_width//2,bg="lightgreen")
        hr.pack(side=TOP,pady=5)
        self.acNumber()

        self.root.mainloop()

    #-------------account number input------------------------ 
    def acNumber(self):
        self.ac_number = StringVar()
        self.ac_number_frame = Frame(self.root)
        self.ac_number_frame.pack(side=TOP,pady=50)
        Label(self.ac_number_frame,text="Enter You Account Number : ",font=( 'aria' ,20, 'italic' )).pack(pady=5)
        Entry(self.ac_number_frame,relief=RIDGE,bd=4,width=30,justify="center",font=( 'aria' ,20),textvariable=self.ac_number).pack()
        Button(self.ac_number_frame,command=self.go,text="Saving Account",bg="lightblue",fg="green",bd=5,width=20,font=( 'aria' ,12,'bold')).pack(pady=10)
        Button(self.ac_number_frame,command=self.go,text="Current Account",bg="lightblue",fg="green",bd=5,width=20,font=( 'aria' ,12,'bold')).pack(pady=10)
        Button(self.ac_number_frame,text="EXIT",command=self.mainExit,width=10,bd=7,bg="lightgreen",font=( 'aria' ,7,'bold')).pack(pady=5)

    #-------------btn cur or save account function-------------
    def go(self):       
        try:
            input_ac_number = int(self.ac_number.get())
            #####################=======Query Here For find user details =======
            self.cur.execute("select name,account_number,mobile_no,total_balance,pin from account_holder where account_number = {0}".format(input_ac_number))
            data = self.cur.fetchone()
            if data:
                self.name_user      = data[0]
                self.user_ac_number = data[1]
                self.mobile_no_user = data[2]
                self.total_amount   = data[3]
                self.user_pin       = data[4]
            #####################=======END Query===============================
                
            if input_ac_number == self.user_ac_number:
                self.ac_number_frame.destroy()
                self.option_frame = Frame(self.root)
                self.option_frame.pack(side=TOP,pady=5)
                Button(self.option_frame,command = self.balanceEnquiry,text="BALANCE ENQUIRY",bg="lightblue",bd=5,width=25,font=( 'arial' ,20, 'bold' ),fg="green").pack(pady=20)
                Button(self.option_frame,command = self.deposit,text="DEPOSIT",bg="lightblue",bd=5,width=25,font=( 'arial' ,20, 'bold' ),fg="green").pack(pady=20)
                Button(self.option_frame,command = self.withdraw,text="WITHDRAW",bg="lightblue",bd=5,width=25,font=( 'arial' ,20, 'bold' ),fg="green").pack(pady=20)
                    
            else:
                messagebox.showerror('Account Error' ,'Incorrect A/C No. : Please Enter Correct Account Number')
        except Exception as e:
            #messagebox.showwarning('Integer Error','Invalid Integer : Please Insert Valid Integer Account Number')
            messagebox.showwarning('Warning',e)

    #-------------Balance Enquiry---------------------
    def balanceEnquiry(self):
        self.option_frame.destroy()
        detail = """
        A/C Number : {0}
        Name : {1}
        Mobile No. : {2}
        """.format(self.user_ac_number,self.name_user,self.mobile_no_user)
        amount = "Current Amount = {0} INR. /-".format(self.total_amount)
        
        Label(self.root,text=detail,font=( 'aria' ,15, 'italic' )).pack()
        Label(self.root,text=amount,font=( 'aria' ,25, 'italic' )).pack(pady=10)
        Button(self.root,command = self.exit,text="EXIT",bg="lightgreen",bd=5,width=10,font=( 'arial' ,15, 'bold' )).pack(pady=15)

    

    #-------------Deposit-------------------------------
    def deposit(self):
        self.option_frame.destroy()
        self.option_frame = Frame(self.root)
        self.option_frame.pack(side=TOP,pady=10)
        
        Label(self.option_frame,text="Enter Amount (INR)",font=( 'aria' ,15, 'italic' )).pack()
        self.amount = StringVar()
        Entry(self.option_frame,relief=RIDGE,bd=4,width=20,justify="center",font=( 'aria' ,15),textvariable=self.amount).pack(pady=5)
        Label(self.option_frame,text="Enter PIN",font=( 'aria' ,15, 'italic')).pack(pady=5)
        self.pin = StringVar()
        Entry(self.option_frame,show="*",relief=RIDGE,bd=4,width=20,justify="center",font=( 'aria' ,15),textvariable=self.pin).pack()
        Button(self.option_frame,command = self.depositAmount,text="DEPOSIT",bg="lightgreen",bd=5,width=10,font=( 'arial' ,15, 'bold' )).pack(pady=20)
        Button(self.option_frame,command = self.exit,text="EXIT",bg="lightgreen",bd=5,width=10,font=( 'arial' ,15, 'bold' )).pack()

    def depositAmount(self):  
        try:
            amount = int(self.amount.get())
            input_pin = int(self.pin.get())
            if input_pin == self.user_pin:
                self.cur.execute("update account_holder set total_balance = total_balance + {0},last_deposit = {2},last_status = 'deposit'  where account_number = {1}".format(amount,self.user_ac_number,amount))
                self.db.commit()
                messagebox.showinfo('Deposit' ,'{0} INR./- Successfully Deposit In Your Account'.format(amount))
                #self.balanceEnquiry()
                self.exit()
                
            else:
                self.pin.set("")
                messagebox.showerror('Pin Error' ,'Incorrect Pin : Please Enter Correct Pin')
        except Exception as e:
            #messagebox.showwarning('Integer Error','Invalid Integer : Please Insert Valid Amount And Pin')
            messagebox.showwarning('Warning',e)
            


    #-------------Withdraw-------------------------------
    def withdraw(self):
        self.option_frame.destroy()
        self.option_frame = Frame(self.root)
        self.option_frame.pack(side=TOP,pady=10)
        
        Label(self.option_frame,text="Enter Amount (INR)",font=( 'aria' ,15, 'italic' )).pack()
        self.amount = StringVar()
        Entry(self.option_frame,relief=RIDGE,bd=4,width=20,justify="center",font=( 'aria' ,15),textvariable=self.amount).pack(pady=5)
        Label(self.option_frame,text="Enter PIN",font=( 'aria' ,15, 'italic')).pack(pady=5)
        self.pin = StringVar()
        Entry(self.option_frame,show="*",relief=RIDGE,bd=4,width=20,justify="center",font=( 'aria' ,15),textvariable=self.pin).pack()
        Button(self.option_frame,command = self.withdrawAmount,text="WITHDRAW",bg="lightgreen",bd=5,width=10,font=( 'arial' ,15, 'bold' )).pack(pady=20)
        Button(self.option_frame,command = self.exit,text="EXIT",bg="lightgreen",bd=5,width=10,font=( 'arial' ,15, 'bold' )).pack()


    def withdrawAmount(self):  
        try:
            input_amount = int(self.amount.get())
            input_pin = int(self.pin.get())
            if input_pin == self.user_pin:
                if input_amount < self.total_amount:
                    self.cur.execute("update account_holder set total_balance = total_balance - {0},last_withdraw = {2},last_status = 'withdraw' where account_number = {1}".format(input_amount,self.user_ac_number,input_amount))
                    self.db.commit()
                    messagebox.showinfo('Deposit' ,'{0} INR./- Successfully Withdraw From Your Account'.format(input_amount))
                    #self.balanceEnquiry()
                    self.exit()
                else:
                    self.amount.set("")
                    messagebox.showinfo('Amount Error' ,'Amount Bounce : Please Enter Amount Below {0} INR./-'.format(self.total_amount))
            else:
                self.pin.set("")
                messagebox.showerror('Pin Error' ,'Incorrect Pin : Please Enter Correct Pin')
        except Exception as e:
            #messagebox.showwarning('Integer Error','Invalid Integer : Please Insert Valid Amount And Pin')
            messagebox.showwarning('Warning',e)

    #-------------Exit function-------------------------------
    def exit(self):
        self.root.destroy()
        ATM_OBJ = ATM()

    def mainExit(self):
        self.cur.close()
        self.db.close()
        self.root.destroy()

ATM_OBJ = ATM()
