#admin.py
# Jerrick Aguilar
# jerricka@uci.edu
# 66335000


import shlex
from pathlib import Path
from inputchecker import *
from Profile import Profile, Post
from loadfile import loadFile_admin
from journaleditor import displayposts

e_opt = ['-usr','-pwd','-bio','-addpost','-delpost'] 


def admin_journal(journal,dsuPath):
    command = shlex.split(input())
    print(command)
#--------------------EDIT MODE----------------------------------------        
    if command[0].lower() == 'e':
            if '-usr' in command:
                index = command.index('-usr')
                username = command[index+1]
                flag = input_check_admin(username)
                if flag is False:
                    #If theres a problem with the input process is restarted
                    admin_journal(journal,dsuPath)
        
                journal.username = username
                journal.save_profile(dsuPath)
                print("USERNAME SET")

            if '-pwd' in command:
                index = command.index('-pwd')
                password = command[index+1]
                flag = input_check_admin(password)
                if flag is False:
                    admin_journal(journal,dsuPath)
                journal.password = password
                journal.save_profile(dsuPath)
                print("PASSWORD SET")
    

            if '-bio' in command:
                index = command.index('-bio')
                bio = command[index+1]
                if not bio or bio.isspace():
                    bio = 'N/A'   
                journal.bio = bio
                journal.save_profile(dsuPath)
                print("BIO SET")

            if '-addpost' in command:
                index = command.index('-addpost')
                postcontent = command[index+1]
                post = Post(postcontent)
                journal.add_post(post)
                journal.save_profile(dsuPath)
                print("ADDED")
            if '-delpost' in command:
                index = command.index('-delpost')
                index_delete = command[index+1]
                i = len(journal.get_posts())
                if not index_delete.isdigit():
                    print("[ERROR]")
                    admin_journal(journal,dsuPath)
                if int(index_delete) > i:
                    print("[ERROR]")
                    admin_journal(journal,dsuPath)
                journal.del_post(int(index_delete)-1)
                journal.save_profile(dsuPath)
                print('DELETED')
    
#-------------------------PRINT COMMAND-----------------------------------------------        
    elif command[0].lower() == 'p':
        if '-usr' in command:
            print(f'USERNAME IS: {journal.username}')
        if '-pwd' in command:
            print(f'PASSWORD IS: {journal.password}')
        if '-bio' in command:
            print(f'BIO IS: {journal.bio}')
        if '-posts' in command:
            displayposts(journal)
        if '-post' in command:
            posts = journal.get_posts()
            index = command.index('-post')
            index_target = int(command[index+1])
            print(posts[index_target-1]['entry'])
        if '-all' in command:
            print(journal.__str__())
            posts = journal.get_posts()
            i = 1
            for post in posts:
                print(f'{i}: {post["entry"]}\nTimestamp: {post["timestamp"]}')
                i += 1


#------------------------------------------------------------------------------------        
    elif command[0].lower() == 'q': 
        return

    admin_journal(journal,dsuPath)
def admin_ui():

    command = shlex.split(input())
    
    if command[0].lower() not in start_options:
        print('[ERROR]')
        command = shlex.split(input())
    
    if command[0].lower() == 'c':
        if len(command) != 4 or command[2] != '-n':
            print('[ERROR]')
        else:
            directory = Path(command[1])
            filename = command[-1]
            flag = input_check_admin(filename)
            if flag is False:
                print('[ERROR]')
                admin_ui()
#-----------------DATA COLLECTION-------------------------------------------
            if directory.is_dir():
                flag = False
                while flag is False:
                    username = input()
                    flag = input_check_admin(username)
                #Checks password input
                flag = False
                while flag is False:
                    password = input()
                    flag = input_check_admin(password)
                #Sets BIO to n/a if left blank
                bio = input() 
                if not bio or bio.isspace():
                    bio = 'N/A'   
                flag = False
#--------------------CREATION----------------------------------------            
                if not (directory / (filename+'.dsu')).exists():
                    dsuPath = directory / f'{filename}.dsu'
                    dsuPath.touch() 
                    journal = Profile(username=username,password=password)
                    journal.bio = bio
                    journal.save_profile(dsuPath)
                    print(f"{dsuPath} CREATED") 
                    admin_journal(journal,dsuPath)
                
                else:
                    dsuPath = directory / f'{filename}.dsu'
                    print(f'{dsuPath} EXISTS. OPENING')
                    journal = Profile()
                    journal.load_profile((directory / (filename+'.dsu')))
                    admin_journal(journal,dsuPath)
#----------------------------------------------------------------- 
            else:
                print('[ERROR]')
                admin_ui()
#--------------------OPENING--------------------------------------------- 
    elif command[0] == 'o':
        directory = Path(command[1])
        journal = loadFile_admin(directory)
        if journal is None:
            admin_ui()
        journal.save_profile(directory)
        print('OPENED')
        admin_journal(journal,directory)
    else:
        return
#----------------------------------------------------------------- 
start_options = ['q','c','o']

