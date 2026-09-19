grades = [85, 92, 78]
grades.append(95)
print(grades)
grades.remove(78)
print(grades)
if 92 in grades:
    print("92 is in the list")
else:
    print("is not in the list")
total_count = len(grades)
total_sum = sum(grades)
lowest = min(grades)
highest = max(grades)
print("total_count=", "total_sum=", "lowest=", "highest=", total_count ,total_sum, lowest, highest)