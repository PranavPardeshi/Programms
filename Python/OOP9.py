class Base:
    def __init__(self):
        print("Inside base constructor")
        self.A = 10

    def fun(self):
        print("Base fun")

#############################################

class Derived(Base):
    def __init__(self):
        #Base.__init__(self)
        super().__init__()
        print(super().A)
        print("Inside derived constructor")
        self.B = 20

    def gun(self):
        print("Derived gun")

def main():
    dobj = Derived()
    dobj.fun()
    print(dobj.A)


if __name__ == "__main__":
    main()



# C++
# class derived : public base

# Java
# class derived extends base