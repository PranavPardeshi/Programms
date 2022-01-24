'''2. Write a program which accept string from user and count number of
small characters.
Input : “Marvellous”
Output : 9
'''

def CalSmall(str):
    iCnt = 0
    for i in str:
        if ((i >= 'a') & (i <='z')):
            iCnt += 1
    return  iCnt

def main():
    str = (input('Enter string:'))
    ret = CalSmall(str)
    print('Small characters is {}.'.format(ret))
if __name__ == '__main__':
    main()
