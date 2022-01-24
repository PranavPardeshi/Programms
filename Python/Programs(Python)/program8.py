"""4. Accept number of rows and number of columns from user and display below
pattern.
Input : iRow = 6 iCol = 5
Output :
* * * * *
* @ @ @ *
* @ @ @ *
* @ @ @ *
* @ @ @ *
* * * * *
"""

class Pattern:
    def __init__(self):
        self.r = int(input('Row: '))
        self.c = int(input('Column: '))
    def Display(self):
        for i in range(1,(self.r+1)):
            for j in range(1,(self.c+1)):
                if (i == 1 ) |(j == 1): 
                    print('*',end=' ')
                elif(i == 6) | (j == 5):
                    print('*',end=' ')
                else:
                    print('@',end=' ')
            print()


def main():
    obj = Pattern()
    obj.Display()
if __name__ == "__main__":
    main()
