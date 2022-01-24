"""1. Accept number of rows and number of columns from user and display below
pattern.
Input : iRow = 4 iCol = 4
Output :
* # # #
* * # #
* * * #
* * * *
"""


class Pattern:
    def __init__(self):
        self.r = int(input('Row: '))
        self.c = int(input('Column: '))
    def Display(self):
        for i in range(1,(self.r+1)):
            for j in range(1,(self.c+1)):
                if(i>=j):
                    print('*',end='\t')
                else:
                    print('#',end='\t')
            print()
        
        print()

    def Display1(self):
        for i in range(1,(self.r+1)):
            for j in range(1,(self.c+1)):
                if(i+j >=6):
                    print('#',end='\t')
                else:
                    print('*',end='\t')
            print()

def main():
    obj = Pattern()
    obj.Display()
    obj.Display1()


if __name__ == "__main__":
    main()