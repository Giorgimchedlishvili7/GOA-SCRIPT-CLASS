def GIORGI():
    print("Hello Giorgi")

def subtrac(num1, num2):
    whole = num1 - num2

    return whole

def for_loop():
    for i in range():

 def is_even(list1):
    even = [] 

    for i in list1:
        if i % 2 == 0:
            even.append(i)
    return even

print(is_even([1,2,3,4,5,6,7,8,9,10]))

def vowels(string1):
    vowels_list = []
    vow = ["a", "i", "o", "u"]

    for i in string1:
        if i in vow:
            vowels_list.append(i)
    return vowels_list

print(vowels("Giorgi"))

def cube(length, width):
    area = length * width
    perimeter = length * 2 + width * 2
    return area, perimeter
print(cube(12, 23))
def cube(length, width):
    area = length * width
    perimeter = length * 2 + width * 2
    return area, perimeter
ar,       per = cube(12, 34)
#area     #perimeter
print(ar, per)

#a function is a resusable block of code