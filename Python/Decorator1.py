def Division(A,B):                  # 0X100
    Ans = 0.0
    Ans =  A/B
    return  Ans

def SmartDivision(Func_Name):       # Func_Name -> 0X100
    def Inner(a,b):                 # 0X200
        if a < b:
            a,b = b,a
        return  Func_Name(a,b)      # return 0X100(____, ___)

    return  Inner                   # return 0X200

Division = SmartDivision(Division)  # Division = SmartDivision(0X100)

def main():
    No1 = 0
    No2 = 0

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))
    ret = Division(No1,No2)         # 0X200(5,10)
    print("Division is  : ",ret)

if __name__ == "__main__":
    main()