'''3. Accept Character from user and check whether it is digit or not
(0-9).
Input : 7
Output : TRUE
Input : d'''

def CheckDigit(ch):
    if (ch >= '0') & (ch <= '9'):
        return  True
    else:
        return  False

def main():
    ch =input('Enter input: ')
    ret = CheckDigit(ch)

    if ret == True:
        print('True')
    else:
        print('False')

if __name__ == '__main__':
    main()