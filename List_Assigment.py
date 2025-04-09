#Assignment1
lst = []
for i in range(1,21):
    lst.append(i)
print(lst)


#Assignment2
print(lst[0],lst[9],lst[19])

#Assignment3
print(lst[0:5],lst[14:20])

lst = []
for i in range(5,16):
    lst.append(i)
print(lst)

#Assignment4

Squer_numbers = [num**2 for num in range(10)]
print(Squer_numbers)

#Assignment5

lst = [num for num in range(21) if num%2==0]
print(lst)

#Assignment6

Rendom_list = [3,23,5,3,6,7,234,45,6,7,4,2,4,6,3,]
newList=Rendom_list.sort
print(newList)

#Assignment7

matrix = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]

for row in matrix:
    print(row)
for row in matrix:
    print(row[1],row[2])
