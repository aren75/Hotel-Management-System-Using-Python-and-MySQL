import mysql.connector 
from tabulate import tabulate
import datetime
from tkinter.tix import DisplayStyle
import random
#PARADISE INN
def Sunset_Hotel():
    while True:
        print('\t\t===============================================================================================')
        print('\t\t░██████╗██╗░░░██╗███╗░░██╗░██████╗███████╗████████╗  ██╗░░██╗░█████╗░████████╗███████╗██╗░░░░░')
        print('\t\t██╔════╝██║░░░██║████╗░██║██╔════╝██╔════╝╚══██╔══╝  ██║░░██║██╔══██╗╚══██╔══╝██╔════╝██║░░░░░')
        print('\t\t╚█████╗░██║░░░██║██╔██╗██║╚█████╗░█████╗░░░░░██║░░░  ███████║██║░░██║░░░██║░░░█████╗░░██║░░░░░')
        print('\t\t░╚═══██╗██║░░░██║██║╚████║░╚═══██╗██╔══╝░░░░░██║░░░  ██╔══██║██║░░██║░░░██║░░░██╔══╝░░██║░░░░░')
        print('\t\t██████╔╝╚██████╔╝██║░╚███║██████╔╝███████╗░░░██║░░░  ██║░░██║╚█████╔╝░░░██║░░░███████╗███████╗')
        print('\t\t╚═════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░╚══════╝░░░╚═╝░░░  ╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝╚══════╝')
        print('\t\t================================================================================================')
        print('\t\tA. GUEST')
        print()
        print('\t\tB. STAFF')
        print()
        print('\t\tC. EXIT')
        print()
        print('\t\t================================================================================================')
        choice=input('\t\tChoose Menu:')
        if choice in 'Aa':
            GUEST_MAIN_MENU()
            print()
        elif choice in 'Bb':
            STAFF_MAIN_MENU()
            print()
        elif choice in 'Cc':
            break
        else:
            print('\t\tINVALID. TRY AGAIN')

#GUEST MAIN MENU
def GUEST_MAIN_MENU():
    while True:
        print('\t\t====================================================')
        print('\t\t******************GUEST MAIN MENU*******************')
        print('\t\t====================================================')
        print('\t\t1.ADD GUEST')
        print('\t\t2.SEARCH GUEST(S)')
        print('\t\t3.COUNT OCCUPIED ROOMS')
        print('\t\t4.DELETE GUEST')
        print('\t\t5.TOTAL BILL')
        print('\t\t6.REPORTS')
        print('\t\t7.EXIT')
        print('\t\t====================================================')
        choice=int(input('\t\tEnter Your Choice: '))
        if choice==1:
            Add_Guest()
            print()
        elif choice==2:
            Search_Menu()
            print()
        elif choice==3:
            Count_Guest()
            print()
        elif choice==4:
            Delete_Guest()
            print()
        elif choice==5:
            Total_Bill()
            print()
        elif choice==6:
            Guest_Reports()
            print()
        elif choice==7:
            return
        else:
            print('\t\tINVALID CHOICE. TRY AGAIN')

  #STAFF MAIN MENU
def STAFF_MAIN_MENU():
    while True:
        print('\t\t====================================================')
        print('\t\t******************STAFF MAIN MENU*******************')
        print('\t\t====================================================')
        print('\t\t1.ADD EMPLOYEE')
        print('\t\t2.SEARCH EMPLOYEE(S)')
        print('\t\t3.UPDATE EMPLOYEE RECORD')
        print('\t\t4.COUNT EMPLOYEES')
        print('\t\t5.DELETE EMPLOYEE')
        print('\t\t6.REPORTS')
        print('\t\t7.EXIT')
        print('\t\t====================================================')
        choice=int(input('\t\tEnter Your Choice:'))
        if choice==1:
            AddEmployee()
            print()
        elif choice==2:
            SearchMenu()
            print()
        elif choice==3:
            UpdateEmployee()
            print()
        elif choice==4:
            CountStaff()
            print()
        elif choice==5:
            DeleteEmployee()
            print()
        elif choice==6:
            Staff_Reports()
            print()
        elif choice==7:
            return  
        else:
            print('\t\tINVALID CHOICE. TRY AGAIN')


    
