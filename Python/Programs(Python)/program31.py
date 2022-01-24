'''5. Accept N numbers from user and display summation of digits of each
number.
Input : N : 6
Elements : 8225 665 3 76 953 858
Output : 17 17 3 13 17 21'''

class SumDigit:
    def __init__(self):
        self.no = int(input('Enter number of elements: '))
        self.data = []
        self.iDigit = 0
        self.sum = 0

    def Accept(self):
        print('Enter elements:')
        for i in range(self.no):
            ele = int(input())
            self.data.append(ele)

    def sumDigit(self):
        for i in self.data:
            self.sum = 0
            while(i != 0):
                self.iDigit = int(i % 10)
                self.sum = self.sum + self.iDigit
                i = int(i / 10)
            print('Output: {}'.format(self.sum))

def main():
    obj = SumDigit()
    obj.Accept()
    obj.sumDigit()

if __name__ == '__main__':
    main()