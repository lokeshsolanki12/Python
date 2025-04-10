my_set = {1,2,3,4,5,6}
print(my_set)
print(type(my_set))

my_empty_set = set([6,7,8,9,10])
print(my_empty_set)


##Basic Set Opration

my_set.add(7)
print(my_set)

my_set.remove(3)
print(my_set)

my_set.discard(20)
print(my_set)


      ### Pop Methode
    
    
removed_element = my_set.pop()
print(removed_element)
print(my_set)

## Clear all the element in the set

print(my_set.clear)

### Set Membership test
my_set = {1,2,3,4,5,6,7}
print(3 in my_set)
print(10 in my_set)
'''
This Set Membership test given only the bulion expration'''

### Mathematical Opration in SETS
set1 = {1,2,3,4,5,6,7}
set2 = {4,5,6,7,8,9}

#union
union_set = set1.union(set2)
print(union_set)

#Intersection

Intersection_set = set1.intersection(set2)
print(Intersection_set)

set1.intersection_update(set2)
print(set1)

### Defference 

set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

print(set1.difference(set2))

### Symmetric Difference 
print(set1.symmetric_difference(set2))

### Set Methods

set1 = {1,2,3}
set2 = {3,4,5}

print(set1.issubset(set2))  # is subset
print(set1.issuperset(set2)) ### issuperset


lst  = [1,2,3,4,5,5,6,4,5,6]
print(set(lst))

### Counting unique words in set

text = "In This tutorial we are disscussing about sets"
words = text.split()
'''
Convert list of words to set to get unique words'''

unique_words = set(words)
print(unique_words)
print(len(unique_words))