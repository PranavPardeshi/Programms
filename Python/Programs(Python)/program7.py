class Pattern:
    def __init__(self):
        self.r = int(input('Row: '))
        self.c = int(input('Col: '))
    
    def Display(self):
        for i in range(1,(self.r+1)):
            for j in range(1,(self.c+1)):
                if i == j :
                    print('$',end=' ')
                else:
                    print('*',end=' ')
            print()
def main():
    obj = Pattern()
    obj.Display()
if __name__ == '__main__':
    main()