'''2.Write a program which accept string from user and accept one character. Return frequency of that character.
Input : “Marvellous Multi OS”
M
Output : 2
Input : “Marvellous Multi OS”
W
Output : 0'''

def FrequencyChar(str,char):
    iCnt = 0
    for i in str:
        if i == char:
            iCnt += 1
    return iCnt

def main():
    str = input('Enter string: ')
    char = input('Enter character: ')

    ret = FrequencyChar(str,char)

    print('Frequency of {} is {}.'.format(char,ret))
if __name__ == '__main__':
    main()