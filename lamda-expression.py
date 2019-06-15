# This is program to illustrate the Lamda Expression

def make_increment(n):
    return lambda x:x+n

f=make_increment(40)
print(f(1)) # f will act as function and set initial value as 40 and each time value get increments
print(f(2))
print(f(3))