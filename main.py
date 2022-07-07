
# # function
# def func(x, y):
#     print(x, y)
#     return x + y

# # print(func(1, 2))

# # # write the element get the index of the element
# # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]10
# # for i in range(len(a)):
# #     print(i, a[i])

# # write the element input by user
# n = int(input("Enter the number a: "))
# print("age your: ",n)
# n1 = int(input("Enter the number b: "))
# print("age your: ",n1)
# a = n + n122
# print("sum: ",a)

# print(f"age your: {n}")



n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
if sorted(a) == a or sorted(a, reverse=True) == a:
    print("YES")
else:
    print("NO")


