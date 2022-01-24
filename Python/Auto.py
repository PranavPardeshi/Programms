# import statements if necessary
from sys import *

# Entry point of automation script
def main():
    print("------ Marvellous Infosystems : Automation1 ------- ")
    print("Script name : ", argv[0])
    print("Number of arguments accepted : ",len(argv) - 1)
    
    if (len(argv) > 3) or (len(argv) < 2):
        print("Invalid number of arguments")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Script is used to perform the addition of 2 numbers")

        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : Name_of_Script First_Argument Second_argument")
        print("First_Argument : Any numeric value")
        print("Second_Argument : Any numeric value")
        exit()

# Starter of the automation script
if __name__ == "__main__":
    main()