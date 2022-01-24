"""1. Accept N numbers from user and return frequency of even numbers.
Input : N : 6
Elements : 85 66 3 80 93 88
Output : 3"""

class Frequency:
    def __init__(self):
        self.no = int(input('Enter number of elements: '))
        self.lst = []

    def CreateList(self):
        print('Enter number of elements: ')
        for i in range(self.no):
            self.ele = int(input())
            self.lst.append(self.ele)

class ChkEvenFreq(Frequency):
    def __init__(self):
        super().__init__()
        super().CreateList()
        self.cnt = 0

    def logic(self):
        for i in self.lst:
            if i % 2 == 0:
                self.cnt = self.cnt + 1

        return self.cnt


def main():
    obj = ChkEvenFreq()
    ret = obj.logic()
    print('Frequency of even number: ',ret)
if __name__ == '__main__':
    main()