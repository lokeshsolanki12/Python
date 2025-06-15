## This is the basic syntax of the Function 

'''
def Function_name(parameters):
    #Docstring
    
    #function Body
    
    return expression '''
    

### Create a Function 
def even_or_odd(num):
    '''This function finds even or odd '''
    
    if num % 2 == 0:
        print("The number is even")
    else:
        print("the Number is odd")

even_or_odd(31)


### Function with multiple parameters

def add(a,b):
    return a+b

result = add(2,4)
print(result)

### Default perameter

def greet(name):
    print(f"hello {name} Wellcome the Python world")
    
greet("Lokesh")

def defalut(name = "User"):
    print(f"Hello {name} in the Site")
    
defalut()

