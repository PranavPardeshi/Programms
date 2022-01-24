"""2. Accept N numbers from user and display all such elements which are
divisible by 5.
Input : N : 6
Elements : 85 66 3 80 93 88
Output : 85 80"""

def DivFive(no):
    lst = []
    ans = []
    for i in range(no):
        ele = int(input('Enter element: '))
        lst.append(ele)

        if ele % 5 == 0:
           ans.append(ele)
    for i in ans:
        print(i,'is divisible by 5') 
def main():
    no = int(input('Enter number of elements: '))
    DivFive(no)
if __name__ == "__main__":
    main()