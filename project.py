# # ============================================
# #           ☕ FAMILY CAFE ☕
# #        CAFE MANAGEMENT SYSTEM
# # ============================================

# menu = {
#     "Pizza": 40,
#     "Chai": 10,
#     "Samosa": 15,
#     "Burger": 60,
#     "Coffee": 110
# }

# order = {}
# total = 0


# # ============================================
# #              WELCOME MESSAGE
# # ============================================

# print("=" * 50)
# print("              ☕ FAMILY CAFE ☕")
# print("           Taste • Quality • Love")
# print("=" * 50)


# # ============================================
# #             CUSTOMER DETAILS
# # ============================================

# customer_name = input("Enter customer name: ")
# table_no = input("Enter table number: ")


# # ============================================
# #                 MENU
# # ============================================

# print("\n" + "=" * 50)
# print("                    MENU")
# print("=" * 50)

# print(f"{'Item':<15}{'Price':>15}")
# print("-" * 30)

# for item, price in menu.items():
#     print(f"{item:<15}Rs.{price:>10}")

# print("=" * 50)


# # ============================================
# #              TAKE CUSTOMER ORDER
# # ============================================

# while True:

#     item = input("\nEnter item name (or 'done' to finish): ").title()

#     # Stop taking order
#     if item == "Done":
#         break

#     # Check item availability
#     if item in menu:

#         try:
#             quantity = int(input(f"Enter quantity of {item}: "))

#             # Check valid quantity
#             if quantity <= 0:
#                 print("❌ Quantity must be greater than 0.")
#                 continue

#             # Add quantity if item already exists
#             if item in order:
#                 order[item] += quantity
#             else:
#                 order[item] = quantity

#             # Calculate item amount
#             amount = menu[item] * quantity

#             # Add amount to total
#             total += amount

#             print(f"✅ {quantity} x {item} added to your order.")
#             print(f"   Item amount: Rs.{amount}")

#         except ValueError:
#             print("❌ Please enter a valid number.")

#     else:
#         print("❌ Sorry! This item is not available.")


# # ============================================
# #                  FINAL BILL
# # ============================================

# print("\n")
# print("=" * 55)
# print("                    FINAL BILL")
# print("=" * 55)

# print(f"Customer : {customer_name}")
# print(f"Table No : {table_no}")

# print("-" * 55)

# print(f"{'Item':<15}{'Qty':<8}{'Rate':<12}{'Amount':>10}")
# print("-" * 55)


# # Display ordered items
# for item, quantity in order.items():

#     rate = menu[item]
#     amount = rate * quantity

#     print(f"{item:<15}{quantity:<8}Rs.{rate:<10}Rs.{amount:>8}")


# # ============================================
# #              BILL CALCULATION
# # ============================================

# print("-" * 55)

# print(f"{'Subtotal':<35}Rs.{total:>8}")

# # GST = 5%
# gst = total * 0.05

# print(f"{'GST (5%)':<35}Rs.{gst:>8.2f}")

# grand_total = total + gst

# print("-" * 55)

# print(f"{'TOTAL AMOUNT':<35}Rs.{grand_total:>8.2f}")

# print("=" * 55)
# print("             Thank You! ❤️")
# print("        Please visit us again.")
# print("=" * 55)









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
        