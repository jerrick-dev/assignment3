#journaleditor.py
# Jerrick Aguilar
# jerricka@uci.edu
# 66335000


from inputchecker import *
from Profile import Post


def displayposts(journal):
    posts = journal.get_posts()
    i = 1
    for post in posts:
        print(f'{i}: {post["entry"]}')
        i+=1
    return i
def journal_edit(entry,journal,directory):
    if entry == "-usr":
        print('Enter new username:')
        flag = False
        while flag is False:
            username = input('* USERNAME: ')
            flag = input_check(username)
        journal.username = username
        journal.save_profile(directory)
        print("USERNAME SET!")
        return
    
    elif entry == "-pwd":
            print('Enter new password:')
            flag = False
            while flag is False:
                password = input('* PASSWORD: ')
                flag = input_check(password)
            journal.password = password
            journal.save_profile(directory)
            print("PASSWORD SET!")
            return
    
    elif entry == "-bio":
            print('Enter new bio:')
            bio = input('* BIO: ')
            if bio.isspace() or bio is None:
                 bio = "N/A"
            journal.bio = bio
            journal.save_profile(directory)
            print("BIO SET!")
            return

    elif entry == "-addpost":
        postcontent = input("Enter post content:\n* POSTCONTENT: ")
        post = Post(postcontent)
        journal.add_post(post)
        journal.save_profile(directory)
        print("\nADDED!")
    else:
        c = displayposts(journal)
        if c == 1:
            print("\nPost list is empty!")
            return
        while True:
            id = input("Enter ID of post to delete:\n* ID: ")
            if not id.isdigit():
                 print("ID must be an integer!")
                 continue 
            if int(id) > c-1:
                 print("Not a valid ID!")
                 continue  
            id = int(id)
            break
        journal.del_post(id-1)
        journal.save_profile(directory)
        print("\nDELETED!")
        return

