#Program to Illustrate about the tuple
tup =()
print(type(tup))
tup=('shrikant',20000,'hashing',"shruti")
print(tup)
print(tup[0:])
print(tup[3:])
tup2=(20,30,20)
tup3=tup+tup2 ## It adds the two tuples and merge returns to another tuple
print(tup3)

#de assigning to different arguments
(a,b,c,d) = tup
print(a) ## each values are assigned in sequencing order
print(b)
print(c)
print(d)

#set data type is like tuple but not allows the duplicate values
basket=['apple','grapes','banana','mango','apple','grapes','gova','none']
fruits=set(basket)
print(fruits)

uniqueKeys=set('ababababababccddfeeeeeeeeeefgghh')
print(uniqueKeys)

#some of set functionality
a=set('abcd')
b=set('cde')
#letters are in a but not in b set
diff=a-b
print(diff)

#letters either in a or in b
diff=a|b
print(diff)

#Letters should be present in both a and b
diff=a&b
print(diff)

#letters in a or b but not both
diff=a^b
print(diff)



