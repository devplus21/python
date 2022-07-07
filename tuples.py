# access value of tuples
tuple1 = ('physics', 'chemistry', 1997, 2000)
tuple2 = (1, 2, 3, 4, 5, 6, 7 )
print("tuple1[0]: ", tuple1[0])  # physics
print("tuple2[1:5]: ", tuple2[1:5]) # [2, 3, 4, 5]


# updating Tuples
tuple1 = (12, 34, 56)
tuple2 = ('abc', 'xyz')

tuple1[0] = 100

tuple3 = tuple1 + tuple2
print(tuple3) # (100, 34, 56, 'abc', 'xyz')


# Delete Tuple Elements
tup = ('physics', 'chemistry', 1997, 2000)
print("Before deleting tup: ", tup)
del tup
print("After deleting tup : ", tup)