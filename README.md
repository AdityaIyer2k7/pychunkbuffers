# pychunkbuffers
An open-source python library for writing large amounts of data to buffers via chunks.

## Description
This repositiory contains the source code for the `pychunkbuffers` library. I came up with the idea for this library while making my other project [AdityaIyer2k7/image-file-hider](https://github.com/AdityaIyer2k7/image-file-hider). In that project, I often had to write large amounts of data (hundreds of megabytes) to lists and buffers. Doing this byte-by-byte took a lot of time, so instead I came up with the solution of chunking.

Basically, let us say we have a `for` loop that has to run 10^8 times, and each time it adds a value to a list. In a chunked implementation, you would pre-define this list like this:
```py
[0]*10**8
```
and then create a function that goes from index a to b and updates that value of the list like this:
```py
def func(startidx, endidx):
  for i in range(startidx, endidx):
    LIST[i] = SOMEVALUE
```
However, if we run `func(0, 10**8)`, we are still running 10^8 iterations in sequence. Instead, we can run parts like `func(0, 10000)`, `func(10000, 20000)` and so on simultaneously on threads. With this library, we can simply use the line
```py
run_chunked(func, 10000, 0, 10**8) # Where 10000 is our chunk size, while 0 and 10**8 are our bounds
```
Now, we would like to check when all chunks have completed their tasks. The library implements this using a completion status list. The `run_chunked` function returns a list of boolean values which are all `False` when the chunks start. Whenever a chunk finishes its task, that specific chunk's status is set to `True` in the list. If we want to wait for all the chunks to finish, we can use a line like this:
```py
while not all(STATUS): pass
```
Example implementation:
```py
# Task: To write the squares values for numbers 1 to 10**8 (inclusive)
squares = [0]*10**8
CHUNKSIZE = 10**5
def func(startidx, endidx):
  for i in range(startidx, endidx):
    squares[i] = (i+1)**2
status = run_chunked(func, CHUNKSIZE, 0, len(squares))
while not all(status): pass
print("Done")
print(squares[:100])
```