#GUEST ADMINISTRATION
import mysql.connector 
#Add Guest
def Add_Guest():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel')
    mycursor=mydb.cursor()
    name=input('\t\tEnter Name: ')
    Gname=name.upper()
    phone=int(input('\t\tEnter phone no: '))
    while True:
        email=input('\t\tEnter email ID: ')
        if '@gmail.com' in str(email):
            break
        else:
            print('Enter Valid Email Address.Try Again')
            print()
    address=input('\t\tEnter Address:')
    adultsnum=int(input('\t\tEnter no of adults: '))
    childnum=int(input('\t\tEnter no of children: '))
    CheckIn=input('\t\tEnter Check In date:')
    CheckOut=input('\t\tEnter Check Out date: ')
    roomtype,roomno=Check_Room()
    com="insert into Guest_Details(NAME,PHONE_NO,EMAIL,ADDRESS,NO_Of_ADULTS,NO_Of_CHILD,CHECK_IN,CHECK_OUT,ROOM_TYPE,ROOM_NO) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    record=(Gname,phone,email,address,adultsnum,childnum,CheckIn,CheckOut,roomtype,roomno)
    mycursor.execute(com,record)
    mydb.commit()
    print()
    print("\t\tRECORD SAVED")
    print('\t\t====================================================')

#Check Room for Add_Guest
import mysql.connector 
def Check_Room():
    while True:
        roomtype=input("\t\tEnter desired room type: ")
        mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel') 
        mycursor=mydb.cursor()
        mycursor.execute("select * from rooms where ROOM_TYPE='{}'".format(roomtype))
        result=mycursor.fetchall()
        for k in result:
            if k[2]=='Available':
                mycursor.execute("update rooms set ROOM_STATUS='Occupied' where ROOM_NO='{}'".format(k[0]))
                mydb.commit()
                print('\t\t====================================================')
                print("\t\tROOM NO:",k[0])
                return roomtype,k[0]
        print("\t\tALL ROOMS OCCUPIED")
         


#SEARCH MENU
def Search_Menu():
    print('\t\t=====================================================')
    print('\t\t******************SEARCH MENU************************')
    print('\t\t=====================================================')
    print('\t\tTo Search BY: ')
    print('\t\t1. Name ')
    print('\t\t2. Room No. ')
    print('\t\t3. Room Type')
    print('\t\t4. Check In Date')
    print('\t\t5. Return To Main Menu')
    print('\t\t====================================================')
    while True:
        choice=int(input('\t\tEnter your choice:'))
        print('\t\t===============================================') 
        if choice==1:
            SearchName()
            print()
        elif choice==2:
            SearchRoomNo()
        elif choice==3:
            SearchRoomType()
        elif choice==4:
            SearchCheckIn()
        elif choice==5:
            return
        else:
            print('\t\t INVALID CHOICE. Please Try Again')

#UNDER SEARCH MENU
import mysql.connector

def SearchName():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel')
    mycursor=mydb.cursor()
    name=str(input('\t\tEnter name of guest: '))
    Gname=name.upper()
    mycursor.execute(f"select * from Guest_details where Name='{Gname}'")
    result=mycursor.fetchall()
    print("\t\t=====================================================")
    if result:
        print(tabulate(result,headers=['Name','Phone No.','Email','Address','No. of Adults','No. of Children','Check_in','Check_out','Room Type','Room No.'],tablefmt='fancy_grid'))
    else:
        print('\t\tRecord not found')
    print('\t\t=====================================================') 
    return 

def SearchRoomNo():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),database='Sunset_Hotel')
    mycursor=mydb.cursor()
    roomno=int(input('\t\tEnter room no: '))
    mycursor.execute(f'select * from Guest_details where Room_No ={roomno}')
    result=mycursor.fetchall()
    print("\t\t=====================================================")
    if result:
        print(tabulate(result,headers=['Name','Phone No.','Email','Address','No. of Adults','No. of Children','Check_in','Check_out','Room Type','Room No.'],tablefmt='fancy_grid'))
    else:
        print('\t\tRecord not found')
    print('\t\t=====================================================') 

def SearchRoomType():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),database='Sunset_Hotel')
    mycursor=mydb.cursor()
    roomtype=input('\t\tEnter Room Type: ')
    mycursor.execute(f"select * from Guest_details where Room_Type='{roomtype}'")
    result=mycursor.fetchall()
    print("\t\t=====================================================")
    if result:
        print(tabulate(result,headers=['Name','Phone No.','Email','Address','No. of Adults','No. of Children','Check_in','Check_out','Room Type','Room No.'],tablefmt='fancy_grid'))
    else:
        print('\t\tRecord not found')
    print('\t\t=====================================================') 
    return

