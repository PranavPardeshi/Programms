"""1.Write a program which accept string from user and count number of
capital characters.
Input : “Marvellous Multi OS”
Output : 4"""


def CalCapital(str):
    iCnt = 0
    for i in str:
        if ((i >= 'A') & (i <='Z')):
            iCnt += 1
    return  iCnt

def main():
    str = (input('Enter string:'))
    ret = CalCapital(str)
    print('Capital characters are {}.'.format(ret))
if __name__ == '__main__':
    main()
