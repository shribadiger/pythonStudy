#Program to illustrate the defining the function


def FIB(n):
    print("Entry of Fib")
    """ Print the Fib series up to n """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

FIB(10)