def SearchCheckIn():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),database='Sunset_Hotel')
    mycursor=mydb.cursor()
    checkin=input('\t\tEnter date of check-in: ')
    mycursor.execute(f"select *  from Guest_details where Check_in='{checkin}'")
    result=mycursor.fetchall()
    print("\t\t=====================================================")
    if result:
        print(tabulate(result,headers=['Name','Phone No.','Email','Address','No. of Adults','No. of Children','Check_in','Check_out','Room Type','Room No.'],tablefmt='fancy_grid'))
    else:
        print('\t\tRecord not found')
    print('\t\t=====================================================') 
    return    

  
#COUNT GUEST AND COUNT REPORT



def Count_Guest():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),database='Sunset_Hotel')
    mycursor=mydb.cursor()
    mycursor.execute('select * from Guest_details')
    result = mycursor.fetchall()
    count=0
    for k in result:
        count+=1
    print('\t\tTOTAL NO. OF ROOMS OCCUPIED: ',count)
    print('\t\t=====================================================')

def Guest_Reports():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),database='Sunset_Hotel')
    mycursor=mydb.cursor()
    mycursor.execute("select * from Guest_details")
    result=mycursor.fetchall()
    print(tabulate(result,headers=['Name','Phone No.','Email','Address','No. of Adults','No. of Children','Check_in','Check_out','Room Type','Room No.'],tablefmt='fancy_grid'))




#Delete Guest

def Delete_Guest():
    while True:
        print('\t\t==============================================')
        print('\t\tDELETE BY:')
        print('\t\t1.ROOM NO')
        print('\t\t2.NAME')
        print('\t\t3.RETURN TO MAIN MENU')
        print('\t\t==============================================')
        choice=int(input('\t\tEnter your choice: '))
        print('\t\t==============================================')
        if choice==1:
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel')
            mycursor=mydb.cursor()
            roomno=int(input('\t\tEnter Room no:'))
            mycursor.execute("delete from Guest_Details where Room_No='{}'".format(roomno))
            mycursor.execute("update Rooms set ROOM_STATUS='Available' where ROOM_NO='{}'".format(roomno))
            mydb.commit()
            print('\t\tGUEST RECORD DELETED')
        elif choice==2:
            mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel')
            mycursor=mydb.cursor()
            name=input('\t\tEnter Name of Guest:')
            Gname=name.upper()
            mycursor.execute("select*from Guest_Details where Name='{}'".format(Gname))
            result=mycursor.fetchall()
            for k in result:
                roomno=k[9]
                mycursor.execute("delete from Guest_Details where Room_No='{}'".format(roomno))
                mycursor.execute("update Rooms set ROOM_STATUS='Available' where ROOM_NO='{}'".format(roomno))
                mydb.commit()
            print('\t\tGUEST RECORD DELETED')
        elif choice==3:
            return
        else:
            print('\t\tINVALID CHOICE')

#TOTAL BILL


def initial_Bill(n):
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel')
    mycursor=mydb.cursor()
    roomno=n
    mycursor.execute("select * from Guest_Details where Room_no='{}'".format(roomno))
    result=mycursor.fetchall()
    for k in result:
        checkin=k[6]
        checkout=k[7]
        adult=k[4]
        child=k[5]
        roomtype=k[8]
    mycursor.execute("select datediff('{}','{}')".format(checkout,checkin))
    result=mycursor.fetchall()
    for k in result:
        days=k[0]
    if roomtype in ('Suite','suite'):
        ibill=(20000.00*adult+10000*child)*days
    elif roomtype in ('Double Deluxe','double deluxe','Double deluxe','double Deluxe'):
        ibill=(16000.00*adult+8000*child)*days
    elif roomtype in ("Single Deluxe",'Single deluxe','single Deluxe','single deluxe'):
        ibill=(12000.00*adult+6000*child)*days
    elif roomtype in ('Twin','twin'):
        ibill=(8000.00*adult+4000*child)*days
    elif roomtype in ('Studio','studio'):
        ibill=(4000.00*adult+2000*child)*days
    return(ibill)



    
def DeleteGuest(n):
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel')
    mycursor=mydb.cursor()
    roomno=n
    mycursor.execute("delete from Guest_Details where Room_No='{}'".format(roomno))

    mycursor.execute("update Rooms set ROOM_STATUS='Available' where ROOM_NO='{}'".format(roomno))
    mydb.commit()
    return

