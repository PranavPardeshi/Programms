import os

def Fun():
    print("PID is : ",os.getpid())
    print("Inside fun")

def Gun():
    print("PID is : ",os.getpid())
    print("Inside gun")

def main():
    print("PID is : ",os.getpid())
    Fun()
    Gun()
    
if __name__ == "__main__":
    main()