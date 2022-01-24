'''1. Write a program which accept string from user and copy that
characters of that string into another string in reverse order.
Input : “Marvellous Python”
Output : “nohtyP suollevraM””'''

def StrCpyRev(str):
    for i in str:
        str = i+str
    print(str)
def main():
    str = input('Enter string: ')
    StrCpyRev(str)

if __name__ == '__main__':
    main()