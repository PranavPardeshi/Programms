"""3. Accept number of rows and number of columns from user and display
below pattern.
Input : iRow = 3 iCol = 5
Output :
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1"""

class Pattern:
    value = 5
    def __init__(self):
        self.row = int(input('Enter rows: '))
        self.col = int(input('Enter columns: '))
    def Display(self):
        for i in range(self.row):
            for j in range(self.col,0,-1):
                print(j,end=' ')
            print()
def main():
    obj = Pattern()
    obj.Display()
if __name__ == "__main__":
    main()