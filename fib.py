'''
Recursive function requires:
    * Base case
    * move toward the base case
'''

def slow_fibonacci(n):
    if n<=1:
        return n
    return slow_fibonacci(n-1) + slow_fibonacci(n-2)


cache = {}

def fibonacci(n):
    if n<=1:
        return n

    if n not in cache:
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
    
    return cache[n]



# Use a cache
# Memoizing

# print(slow_fibonnacci(8))
# print(slow_fibonnacci(9))
# print(slow_fibonnacci(15))
# print(slow_fibonnacci(25))


print(fibonacci(8))
print(fibonacci(9))
print(fibonacci(15))
print(fibonacci(1000))