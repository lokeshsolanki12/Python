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
# print(popped_fruits)  for given last element of list

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
or dusri kitni baar banana hai 

Basic Syntax = [expression for item in treable]'''


#Basic List Comprehension

Squere = [num**2 for num in range(10)]
print(Squere)
'''Output=[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]'''

#List Comprehension With Conditional statement

lst = []
for i in range(10):
     if i%2==0:
        lst.append(i)
print(lst)                      # This is normal syntax 

even_number = [num for num in range(10) if num%2==0]
print(even_number)

### Nasted List Coprehension

lst1 = [1,2,3,4,5]
lst2 = ['a','b','c','d','e']

pair = [(x,y)for x in lst1 for y in lst2]
print(pair)

### List Comprehension with function calls

words = ['Lokesh','Solanki','is','a','B.Tech','Student']
lenght = [len(word) for word in words]
print(lenght) 
'''
output[6, 7, 2, 1, 6, 7]'''

