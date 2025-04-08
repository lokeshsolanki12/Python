# names = ["lokesh", "Vikash ", "ankit", "nitesh"]
# print(names)

# mixed_list = ["lokesh", 6.6, 17, True]
# print(mixed_list)
# print(type(mixed_list))


           #Accessing list Elements
           
# fruits = ["Apple", "Banana", "cherry", "Mango", "kiwi"]
# print(fruits[0])
# print(fruits[0:])

           #Modifying the list elements

# fruits[1]= "kiwi"
# print(fruits)

# fruits.append("watemelen")
# print(fruits)

# fruits.insert(1,"orenge")
# print(fruits)

# fruits.remove("kiwi")
# print(fruits)

# popped_fruits = fruits.pop()
# print(popped_fruits)

# index = fruits.index("orenge")
# print(index)

# fruits.sort()
# print(fruits)

# fruits.reverse()
# print(fruits)

# print(fruits.clear)

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[2:5])
print(numbers[:5])
print(numbers[2:])
print(numbers[::2])
print(numbers[::-1]) # Basicaly :: meaning as print aal element of the list and the number is given the difference the skeep

# For loop use in the list

for num in numbers:
    print(num)
    
    
#iterate with index

for num,index in enumerate(numbers):
    print(num,index)                      #enumerate is predifine function in python
    
#List comprehension

lst = []
for x in range(10):
    lst.append(x**3)
print(lst)

print([x**2 for x in range(10)]) 
'''
List comprehension ke liye do chij chiye pahali hame kya banana hai. 
or dusri kitni baar banana hai '''