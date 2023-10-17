import time
import concurrent.futures


def do_something(seconds):
    print(f'Sleeping {seconds} second')
    time.sleep(seconds)
    return f'Done sleeping... {seconds}'


if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        # Return result in the order that they are started
        # Exception will be raised when its value is retrieved from results iterator
        results = executor.map(do_something, secs)

        # automatically join processes
        for result in results:
            print(result)

        # results = [executor.submit(do_something, sec) for sec in secs]

        # # Results are printed as they completed
        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())

    end = time.perf_counter()

    print(f"Finished in {round(end - start, 2)} seconds")