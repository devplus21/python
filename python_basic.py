# Variables in Python
x = 5
y = "John"
print(x)
print(type(y))


# String in Python
str = 'hello WORLD'

test_upper = str.upper() # HELLO WORLD
test_lower = str.lower() # hello world
test_replace = str.replace('world', 'python') # hello python
test_split = str.split(' ') # ['hello', 'python']
test_join = ' '.join() # hello python


# Ternary Operator in Python
x = int(input('Enter a number: '))

check = 'Chan' if (x % 2 == 0) else 'Le'

print(check)


# if else in Python
for i in range(1, 100):
    if (i % 3 == 0) and (i % 5 == 0):
        print('Bui Van Tan')
    elif i % 3 == 0:
        print('Bui')
    elif i % 5 == 0:
        print('Tan')
   
    else:
        print('default')    
      
        
# function in Python
def my_function(fname):
  print(fname + " Dev")

my_function("Tan")
my_function("Chi")
my_function("Hai")



# For Loops in Python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
# sort
n = int(input("Enter n number: "))
a = []
for i in range(n):
   a.append(int(input()))
a.sort()
for i in a:
  print(i, end=' ')
  
# Generator
def square_nums(list_nums):
    for x in list_nums:
       yield x*x

list_nums = [1, 2, 3 ,4]


# Try Except in Python
try:
    a = int(input('Enter a number: '))
    b = int(input('Enter b number: '))
    print(a + b)
except:
    print('Invalid input')    


