import time
import threading


def fun(n):
    while n > 0:
        n -= 1


start_time = time.time()

t1 = threading.Thread(target=fun, args=(10000000,))
t1.start()
t2 = threading.Thread(target=fun, args=(10000000,))
t2.start()

t1.join()
t2.join()
print('{} s'.format(time.time() - start_time))