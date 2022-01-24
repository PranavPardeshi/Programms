'''3.Write a program which accept string from user and accept one
character. Return index of first occurrence of that character.
Input : “Marvellous Multi OS”
M
Output : 0
Input : “Marvellous Multi OS”
W
Output : -1
Input : “Marvellous Multi OS”
e
Output : 4'''

def IndexFirstOcc(str,ch):
    index = 0
    for i in str:
        index += 1
        if i == ch:
            break
    return  index

def main():
    str = input('Enter string: ')
    ch = input('Enter character: ')

    ret = IndexFirstOcc(str,ch)
    print('First occurence index of {} is {}'.format(ch,ret))

if __name__ == '__main__':
    main()


