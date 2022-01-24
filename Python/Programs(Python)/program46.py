'''4. Write a program which accept string from user and display only digits from that string.
Input : “marve89llous121”
Output : 89121
Input : “Demo”
Output :'''


def DisplayInt(str):
    for i in str:
        if ((i >= '0') & (i <= '9')):
            print(i,end='')
def main():
    str = input('Enter string: ')
    DisplayInt(str)
if __name__ == '__main__':
    main()




