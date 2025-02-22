#createfile.py
# Jerrick Aguilar
# jerricka@uci.edu
# 66335000


from pathlib import Path
from inputchecker import *
from Profile import Profile


def dsu_create():
    directory = Path(input('\nEnter file directory:\n\n* DIRECTORY: ').replace('"', ''))
    if directory.is_dir():
        #UI for file creation
        print("\n\n- REQUESTING DETAILS FROM USER -")
        print('----------------------------------------')

        #Checks username input
        flag = False
        while flag is False:
            username = input('* USERNAME: ')
            flag = input_check(username)
        #Checks password input
        flag = False
        while flag is False:
            password = input('* PASSWORD: ')
            flag = input_check(password)
        #Sets BIO to n/a if left blank
        bio = input('* BIO: ') 
        if not bio or bio.isspace():
            bio = 'N/A' 
        #Check file name input
        flag = False
        while flag is False:
            filename = input("\n* .dsu FILE NAME: ")
            flag = input_check(filename) 
        
        #File Creation (if not existing)
        if not (directory / (filename+'.dsu')).exists():
            dsuPath = directory / f'{filename}.dsu'
            dsuPath.touch() 
            journal = Profile(username=username,password=password)
            journal.bio = bio
            journal.save_profile(dsuPath)
            print("\nFile created!")
            file_details = {"Directory":directory,
                            "Filename":filename,
                            "Journal":journal,
                            "dsuPath":dsuPath}
            return file_details
        else:
            print('File exists already! Opening...')
            journal = Profile()
            journal.load_profile((directory / (filename+'.dsu')))
            file_details = {"Directory":directory,
                            "Filename":filename,
                            "Journal":journal,
                            "dsuPath": directory / f'{filename}.dsu'}
            return file_details

    else:
        print("Invalid directory! Redirecting to menu...\n")
        return