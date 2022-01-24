#import  sys
from sys import *

def main():
    print("Number of command line arguments are : ",len(argv))
    print("Name of application is  : ",argv[0])

    ans = int(argv[1]) + int(argv[2])
    print("Datatype of argument is  : ",type(argv[1]))
    print("Addition is : ",ans)

if __name__ == "__main__":
    main()
