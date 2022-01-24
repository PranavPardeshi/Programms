def Division(A,B):
    ans = 0.0
    try:
        ans = A / B

    except ZeroDivisionError:
        print("Exception occured in ZeroDivisionError block")

    finally:        # Block which is used to deallocate the resources
        print("Inside Finally,This block executed always irrespective of exception.")
        
    return  ans

def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))

    ret = Division(no1,no2)

    print("Division is : ",ret)
if __name__ == "__main__":
    main()