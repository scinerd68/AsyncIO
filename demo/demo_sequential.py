import time


start = time.perf_counter()


def do_something():
    print('Sleeping 1 second')
    time.sleep(1)
    print('Done sleeping')


do_something()
do_something()

end = time.perf_counter()

print(f"Finished in {round(end - start, 2)} seconds")