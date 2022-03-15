"""1.Design automation script which accept directory name and file extension from user. Display all
files with that extension.
Usage : DirectoryFileSearch.py “Demo” “.txt”
Demo is name of directory and .txt is the extension that we want to search."""

import os
from sys import *

def SearchFile(dir,ext):
    flag = os.path.isabs(dir)
    if flag == False:
        dir = os.path.abspath(dir)
    exists = os.path.isdir(dir)

    if exists:
        for foldername,subfolder,filename in os.walk(dir):
            for filen in filename:
                if filen.endswith(ext):
                    print(filen)
    else:
        print("Invalid Path")

def main():
    print("-----------Script by Pranav Pardeshi-----------")
    print("Application name:",argv[0])


    if (len(argv) > 3) or (len(argv) < 2):
        print("Invalid number of argument")
        print("Use -u flag for usage.")

    if(len(argv) == 2):
        if argv[1] == "-u" or argv[1] == "-U":
            print("Usage:This script is used to traverse specific directory")
            exit()

        elif argv[1] == "-h" or argv[1] == "-H":
            print("Help: ")
            print('First_Argument:Directory name')
            print('Second_Argument:File extension')
            exit()
        else:
            print("There is no such a flag")
    if(len(argv) == 3):
        try:
            SearchFile(argv[1],argv[2])
        except ValueError:
            print('Exception while executing the script')
            print('Please check the input or contact the developer')


if __name__ == "__main__":
    main()
