
tuple = ("apple", "banana", "cherry", "rasberry", "bluebarry")
print("first", tuple[0])
print("last", tuple[1])

numbers = (1, 2, 3, 4, 5)

a, b, c, d, e = numbers 

print(a)
print(b)
print(c)
print(d)
print(e)


my_tuples = (10, 20, 30, 40)

first, *middle, last = my_tuples

print(middle)

