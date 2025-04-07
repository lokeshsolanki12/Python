#if Statement

# age = int(input("Enter your age : "))

# if age>=18:
#     print("You are allow to voting")
# else:
#     print("Not allow")
    
    
#elif :- It is allow for multiple conditon

# num = int(input("Enter a number : "))

# if num > 0:
#     print("Number is positive ")
#     if num%2==0:
#         print("Number is even")
#     else:
#         print("Number is odd")
# else:
#     print("not define")
    
# Determine the year is leaf year

# year = int(input("Enter days of the year"))

# if year%4==0:
#     if year%100:
#         if year%400:
#             print("the year is leaf year")
#         else:
#             print("Not a leaf year")
#     else:
#         print("year is a leap year")
# else:
#     print("year is not a leaf year")


              # Simple Calculetor 
              
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
 
print("choose the oparetion to perform by the calculator:")
op = input("+ , - , * , / ,% , //")


if op == "+":
    print("Addition is : " , num1+num2)
elif op == "-":
    print("Subtreaction is : " , num1-num2)
elif op == "*":
    print("Multiplication is : " , num1*num2)
elif op == "/":
    print("Division is : " , num1/num2)
elif op == "%":
    print("Moad is : " , num1%num2)
elif op == "//":
    print("Double division is : " , num1//num2)

else:
    print("Oprater not define please try again")
 