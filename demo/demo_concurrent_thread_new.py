import time
import concurrent.futures


start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    return f'Done sleeping... {seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    # Return result in the order that they are started
    # Exception will be raised when its value is retrieved from results iterator
    results = executor.map(do_something, secs)

    # automatically join threads
    for result in results:
        print(result)

    # results = [executor.submit(do_something, sec) for sec in secs]

    # # Results are printed as they completed
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

end = time.perf_counter()

print(f"Finished in {round(end - start, 2)} seconds")