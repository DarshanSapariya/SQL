
import  mysql.connector as sql
from loging_func import log_thisError
import getpass

"Enter your hostname, username and password from MySQL workbench "
def main_bank(host_name, user_name, user_password) :
     """Funcion to initialize the entire program with all the necesarry tables

     Args:
         host_name (str): hostname of your MySQL machine (example:localhost)
         user_name (str): username of MySQL instance
         user_password (str): passord of MySQL instance

     Raises:
         Exception: covered all the exceptions
     """
     DB_NAME = "BANKDATA" #Name of Database
     # conn = sql.connect(host = "localhost", user="root", passwd="mysql8976", use_pure= True)
     conn = sql.connect(host = host_name, user=user_name, passwd=user_password, use_pure= True)
     cur = conn.cursor()
     conn.database = DB_NAME
     #cur.execute('create table user_table(username varchar(25) primary key,passwrd varchar(25) not null )')
     print('=========================WELCOME TO INEURON BANK============================================================')
     import datetime as dt
     print(dt.datetime.now())
     print('1.REGISTER')
     print()
     print('2.LOGIN')
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
               else :
                    raise Exception("INVALID INPUT : Enter either 1 or 2 only !!")
                    
               #break
          except Exception as e:
               print(e)
               log_thisError(e)

     try: 
          if n== 1:
               name=input('Enter a Username=')
               print()
               # passwd=int(input('Enter a 4 DIGIT Password='))
               passwd = getpass.getpass(prompt='Type your 4 digit password:', stream=None)
               print()
               V_SQLInsert="INSERT  INTO user_table (passwrd,username) values (" +  str (passwd) + ",' " + name + " ') "
               cur.execute(V_SQLInsert)
               conn.commit()
               print()
               print('USER created succesfully')
               from menu import menu_func
               menu_func(host_name, user_name, user_password)

          elif  n==2 :
               name=input('Enter your Username=')
               print()
               passwd=int(input('Enter your 4 DIGIT Password='))
               V_Sql_Sel="select * from user_table where passwrd='"+str (passwd)+"' and username=  ' " +name+ " ' "
               cur.execute(V_Sql_Sel)
               if cur.fetchone() is  None:
                    print()
                    print('Invalid username or password')
               else:
                    print()
                    from menu import menu_func
                    menu_func(host_name, user_name, user_password)

          
     except Exception as e:
          print(e)
          log_thisError(e)
          
          
