std = {}

def add_student(nameStd, marks):
    std[nameStd] = marks

def update_marks(nameStd, marks):
    if nameStd in std:
        std[nameStd] = marks

def delete_student(nameStd):
    if nameStd in std:
        del std[nameStd]

def topper():
    return max(std, key=std.get)
add_student("Dev", 0)
add_student("Areeb", 95)
add_student("Pasha", 6.9)

update_marks("Dev", 1)
delete_student("Dev")

print("All students:", std)
print("Topper:", topper())
print("Areeb Marks:", std["Areeb"])