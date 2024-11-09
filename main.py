# Enhanced ice cream buying simulation with bill generation
def buy_ice_cream():
    # List of available ice cream flavors with prices
    flavors = {
        "Vanilla": 1.50,
        "Chocolate": 2.00,
        "Strawberry": 1.75,
        "Mint": 2.25,
        "Mango": 2.00
    }

    print("Welcome to the Ice Cream Shop!")
    print("Available flavors and prices:")
    for i, (flavor, price) in enumerate(flavors.items(), 1):
        print(f"{i}. {flavor} - ${price:.2f}")
    
    # Initialize variables for order and total cost
    order = []
    total_cost = 0.0

    # Allow user to select multiple flavors
    while True:
        choice = int(input("Enter the number of the flavor you want to buy (or 0 to finish): "))

        if choice == 0:
            break  # Exit loop if user is done selecting

        if 1 <= choice <= len(flavors):
            selected_flavor = list(flavors.keys())[choice - 1]
            price = flavors[selected_flavor]
            print(f"You selected: {selected_flavor} - ${price:.2f}")
            
            # Confirm adding to order
            confirm = input(f"Would you like to add {selected_flavor} to your order? (yes/no): ").strip().lower()
            
            if confirm == "yes":
                order.append((selected_flavor, price))
                total_cost += price
                print(f"{selected_flavor} added to your order.")
            else:
                print(f"{selected_flavor} not added.")
        else:
            print("Invalid choice, please try again.")

    # Generate bill if the order is not empty
    if order:
        print("\nYour Bill:")
        print("Flavor               Price")
        print("---------------------------")
        for flavor, price in order:
            print(f"{flavor:<20} ${price:.2f}")
        print("---------------------------")
        print(f"Total Cost:          ${total_cost:.2f}")
        print("Thank you for your purchase! Enjoy your ice cream!")
    else:
        print("You did not purchase any ice cream. Maybe next time!")

# Run the ice cream buying simulation
buy_ice_cream()
