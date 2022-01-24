"""2. Accept number of rows and number of columns from user and display
below pattern.
Input : iRow = 4 iCol = 3
Output : 
1 2 3
1 2 3
1 2 3
1 2 3"""


class Pattern:
    def __init__(self):
        self.row = int(input('Enter number of rows: '))
        self.col = int(input('Enter number of columns: '))

    def Display(self):
        for i in range(self.row):
            for j in range(1,(self.col+1)):
                print(j,end=" ")
            print()
def main():
    obj = Pattern()
    obj.Display()
if __name__ == "__main__":
    main()