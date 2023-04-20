from typing import Any, Callable, Iterable, List, Mapping, Tuple

import threading
import math

class ChunkedFunction:
    def __init__(self, func:Callable, idx:int, chunksz:int, minidx:int, maxidx:int, daemon:bool=False, args:Iterable[Any]=None, kwargs:Mapping[str,Any]=None, statuslist:Iterable[bool]=None):
        self.func = func
        self.idx = idx
        self.startidx = minidx+idx*chunksz
        self.endidx = min((idx+1)*chunksz, maxidx)
        self.args = args
        self.kwargs = kwargs
        self.statuslist = statuslist
        self.thread = threading.Thread(target=self.run)
        self.thread.setDaemon(daemon)
    def run(self):
        if self.args==None: self.args=[]
        if self.kwargs==None: self.kwargs={}
        self.func(*self.args, **self.kwargs, startidx=self.startidx, endidx=self.endidx)
        self.statuslist[self.idx] = True
    def start(self):
        self.thread.start()

def run_chunked(func:Callable, chunksz:int, minidx:int, maxidx:int, daemon:bool=False, args:Iterable[Any]=None, kwargs:Mapping[str,Any]=None) -> List[bool]:
    """
    Params:
     - func    : Function or callable, must take keyword arguments `startidx` and `endidx`
     - chunksz : Integer, size of each chunk
     - minidx  : Integer, minimum index ie starting index of first chunk
     - maxidx  : Integer, maximum index ie ending index of last chunk
     - daemon  : Bool, whether the chunks should be run as a daemon thread (killed upon program completion)
     - args    : Iterable (like list), passed directly to the function
     - kwargs  : Mapping (like dict), passed directly to the function
    Returns: List of Bool values.
        This list holds the completion status of all chunks.
        Initially, all values are False.
        When a chunk finishes its function, it's corresponding status is set to True.
        `while not all(LIST): pass` can be used to wait for all chunks to finish
    """
    assert type(chunksz)==int
    assert type(minidx)==int
    assert type(maxidx)==int
    n = minidx+math.ceil((maxidx-minidx)/chunksz)
    statuslist = [False]*n
    for i in range(n):
        ChunkedFunction(func, i, chunksz, minidx, maxidx, args, kwargs, daemon, statuslist).start()
    return statuslist

def run(func:Callable, *args, **kwargs) -> List[bool]:
    return run_chunked(func, *args, **kwargs)

run.__doc__ = run_chunked.__doc__

if __name__ == "__main__":
    l1 = [0]*100000000
    def a(startidx=0, endidx=10):
        for i in range(startidx, endidx):
            l1[i]=i
    b = run(a, 1000, 0, len(l1))
    while not all(b): pass
    print("Done")
