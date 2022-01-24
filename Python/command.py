#import  sys
from sys import *

def main():
    print("Number of command line arguments are : ",len(argv))
    print("Name of application is  : ",argv[0])
    print("First argument : ",argv[1])
    print("Second argument : ",argv[2])

if __name__ == "__main__":
    main()
