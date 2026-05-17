def sqrt(x):
    if not isinstance(x,(int, float)):
        raise TypeError('Enter a numeric')
    if x < 0:
        raise ValueError('Number cannot be negative')
    return x**(1/2)

print(sqrt(25))