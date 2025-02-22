#journalfunctions.py
# Jerrick Aguilar
# jerricka@uci.edu
# 66335000


from journaleditor import *
from journalprint import *


def edit_menu():
    print("-------------------------------------")
    print("-usr: Change username")
    print("-pwd: Change password")
    print("-bio: Change bio")
    print("-addpost: Make a post")
    print("-delpost: Delete a post")
    print("-publish: publish info to a server")
    print("-publishbio: publish a new bio to server")
    print("-------------------------------------")

def print_menu():
    print("-------------------------------------")
    print("-usr: View username")
    print("-pwd: View password")
    print("-bio: View bio")
    print("-posts: View all posts")
    print("-post: View a post")
    print("-all: View all content on file")
    print("-------------------------------------")

def journalcmds(dsuPath,journal):
    while True:
        print(f"\nPreviewing {dsuPath.name}")
        print('---------------------------------')
        print("\nJOURNAL COMMANDS\n\nE - Edit file\nP - Print file data\nQ - Quit menu\n")
        user_entry = input("* USER_ENTRY: ").lower()
        while user_entry not in opt:
            user_entry = input("Invalid entry, please select one of the choices above!\n* USER_ENTRY:  ")
        if user_entry == 'q':
            return False
        else:
            journalui(user_entry,dsuPath,journal)

def journalui(entry,dsuPath,journal):
    if entry == 'e':
            print(f'\nEDITING {dsuPath.name}')
            edit_menu()
            user_option = input("* USER_ENTRY: ")
            while user_option.lower() not in e_opt:
                user_option = input("Invalid entry, please select one of the choices above!\n* USER_ENTRY:  ")
            journal_edit(user_option,journal,dsuPath) 
    
    elif entry == 'p':
        print(f'\nVIEWING {dsuPath.name}')
        print_menu()
        user_option = input("* USER_ENTRY: ")
        while user_option.lower() not in p_opt:
            user_option = input("Invalid entry, please select one of the choices above!\n* USER_ENTRY:  ")
        journal_print(user_option,journal,dsuPath)

e_opt = ['-usr','-pwd','-bio','-addpost','-delpost','-publish','-publishbio'] 
p_opt = ['-usr','-pwd','-bio','-posts','-post','-all']
opt = ['e','p','q']