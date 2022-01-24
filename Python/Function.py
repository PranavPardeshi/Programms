def Arithematic(value1,value2):
    add = value1 + value2
    sub = value1 - value2
    return add,sub

def main():
    print("Enter first number : ")
    no1 = int(input())
    
    print("Enter second number : ")
    no2 = int(input())
    
    ret1, ret2 = Arithematic(no1,no2)
    
    print("Addition is : ",ret1)
    print("Substraction is : ",ret2)
    
if __name__ == "__main__":
    main()
