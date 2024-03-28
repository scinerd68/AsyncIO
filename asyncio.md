# Asyncio basics

In <code>asyncio</code>, Python will not pause a coroutine and allow something else to execute just because it is sleeping. The only time a coroutine might pause and let something else run is when it was awaited (```await```) (cooperative multitask), so ```time.sleep``` has to be replaced by ```await asyncio.sleep()```.

```await```: wait here until something is done

```asyncio.create_task()```: wrap coroutine in task object and schedule it in the event loops, it does not ```await`````` task immediately, allow schedule multiple tasks before waiting on them

```asyncio.wait()```: wait on specified tasks

```asyncio.gather()```: accumulate task results in a list
