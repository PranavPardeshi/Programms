"""4. Accept N numbers from user and display all such elements which are
divisible by 3 and 5.
Input : N : 6
Elements : 85 66 3 15 93 88
Output : 15"""

class Base:
    def __init__(self):
        self.no = int(input('Enter number of elements: '))
        self.lst = []
    def CreateList(self):
        for i in range(self.no):
            self.ele = int(input('Enter element: '))
            self.lst.append(self.ele)

class DivThreeFive(Base):
    def __init__(self):  
        Base.__init__(self)
        Base.CreateList(self)
        self.ans = []

    def fun(self):
        for i in self.lst:
            if ((i % 3==0) & (i % 5==0)):
                self.ans.append(i)
        
        for i in self.ans:
            print(i,end=' ')

def main():
    obj = DivThreeFive()
    obj.fun()

if __name__ == "__main__":
    main()

