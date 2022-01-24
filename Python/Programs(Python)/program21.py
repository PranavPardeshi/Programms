'''5.Accept N numbers from user and accept one another number as NO ,
return frequency of NO form it.
Input : N : 6
NO: 66
Elements : 85 66 3 66 93 88
Output : 2
Input : N : 6
NO: 12
Elements : 85 11 3 15 11 111
Output : 0'''

class List:
    def __init__(self):
        self.number = int(input('Enter number of elements: '))
        self.data = []
    def CreateList(self):
        print('Enter elements: ')
        for i in range(self.number):
            self.ele = int(input())
            self.data.append(self.ele)

class CheckFreq(List):
    def __init__(self):
        super().__init__()
        self.no = int(input('Enter Number: '))
        self.Cnt = 0
        super().CreateList()
        
    def logic(self):
        for i in self.data:
            if i == self.no:
                self.Cnt += 1
        return self.Cnt

def main():
    obj = CheckFreq()
    ret = obj.logic()
    
    print('Frequency of given number is : {} '.format(ret))
    
if __name__ == '__main__':
    main()