"""1. Accept N numbers from user and return difference between summation
of even elements and summation of odd elements.
Input : N : 6
Elements : 85 66 3 80 93 88
Output : 53 (234 - 181)"""

def DiffEvenOdd(no):
    lst = []
    Esum = 0
    Osum = 0

    for i in range(no):
        ele = int(input('Enter element: '))
        lst.append(ele)

        if ele % 2 == 0:
            Esum = Esum + ele
        else:
            Osum = Osum + ele

    iDiff = Esum - Osum
    return iDiff
    
        
def main():
    no = int(input('Enter number of elements: '))
    ret = DiffEvenOdd(no)
    print('Diffrence between Even and odd elements is: ',ret)
            
if __name__ == "__main__":
    main()