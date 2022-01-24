def Division(A,B):
    ans = 0.0
    ans = A / B
    return  ans

def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))

    ret = Division(no1,no2)

    print("Division is : ",ret)
if __name__ == "__main__":
    main()