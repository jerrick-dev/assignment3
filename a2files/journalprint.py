#journalprint.py
# Jerrick Aguilar
# jerricka@uci.edu
# 66335000


from journaleditor import displayposts

def journal_print(entry,journal,directory):
    if entry == '-usr':
        print(f'USERNAME IS: {journal.username}')
        return
    elif entry == '-pwd':
        print(f'PASSWORD IS: {journal.password}')
        return
    elif entry == '-bio':
        print(f'BIO IS: {journal.bio}')
        return
    elif entry == '-posts':
        displayposts(journal)
        return
    elif entry == '-post':
        posts = journal.get_posts()
        i = 1
        for post in posts:
            print(f'{i}:')
            i+=1
        while True:
            id = input("Enter ID of post to view:\n* ID: ")
            if not id.isdigit():
                 print("ID must be an integer!")
                 continue 
            if int(id) > len(posts):
                 print("Not a valid ID!")
                 continue  
            id = int(id)
            break  
        print(posts[id-1]['entry'])
    else:
        print(journal.__str__())
        posts = journal.get_posts()
        i = 1
        for post in posts:
            print(f'{i}: {post["entry"]}\nTimestamp: {post["timestamp"]}')
            i += 1

p_opt = ['-usr','-pwd','-bio','-posts','-post','-all']