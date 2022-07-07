# string
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
        
