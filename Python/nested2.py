# 0X100
def fun():
    print("Inside fun")
    
# 0X200
def gun(func_Name):
    print("Inside gun")
    func_Name()     # fun()
    
def main():
    gun(fun)    # gun(0X100)
    
if __name__ == "__main__":
    main()