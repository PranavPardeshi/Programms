"""3. Accept character from user. If it is capital then display all the
characters from the input characters till Z. If input character is small
then print all the characters in reverse order till a. In other cases
return directly.
Input : Q
Output : Q R S T U V W X Y Z
Input : m
Output : m l k j i h g f e d c b a
Input : 8"""

def DisplayCharacters(ch):
    if((ch >= 'A') & (ch <= 'Z')):
        char = ch
        while(char != chr(ord('Z') + 1)):
            print(char,end=' ')
            char = chr(ord(char) + 1)
    elif((ch >= 'a') & (ch <= 'z')):
        char = ch
        while(char != chr(ord('a') - 1)):
            print(char, end=' ')
            char = chr(ord(char) - 1)
    else:
        print(ch)

def main():
    ch = input('Enter Character: ')
    DisplayCharacters(ch)
if __name__ == '__main__':
    main()