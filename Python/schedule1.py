import time
import datetime
import schedule

def task():
    print("Task after each minute gets executated")
    print("Current time is : ", datetime.datetime.now())


def main():
    print("Inside main function")
    print("Schedular starts....")

    schedule.every(1).minutes.do(task)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()