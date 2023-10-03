import asyncio
import time


async def do_something(seconds):
    print(f'Sleeping {seconds} second(s)')
    await asyncio.sleep(seconds)
    print('Done sleeping')

async def main():
    start = time.perf_counter()

    # tasks = [asyncio.create_task(do_something(1)) for _ in range(10)]
    # done, pending = await asyncio.wait(tasks) # pending might not be empty if there's a timeout
    # for task in done:
    #     result = task.result() # raise exception if any

    tasks = [asyncio.create_task(do_something(1)) for _ in range(10)]
    results = await asyncio.gather(*tasks) # accumulate tasks' results in a list

    # coros = [do_something(1) for _ in range(10)]
    # results = await asyncio.gather(*coros, return ex) # can also gather on coroutine instead of task, create task automatically

    # tasks are awaited automatically
    # async with asyncio.TaskGroup() as tg: # Python 3.11
    #     tasks = [tg.create_task(do_something(1)) for _ in range(10)]

    end = time.perf_counter()

    print(f"Finished in {round(end - start, 2)} seconds")

asyncio.run(main())