def Discount(t):
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel')
    mycursor=mydb.cursor()
    name=input("\t\tEnter Name:")
    Ename=name.upper()
    mycursor.execute("select count(*) from billing where Name='{}'".format(Ename))
    result=mycursor.fetchall()
    total=t
    for k in result:
        if 7>k[0]>=3:
            total=(10*t)/100
        elif k[0]>7:
            total-=(15*t)/100
    return total

def Total_Bill():
    print('\t\t=====================================================')
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel')
    mycursor=mydb.cursor()
    roomno=int(input("\t\tEnter Room No:"))
    mycursor.execute("select * from Guest_Details where Room_No='{}'".format(roomno))
    result=mycursor.fetchall()
    for k in result:
        name=k[0]
        checkin=k[6]
        checkout=k[7]
    initialbill=initial_Bill(roomno)
    t=initialbill
    total=Discount(t)
    print('\t\tTOTAL BILL:',total)
    paystatus=input('\t\tEnter Paid Status: ')
    if paystatus in 'YesYESyes':
        try:
            mycursor.execute(f"Insert into billing(Name,Room_No,Check_In,Check_Out,Initial_Bill,Total_Bill) values('{name}',{roomno},'{checkin}','{checkout}','{initialbill}','{total}')")
        except:
            mycursor.execute(f"update billing set Name='{name}',Room_No={roomno},Check_In='{checkin}',Check_Out='{checkout}',Initial_Bill='{initialbill}',Total_Bill='{total}' ")
        mydb.commit()
        DeleteGuest(roomno)
        print()
        print("\t\tPAID")
        print('\t\t=====================================================')
    elif paystatus in 'NoNOno':
        try:
            mycursor.execute(f"Insert into billing(Name,Room_No,Check_In,Check_Out,Initial_Bill,Total_Bill) values('{name}',{roomno},'{checkin}','{checkout}','{initialbill}','{total}')")
        except:
            mycursor.execute(f"update billing set Name='{name}',Room_No={roomno},Check_In='{checkin}',Check_Out='{checkout}',Initial_Bill='{initialbill}',Total_Bill='{total}' ")
        print()
        print("\t\tNOT PAID")
    print('\t\t=====================================================')
    return

#Staff Administration
#Add employee

def CheckEmpNo():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel')
    mycursor=mydb.cursor()
    mycursor.execute("select count(*) from staff")
    result=mycursor.fetchall()
    for k in result:
        e=101+k[0]
    return e

def AddEmployee():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel')
    mycursor=mydb.cursor()
    Name=input("\t\tEnter Name:")
    Ename=Name.upper()
    dept=input("\t\tEnter Department:")
    shift=input("\t\tEnter Shift:")
    position=input("\t\tEnter Position:")
    EmploymentDate=input('\t\tEnter Date of Employment:')
    salary=float(input('\t\tEnter Salary:'))
    empno=CheckEmpNo()
    print('\t\t==============================================')
    print("\t\tEmployee No:",empno)
    mycursor.execute(f"insert into staff values('{Ename}','{dept}','{shift}','{position}','{EmploymentDate}',{salary},{empno})")
    mydb.commit()
    print("\t\tNEW EMPLOYEE RECORD SAVED")
    print('\t\t==============================================')



#DELETE EMPLOYEE

def SearchDepartment():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel')
    mycursor=mydb.cursor()
    dept=input('\t\tEnter Department:')
    print('\t\t=====================================================')
    mycursor.execute("select * from Staff where Department='{}'".format(dept))
    result=mycursor.fetchall()
    if result:
        print(tabulate(result, headers=['Name','Department','Shift','Position','Date of Employement','Salary','EmpNo'],tablefmt='fancy_grid'))
        return
    else:
        print("\t\tRecord Not Found")
        return

def SearchPosition():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel')
    mycursor=mydb.cursor()
    position=input('\t\tEnter Position:')
    print('\t\t=====================================================')
    mycursor.execute("select * from Staff where position='{}'".format(position))
    result=mycursor.fetchall()
    if result:
        print(tabulate(result, headers=['Name','Department','Shift','Position','Date of Employement','Salary','EmpNo'],tablefmt='fancy_grid'))
        return
    else:
        print("\t\tRecord Not Found")
        return
    

