"""2. Accept N numbers from user and return difference between frequency of
even number and odd numbers.
Input : N : 7
Elements : 85 66 3 80 93 88 90
Output : 1 (4 -3)"""

def Diffrequency(lst):
    Ecnt = 0
    Ocnt = 0
    iDiff= 0
    for i in lst:
        if i % 2 == 0:
            Ecnt = Ecnt + i
        else:
            Ocnt = Ocnt + i
    iDiff = Ecnt - Ocnt
    return iDiff

def main():
    lst = []

    no = int(input('Enter elements: '))
    print('Enter number of elements: ')
    for i in range(no):
        ele = int(input())
        lst.append(ele)

    ret = Diffrequency(lst)

    print('Difference between frequency of even number and odd numbers is {}.'.format(ret))

if __name__ == '__main__':
    main()