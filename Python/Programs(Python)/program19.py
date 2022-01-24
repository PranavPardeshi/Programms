"""3. Accept N numbers from user check whether that numbers contains 11 in it or not.
Input : N : 6
Elements : 85 66 11 80 93 88
Output : 11 is present
Input : N : 6
Elements : 85 66 3 80 93 88
Output : 11 is absent"""

class Base:
    def __init__(self):
        self.no = int(input('Enter number of elements: '))
        self.lst = []

    def CreateList(self):
        print('Enter elements: ')
        for i in range(self.no):
            self.ele = int(input())
            self.lst.append(self.ele)

class CheckEleven(Base):
    def __init__(self):
        super().__init__()
        Base.CreateList(self)
    
    def Logic(self):
        for i in self.lst:
            if i == 11:
                return True
                
def main():
    obj = CheckEleven()
    ret = obj.Logic()

    if ret == True:
        print('11 is present')
    else:
        print('11 is absent')

if __name__ == '__main__':
    main()