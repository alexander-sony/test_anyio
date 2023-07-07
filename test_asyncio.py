import requests
import asyncio
import time

async def counter():
    now = time.time()
    print("Started counter")
    for i in range(0, 10):
        last = now
        await asyncio.sleep(0.001)
        now = time.time()
        print(f"{i}: Was asleep for {now - last}s")

def blocker(id, t):
    print(f'blocker {id} to sleep for {t}s...')
    time.sleep(t)
    print(f'blocker {id} finished')    

async def main():
    t = asyncio.get_event_loop().create_task(counter())

    #await asyncio.get_event_loop().run_in_executor(None, send_request)
    await asyncio.get_event_loop().run_in_executor(None, blocker, 1, 2)

    await t

asyncio.get_event_loop().run_until_complete(main())