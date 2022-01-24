"""5. Accept division of student from user and depends on the division
display exam timing. There are 4 divisions in school as A,B,C,D. Exam
of division A at 7 AM, B at 8.30 AM, C at 9.20 AM and D at 10.30 AM.
(Application should be case insensitive)
Input : C
Output : Your exam at 9.20 AM
Input : d
Output : Your exam at 10.30 AM"""

class School:
    def __init__(self):
        self.div = input('Enter Division: ')

    def DisplayTime(self):
        if ((self.div >= 'A') & (self.div <= 'D')) | ((self.div >= 'a') & (self.div <= 'd')) :
            if ((self.div == 'A') | (self.div == 'a')):
                print('Exam at 7 am!')
            elif ((self.div == 'B') | (self.div == 'b')):
                print('Exam at 8.30 am!')
            elif ((self.div == 'C') | (self.div ==  'c')):
                print('Exam at 9.20 am!')
            else:
                print('Exam at 10.30 am!')
        else:
            print('Please,enter valid division!!!')

def main():
    obj = School()
    obj.DisplayTime()

if __name__ == '__main__':
    main()