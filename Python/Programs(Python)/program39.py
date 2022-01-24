"""4. Accept Character from user and check whether it is special symbol
or not (!, @, #, $, %, ^, &, *).
Input : %
Output : TRUE
Input : d
Output : FALSE"""

def CheckSpecialChar(ch):

    if((ch == '!') | (ch == '@') |(ch == '#')|(ch == '$') | (ch == '%') | (ch == '^') | (ch == '&') | (ch == '*')):
        return  True
    else:
        return  False
def main():
    ch = input('Enter character: ')
    ret = CheckSpecialChar(ch)
    if ret == True:
        print('{} special character'.format(ch))
    else:
        print('{} is not special character'.format(ch))
if __name__ == "__main__":
    main()




