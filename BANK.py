from tkinter import *
from tkinter import messagebox
from mysql import connector

db=connector.connect(user='root',host='localhost',database='atm')
if db:
    print("Databse Connected Successfully")

#Procedure code------------------------------------------------------------------
##    
##try:
##    cur=db.cursor()
##    cur.execute("drop procedure if exists create_account;")
##    cur.execute("""create procedure create_account(In name varchar(50),IN account_number int,In pin int,IN address varchar(100),IN mobile_no int,IN ifsc_code varchar(11))
##    begin
##    insert into account_holder(name,account_number,pin,address,mobile_no,ifsc_code)
##    values (name,account_number,pin,address,mobile_no,ifsc_code);
##    end
##    """)
##    cur.close()
##    db.close()
##    print("successfull created procedure")
##except Exception as e:
##    messagebox.showwarning('Warning',e)




#-------------root configuration--------------------
root = Tk()
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
print(screen_width,"*",screen_height)
root.geometry('{0}x{1}+{2}+{3}'.format((screen_width//2)- 150 ,(screen_height//2)+200,(screen_width//4)+50,(screen_height//4)-150))
root.title('ATM')
root.resizable(width=False, height=False)

heading = Label(root,text="Create Account To Access ATM",font=( 'aria' ,30, 'bold' ),fg='green')
heading.pack()
hr=Frame(root,height=3,width=screen_width//2,bg="lightgreen")
hr.pack(side=TOP,pady=5)

main_frame = Frame(root)
main_frame.pack()

name = StringVar()
ac_number = StringVar()
pin = StringVar()
address = StringVar()
mb_number = StringVar()
ifsc_code = StringVar()



#=====================Database Query=================
db=connector.connect(user='root',host='localhost',database='atm')
cur=db.cursor()

def reset():
    name.set("")
    ac_number.set("")
    pin.set("")
    address.set("")
    mb_number.set("")
    ifsc_code.set("")

def exit():
    cur.close()
    db.close()
    root.destroy()

def submit():
    try:
        input_name = str(name.get())
        input_ac_number = ac_number.get()
        input_pin = pin.get()
        input_address = address.get()
        input_mb_number = mb_number.get()
        input_ifsc_code = ifsc_code.get()
        query = "call create_account('{0}',{1},{2},'{3}',{4},'{5}');".format(input_name,input_ac_number,input_pin,input_address,input_mb_number,input_ifsc_code)
        #query = "insert into account_holder(name,account_number,pin,address,mobile_no,ifsc_code) values ('{0}',{1},{2},'{3}',{4},'{5}');".format(input_name,input_ac_number,input_pin,input_address,input_mb_number,input_ifsc_code)
        cur.execute(query)
        db.commit()
        messagebox.showinfo('Success','Your Account was Successfully Created')
        reset()
    except Exception as e:
        messagebox.showerror('Database Error',e)


def delete():
    db.close()
    global main_frame
    main_frame.destroy()
    
    ac_number = StringVar()
    Label(root,text="").pack(pady=50)
    Label(root,text="Account Number",font=( 'aria' ,15, 'italic' )).pack(pady=5)
    Entry(root,width=30,justify="center",font=( 'aria' ,20),textvariable = ac_number).pack(pady=10)
    
    def submit():
        db=connector.connect(user='root',host='localhost',database='atm')
        cur=db.cursor()
        try:
            input_ac_number = ac_number.get()
            query = "select name from account_holder where account_number = {0}".format(input_ac_number)
            cur.execute(query)
            data = cur.fetchall()
            if data:
                query2 = "DELETE FROM `account_holder` WHERE account_number = {0}".format(input_ac_number)
                cur.execute(query2)
                db.commit()
                messagebox.showinfo('Success','Account Number - {0} was Successfully Deleted'.format(input_ac_number))
                exit()
            else :
                raise Exception("Account Does Not Exists!!")
        except Exception as e:
            messagebox.showerror('Database Error',e)
        
    Button(root,text="SUBMIT",command=submit,width=15,bd=7,bg="lightgreen",font=( 'aria' ,15,'bold')).pack(pady=25)
    Button(root,text="EXIT",command=exit,width=20,bd=7,bg="lightgreen",font=( 'aria' ,10,'bold')).pack(pady=5)
    

#-----------------------Input GUI Form---------------------------------------

Label(main_frame,text="Account Holder Name",font=( 'aria' ,15, 'italic' )).pack(pady=5)
Entry(main_frame,width=25,justify="center",font=( 'aria' ,15),textvariable = name).pack()

Label(main_frame,text="Account Number",font=( 'aria' ,15, 'italic' )).pack(pady=5)
Entry(main_frame,width=25,justify="center",font=( 'aria' ,15),textvariable = ac_number).pack()

Label(main_frame,text="ATM Pin",font=( 'aria' ,15, 'italic' )).pack(pady=5)
Entry(main_frame,width=25,justify="center",font=( 'aria' ,15),textvariable = pin).pack()

Label(main_frame,text="Holder Address",font=( 'aria' ,15, 'italic' )).pack(pady=5)
Entry(main_frame,width=25,justify="center",font=( 'aria' ,15),textvariable = address).pack()

Label(main_frame,text="Holder Mobile Number",font=( 'aria' ,15, 'italic' )).pack(pady=5)
Entry(main_frame,width=25,justify="center",font=( 'aria' ,15),textvariable = mb_number).pack()

Label(main_frame,text="IFSC Code",font=( 'aria' ,15, 'italic' )).pack(pady=5)
Entry(main_frame,width=25,justify="center",font=( 'aria' ,15),textvariable = ifsc_code).pack()


Button(main_frame,text="SUBMIT",command=submit,width=15,bd=7,bg="lightgreen",font=( 'aria' ,15,'bold')).pack(pady=15)
Button(main_frame,text="Delete Users",command=delete,width=10,bd=7,bg="lightgreen",font=( 'aria' ,10,'bold')).pack(pady=5)

Button(main_frame,text="EXIT",command=exit,width=10,bd=7,bg="lightgreen",font=( 'aria' ,7,'bold')).pack(pady=5)

root.mainloop()
