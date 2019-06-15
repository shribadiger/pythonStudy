
# This is Program to Illustrate more about the Lists in Python

def listOperation():
    myList =[1,2,3,4,5,6,7,8,9]

    myList.append(10);
    print(myList)

    oneMoreList=[11,12,13]
    myList.extend(oneMoreList)
    print(myList)

    myList.insert(1,200)
    print(myList)

    myList.remove(9)
    print(myList)

    popValue=myList.pop()
    print(f"Pop value: {popValue}")

    index=myList.index(200)
    print(f"index : {index} of value 200")

    rep=myList.count(200)
    print(f"Number of times 200 repeated : {rep}")

    #sort the list and print
    myList.sort()
    print(myList)

    myList.reverse()
    print(myList)

listOperation()


from collections import deque
queue = deque(["Shrikant","Shruti","sorry"])
queue.append("Gowthami")
print(f"{queue}")
print(queue.popleft())
print(queue.pop())

# using some build in functions
def foo(x):
    return x%3 ==0 or x%5 == 0

filter(foo, range(2,300))

#list of comprehension 
squares = [] # define an empty list
for x in range(100):
    squares.append(x*x)

print(squares)
squares = [x**2 for x in range(10)]
print(squares)

values = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(values)

#list inside a list
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
print(matrix)

#checking how for loop works
for i in range(4):
    print("--" * 10)
    for row in matrix:
        print(f"ROW : {row[i]}")
print("--" * 10)

traspose = [[row[i] for row in matrix] for i in range(4)]
print(traspose)

traspose_manual = []
for i in range(4):
    traspose_manual.append([row[i] for row in matrix])
    print(traspose_manual)

print(traspose_manual)
