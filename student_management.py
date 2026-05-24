# student marks manangement system

list1=[]
list2=[]
n=int(input("enter the value of n: "))
print("enter the names of the students:  ")
for i in range(0,n):
    values=input(f"enter the name of the student {i+1}: ")
    list1.append(values)

print("enter the marks of the students: ")
for j in range(0,n):
    marks=int(input(f"enter the marks of the student {j+1}: "))
    list2.append(marks)


print("1.MAX from student list\n2.MIN marks from the student list\n3.SUM of all students\n4.AVERAGE of all students")
choice=int(input("enter your choice: "))
max=list2[0]
students=list1[0]
if choice==1:
    print("the maximum mark in the list")
    for i in range(0,n):
        if list2[i]>max:
            max=list2[i]
            students=list1[i]
    print("the max marks is: ",max,"by",students)
    
min=list2[0]
students=list1[0]
if choice==2:
    print("the minimum marks in the list")
    for i in range(0,n):
        if list2[i]<min:
            min=list2[i]
            students=list1[i]
    print("the min marks is: ",min,"by",students)
        
        
sum=0
if choice==3:
    print("the sum of all students marks: ")
    for marks in list2:
        sum=sum+marks
    print("the sum of all students: ",sum)

if choice==4:
    sum=0
    print("the average of all students marks: ")
    for marks in list2:
        sum+=marks
    average=sum/n
    print("the average of the all students marks: ",average)

if choice==5:
    print("ALL STUDENTS NAMES WITH MARKS")
    for i in range(0,n):
        students=list1[i]
        marks=list2[i]
        print(f"the student{i+1} name is ",students,"and marks is ",marks)
