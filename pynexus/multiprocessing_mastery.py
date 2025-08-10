import multiprocessing

def worker(q, name):
    """A worker function that processes items from the queue."""
    print(f"{name} is starting!")
    item = q.get()
    print(f"{name} processed: {item}")

if __name__ == "__main__":
    queue = multiprocessing.Queue()

    process1 = multiprocessing.Process(target=worker, args=(queue, "Worker 1"))
    process2 = multiprocessing.Process(target=worker, args=(queue, "Worker 2"))

    process1.start()
    process2.start()

    print("Main process putting items on the queue...")
    queue.put("Hello from Main")
    queue.put("Another message")

    process1.join()
    process2.join()

    print("All workers finished.")