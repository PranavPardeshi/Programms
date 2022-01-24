"""2. Accept N numbers from user and accept one another number as NO, return index of first occurrence of that NO.
Input : N : 6
NO: 66
Elements : 85 66 3 66 93 88
Output : 1
Input : N : 6
NO: 12
Elements : 85 11 3 15 11 111
Output : -1"""

def FirstOcc(data,num):
    iCnt = 0
    for i in data:
        iCnt += 1
        if num == i:
            return iCnt

def main():
    no = int(input('Enter number of elements: '))
    number = int(input('Enter number: '))

    lst = []
    print('Enter elements: ',end=' ')
    for i in range(no):
        ele = int(input())
        lst.append(ele)
    
    ret = FirstOcc(lst,number)
    print('First Occurance: {}'.format(ret))
if __name__ == '__main__':
    main()