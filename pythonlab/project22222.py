# A school decided to replace the desks in three classrooms. each desk sits two students.
#given the number of students in each class, print the smallest possible numbers of desks
#that can be purchased
#the program should read three integers: the number of students in each of the three classes,
# a,b,c respectively
no_students_class1= int(input("enter the number of students in first class:"))
no_students_class2= int(input("enter the number of students in second class:"))
no_students_class3= int(input("enter the number of students in third class:"))
desk_class1=(no_students_class1/2)
print(f"the required number of desk for first class is {desk_class1}")
desk_class2=(no_students_class2/2)
print(f"the required number of desk for second class is {desk_class2}")
desk_class3=(no_students_class3/2)
print(f"the required number of desk for third class is {desk_class3}")
remain_class1= (no_students_class1%2)
print(f"remaining desk for first class is {remain_class1}")
remain_class2=(no_students_class2%2)
print(f"remaining desk for second class is {remain_class2}")
remain_class3=(no_students_class3%2)
print(f"remaining desk for third class is {remain_class3}")
total_desk = desk_class1 + desk_class2 + desk_class3 + remain_class1 + remain_class2 + remain_class3
print(f"total number of desk that can be purchased is{total_desk}")
