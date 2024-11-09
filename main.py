# Simple ice cream buying simulation
def buy_ice_cream():
    # List of available ice cream flavors
    flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint", "Mango"]
    
    print("Welcome to the Ice Cream Shop!")
    print("Available flavors:")
    for i, flavor in enumerate(flavors, 1):
        print(f"{i}. {flavor}")
    
    # Prompt user to select a flavor
    choice = int(input("Enter the number of the flavor you want to buy: "))
    
    if 1 <= choice <= len(flavors):
        selected_flavor = flavors[choice - 1]
        print(f"You selected: {selected_flavor}")
        
        # Confirm purchase
        confirm = input("Would you like to buy this ice cream? (yes/no): ").strip().lower()
        
        if confirm == "yes":
            print(f"Thank you for purchasing {selected_flavor} ice cream! Enjoy!")
        else:
            print("No worries! Maybe next time.")
    else:
        print("Invalid choice, please try again.")

# Run the ice cream buying simulation
buy_ice_cream()
