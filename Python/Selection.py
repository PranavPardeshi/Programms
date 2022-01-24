
def Maximum(value1,value2):
    if (value1 > value2):
        return value1
    else:
        return value2

def main():
    print("Enter first number")
    no1 = int(input())          #   11
    
    print("Enter second numer")
    no2 = int(input())          #   21
    
    ret = Maximum(no1, no2)
    # ret = Maximum(11,21)
    
    print("Maximum number is : ",ret)

if __name__ == "__main__":
    main()
