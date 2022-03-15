'''1.Design automation script which accept directory name and display checksum of all files.
Usage : DirectoryChecksum.py “Demo”
Demo is name of directory.'''

import os
import hashlib
from sys import *

def hashfile(path,blocksize = 1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DisplayCheckSum(path):
    flag = os.path.isabs(path)
    if flag == False:
        os.path.abspath(path)
    
    exists = os.path.isdir(path)

    if exists:
        for foldername,subfoldername,filelist in os.walk(path):
            print('Current folder is : ',foldername)
            for file in filelist:
                path = os.path.join(foldername,file)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print('')
    else:
        print('Invalid Path')

def main():
    print('----Script by Pranav Pardeshi-----')

    print('Application name : '+argv[0])

    if(len(argv) != 2):
        print('Error : Invalid number of arguments')
        exit()
    
    if((argv[1] == '-h') or (argv[1] == '-H')):
        print('Help : This scripts is used to traverse specific directory and display checksum of files')
        exit()
    if((argv[1] == '-u') or (argv[1] == '-U')):
        print('Usage : ApplicationName AbsolutePath_of_Directory Extension')
        exit()
    
    try:
        arr = DisplayCheckSum(argv[1])
    except ValueError:
        print('Error : Invalid datatype of input')

    except Exception as E:
        print('Error : Invalid input',E)

if __name__ == '__main__':
    main()




