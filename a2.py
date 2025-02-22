# a2.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Jerrick Aguilar
# jerricka@uci.edu
# 66335000

from ui import *
from admin import *


start_options = ['q', 'c', 'o', 'admin']


def main():
    while True:
        user_entry = input("WELCOME TO PyJournal\nPlease enter one of the following:\n\nC - Create a file\nO - Open a file\nQ - Quit\n\n* USER_ENTRY: ")
        while user_entry.lower() not in start_options:
            user_entry = input("Invalid entry, please select one of the choices above!\n* USER_ENTRY:  ")
        if user_entry.lower() == 'q':
            print('ENDING...')
            break

        elif user_entry.lower() == 'admin':
            print("\nLAUNCHED ADMIN MODE")
            admin_ui()
            return False
        else:
            launch_ui(user_entry)

if __name__=="__main__": 
    main()