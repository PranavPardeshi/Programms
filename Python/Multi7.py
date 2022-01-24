import os
import  threading

def Fun(X):
    print("PID of Fun is : ",os.getpid())   # 1000
    print("PPID of Fun : ",os.getppid())    # 3300
    print("Thread name of fun : ",threading.current_thread().name)
    print("Inside fun")
    print("Inside fun")
    for i in range(X):
        print("Fun : ",i)

def Gun(X):
    print("PID of Gun is : ",os.getpid())   # 1000
    print("PPID of Gun : ",os.getppid())    # 3300
    print("Thread name of gun : ",threading.current_thread().name)
    print("Inside gun")
    for i in range(X):
        print("Gun : ",i)

def main():             # 1000
    No = 5
    print("PID of parent process : ",os.getpid())   # 1000
    print("Thread name of main is : ",threading.current_thread().name)

    thread1 = threading.Thread(target = Fun, args = (No,), name = 'FunThread')
    thread2 = threading.Thread(target = Gun, args = (No,), name = 'GunThread')

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    
    print("End of main")
    
if __name__ == "__main__":
    main()