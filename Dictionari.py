# empty_dict = {}
# print(type(empty_dict))

# empty_dict = dict()
# print(empty_dict)

# student = {"name":"lokesh","age":18,"grade":"A"}
# print(student)

# student1 = {"name":"lokesh","age":18,"name":"Akashay"}
# print(student1)  ## No repted the same key in the Dictionary

### AccessingnDictionary Elements
# student = {"name":"lokesh","age":18,"grade":"A"}
# print(student['grade'])
# print(student['name'])

### Accessing using get() method

# print(student.get('name'))
# print(student.get('age'))

### Modify Dictonary Elements
'''
:- Dictionary are mutable, So you can add, update or delete element
'''

# student["addersh"] = "India" ## Add the new key value
# print(student)
# student["age"] = 19   ## Modify the value
# print(student)

### Delete key

# del student["grade"]
# print(student)

### Comman Dictories Methods

# keys = student.keys() ## get all keys
# print(keys)

# values = student.values()  ## get all values
# print(values)

# items = student.items()  ## get all key and values
# print(items)   

### Shallow copy
'''
When we are normaly copy the any dictionary then this is all time the copy the same values.
after the modify this is the proble for solving the problem we are use the shallow copy'''

# student_copy = student
# print(student)
# print(student_copy)

# student["name"] = "Lokesh Solanki"
# print(student)                     ##{'name': 'Lokesh Solanki', 'age': 19, 'addersh': 'India'}
# print(student_copy)                ##{'name': 'Lokesh Solanki', 'age': 19, 'addersh': 'India'}

## solving the problem we are use the shallow copy

# student_copy1 = student.copy()
# print(student_copy1)
# print(student)

# student["name"] = "Lokesh bharat"
# print(student_copy1)      ##{'name': 'Lokesh Solanki', 'age': 19, 'addersh': 'India'}
# print(student)          ##{'name': 'Lokesh bharat', 'age': 19, 'addersh': 'India'}

### interating over Dictionaries 
'''
You can use the loops to itetaye over dictionaries ,key,value,or items'''

student = {"name":"lokesh","age":18,"grade":"A"}

for keys in student.keys():
    print(keys)

for values in student.values():
    print(values)

for key,value in student.items():
    print(f"{key}:{value}")
    
    
### Nested Dictionaries
''' Dictionaries into the another dictinories'''

students = {
    "student1" : {"name":"Lokesh","age":18},
    "student2" : {"name":"Gaytri","age":17}
}
print(students)

### Access the Nested Dictneries  elements
print(students["student2"]["name"])
print(students["student2"]["age"])

### Iterating over nested Dictionaries

for student_id,student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items():
        print(f"{key}:{value}")
        


### Dictionary compherehension

squere = {x:x**2 for x in range(5)}
print(squere)

### Conditional Dictionary comprehention

even = {x:x**2 for x in range(10) if x%2==0}
print(even)


### Practical examples 

'''
Q1 use a dictionary to count the frequency of element in list'''

numbers = [1,1,2,2,2,2,3,3,3,3,3,3,3,4,4,4]
frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number]+=1
    else:
        frequency[number]=1
print(frequency)

'''
Q2 Merege 2 Dictionary into one'''

dict1 = {"a":1,"b":2}
dict2 = {"c":3,"d":4}

merge_dict = {**dict1 ,**dict2}
print(merge_dict)