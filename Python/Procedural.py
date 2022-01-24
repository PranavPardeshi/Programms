def Addition(a,b):
    ans = a + b
    return  ans

def main():
    print("Enter first number : ")
    no1 = int(input())

    print("Enter second number : ")
    no2 = int(input())

    ret = Addition(no1,no2)

    print("addition is : ",ret)

if __name__ == "__main__":
    main()