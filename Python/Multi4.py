import os
import  multiprocessing

def Fun(X):
    print("PID of Fun is : ",os.getpid())
    print("Inside fun")
    for i in range(X):
        print("Fun : ",i)

def Gun(X):
    print("PID of Gun is : ",os.getpid())
    print("Inside gun")
    for i in range(X):
        print("Gun : ",i)

def main():
    print("PID of parent process : ",os.getpid())
    Fun(5)
    Gun(10)
    
if __name__ == "__main__":
    main()