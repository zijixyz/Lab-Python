x = (1, 2, 3)
print(x)  # Output: (1, 2, 3)
print(type(x))  # Output: <class 'tuple'>
x = list(x)
print(x)  # Output: [1, 2, 3]
print(type(x))  # Output: <class 'list'>
x[0] = 10
print(x)  # Output: [10, 2, 3]
print(type(x))  # Output: <class 'list'>
x = tuple(x)
print(x)  # Output: (10, 2, 3)
print(type(x))  # Output: <class 'tuple'>
