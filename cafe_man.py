# Infinite loop for serving multiple customers
while True:
    # Greet and show menu
    print("\n___________ Welcome to our restaurant _____________")

    menu = {
        "pizza": 100,
        "pasta": 60,
        "salad": 80,
        "burger": 70,
        "coffee": 90
    }

    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item.title()}: {price}")

    order_total = 0

    # Take orders until customer is done
    while True:
        item = input("\nEnter an item from the menu you want (or type 'exit' to stop): ").lower()

        if item == "exit":
            break

        if item in menu:
            order_total += menu[item]
            print(f"Your {item} is ordered.")
        else:
            print(f"The item '{item}' is currently unavailable.")

        another_order = input("Do you want to order something else? (yes/no): ").lower()

        if another_order != "yes":
            break

    # Final bill for the customer
    print(f"\nThank you! Your total bill is: {order_total}")

    # Ask if we should serve another customer
    new_customer = input("\nIs there another customer? (yes/no): ").lower()
    if new_customer != "yes":
        print("Restaurant is closing. Goodbye!")
        break
