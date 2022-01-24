'''5. Write a program which accept string from user and count number of white spaces
Input : “MarvellouS”
Output : 0
Input : “MarvellouS Infosystems”
Output : 1
Input : “MarvellouS Infosystems by Piyush Manohar Khairnnar”
Output : 5
'''

def CountWhiteSpace(str):
    iCnt = 0
    for i in str:
        if (i == ' '):
            iCnt += 1
    return iCnt

def main():
    str = input('Enter string: ')
    ret = CountWhiteSpace(str)
    print('White spaces are {}'.format(ret))
if __name__ == '__main__':
    main()
