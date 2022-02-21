"""3. Design automation script which accept two directory names. Copy all files from first directory
into second directory. Second directory should be created at run time.
Usage : DirectoryCopy.py “Demo” “Temp”
Demo is name of directory which is existing and contains files in it. We have to create new
Directory as Temp and copy all files from Demo to Temp."""

import os
import shutil
from sys import *

def DirectoryCopy(dir1,dir2):
    flag = os.path.isabs(dir1)

    if flag == False:
        dir1 = os.path.abspath(dir1)

    exists = os.path.isdir(dir1)

    if exists:
        for foldername,subfolderlist,filelist in os.walk(dir1):
            print("Current folder is : "+foldername)
            for subf in subfolderlist:
                print("Subfolder of "+foldername+" is "+subf)
            
            for filen in filelist:
                flag = os.path.isdir(dir2)
                if flag == False:
                    os.mkdir(dir2)
                    shutil.copy2(os.path.join(dir1,filen),dir2)    
                    ''' For file cut paste : shutil.move(os.path.join(dir1,filen),os.path.join(dir2,filen))
                    '''
                else:
                    try:
                        shutil.copy2(os.path.join(dir1,filen),dir2)
                    except:
                        pass

def main():
    print("-----Script by Pranav Pardeshi-----")
    print("Application name:" + argv[0])

    if (len(argv) > 3) or (len(argv) < 2):
        print("Invalid arguments.")
        print("use flag -u or -h for more info.")
        exit()

    if (len(argv) == 2):
        if argv[1] == "-u" or argv[1] == "-U":
            print("Usage: DirectoryCopy.py “Demo” “Temp”")
            exit()

        elif argv[1] == "-h" or argv[1] == "-H":
            print("Help: Application_name Absolute_pathOf_Directory Second_Directory")
            exit()
        else:
            print("There is no such flag.")

    if (len(argv) == 3):
        try:
            DirectoryCopy(argv[1],argv[2])
            print("Successfully run!!")
        except Exception:
            print("Exception while executing script")
            print("Please check input or contact developer.")
        
if __name__ == "__main__":
    main()
