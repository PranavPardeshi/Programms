"""4. Accept Character from user and check whether it is small case or not (a-z).
Input : g
Output : TRUE
Input : D
Output : FALSE"""

def CheckSmall(ch):
    if (ch >= 'a') & (ch <= 'z'):
        return  True
    else:
        return  False

def main():
    ch =input('Enter character: ')
    ret = CheckSmall(ch)

    if ret == True:
        print('{} is small case'.format(ch))
    else:
        print('False')

if __name__ == '__main__':
    main()