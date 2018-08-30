import multiprocessing


def worker(name, que):
    que.put("%d is done" % name)

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=3)
    m = multiprocessing.Manager()
    q = m.Queue()
    print q.empty()
    print dir(q)
    workers = pool.apply_async(worker, (33, q))
    workers.wait()
    print q.empty()
    print q.qsize()
    print q.get()
    print q.qsize()
