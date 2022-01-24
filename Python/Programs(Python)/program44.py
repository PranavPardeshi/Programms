'''1.Write a program which accept string from user and convert it into
lower case.
Input : “Marvellous Multi OS”
Output : marvellous multi os'''


def LowerCase(str):
    for i in str:
        if ((i >= 'A') & (i <= 'Z')):
            str = chr(ord(i)+32)
            print(str,end='')
    return str

def main():
    str = input('Enter string: ')
    ret = LowerCase(str)
    print(ret)
if __name__ == '__main__':
    main()