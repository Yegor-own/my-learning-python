from math import factorial as f


# factorial function from my own
def factorial(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


curt = lambda x: x ** 3


# exponentiate all elements of a list
lst = [1, 2, 3, 4, 5]
lst2 = list(map(curt, lst))
print(lst2)
print(curt(100))
print(f(5))
print(factorial(6) - factorial(5))
