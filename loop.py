# for i in range(99):
#     print(i)
    
# for j in range(34,44):
#     print(j)

# for j in range(1,10,2):
#     print(j)

# for j in range(10,0,-1):
#     print(j)


        #String
        
# str = "Lokesh solanki"

# for i in str:
#     print(i)
    
  #Output
  
# L
# o
# k
# e
# s
# h

# s
# o
# l
# a
# n
# k
# i

            #while loop
            
            
# count = 0

# while count<5:
#   print(count)
#   count = count+1
  
  
                  # Loop controle statement
                  
                  
#break :- The break stement exit the parmanenlty the loop


# for i in range(10):
#   if i == 5:
#     break
#   print(i)

# for i in range(20):
#   if i%2==0:
#     continue
#   print(i)

# for i in range(5):
#   if i==3:
#     print("the number is", i)
#     pass
#   print(i)


      #Nested loop :- Loop in the loop
      
# for i in range(3):
#   for j in range(2):
#     print(f"i:{i} and j:{j}")
    
    #Output
#     i:0 and j:0
# i:0 and j:1
# i:1 and j:0
# i:1 and j:1
# i:2 and j:0
# i:2 and j:1

   #Q1 Calculate the first 10 natural number
   
# n = int(input("enter the natural number"))
# sum = 0
# count = 1

# while count<=n:
#   sum = sum+count
#   count = count+1
  
# print("Sum of first 10 natural number is",sum)

# n = int(input("Enter the natural number"))
# sum = 0
# for i in range(n+1):
#   sum = sum+i
  
# print(sum)
    
    
    
# Q1. Explain the prime number b/w 1 to 100

for i in range(1,101):
  if i>1:
    for num in  range(2,i):
      if i%num==0:
        break
    else:
      print(i)