import os
import  multiprocessing

def Square(No):
    print("PID is : ",os.getpid())
    return  No*No

def main():
    data = [5,3,1,4,8,2]

    result = list()
    
    for i in range(len(data)):
        result.append(Square(data[i]))

    print("Result is : ",result)

if __name__ == "__main__":
    main()