"""4. Design automation script which accept two directory names and one file extension. Copy all
files with the specified extension from first directory into second directory. Second directory
should be created at run time.
Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe”
Demo is name of directory which is existing and contains files in it. We have to create new
Directory as Temp and copy all files with extension .exe from Demo to Temp."""

import os
import shutil
from sys import *

def DirectoryCopyExt(src,dest,ext):
    flag = os.path.isabs(src)

    if flag == False:
        os.path.abspath(src)

    exists = os.path.isdir(src)

    if exists:
        for folderName,subfolderName,fileList in os.walk(src):
            print('Current folder name : ',folderName)
            
            for subf in subfolderName:
                print('Current sub folder name: ',subfolderName)
            
            for file in fileList:
                fSplit = os.path.splitext(file)
                if fSplit[1] == ext:
                    flag = os.path.isdir(dest)
                    if flag == False:
                        os.mkdir(dest)
                        shutil.copy2(os.path.join(src,file),dest)
                    else:
                        try:
                           shutil.copy2(os.path.join(src,file),dest)
                        except:
                            pass
                        
def main():
    print("-----Script by Pranav Pardeshi-----")
    print("Application name:" + argv[0])

    if (len(argv) > 4) or (len(argv) < 2):
        print("Invalid arguments.")
        print("use flag -u or -h for more info.")
        exit()

    if (len(argv) == 2):
        if argv[1] == "-u" or argv[1] == "-U":
            print("Usage: DirectoryCopy.py “Demo” “Temp” “.exe”")
            exit()

        elif argv[1] == "-h" or argv[1] == "-H":
            print("Help: Application_name Absolute_pathOf_Directory Second_Directory  File_Extension")
            exit()
        else:
            print("There is no such flag.")

    if (len(argv) == 4):
        try:
            DirectoryCopyExt(argv[1],argv[2],argv[3])
            print("Successfully run!!")
        except Exception:
            print("Exception while executing script")
            print("Please check input or contact developer.")
        
if __name__ == "__main__":
    main()