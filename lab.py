a = ["apple", "banana"]
b = a

print(a)  # ['apple', 'banana']
print(b)  # ['apple', 'banana']
print("=============")

a.extend(["cherry"])  # b ikut berubah

print(a)  # ['apple', 'banana', 'cherry']
print(b)  # ['apple', 'banana', 'cherry']
print("=============")

a = a + ["durian"]    # a jadi list baru, b tetap lama

print(a)  # ['apple', 'banana', 'cherry', 'durian']
print(b)  # ['apple', 'banana', 'cherry'] (tidak berubah)
