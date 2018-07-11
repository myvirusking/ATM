from tkinter import *
from tkinter import messagebox
#print(dir(messagebox))


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

    #-------------btn cur or save account function-------------
    def go(self):
        ####################=============Query Here For find A/C Number=====================================
        self.user_ac_number = 12345
        
        try:
            input_ac_number = int(self.ac_number.get())
            if input_ac_number == self.user_ac_number:
                self.ac_number_frame.destroy()
                self.option_frame = Frame(self.root)
                self.option_frame.pack(side=TOP,pady=5)
                Button(self.option_frame,command = self.balanceEnquiry,text="BALANCE ENQUIRY",bg="lightblue",bd=5,width=25,font=( 'arial' ,20, 'bold' ),fg="green").pack(pady=20)
                Button(self.option_frame,command = self.deposit,text="DEPOSIT",bg="lightblue",bd=5,width=25,font=( 'arial' ,20, 'bold' ),fg="green").pack(pady=20)
                Button(self.option_frame,command = self.withdraw,text="WITHDRAW",bg="lightblue",bd=5,width=25,font=( 'arial' ,20, 'bold' ),fg="green").pack(pady=20)
                    
            else:
                messagebox.showinfo('Account Error' ,'Incorrect A/C No. : Please Enter Correct Account Number')
        except:
            messagebox.showinfo('Integer Error','Invalid Integer : Please Insert Valid Integer Account Number')


    #-------------Balance Enquiry---------------------
    def balanceEnquiry(self):
        self.option_frame.destroy()
        
        ####################=============Query Here For find detail of user=====================================
        name_user = "Ramulal Yadav"
        mobile_no_user = 8282828282
        
        detail = """
        A/C Number : {0}
        Name : {1}
        Mobile No. : {2}
        """.format(self.user_ac_number,name_user,mobile_no_user)
        Label(self.root,text=detail,font=( 'aria' ,15, 'italic' )).pack()
        
        ####################=============Query Here For find total amount of user account=====================================
        self.total_amount = 15000
        
        amount = "Total Amount = {0} INR. /-".format(self.total_amount)
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
        ####################=============Query Here For find pin of user account=====================================
        user_pin = 8282
        
        try:
            amount = int(self.amount.get())
            input_pin = int(self.pin.get())
            if input_pin == user_pin:
                messagebox.showinfo('Deposit' ,'{0} INR./- Successfully Deposit In Your Account'.format(amount))
                #self.balanceEnquiry()
                self.exit()
                
            else:
                messagebox.showinfo('Pin Error' ,'Incorrect Pin : Please Enter Correct Pin')
        except:
            messagebox.showinfo('Integer Error','Invalid Integer : Please Insert Valid Amount And Pin')


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
        ####################=============Query Here For find pin and total_amount of user account=====================================
        user_pin = 8282
        total_amount = 15000
        
        try:
            input_amount = int(self.amount.get())
            input_pin = int(self.pin.get())
            if input_pin == user_pin:
                if input_amount < total_amount:
                    messagebox.showinfo('Deposit' ,'{0} INR./- Successfully Withdraw From Your Account'.format(input_amount))
                    #self.balanceEnquiry()
                    self.exit()
                else:
                    messagebox.showinfo('Amount Error' ,'Amount Bounce : Please Enter Amount Below {0} INR./-'.format(total_amount))
            else:
                messagebox.showinfo('Pin Error' ,'Incorrect Pin : Please Enter Correct Pin')
        except:
            messagebox.showinfo('Integer Error','Invalid Integer : Please Insert Valid Amount And Pin')

    #-------------Exit function-------------------------------
    def exit(self):
        self.root.destroy()
        ATM_OBJ = ATM()

 

ATM_OBJ = ATM()