def SearchShift():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel')
    mycursor=mydb.cursor()
    shift=input('\t\tEnter Shift:')
    print('\t\t=====================================================')
    mycursor.execute("select * from Staff where shift='{}'".format(shift))
    result=mycursor.fetchall()
    if result:
        print(tabulate(result, headers=['Name','Department','Shift','Position',
       'Date_of_Employment','Salary','EmpNo'],tablefmt='fancy_grid'))
        return
    else:
        print("\t\tRecord Not Found")
        return
    

def SearchEmpName():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel')
    mycursor=mydb.cursor()
    name=input('\t\tEnter Name of Employee:')
    Ename=name.upper()
    print('\t\t=====================================================')
    mycursor.execute("select * from Staff where Name='{}'".format(Ename))
    result=mycursor.fetchall()
    if result:
        print(tabulate(result, headers=['Name','Department','Shift','Position','Date_of_Employement','Salary','EmpNo'],tablefmt='fancy_grid'))
        return
    else:
        print("Record Not Found")
        return
        
def SearchEmpNo():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel')
    mycursor=mydb.cursor()
    empno=input('\t\tEnter EmpNO: ')
    print('\t\t=====================================================')
    mycursor.execute("select * from Staff where EmpNo='{}'".format(empno))
    result=mycursor.fetchall()
    if result:
        print(tabulate(result, headers=['Name','Department','Shift','Position','Date of Employement','Salary','EmpNo'],tablefmt='fancy_grid'))
        return
    else:
        print("\t\tRecord Not Found")
        return
    


def SearchMenu():
    print('\t\t====================================================')
    print('\t\t****************SEARCH MENU*************************')
    print('\t\t====================================================')
    print('\t\tTO SEARCH BY:')
    print('\t\t1. EMPLOYEE NAME')
    print('\t\t2. EMPLOYEE NO')
    print('\t\t3. SHIFT')
    print('\t\t4. POSITION')
    print('\t\t5. DEPARTMENT')
    print('\t\t6. RETURN TO MAIN MENU')
    print('\t\t====================================================')
    while True:
        choice=int(input("\t\tENTER YOUR CHOICE: "))
        if choice==1:
            SearchEmpName()
            print()
        elif choice==2:
            SearchEmpNo()
            print()
        elif choice==3:
            SearchShift()
            print()
        elif choice==4:
            SearchPosition()
            print()
        elif choice==5:
            SearchDepartment()
            print()
        elif choice==6:
            return
        else:
            print("\t\tINVALID CHOICE. Please try again.")
            print()





#Update Staff

def UpdateEmployee():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel')
    mycursor=mydb.cursor()
    print('\t\t1. Update Position')
    print('\t\t2. Update Shift')
    print('\t\t3. Return to Staff Menu')
    print('\t\t=====================================================')
    choice=int(input('\t\tEnter your choice:'))
    if choice==1:
        empno=int(input('\t\tEnter Employee no:')) 
        mycursor.execute("select * from Staff where EmpNo='{}'".format(empno))
        result=mycursor.fetchall()
        print(tabulate(result,headers=['Name','Department','Shift','Position','Date of Employment','Salary','EmpNo'],tablefmt='fancy_grid'))
        print()
        x=input('\t\tDo you want to update the position of the Employee?[Y/N]:')
        if x in 'Yy':
            position=input('\t\tEnter New Position: ')
            salary=float(input('\t\tEnter New Salary: '))
            mycursor.execute("update staff set position='{}' where EmpNo='{}'".format(position,empno))
            mycursor.execute("update staff set Salary='{}' where EmpNo='{}'".format(salary,empno))
            mydb.commit()
            print('\t\tRECORD UPDATED')
        elif x in 'Nn':
            print('\t\tTry Again Later')
            return
        else:
            print('\t\tInvalid Choice')
        mycursor.execute("Select * from Staff")
        result=mycursor.fetchall()
    elif choice==2:
        empno=int(input('\t\tEnter Employee no:'))
        mycursor.execute("select * from Staff where EmpNo='{}'".format(empno))
        result=mycursor.fetchall()
        print(tabulate(result,headers=['Name','Department','Shift','Position','Date of Employment','Salary','Empno'],tablefmt='fancy_grid'))
        print()
        x=input('\t\tDo you want to update the shift of the Employee?[Y/N]:')
        if x in 'Yy':
            shift=input('\t\tEnter New Shift:')
            query="update staff set shift='{}' where EmpNo='{}'".format(shift,empno)
            mycursor.execute(query)
            mydb.commit()
            print('\t\tRECORD UPDATED')
        elif x in 'Nn':
            print('\t\tTry Again Later')
            return
        else:
            print('\t\tInvalid Choice')
    elif choice==3:
        return




