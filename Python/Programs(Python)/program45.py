'''2.Write a program which accept string from user and convert it into
upper case.
Input : “Marvellous Multi OS”
Output : MARVELLOUS MULTI OS'''

def UpperCase(str):
    for i in str:
        if(((i >= 'a')) & ((i <= 'z'))):
            str = chr(ord(i)-32)
            print(str,end='')
        else:
            str = str + i

def main():
    str = input('Enter string: ')
    UpperCase(str)




if __name__ == '__main__':
    main()

