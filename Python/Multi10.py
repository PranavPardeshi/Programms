import os
import  multiprocessing

def Square(No):
    print("PID is : ",os.getpid())
    return  No*No

def main():
    data = [5,323,15,41,2,15,61,32,156,1,21531,1,4,8,2]

    p = multiprocessing.Pool()

    result = list()
    
    result = p.map(Square,data)

    print("Result is : ",result)

if __name__ == "__main__":
    main()