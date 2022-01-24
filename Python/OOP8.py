class Demo:
    def __init__(self):
        self.A = 10
        self.__B = 20       # private variable of class     Abstraction

    def fun(self):
        print("Inside fun")
        self.__gun()

    def __gun(self):        # private method of class
        print("Inside gun")

def main():
    obj = Demo()
    obj.fun()
    # obj.__gun()

if __name__ == "__main__":
    main()
    
# A ia a public variable
# B is a private variable
# fun is public
# gun is private