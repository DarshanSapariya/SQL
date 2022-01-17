import getpass
import  mysql.connector as sql
from loging_func import log_thisError

from main_bank import main_bank
from menu import menu_func
from tables import customer_table, transaction_table, user_table

# If you wish to change the name of your database change 'DB_NAME' variable in all other scritps

try:
    print("======Welcome to System========")
    print()
    print("SETTING UP MySQL ")
    print()
    while True:
        hostname = input("Enter your Hostname here :")
        username = input("Enter your Username of instance :")
        passwrd = getpass.getpass(prompt= f"Enter password for {username} :")
        try :
            sql.connect(host = hostname, user=username, passwd=passwrd, use_pure= True)
            break
        except Exception as e:
            print()
            print(e)
            print("\nEnter the credentials again !\n")
            log_thisError(e)


    customer_table(hostname, username, passwrd)
    transaction_table(hostname, username, passwrd)
    user_table(hostname, username, passwrd)

    main_bank(hostname, username, passwrd)
except Exception as e:
    print(e)
    log_thisError(e)
