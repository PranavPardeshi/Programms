class Base1:
    def __init__(self):
        print("Inside Base1")

    def fun(self):
        print("fun of Base1")

class Base2:
    def __init__(self):
        print("Inside Base2")

    def fun(self):
        print("fun of Base2")

class Derived(Base2,Base1):
    def __init__(self):
        print("Inside Derived")
        Base2.__init__(self)
        Base1.__init__(self)

def main():
    dobj = Derived()
    dobj.fun()

if __name__ == "__main__":
    main()
