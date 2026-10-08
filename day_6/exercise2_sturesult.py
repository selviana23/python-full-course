# 1.Define Student class with logic
class Students:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
    def result (self):
        if self.marks >= 40:
            return 'Pass'
        else :
            return 'Fail'
s1 = Students ('Bean',45)
s2 = Students ('Jennie',50)
s3 = Students ('Sima',80)

print(s1.name ,s1.result())
print(s2.name ,s2.result())
print(s3.name, s3.result())
