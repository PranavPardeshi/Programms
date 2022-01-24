import os
import  threading

def Fun(X):
    print("PID of Fun is : ",os.getpid())   # 1000
    print("PPID of Fun : ",os.getppid())    # 3300
    print("Inside fun")
    for i in range(X):
        print("Fun : ",i)

def Gun(X):
    print("PID of Gun is : ",os.getpid())   # 1000
    print("PPID of Gun : ",os.getppid())    # 3300
    print("Inside gun")
    for i in range(X):
        print("Gun : ",i)

def main():             # 1000
    No = 5
    print("PID of parent process : ",os.getpid())   # 1000

    thread1 = threading.Thread(target = Fun, args = (No,))
    thread2 = threading.Thread(target = Gun, args = (No,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    
    print("End of main")
    
if __name__ == "__main__":
    main()