'''
Recursive function requires:
    * Base case
    * move toward the base case
'''

def slow_fibonnacci(n):
    if n<=1:
        return n
    return slow_fibonnacci(n-1) + slow_fibonnacci(n-2)


cache = {}



print(slow_fibonnacci(8))
print(slow_fibonnacci(9))
print(slow_fibonnacci(15))
print(slow_fibonnacci(25))