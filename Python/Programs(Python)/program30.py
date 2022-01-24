'''4. Accept N numbers from user and display all such numbers which contains
3 digits in it.
Input : N : 6
Elements : 8225 665 3 76 953 858
Output : 665 953 858'''

class ThreeDigits:
    def __init__(self):
        self.no = int(input('Enter number of elements: '))
        self.data = []
        self.iDigit = 0
        self.iCnt = 0
        self.temp = 0

    def Accept(self):
        print('Enter elements:')
        for i in range(self.no):
            ele = int(input())
            self.data.append(ele)

    def threeDig(self):
        for i in self.data:
            self.temp = i
            while(i != 0):
                self.iDigit = int(i % 10)
                self.iCnt = self.iCnt + 1
                i = int(i / 10)
            if self.iCnt == 3:
                print(self.temp)



def main():
    obj = ThreeDigits()
    obj.Accept()
    obj.threeDig()

if __name__ == '__main__':
    main()