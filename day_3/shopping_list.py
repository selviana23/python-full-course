shopping_list = []
shopping_list.append('strawberry')
shopping_list.append('milk')
shopping_list.append('chocolate')
shopping_list.append('eggs')
shopping_list.remove('milk')
print(shopping_list)

if 'eggs'in shopping_list:
    print("eggs is in the list")
total_count = len(shopping_list)
print(total_count)
for i in range(len (shopping_list)):
   print(i + 1, shopping_list)


