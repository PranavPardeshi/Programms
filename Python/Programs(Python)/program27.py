"""1. Accept N numbers from user and return the largest number.
Input : N : 6
Elements : 85 66 3 66 93 88
Output : 93"""

class LargestNum:
    def __init__(self):
        self.no = int(input('Enter number of elements: '))
        self.data = []
        self.temp = 0
        self.large = 0

    def Accept(self):
        print('Enter elements: ')
        for i in range(self.no):
            self.ele = int(input())
            self.data.append(self.ele)

    def largeNum(self):
        for i in self.data:
            self.temp = i
            if self.temp > self.large:
                self.large = self.temp
        return  self.large

def main():
    obj = LargestNum()
    obj.Accept()
    ret = obj.largeNum()
    print('Largets number is {}.'.format(ret))

if __name__ == "__main__":
    main()
