# x = (1, 2, 3)
# print(x)  # Output: (1, 2, 3)
# print(type(x))  # Output: <class 'tuple'>
# x = list(x)
# print(x)  # Output: [1, 2, 3]
# print(type(x))  # Output: <class 'list'>
# x[0] = 10
# print(x)  # Output: [10, 2, 3]
# print(type(x))  # Output: <class 'list'>
# x = tuple(x)
# print(x)  # Output: (10, 2, 3)
# print(type(x))  # Output: <class 'tuple'>

# =====================================================

# thistuple = (1, 2, 3, 4, 5)
# print(thistuple)  # Output: (1, 2, 3, 4, 5)
# newtuple = (6, 7, 8, 9, 10)
# print(newtuple)  # Output: (6, 7, 8, 9, 10)
# thistuple += newtuple
# print(thistuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) 

# ================================================================

# thistuple = (1, 2, 3, 4, 5)
# del thistuple

# if thistuple:
#     print(thistuple)
# else:
#     print("The tuple has been deleted.")  # Output: The tuple has been deleted.

# ====================================================================================

tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
(apple, *banana, cherry) = tuple
print(apple)  # Output: The first fruit is: apple
print(banana)  # Output: The second fruit is: banana
print(cherry)  # Output: The third fruit is: cherry
