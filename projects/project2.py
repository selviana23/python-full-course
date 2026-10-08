#functions defination
def add(x, y):
    return x + y
def subtract(x , y):
    return x - y
def multiple(x , y):
    return x * y
def division (x , y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Select Operations:")
print("1.Add")
print("2.Subtract")
print("3.Multiplication")
print("4.Divide")
choice = int (input("Enter choice (1/2/3/4):"))
x = float(input("Enter your first number:"))
y = float(input("Enter your second number:"))
if choice == 1:
    print ("Result:", add(x,y))
elif choice == 2:
    print("Result:",subtract(x,y))
elif choice == 3:
    print("Result:", multiple(x, y))

elif choice == 4:
    print("Result:", division(x, y))

else:
    print("Invalid choice")

