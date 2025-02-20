#loadfile.py
# Jerrick Aguilar
# jerricka@uci.edu
# 66335000


from Profile import Profile

def loadFile(pathobj):
    if pathobj.is_file():
        if pathobj.suffix == '.dsu':
            journal = Profile()
            journal.load_profile(pathobj)
            return journal
        else:
            print("Non .dsu file! Redirecting to menu...")
            return
    else:
        print("File does not exist! Redirecting to menu...")   
        
def loadFile_admin(pathobj):
    if pathobj.is_file():
        if pathobj.suffix == '.dsu':
            journal = Profile()
            journal.load_profile(pathobj)
            return journal
        else:
            print("[NON .dsu FILE]")
            return
    else:
        print("[FILE DOES NOT EXIST]")  
