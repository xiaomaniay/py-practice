from threading import Thread, Lock

lock = Lock()
some_var = 0


class IncrementThread(Thread):
    def run(self):
        global some_var
        lock.acquire()
        read_value = some_var
        print("some_var in %s is %d" %(self.name, read_value))
        some_var = read_value + 1
        print("some_var in %s after increment is %d" %(self.name, some_var))
        lock.release()


def use_increment_thread():
    threads = []
    for i in range(1000):
        t = IncrementThread()
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("After 1000 modifications, some_var should have become 1000")
    print("After 1000 modifications, some_var is %d" % some_var)


use_increment_thread()
