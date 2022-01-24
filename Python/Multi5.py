import os
import  multiprocessing

def Fun(X):
    print("PID of Fun is : ",os.getpid())
    print("PPID of Fun : ",os.getppid())
    print("Inside fun")
    for i in range(X):
        print("Fun : ",i)

def Gun(X):
    print("PID of Gun is : ",os.getpid())
    print("PPID of Gun : ",os.getppid())
    print("Inside gun")
    for i in range(X):
        print("Gun : ",i)

def main():
    No = 5
    print("PID of parent process : ",os.getpid())

    process1 = multiprocessing.Process(target = Fun, args = (No,))
    process2 = multiprocessing.Process(target = Gun, args = (No,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
    
    print("End of main")
    
if __name__ == "__main__":
    main()