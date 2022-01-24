"""5. Accept N numbers from user and display all such elements which are
multiples of 11.
Input : N : 6
Elements : 85 66 3 55 93 88
Output : 66 55 88"""    

class Base:
    def __init__(self):
        self.no = int(input('Enter number of elements: '))
        self.lst = []

    def createList(self):
        print('Enter Elements: ')
        for i in range(self.no):
            self.ele = int(input())
            self.lst.append(self.ele)

class MultEleven(Base):
    def __init__(self):
        super().__init__()
        Base.createList(self)
    def logic(self):
        self.ans = []
        for i in self.lst:
            if i % 11 == 0:
                self.ans.append(i)
        
        for i in self.ans:
            print(i,end=' ')

def main():
    obj = MultEleven()
    obj.logic()
if __name__ == "__main__":
    main()