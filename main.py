# Function: calculateTotal
def calculateTotal(prices):
    total = 0
    for price in prices:
        total += price
    return total


# Function: applyDiscount
def applyDiscount(total):
    if total > 10:
        total = total * 0.9   # 10% discount
    return total


# Procedure: displayReceipt
def displayReceipt(name, items, final_cost):
    print("\n----- RECEIPT -----")
    print("Student Name:", name)
    print("Items Ordered:")
    
    for item in items:
        print("-", item)
    
    print("Final Cost: $", round(final_cost, 2))
    print("-------------------")


# Main Algorithm
def main():
    menu = {
        1: ("Burger", 5.00),
        2: ("Scroll", 4.50),
        3: ("Chocolate Milk", 2.50),
        4: ("Pasta", 6.50),
        5: ("Garlic Bread", 2.50)
    }

    prices = []
    items_ordered = []

    name = input("Enter student name: ")

    while True:
        print("\n--- SCHOOL CANTEEN MENU ---")
        for number, item in menu.items():
            print(f"{number}. {item[0]} - ${item[1]}")
        print("0. Finish Order")

        choice = int(input("Select item number(type 0 if order is done): "))

        if choice == 0:
            break
        elif choice in menu:
            item_name, item_price = menu[choice]
            items_ordered.append(item_name)
            prices.append(item_price)
            print(item_name, "added to order.")
        else:
            print("Invalid choice. Try again.")

    total = calculateTotal(prices)
    final_cost = applyDiscount(total)

    displayReceipt(name, items_ordered, final_cost)


# Run program
main()