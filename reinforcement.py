"""
R-1.1 Write a short Python function, is_multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is,n = mi for some
integer i,andFalse otherwise.
"""
def is_multiple(n, m):
    return True if m % n == 0 else False


"""
R-1.2 Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""
def is_even(k):
    return True if k in range(0, k+1, 2) else False


"""
R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""
def minmax(data):
    u = data[0] # max variable
    l = data[0] # min variable

    for i in range(len(data)):
        print(data[i], i)
        if data[i] > u:
            u = data[i]
        elif data[i] < l:
            l = data[i]
    return (l, u)


"""
R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""
def facto_square(n):
    m = 0
    for i in range(n):
        m += i**2
    return m
        

print(facto_square(3))