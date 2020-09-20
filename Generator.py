# A Generator object is an iterator, whose values are created at the time of accessing them.

# A generator can be obtained either from a generator expression or a generator function.

x = [6, 3, 1]
g = (i**2 for i in x)  # generator expression
print(next(g))         # -> 36
