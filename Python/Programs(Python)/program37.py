"""2. Accept character from user. If character is small display its
corresponding capital character, and if it small then display its
corresponding capital. In other cases display as it is.
Input : Q
Output : q
Input : m
Output : M
Input : 4
Output : 4
Input : %
Output : %
void"""

def DisplayReverse(ch):
    char = ''
    if ((ch >= 'A') & (ch <= 'Z')):
        char = chr(ord(ch) + 32)
        print(char)
    elif((ch >= 'a') & (ch <= 'z')):
        char = chr(ord(ch)-32)
        print(char)
    else:
        print(ch)
def main():
    ch = input('Enter character: ')
    DisplayReverse(ch)

if __name__ == '__main__':
    main()