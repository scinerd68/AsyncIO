import asyncio
import time


async def main():
    print('tim')
    # Task will be run as soon as possible
    task = asyncio.create_task(foo('text'))
    # Uncomment next line to ensure foo is done before print(finished)
    # await task

    # await return the control back to the processor when idle so that in can excute a different couroutine
    # so asyncio.sleep(2) will allow 'text' to be printed 'finished'
    # whereas time.sleep(2) do not return the control back so 'finished' is printed before 'text'
    await asyncio.sleep(2)
    # time.sleep(2)
    # main() must wait when encouter 'await' before continue executing
    print('finished')

async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())