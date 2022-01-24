import os

def Fun():
    print("PID is : ",os.getpid())
    print("Inside fun")
    for i in range(500000000):
        print("Fun : ",i)

def Gun():
    print("PID is : ",os.getpid())
    print("Inside gun")
    for i in range(500000000):
        print("Gun : ",i)

def main():
    print("PID is : ",os.getpid())
    Fun()
    Gun()
    
if __name__ == "__main__":
    main()