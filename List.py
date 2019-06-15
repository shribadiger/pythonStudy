#Function to indicate about the list functionality in Python
names = ['shriaknt','shruti','Gowthami']
print(names[-1])
print(names[-2])
print(names[-3])
#print(names[-4]) # Error: Out of index

print(names[0:3])

#function with default argument
def user_manual(prompt, retries=4, entry="Yes or No Please"):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes','Y','YE','YES'):
            return True
        if ok in ('n','no','N','NO'):
            return False
        retries=retries -1
        if retries < 0:
            raise IOError('Refuseniks User')
        print(entry)

user_manual("Do you really want to quit!")


#Function to append the List and Pass via function
def append_list(value, myList=[]):
    myList.append(value)
    return myList

print(append_list(1)) # each value which passing in the function will be appending to List
print(append_list(2))
print(append_list(3))
print(append_list(4))

#in case if I don't want to append the list each time following function will help

def not_append_list(value, myList=None):
    if myList is None:
        myList=[]
    myList.append(value)
    return myList

print(not_append_list(1))
print(not_append_list(2))
print(not_append_list(3))


#Function can be called with Keyword arguments
def print_sender_info(name="First_Name", age=30, dob="08-08-1988"):
    print(f"User Information Name {name}")
    print(f" Age : {age}")
    print(f"Date of Birth : {dob}")

print_sender_info(name="Shrikant")
print_sender_info(age=34,name="Bhavani") # you can send any order 

def checkOrder(kind, *arguments, **keyword):
    print(f"-Order Type : {kind}");
    for arg in arguments:
        print(arg)
    print("__" * 30)
    keys=sorted(keyword.keys())
    for kw in keys:
        print(f"{kw} :- {keyword[kw]}")
    

checkOrder("Bread",
            "Price","Total",
            price=400,
            total=500)


# Now function to check only argument list
def printArgumentList(*arguments):
    for arg in arguments:
        print(f" {arg} ")

printArgumentList("Shrikant","Shruti","Sorry")
