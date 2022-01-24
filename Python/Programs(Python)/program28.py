"""2. Accept N numbers from user and return the smallest number.
Input : N : 6
Elements : 85 66 3 66 93 88
Output : 3"""

class SmallNum:
    def __init__(self):
        self.no = int(input('Enter number of elements: '))
        self.data = []
        self.temp = 0
        self.small = 0

    def Accept(self):
        print('Enter elements:')
        for i in range(self.no):
            ele = int(input())
            self.data.append(ele)

    def smallNum(self):
        for i in self.data:
            self.temp = i
            if self.small == 0:
                self.small = self.temp
            elif self.small > self.temp:
                self.small = self.temp
            else:
                pass
        return  self.small

def main():
    obj = SmallNum()
    obj.Accept()
    ret = obj.smallNum()

    print('Smallest number is: {}.'.format(ret))

if __name__ == '__main__':
    main()


