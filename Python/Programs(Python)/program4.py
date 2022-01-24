"""3. Accept number of rows and number of columns from user and display
below pattern.
Input : iRow = 3 iCol = 5
Output :
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1"""

class Pattern:

    def __init__(self):
        self.row = int(input('Enter rows: '))
        self.col = int(input('Enter columns: '))
    
    def Display(self):
        for i in range(1,(self.row+1)):
            for j in range(1,(self.col+1)):
                if((j % 2) == 0):
                    print('#',end=" ")
                else:
                    print('*',end=" ")
            print()
def main():
    obj = Pattern()
    obj.Display()
if __name__ == "__main__":
    main()