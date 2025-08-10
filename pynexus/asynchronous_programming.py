import asyncio
import time

async def make_salad():
    print("Starting to make the salad...")
    print("Salad is ready!")


async def boil_water():
    print("Putting water on the stove...")

    await asyncio.sleep(3)

    print("Water is boiling!")


async def chop_vegetables():
    print("Starting to chop vegetables...")

    time.sleep(1)

    print("Vegetables are chopped!")


async def main():
    await asyncio.gather(
        boil_water(),
        chop_vegetables()
    )

asyncio.run(main())