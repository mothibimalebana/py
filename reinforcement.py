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