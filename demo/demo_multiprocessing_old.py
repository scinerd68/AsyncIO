import multiprocessing
import time


def do_something(seconds):
    print(f'Sleeping {seconds} second')
    time.sleep(seconds)
    print('Done sleeping')


if __name__ == '__main__':
    start = time.perf_counter()

    processes = []
    for _ in range(10):
        # Arguments must be serieziable by pickle to run multiprocessing
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
    
    end = time.perf_counter()

    print(f"Finished in {round(end - start, 2)} seconds")