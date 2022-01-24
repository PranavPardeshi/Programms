'''3. Write a program which accept string from user and return
difference between frequency of small characters and frequency of
capital characters.
Input : “MarvellouS”
Output : 6 (8-2)'''

def DiffFrequency(str):
    iSmallCnt = 0
    iCapCnt = 0
    for i in str:
        if ((i >= 'a') & (i <='z')):
            iSmallCnt += 1
        elif((i >= 'A') & (i <= 'Z')):
            iCapCnt += 1

    iDiff = iCapCnt - iSmallCnt
    return  iDiff

def main():
    str = (input('Enter string:'))
    ret = DiffFrequency(str)
    print('Differnce between small characters and capital character is {}.'.format(ret))
if __name__ == '__main__':
    main()