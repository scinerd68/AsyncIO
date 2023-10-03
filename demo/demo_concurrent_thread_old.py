import time
import threading


start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    print('Done sleeping')


thread_list = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1])
    t.start()
    thread_list.append(t)

# Make sure all threads complete before calculate exec time
for thread in thread_list:
    thread.join()

end = time.perf_counter()

print(f"Finished in {round(end - start, 2)} seconds")