"""1. Accept Character from user and check whether it is alphabet or not (A-Z a-z).
Input : F
Output : TRUE
Input : &
Output : FALSE"""

def CheckAlha(ch):
    if ((ch >= 'A') | (ch <= 'Z')) & ((ch >= 'a') | (ch <= 'z')):
        return  True
    else:
        return  False

def main():
    char = input('Enter character: ')

    ret = CheckAlha(char)

    if ret == True:
        print('True')
    else:
        print('False')
if __name__ == '__main__':
    main()