"""
5. Accept number of rows and number of columns from user and display
below pattern.
Input : iRow = 4 iCol = 4
Output : 1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4"""

class Pattern:
    def __init__(self):
        self.row = int(input('Enter rows: '))
        self.col = int(input('Enter columns: '))

    def Display(self):
        for i in range(1,(self.row+1)):
            for j in range(1,(self.col+1)):
                print(i,end=" ")
            print()    
def main():
    obj = Pattern()
    obj.Display()

if __name__ == "__main__":
    main()