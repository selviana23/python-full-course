# 1. Creation & Types
fruits = ("apple", "banana", "cherry")
single = (10) 
mixed = ("Prajwol", 25, "Developer")
# 2. Accessing & Slicing
print(fruits[0], fruits[-1]) # Output: apple cherry
print(fruits[0:2]) # Output: ('apple', 'banana')
print(single)
# 3. Unpacking
name, age, role = mixed
print(f"{name} is {age} as {role}")
# 4. Operations & Methods
nums = (4, 2, 7, 2)
print("Count of 2:", nums.count(2)) # Output: 2
combined = fruits + ("mango",)
print("Total items:", len(combined)) # Output: 4
# 5. Nested Tuples
nested = ("point", (3, 4))
print("X:", nested[1][0]) # Output: 3