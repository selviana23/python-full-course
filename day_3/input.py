shopping_list = []
for i in range (4):
   item = input("What item do you need?")
   shopping_list.append(item)
   print(shopping_list)
for i in range(len(shopping_list)):
    print(i + 1,shopping_list[i])