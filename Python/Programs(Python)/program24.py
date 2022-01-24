"""3. Accept N numbers from user and accept one another number as NO ,return index of last occurrence of that NO.
Input : N : 6
NO: 66
Elements : 85 66 3 66 93 88
Output : 3
Input : N : 6
NO: 93
Elements : 85 66 3 66 93 88
Output : 4
Input : N : 6
NO: 12
Elements : 85 11 3 15 11 111
Output : -1"""

def LastOcc(data,num):
    iCnt = len(data)
    for i in range(iCnt,0,-1):
        if i == num:
            return iCnt
        iCnt -= 1
def main():
    no = int(input('Enter number of elements: '))
    number = int(input('Enter number: '))

    lst = []
    print('Enter elements: ',end=' ')
    for i in range(no):
        ele = int(input())
        lst.append(ele)
    
    ret = LastOcc(lst,number)
    print('Last Occurance: {}'.format(ret))
if __name__ == '__main__':
    main()