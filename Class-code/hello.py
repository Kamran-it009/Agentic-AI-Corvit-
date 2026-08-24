# synchronous Programing is a programming paradigm that executes tasks sequentially, one after the other. In synchronous programming, each task must complete before the next one begins. This can lead to blocking behavior, where the program waits for a task to finish before moving on to the next one.
import time

def boil_water():
    print("Boiling water...")
    time.sleep(3)
    print("Water is ready!")

def toast_bread():
    print("Toasting bread...")
    time.sleep(2)
    print("Bread is toasted!")

def make_breakfast():
    boil_water()
    toast_bread()
    print("Breakfast is ready!")

start_time = time.time()
make_breakfast()
end_time = time.time()

print(f"Total time taken: {end_time - start_time:.2f} seconds")