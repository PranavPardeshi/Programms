'''5. Write a program which accept string from user reverse that string
in place.
Input : “abcd”
Output : “dcba”
Input : “abba”
Output : “abba”'''


def ReverseString(str):
    if(str == None):
        return      
    else:
        rev = ''
        for i in str:
            rev = i + rev
        return rev

def main():
    str = input('Enter string: ')
    ret = ReverseString(str)
    print('Reverse string is {}'.format(ret))
if __name__ == '__main__':
    main()