# student management system :::::::

students=[]
def add_student():
    name=input("Enter name :")
    marks=int(input("Enter the marks :"))
    
    student={
        "name":name,
        "marks":marks
    }
    
    students.append(student)
    print("student added succesfully")
def show_student(students):
    if len(students)==0:
        print("student is not found :")
    else:
        for student in students:
            print("name :",student["name"])
            print("marks :",student["marks"])
            print("==========================")
            
while True:
    print("1. Add Student ")
    print("2. Show Student ")
    print("3. Exit")
    
    choice=input("enter your choice :")
    
    if choice=="1":
        add_student()
    elif choice=="2":
        show_student(students)
    elif choice=="3":
        print("Program ended ")
        break
    else:
        print("invalid choice")
        
