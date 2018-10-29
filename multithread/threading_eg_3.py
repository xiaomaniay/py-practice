import time
import requests
from threading import Thread


class GetUrlThread(Thread):
    def __init__(self, url):
        self.url = url
        super(GetUrlThread, self).__init__()

    def run(self):
        resp = requests.get(self.url)
        print(self.url, resp.status_code)


def get_response():
    urls = [
        'http://www.google.com',
        'http://www.amazon.com',
        'http://www.ebay.com',
        'http://www.alibaba.com',
        'http://www.reddit.com'
    ]

    start = time.time()
    threads = []
    for url in urls:
        t = GetUrlThread(url)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("Elapsed time: %s s" % (time.time() - start))


get_response()
