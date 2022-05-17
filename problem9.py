import time
from threading import Thread

def scheduler():

    def delayed_execution(func, delay):
        time.sleep(delay)
        return func()

    def hello(name):
        print("Hello, " + name)


    job = Thread(target=delayed_execution, args=(lambda : hello('from thread'),2))
    job.start()

    print("Thread, you there?")
    time.sleep(3)
    print("Hello to you, too")


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
