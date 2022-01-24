def DisplayR(no):
    print(no)
    no = no + 1
    DisplayR(no)      # Recursive call

def main():
    DisplayR(0)

if __name__ == "__main__":
    main()