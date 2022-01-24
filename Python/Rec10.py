
def fun():
    # static int i = 0      in C / C++
    i = 0               # Local variable (Auto storage class)
    if (i < 5):
        print(i)
        i = i + 1       # i++
        fun()       # Recursive call

def main():
    fun()

if __name__ == "__main__":
    main()