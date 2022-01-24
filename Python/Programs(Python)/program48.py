'''1.Write a program which accept string from user and accept one
character. Check whether that character is present in string or not.
Input : “Marvellous Multi OS”
e
Output : TRUE
Input : “Marvellous Multi OS”
W
Output : FALSE'''

def CheckChar(str,ch):
    for i in str:
        if i == ch:
            return  True
        else:
            return  False

def main():
    str = input('Enter string: ')
    ch = input('Enter character: ')

    ret = CheckChar(str,ch)
    if ret == True:
        print('{} is present in {}.'.format(ch,str))
if __name__ == '__main__':
    main()