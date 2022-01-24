"""4. Accept N numbers from user and return frequency of 11 form it.
Input : N : 6
Elements : 85 66 3 15 93 88
Output : 0
Input : N : 6
Elements : 85 11 3 15 11 111
Output : 2"""

class List:
    def __init__(self):
        self.number = int(input('Enter number of elements: '))
        self.data = []
    
    def CreateList(self):
        print('Enter elements:',end=' ')
        for i in range(self.number):
            self.ele = int(input())
            self.data.append(self.ele)

class CheckFreEleven(List):
    def __init__(self):
        super().__init__()
        super().CreateList()
        self.Cnt = 0

    def logic(self):
        for i in self.data:
            if i == 11:
                self.Cnt += 1
        return self.Cnt

def main():
    obj = CheckFreEleven()
    ret = obj.logic()

    print('frequency of 11 is: {}'.format(ret))
if __name__ == '__main__':
    main()