#Count Employee & Staff Reports

def CountStaff():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel')
    mycursor=mydb.cursor()
    while True: 
        print('\t\tCOUNT BY:')
        print('\t\t1. By Specific Department')
        print('\t\t2. All Departments')
        print('\t\t3. Exit')
        print('\t\t=====================================================')
        choice=int(input('\t\tEnter your choice: '))
        print()
        count=0
        if choice==1:
            dept=input('\t\tEnter Department')
            mycursor.execute("select count(*) from Staff where Department='{}'".format(dept))
            result=mycursor.fetchall()
            for k in result:
                print('\t\tNumber of required records:',k[0])
                print('\t\t=====================================================')
        elif choice==2:
            mycursor.execute("select count(*) from Staff")
            result=mycursor.fetchall()
            for k in result:
                print('\t\tNumber of required records:',k[0])
                print('\t\t====================================================')
        elif choice==3: 
            return

def Staff_Reports():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel')
    mycursor=mydb.cursor()
    mycursor.execute('select * from Staff')
    result=mycursor.fetchall()
    print(tabulate(result, headers=['Name','Department','Shift','Position','Date of  Employement','Salary','EmpNo'],tablefmt='fancy_grid'))
    print('\t\t=====================================================')





#Delete Employee

def DeleteEmployee():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd=str(passwd),charset='utf8',database='Sunset_Hotel')
    mycursor=mydb.cursor()
    print('\t\t====================================================')
    empno=input("\t\tEnter employee number: ")
    mycursor.execute("select * from staff where EmpNo='{}'".format(empno))
    result=mycursor.fetchall()
    print(tabulate(result,headers=["Name","Department","Shift","Position","Date_of_Employment","Salary","EmpNo"],tablefmt='fancy_grid'))
    m=input('\t\tDo u want to delete this record? [Y/N]:')
    if m in 'Yy':
        query=("delete from staff where EmpNo='{}'".format(empno))
        mycursor.execute(query)
        mydb.commit()
        print('\t\tRECORD DELETED')
        print('\t\t=====================================================')
        return
    else:
        print("\t\tTry again later")
        print('\t\t=====================================================')
        return

    print()    


def Create_Database_Structure():
    db=mysql.connector.connect(host='localhost',user='root',passwd=passwd)
    mycursor=db.cursor()
    mycursor.execute("create database if not exists Sunset_Hotel;")
    mycursor.execute("use Sunset_Hotel;")
    mycursor.execute("create table if not exists Guest_Details (NAME varchar(20),PHONE_NO int(20),EMAIL varchar(20),ADDRESS varchar(20),NO_OF_ADULTS int(20),NO_OF_CHILD int(20),CHECK_IN date,CHECK_OUT date,ROOM_TYPE varchar(20),ROOM_NO int(20) primary key);")
    mycursor.execute("create table if not exists Rooms (ROOM_NO int(20) primary key,ROOM_TYPE varchar(20),ROOM_STATUS varchar(20));")
    mycursor.execute("create table if not exists Billing (Name varchar(20),Room_No int(20) primary key,Check_In date,Check_Out date,Initial_Bill decimal(20,2),Total_Bill decimal(20,2));")
    mycursor.execute("create table if not exists Staff (Name varchar(20), Department varchar(20),Shift varchar(20),Position varchar(20),Date_of_Employment date,Salary decimal(10,2),EmpNo int(20) primary key);")
    for i in range(1,101):
        if i<=20:
            room_type='Studio'
        elif i<=40:
            room_type='Twin'
        elif i<=60:
            room_type='Suite'
        elif i<=80:
            room_type='Single Deluxe'
        else:
            room_type='Double Deluxe'
        try:
            mycursor.execute(f"insert into Rooms values({i},'{room_type}','Available');")
            db.commit()
        except:
            break

#START OF PROGRAM
passwd=str(input('\t\tEnter passwd of your mysql client: '))
Create_Database_Structure()
user=input('\t\tENTER USERNAME: ')
while True:
    import mysql.connector
    passw=input('\t\tENTER PASSWORD(press X to exit): ')
    if passw=='####':
          Sunset_Hotel()
    elif passw in 'Xx':
          break
    else:
        print('\t\tWRONG PASSWORD. TRY AGAIN')
