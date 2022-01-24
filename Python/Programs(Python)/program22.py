"""1. Accept N numbers from user and accept one another number as NO ,
check whether NO is present or not.
Input : N : 6
NO: 66
Elements : 85 66 3 66 93 88
Output : TRUE
Input : N : 6
NO: 12
Elements : 85 11 3 15 11 111
Output : FALSE"""

class List:
    def __init__(self):
        self.number = int(input('Enter number of elements: '))
        self.data = []
    def CreateList(self):
        print('Enter elements: ')
        for i in range(self.number):
            self.ele = int(input())
            self.data.append(self.ele)

class CheckNumber(List):
    def __init__(self):
        super().__init__()
        self.no = int(input('Enter Number: '))
        super().CreateList()

    def chknum(self):
        for i in self.data:
            if i == self.no:
                return True

def main():
    obj = CheckNumber()
    ret = obj.chknum()
    if ret == True:
        print('Ans: {}'.format(ret))
    else:
        print('False')
if __name__ == '__main__':
    main()