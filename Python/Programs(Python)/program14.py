"""3. Accept N numbers from user and display all such elements which are
even and divisible by 5.
Input : N : 6
Elements : 85 66 3 80 93 88
Output : 80"""

class DivFiveEven:
    
    def __init__(self):
        self.no = int(input('Enter number of elements: '))
        self.lst = []
    
    def CreateList(self):
        for i in range(self.no):
            self.ele = int(input('Enter element: '))
            self.lst.append(self.ele)

class divFiveEven(DivFiveEven):

    def __init__(self):
        super().__init__()
        super().CreateList()
        self.ans = []
    
    def Logic(self):
        for i in self.lst:
            if i % 2 == 0:
                if i % 5 == 0:
                    self.ans.append(i)
        for i in self.ans:
            print(i,'is even number and divisible by 5')

def main():
    obj = divFiveEven()
    obj.Logic()

if __name__ == "__main__":
    main()

