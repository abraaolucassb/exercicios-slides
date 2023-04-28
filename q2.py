'''
Explique a função map()
'''


# map(function, iterable, *iterables)

'''
    Return an iterator that applies function to every item of iterable, yielding the results. 
    If additional iterables arguments are passed, function must take that many arguments and is 
    applied to the items from all iterables in parallel. With multiple iterables, the iterator 
    stops when the shortest iterable is exhausted. For cases where the function inputs are already 
    arranged into argument tuples, see itertools.starmap().

'''


# itertools.starmap(function, iterable)

'''
    Make an iterator that computes the function using arguments obtained from the iterable. 
    Used instead of map() when argument parameters are already grouped in tuples from a single 
    iterable (when the data has been “pre-zipped”).

    The difference between map() and starmap() parallels the distinction between function(a,b) 
    and function(*c). Roughly equivalent to:

    def starmap(function, iterable):
        # starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
        for args in iterable:
            yield function(*args)
'''
