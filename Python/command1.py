#import  sys
from sys import *

def main():
    print("Number of command line arguments are : ",len(argv))
    print("Name of application is  : ",argv[0])

    print("Command line argumnents are : ")
    for data in argv:
        print(data)

if __name__ == "__main__":
    main()
