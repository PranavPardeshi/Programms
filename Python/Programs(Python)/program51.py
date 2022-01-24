'''4.Write a program which accept string from user and accept one
character. Return index of last occurrence of that character.
Input : “Marvellous Multi OS”
M
Output : 11
Input : “Marvellous Multi OS”
W
Output : -1
Input : “Marvellous Multi OS”
e
Output : 4'''

def IndexLastOcc(str,ch):
    index = len(str)
    for i in range(len(str),0,-1):
        index = index - 1
        if i == ch:
            break
    return index

def main():
    str = input('Enter string: ')
    ch = input('Enter character: ')

    ret = IndexLastOcc(str,ch)
    print('Last occurance index of {} is {}'.format(str,ret))
if __name__ == '__main__':
    main()