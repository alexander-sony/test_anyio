import time

import anyio

async def counter():
    now = time.time()
    print("Started counter")
    for i in range(0, 10):
        last = now
        await anyio.sleep(0.01)
        now = time.time()
        print(f"{i}: Was asleep for {now - last}s")

def blocker(id, t):
    print(f'blocker {id} to sleep for {t}s...')
    time.sleep(t)
    print(f'blocker {id} finished')

async def main():
    async with anyio.create_task_group() as tg:
        tg.start_soon(counter)
        await anyio.to_thread.run_sync(blocker, 1, 5)

anyio.run(main)
