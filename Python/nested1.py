def outer():    # 0X100
    print("Inside Outer function")

    def Inner():    # 0X200
        print("Inside Inner function")

    return  Inner   # return  0X200

def main():
    func_name = outer() # Its call to the outer function
    func_name()     # Its call to the inner function
    # Inner()

if __name__ == "__main__":
    main()