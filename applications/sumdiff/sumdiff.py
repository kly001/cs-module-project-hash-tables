"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here


def sum_diff(q):
    for a in q:
        for b in q:
            for c in q:
                for d in q:
                    if f(a) + f(b) == f(c) - f(d):

                         print(f'The sum of {f(a)} + {f(b)} ({f(a) + f(b)}) is equal to the difference of {f(c)}-{f(d)} ({f(c)-f(d)})')


print(sum_diff(q))