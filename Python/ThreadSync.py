import threading

amount = 0

def Counter(fun,lock):
    fun(lock)

def Credit(lock):
    value = int(input('Enter amount to Credit: '))
    lock.acquire()
    global amount
    amount = amount + value
    print('Balance is: ',amount)
    lock.release()

def Debit(lock):
    value = int(input('Enter amount to withdraw: '))
    lock.acquire()
    global amount
    if value > amount:
        print('Unable to withdraw!')
    else:
        amount = amount - value
        print('Amount withdraw ',value)
        print('Balance is: ',amount)
    lock.release()

def main():
    lock = threading.Lock()

    t1 = threading.Thread(target=Counter,args=(Credit,lock))
    t2 = threading.Thread(target=Counter,args=(Debit,lock))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
if __name__ == '__main__':
    main()