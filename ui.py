# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Jerrick Aguilar
# jerricka@uci.edu
# 66335000

from createfile import *
from journalfunctions import *
from loadfile import loadFile

def launch_ui(entry):
    
    if entry.lower() == 'c':
        file = dsu_create()
        if file is None:
            return 
        journalcmds(file["dsuPath"],file["Journal"])
    elif entry.lower() == 'o':
        directory = Path(input('\nEnter directory of desired file:\n\n* DIRECTORY: ').replace('"', ''))
        journal = loadFile(directory)
        if journal is None:
            return 
        journal.save_profile(directory)
        journalcmds(directory,journal)
    else:
        return



e_opt = ['-usr','-pwd','-bio','-addpost','-delpost'] 
p_opt = ['-usr','-pwd','-bio','-posts','-post','-all']


