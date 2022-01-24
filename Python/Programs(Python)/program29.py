'''3. Accept N numbers from user and return the difference between largest and smallest number.
Input : N : 6
Elements : 85 66 3 66 93 88
Output : 90 (93 -3)'''

class DiffLargeSmall:
    def __init__(self):
        self.no = int(input('Enter number of elements: '))
        self.data = []
        self.iDiff = 0
        self.temp = 0
        self.large = 0
        self.small = 0

    def Accept(self):
        print('Enter elements:')
        for i in range(self.no):
            ele = int(input())
            self.data.append(ele)

    def diffLargeSmall(self):
        for i in self.data:
            self.temp = i
            if self.small == 0 & self.large == 0:
                self.large = self.temp
                self.small = self.temp
            elif self.temp > self.large:
                self.large = self.temp
            elif self.temp < self.small:
                self.small = self.temp
            else:
                pass

        self.iDiff = self.large - self.small
        return  self.iDiff

def main():
    obj = DiffLargeSmall()
    obj.Accept()
    ret = obj.diffLargeSmall()

    print('Difference between large and small number is {}.'.format(ret))
if __name__ == '__main__':
    main()