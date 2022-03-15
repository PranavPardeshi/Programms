"""2. Design automation script which accept directory name and two file extensions from user.
Rename all files with first file extension with the second file extention.
Usage : DirectoryRename.py “Demo” “.txt” “.doc”
Demo is name of directory and .txt is the extension that we want to search and rename
with .doc.
After execution this script each .txt file gets renamed as .doc."""

import os
from sys import *


def RenameFiles(path,ext1,ext2):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists == True:
        for foldername,subfolderlist,filelist in os.walk(path):
            for subf in subfolderlist:
                pass
            for filen in filelist:
                fSplit = os.path.splitext(filen)
                if fSplit[1] == ext1:
                    newfile = fSplit[0] + ext2
                    os.rename(os.path.join(path,filen),os.path.join(path,newfile))

            print("Files are succesfully renamed.")
    else:
        print("No such directory")

def main():
    print("-----Script by Pranav Pardeshi-----")
    print("Application name:"+argv[0])

    if (len(argv) > 4) | (len(argv) < 2):
        print("Invalid arguments.")
        print("use flag -u or -h for more info.")

    if (len(argv) == 2):
        if argv[1] == "-u" or argv[1] == "-U":
            print("Usage: This script is used to rename all files with first file extension with the second file extention.")
            exit()

        elif argv[1] == "-h" or argv[1] == "-H":
            print("Help: Application_name Absolute_pathOf_Directory FirstFileName_extension SecondFileName_extension")
            exit()
        else:
            print("There is no such flag.")
    if (len(argv) == 4):
        try:
            RenameFiles(argv[1],argv[2],argv[3])
        except Exception:
            print("Exception while executing script")
            print("Please check input or contact developer.")

if __name__ == "__main__":
    main()
