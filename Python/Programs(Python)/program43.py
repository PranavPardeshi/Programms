'''3. Write a program which accept string from user and display it inn
reverse order.
Input : “MarvellouS”
Output : “SuollevraM”'''


def ReverseStr(str):
  str1 = ""
  for i in str:
    str1 = i + str1
  print(str1)

  #rev = str[::-1]
  #print(rev)

def main():
    str = input('Enter string: ')
    ret = ReverseStr(str)

if __name__ == '__main__':
    main()