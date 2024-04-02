# variables
name = "Beau"
__name_last__ = "Smith"
age = 39
ADDRESS = "123 Main St"
_city_ = "Boston"; print(name)

print(type(name) == str)
print(isinstance(name, str))
age = 2
print(isinstance(age, float))
age = float(2)
print(isinstance(age, float))
age = int("20")
print(isinstance(age, int))
number = "20"
new_age = int(number)
print(isinstance(new_age, int))
# datatyping
# complex for complex numbers
# bool for booleans
# list for lists
# tuple for tuples
# range for ranges
# dict for dictionaries
#  set for sets

# Operators
1 + 1 #2
2 - 1 #1
2 * 2 #4
4 / 2 #2
4 % 3 #1
4 ** 2 #16
5 // 2 #2
age = 8
age += 8 #age = age + 8
print(age)
print(1 + -1)
print ("Scamp" + " is a good dog")

age = 8
age *= 8
print(age)

# Comparison Operators
a = 1
b = 2

a == b #False
a != b #True
a > b #False
a <= b #True

# Boolean Operators
condition1 = True
condition2 = False

not condition1 #False
condition1 and condition2 #False
condition1 or condition2 #True

# if x is false, then x, else y. ex: print(x or y)
print(0 or 1) # 1, false value
print(False or 'hey') # hey, true value
print('hi' or 'hey') # hi, true value
print([] or False) # False
print(False or []) # [], false value

# and only evaluates the second argument if the first one is true
print(0 and 1) # 0, false value
print(1 and 0) # 0, false value
print(False and 'hey') # False
print('hi' and 'hey') # hey
print([] and False) # []
print(False and []) # False

# Bitwise Operators
# & performs binary AND
# | performs binary OR
# ^ performs binary XOR operation
# ~ performs a binary NOT operation
# << shift left operation
# >> shift right operation 
