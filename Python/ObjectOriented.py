# Encapsulation -> Class = Characteristics + Behaviour

# Class defination
class Arithematic:
    #___________
    def __init__(self,a,b): # Constructor
        print("Inside init (Constructor)")
        self.no1 =a     # Characteristics
        self.no2 = b    # Characteristics

    def Addition(self):     # Behaviour
        ans = self.no1 + self.no2
        return  ans

def main():
    print("Enter first number : ")
    x = int(input())

    print("Enter second number : ")
    y = int(input())

    obj = Arithematic(x,y)  # Object Creation
    ret = obj.Addition()

    print("Addition is  : ",ret)

if __name__ == "__main__":
    main()