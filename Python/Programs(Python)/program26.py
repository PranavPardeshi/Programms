"""5. Accept N numbers from user and return product of all odd elements.
Input : N : 6
Elements : 15 66 3 70 10 88
Output : 45
Input : N : 6
Elements : 44 66 72 70 10 88
Output : 0"""

class DisplayRange:
    def __init__(self):
        self.no = int(input('Enter of elements: '))
        self.lst = []
    
    def Accept(self):
        print('Enter numbers: ')
        for i in range(self.no):
            self.ele = int(input())
            self.lst.append(self.ele)

    def Display(self):    
        print('Odd Numbers:',end='\t')
        for i in self.lst:
            if i % 2 != 0:
                print(i,end='\t')

def main():
    obj = DisplayRange()
    obj.Accept()
    obj.Display()

if __name__ == '__main__':
    main()