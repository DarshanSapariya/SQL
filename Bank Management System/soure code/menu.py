
def menu_func(host_name, user_name, user_password) :
     """Funcion to operate menu

     Args:
         host_name (str): hostname of your MySQL machine (example:localhost)
         user_name (str): username of MySQL instance
         user_password (str): passord of MySQL instance

     Raises:
         Exception: covered all the exceptions
     """
     import datetime as dt
     import  mysql.connector as sql
     from loging_func import log_thisError

     DB_NAME = "BANKDATA"
     # conn = sql.connect(host = "localhost", user="root", passwd="mysql8976", use_pure= True)
     conn = sql.connect(host = host_name, user=user_name, passwd=user_password, use_pure= True)
     cur = conn.cursor()
     conn.database = DB_NAME
          

     conn.autocommit = True
     c = 'n'
     while c == 'n':

          print()
          print('1.CREATE BANK ACCOUNT')
          print()
          print('2.TRANSACTION')
          print()
          print('3.CUSTOMER DETAILS')
          print()
          print('4.TRANSACTION DETAILS')
          print()
          print('5.DELETE ACCOUNT')
          print()
          print('6.QUIT')

          print()
          while True:
               try:
                    n = input("Enter your choice :")
                    if n == '1':
                         n= int(n)
                         break
                    elif n == '2':
                         n= int(n)
                         break
                    elif n == '3':
                         n= int(n)
                         break
                    elif n == '4':
                         n= int(n)
                         break
                    elif n == '5':
                         n= int(n)
                         break
                    elif n == '6':
                         n= int(n)
                         break
                    else :
                         raise Exception("INVALID INPUT : Enter From menu only !!")
                         
                    #break
               except Exception as e:
                    print(e)
                    log_thisError(e)

          print()

          if n == 1:

                    acc_no=int(input('Enter your ACCOUNT NUMBER='))
                    print()
                    acc_name=input('Enter your ACCOUNT NAME=')
                    print()
                    ph_no=int(input('Enter your PHONE NUMBER='))
                    print()
                    add=(input('Enter your place='))
                    print()
                    cr_amt=int(input('Enter your credit amount='))
                    V_SQLInsert="INSERT  INTO customer_details values (" +  str (acc_no) + ",' " + acc_name + " ',"+str(ph_no) + ",' " +add + " ',"+ str (cr_amt) + " ) "
                    cur.execute(V_SQLInsert)
                    print()
                    print('Account Created Succesfully!!!!!')
                    conn.commit()


          if n == 2:
               acct_no=int(input('Enter Your Account Number='))
               cur.execute('select * from customer_details where acct_no='+str (acct_no) )
               data=cur.fetchall()
               count=cur.rowcount
               conn.commit()
               if count == 0:
                    print()
                    print('Account Number Invalid Sorry Try Again Later')
                    print()
               else:
                    print()
                    print('1.WITHDRAW AMOUNT')
                    print()
                    print('2.ADD AMOUNT')
                    print()

                    print()
                    x=int(input('Enter your CHOICE='))
                    print()
                    if x == 1:
                         amt=int(input('Enter withdrawl amount='))
                         cr_amt=0
                         cur.execute('update customer_details set   cr_amt=cr_amt-'+str(amt) +  ' where acct_no=' +str(acct_no) )
                         V_SQLInsert="INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,dt.datetime.today(),amt,cr_amt) 
                         cur.execute(  V_SQLInsert)
                         conn.commit()
                         print()
                         print('Account Updated Succesfully!!!!!')
                         
                         

                    if x== 2:
                         amt=int(input('Enter amount to be added='))
                         cr_amt=0
                         cur.execute('update customer_details set  cr_amt=cr_amt+'+str(amt) +  ' where acct_no=' +str(acct_no) )
                         V_SQLInsert="INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,dt.datetime.today(),cr_amt,amt)
                         cur.execute(  V_SQLInsert)
                         conn.commit()
                         print()
                         print('Account Updated Succesfully!!!!!')

          if n == 3:
               acct_no=int(input('Enter your account number='))
               print()
               cur.execute('select * from customer_details where acct_no='+str(acct_no) )
               if cur.fetchone() is  None:
                    print()
                    print('Invalid Account number')
               else:
                    cur.execute('select * from customer_details where acct_no='+str(acct_no) )
                    data=cur.fetchall()
                    for row in data:
                         print('ACCOUNT NO=',acct_no)
                         print()
                         print('ACCOUNT NAME=',row[1])
                         print()
                         print(' PHONE NUMBER=',row[2])
                         print()
                         print('ADDRESS=',row[3])
                         print()
                         print('cr_amt=',row[4])
          if n == 4:
               acct_no=int(input('Enter your account number='))
               print()
               cur.execute('select * from customer_details where acct_no='+str(acct_no) )
               if cur.fetchone() is  None:
                    print()
                    print('Invalid Account number')
               else:
                    cur.execute('select * from transactions where acct_no='+str(acct_no) )
                    data=cur.fetchall()
                    for row in data:
                         print('ACCOUNT NO=',acct_no)
                         print()
                         print('DATE=',row[1])
                         print()
                         print(' WITHDRAWAL AMOUNT=',row[2])
                         print()
                         print('AMOUNT ADDED=',row[3])
                         print()
               

          if n == 5:
               print('DELETE YOUR ACCOUNT')
               acct_no=int(input('Enter your account number='))
               
               cur.execute('delete from customer_details where acct_no='+str(acct_no) )
               print('ACCOUNT DELETED SUCCESFULLY')

          if n == 6:
               print('DO YO WANT TO EXIT(y/n)')
               c=input ('enter your choice=')
          

          
          
     else:
          print('THANK YOU PLEASE VISIT AGAIN')
          quit()
          
     
                               
                              
                              
                              

                                        
               
     


