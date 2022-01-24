#import Marvellous

def Addition(Value):
    sum = 0
    i = 0
    # for i in range(3)
    # for i in (0,1,2)
    for i in range(len(Value)):
        sum = sum + Value[i]

    return sum

def main():
    size = 0
    i = 0
    Data = []

    print("How many elements you want?")
    size = int(input())
    
    print("Enter the elements : ")
    for i in range(size):   # for i in range(0,1,2)
        Data.append(int(input()))
        
    print("Your enetered data is : ",Data)
    
    ret = Addition(Data)
    print("Addition is : ",ret)
    
if __name__ == "__main__":
    main()
