import asyncio
import time


async def boil_water():
    print("Boiling water... (3 seconds)")
    await asyncio.sleep(3)
    print("Water is ready!")

async def toast_bread():
    print("Toasting bread...(2 seconds)")
    await asyncio.sleep(2)
    print("Bread is toasted!")

start_time = time.time()  # Start the timer
async def make_breakfast():
    # Run both tasks at the same time
    await asyncio.gather(
        boil_water(),
        toast_bread()
    )
    print("Breakfast is ready!")

start_time = time.time()  # Start the timer
asyncio.run(make_breakfast())
end_time = time.time()  # End the timer
print(f"Total time taken: {end_time - start_time:.2f} seconds")