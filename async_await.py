
""" Synchronous programming means that everything that is written
is happening sequential """

# here the 'print' statement is not gonna be run until the 'foo' is executed
def foo1():
	return

foo1()
print('Tim')

""" in Asynchronous programming we don't need to awat for something to be
completely done before we run other parts of code """

# it creates a wrapper around this function, it returns a coroutine object
# (it's function that can be executed through 'await')
import asyncio
async def main1():
	print('Tim')
	# when creating the task, the 'main' function is still running
	task = asyncio.create_task(foo2('text'))
	await task # it means 'wait until this task is done, only then go on'
	print('finished')

async def foo2(text):
	print(text)
	await asyncio.sleep(3)

asyncio.run(main1())