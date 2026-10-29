
print("===== CAMPUS CANTEEN BILLING SYSTEM =====")

print("\nMenu:")
print("1. Burger       - PKR 300")
print("2. Pizza        - PKR 500")
print("3. Sandwich     - PKR 200")
print("4. Tea          - PKR 100")
print("0. Checkout")

subtotal = 0
total_quantity = 0

while True:
    choice = input("\nEnter item number (0 to checkout): ")

    if choice == "0":
        break

    elif choice == "1":
        price = 300
        item = "Burger"

    elif choice == "2":
        price = 500
        item = "Pizza"

    elif choice == "3":
        price = 200
        item = "Sandwich"

    elif choice == "4":
        price = 100
        item = "Tea"

    else:
        print("Invalid choice! Please select 1, 2, 3, 4 or 0.")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Invalid quantity! Please enter a positive number.")
        continue

    item_total = price * quantity
    subtotal = subtotal + item_total
    total_quantity = total_quantity + quantity

    print(item, "x", quantity, "=", "PKR", item_total)
    print("Current subtotal: PKR", subtotal)

discount = 0

if subtotal >= 1000:
    discount = subtotal * 0.10

final_bill = subtotal - discount

print("\n========== FINAL BILL ==========")
print("Subtotal:       PKR", subtotal)
print("Discount:       PKR", discount)
print("Total quantity:", total_quantity)
print("Final bill:     PKR", final_bill)
print("Thank you for visiting!")
