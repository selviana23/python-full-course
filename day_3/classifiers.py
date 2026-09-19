def check_even_odd(n):
    return "even"if n % 2==0 else "odd"
numbers =[12, 7, 15, 18, 14]
evens, odds = 0, 0
for num in numbers:
    result = check_even_odd(num)
    print(f"{num} is {result}")
    if result =="even": evens +=1
    else: odds +=1
print('total even',total evens)
print('total odd',total odds)