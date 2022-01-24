"""4. Accept N numbers from user and accept Range, Display all elements from that range
Input : N : 6
Start: 60
End : 90
Elements : 85 66 3 76 93 88
Output : 66 76 88
Input : N : 6
Start: 30
End : 50
Elements : 85 66 3 76 93 88
Output : """


class DisplayRange:
    def __init__(self):
        self.no = int(input('Enter of elements: '))
        self.start = int(input('Start: '))
        self.end = int(input('End: '))
        self.lst = []
    
    def Accept(self):
        print('Enter numbers: ')
        for i in range(self.no):
            self.ele = int(input())
            self.lst.append(self.ele)

    def Display(self):    
        print('Output:',end=' ')
        for i in self.lst:
            if (i >= self.start) & (i <= self.end):
                print(i,end='\t')

def main():
    obj = DisplayRange()
    obj.Accept()
    obj.Display()

if __name__ == '__main__':
    main()