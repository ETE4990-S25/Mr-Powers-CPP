import asyncio

# Define an asynchronous function to print numbers
async def print_number(number):
    print(number)

# Set up the loop and run the coroutine
loop = asyncio.get_event_loop()  # Get the current event loop
loop.run_until_complete(  # Run the event loop until the coroutines finish
    asyncio.gather(*(print_number(num) for num in range(10)))
)
loop.close()  # Make sure to close the loop
