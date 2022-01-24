"""1. Accept number of rows and number of columns from user and display
below pattern.
Input : iRow = 4 iCol = 3
Output :
* * *
* * *
* * *
* * *"""

class Pattern:
    def __init__(self):
        self.row = int(input('Enter rows: '))
        self.col = int(input('Enter columns: '))
    def Display(self):
        for i in range(self.row):
            for j in range(self.col):
                print('*',end=' ')
            print()


def main():
    obj = Pattern()
    obj.Display()
if __name__ == "__main__":
    main()