import asyncio

async def one():
    print("start one")
    await asyncio.sleep(3)
    print("end one")

async def two():
    print("two start")
    await asyncio.sleep(2)
    print("end two")
async def thee():
    print("three start")
    await asyncio.sleep(1)
    print("end three")

async def main():
    await asyncio.gather(one(), two(), thee())

if __name__ == "__main__":
    asyncio.run(main())