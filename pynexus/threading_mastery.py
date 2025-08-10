import threading

shared_counter = 0

lock = threading.Lock()

def increment_counter():
    global shared_counter
    for _ in range(1000000):
        with lock:
            shared_counter += 1

thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Final counter value: {shared_counter}")