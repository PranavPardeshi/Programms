def fun(i = 0):
    if (i < 5):
        print(i)
        i = i + 1       # i++
        fun(i)       # Recursive call

def main():
    fun()

if __name__ == "__main__":
    main()