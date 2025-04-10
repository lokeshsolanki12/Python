## Create a Tuple

emty_tuple = ()
print(emty_tuple)
print(type(emty_tuple))

### List to tuple and tuple to list

number = tuple([1,2,3,4,5])
print(number)

numbers = list((1,2,3,4,5))
print(numbers)

mixed_tuples = (17,6.2,"Lokesh", True)
print(mixed_tuples)

number = (1,2,3,4,5,6)
print(number)

print(number[1])
print(number[:4])

###Tuple opration

concarination_tuples = number + mixed_tuples
print(concarination_tuples)
print(concarination_tuples)

print(mixed_tuples * 3)

### Immutable Tuples
# Tuples are immutable , meaning their elements connec be change once assigned

lst = [1,2,3,4,5]
print(lst)

lst[1] = "lokesh"
print(lst)

# number[2] = "lokesh"
# print(number)         
'''
this syntax are give a error in the output'''

### Tuples method

number = (1,2,34,5,6,5)
print(number.count(2))
print(number.index(5))


###packing and unpacking tuples

pack_tuple = 17 , "Lokesh", 6.3, True
print(pack_tuple)

a,b,c,d = pack_tuple
print(a)
print(b)
print(c)
print(d)

### unpacking with *

number = (1,2,3,4,5,6)
first,*middel,last = number
print(first)
print(middel)
print(last)

###Nested Tuple

lst = [[1,2,3,4],[6,7,8,9],[17,"lokesh",6.3,True]]
print(lst[0][:3])



nested_tuples = ((1,2,3,4),('a','b','c','d'),(True,False))
print(nested_tuples[2])

### Intreating over nested tuples

for sub_tuple in nested_tuples:
    for item in sub_tuple:
        print(item,end=" ")
    print()
    
