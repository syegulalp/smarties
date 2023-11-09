import smarties
from pathlib import Path
from time import perf_counter

def _test():
    test_file = Path(__file__).parent / "test.html"
    data = open(test_file,encoding="utf8").read()
    start = perf_counter()
    result = smarties.smartquote(data)
    print (perf_counter()-start)
    print (result)

def _test2():
    test_file = Path(__file__).parent / "frankenstein.html"
    data = open(test_file,encoding="utf8").read()    
    start = perf_counter()
    result = smarties.smartquote(data)
    print (len(data), "characters in", perf_counter()-start, "sec")

_test()
_test2()