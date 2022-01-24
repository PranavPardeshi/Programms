class Base:
    def __init__(self):
        self.i = 10
        self.j = 20

    def fun(self):
        print("Base fun")

    def gun(self):
        print("Base gun")

class Derived(Base):
    def __init__(self):
        self.a= 11
        self.b = 21

    def fun(self):
        print("Derived fun")

    def sun(self):
        print("Derived sun")

def main():
    bobj = Base()
    dobj = Derived()

    bobj.fun()
    dobj.fun()
    dobj.sun()
    dobj.gun()

if __name__ == "__main__":
    main()