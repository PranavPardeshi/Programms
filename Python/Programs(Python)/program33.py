'''2. Accept Character from user and check whether it is capital or not
(A-Z).
Input : F
Output : TRUE
Input : d
Output : FALSE'''

def CheckCaps(ch):
    if (ch >= 'A') & (ch <= 'Z'):
        return  True
    else:
        return  False

def main():
    ch =input('Enter character: ')
    ret = CheckCaps(ch)

    if ret == True:
        print('True')
    else:
        print('False')

if __name__ == '__main__':
    main()


