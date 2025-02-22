#inputchecker.py
# Jerrick Aguilar
# jerricka@uci.edu
# 66335000

#used to check inputs when ingesting username, password, bio

def input_check(detail):
    if detail == " ":
        print('!! Input cannot be empty !!')
        return False
    if " " in detail:
        print('!! Input cannot be empty!!')
        return False
    return True 

def input_check_admin(detail):
    if detail == " ":
        print('[ERROR]')
        return False
    if detail is None:
        print('[ERROR]')
        return False
    return True 
