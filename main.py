import sys # for program termination

"""This is an online ordering program for 'Queenstown Quesadillas' made for customers who want to pre order food and beverages for pickup or delivery."""

# quesadilla, description, price
quesadillas = [["Classic Cheese Quesadilla", "Melted cheddar & mozzarella in a crispy flour tortilla, served with salsa & sour cream.", 9.99], 
               ["Chicken & Cheese Quesadilla", "Grilled chicken, cheddar, mozzarella, and mild spices, served with sour cream & guacamole.", 12.99], 
               ["Beef Quesadilla", "Seasoned ground beef, melted cheese blend, and smoky chipotle sauce.", 13.99], 
               ["BBQ Pulled Pork Quesadilla", "Slow-cooked pulled pork, smoky BBQ sauce, and cheese blend.", 14.99], 
               ["Spicy Jalapeño & Cheese Quesadilla", "A fiery combo of jalapeños, cheddar, mozzarella, and spicy mayo.", 11.99], 
               ["Vegetarian Quesadilla", "Black beans, roasted capsicum, mushrooms, cheese, and fresh herbs.", 11.99], 
               ["Seafood Quesadilla ", "Garlic butter prawns, creamy cheese blend, and zesty lime drizzle.", 15.99], 
               ["Breakfast Quesadilla","Scrambled eggs, crispy bacon, hash browns, and cheese blend with hollandaise drizzle.", 13.99]] 

"""I put the user information in the main scope because the program has to utilise this information at the end (to confirm with the user)."""
user_info = [] # information will be saved after pickup/delivery function called.
user_cart = []


DELIVERY_FEE = 15 # constant

#integer
def check_rem_int(txt):
    """This function is specific to the remove items function. Its special because the barier amounts (options) can change all the time according to how many items the user has in their cart."""
    while True:
        try:
            x = int(input(txt)) # checks if this is an integer
            max_options = len(user_cart) # length of the list
            if x >= 1 and x <= max_options:
                return x
            else:
                print(f"Invalid choice. You can only select a number between 1-{max_options}.")
                print()
        except ValueError:
            print("Invalid Input. Please enter a number.")
            print()

# integer
def check_quantity(txt):
    """This function is specific to how many quesadillas the user wants. It sets bounderies to deal with unexpected inputs."""
    while True:
        try:
            x = int(input(txt)) # checks if this is an integer
            if x >= 1 and x <= 5:
                return x
            else:
                print("Invalid quantity. You can only order 1-5 quesadillas of each type at a time.")
                print()
        except ValueError:
            print("Invalid Input. Please enter a number.")
            print()

# string
def check_response(txt):
    """This function is only applied to yes or no answers and deals with potential input errors."""
    while True:
        x = input(txt).strip().lower() # strips any potential accidental spaces and makes it all lowercase.
        if x in ["y", "yes", "n", "no"]: 
            return x
        elif x == "":
            print("Input can't be blank. Please enter something.")
            print()
        else: 
            print("Please enter an appropriate response. (y/n)")
            print()

# integer
def check_deliver_int(txt):
    """This function is specific to checking the user's input for the pickup or delivery prompt and when removing items."""
    while True:
        try:
            x = int(input(txt)) # checks if this is an integer
            if x in [1, 2]:
                return x
            else:
                print("Please enter 1 or 2.")
                print()
        except ValueError:
            print("Invalid Input. Please enter a number.")
            print()

# integer
def check_order_int(txt):
    """This function is specific to the user's selection of quesadillas according to the menu."""
    while True:
        try:
            x = int(input(txt)) # won't count floats either
            if x >= 1 and x <= 8: # prevents negatives and other larger num
                return x
            else:
                print("Please enter a number between 1 and 8.")
                print()
        except ValueError:
            print("Invalid Input. Please enter a number.")
            print()

# integer
def check_menu_int(txt):
    """This function is specific to the user's operation selection in the main menu system."""
    while True:
        try:
            x = int(input(txt))
            if x >= 1 and x <= 6: 
                return x
            else:
                print("Please enter either a number between 1 and 7.")
        except ValueError:
            print("Invalid Input. Please enter a number.")

# string
def check_string(txt):
    """This function checks strings and prevents the program from saving nothing."""
    while True:
        x = input(txt).strip()
        if x: # if it contains a value, it will be the same as "if True:"
            return x
        print("Input can't be blank. Please enter something.")
        print()

#integer
def check_phone_characters(txt):
    """This function checks the number of integer characters entered for the phone number, and provides a range of how many characters they should enter in."""
    while True:
        try:
            x = int(input(txt)) # checks if this is an integer
            if len(str(x)) >= 9 and len(str(x)) <= 10: # checks the length of the number by converting it into a string and through len
                return x
            else:
                print("Please enter a 9 or 10 digit number.")
        except ValueError:
            print("Invalid phone number. Please enter a 9 or 10 digit number.")


def delivery_user_info():
    """This function saves the user's info which is specific for the delivery option."""
    print()
    print("-- -- -- -- Customer Details -- -- -- --")
    print()
    first_name = check_string("First Name: ").lower().strip()
    address = check_string("Address: ") # fix? .lower().strip()
    phone_number = check_phone_characters("Phone Number: ") 
    user_info.extend([first_name.capitalize(), address, phone_number]) # ".extend" is like .append, but appends more than 1 element into the list. 
    user_info.append("delivery") # operation (index 3)
    print()
    print("Details Saved.")
    

def pick_up_user_info():
    """This function saves the user's info which is specific for the pick up option."""
    print()
    print("-- -- -- -- Customer Detail -- -- -- --")
    print()
    first_name = check_string("First Name: ").lower().strip()
    user_info.append(first_name.capitalize()) # puts it into the user info list with the first letter of the name capitalised
    user_info.append("pick-up") # operation (index 1)
    print()
    print("Detail Saved.")


def pickup_or_delivery():
    """This funciton asks the user to choose whether they want to pick up or get their items delivered."""
    print()
    option = check_deliver_int("Please select from the following options: \n1) Pick up \n2) Delivery\n> ")
    if option == 1:
        pick_up_user_info()
    elif option == 2:
        delivery_user_info()


def add_to_cart():
    """This function allows the user to add different items to their cart, which saves the information in a list on the main scope"""
    print()
    user_quesadilla = check_order_int("Which quesadilla would you like?: ")
    quantity = check_quantity("Quantity?: ") # checks if its in range 1-5
    # checks first if they want to add more than 5 quesadillas.

    selected_item = quesadillas[user_quesadilla -1]
    name = selected_item[0]
    price = selected_item[2]
    
    for item in user_cart:
        if item[0] == name: # if the name of the item is equal to the quesadilla the user selected. (user_quesadilla -1 gets the index of the quesadilla since the menu system is also arranged accordingly.)
            total_quantity = item[2] + quantity # initial existing quantity + new quantity they want to add
            if total_quantity <= 5: # barrier, limit = 5
                item[2] = total_quantity # replaces (updates) element 2 of the list within user_cart list which in this case is the quantity of the item.
                print(f"x{quantity} more {name}(s) added to cart.")
                return # exit & don't run the code below this.
            else:
                print("You can only order a maximum amount of 5 quesadillas of each kind.")
                return # exit & don't run the code below this.
    # if it isnt in the cart at all, the program should add it.
    user_cart.append([selected_item[0], selected_item[2], quantity])
    print(f"x{quantity} {selected_item[0]}(s) added to cart.")


def quesadillas_menu():
    """This function displays all the available quesadillas with a price and a description + allows the user to order off the menu."""
    count = 0 # to keep count of how many elements three are in the list.
    for quesadilla in quesadillas:
        count += 1 # adds 1 to count 
        print()
        print(f"{count}) {quesadilla[0]} - ${quesadilla[2]}\n{quesadilla[1]}")
    print()
    print("🛒 Add items to cart? (y/n):")
    order = check_response("> ")
    if order in ["y", "yes"]:
        add_to_cart()
    while order in ["y", "yes"]: # while loop so that it asks the user again and again if they want to add more things to their order until they are satisfied.
        print()
        print("🛒 Add more items? (y/n):")
        order = check_response("> ")
        if order in ["y", "yes"]:
            add_to_cart()


def rem_items():
    """This funciton targets and removes the items the user wants to take out of their cart."""
    if len(user_cart) == 0:
        print("Your cart is empty. No items to remove.")
    else:
        print("🛒 Your Cart:")
        for index, quesadilla in enumerate(user_cart):
            name = quesadilla[0]
            price = quesadilla[1]
            quantity = quesadilla[2]
            print(f"{index + 1}) {name} (x{quantity}) - ${price:.2f} each")
        
        print(f"Enter the item number you want to remove:")
        index_item_rem = check_rem_int("> ") - 1 # minus 1 because we need to keep in mind the index. Since we added +1, we have to subtract it again to get the index #.
        removed_item = user_cart[index_item_rem] # saves info about the item about to be removed so it can tell the user what has been removed.
        user_cart.remove(user_cart[index_item_rem])
        print(f"All {removed_item[0]}s removed from cart.")

    
def calculate_standard():
    """This function calculates the total cost of the user's items."""
    total = 0
    for quesadilla in user_cart:
        price = quesadilla[1]
        quantity = quesadilla[2]
        total += price * quantity
    print(f"Total Cost: ${total:.2f}") # make sure the output is 2dp


def calculate_delivery():
    """This function calculates the total cost of the user's items plus adds on a delivery fee."""
    total = 0
    for quesadilla in user_cart:
        price = quesadilla[1]
        quantity = quesadilla[2]
        total += price * quantity
    total += DELIVERY_FEE
    print(f"Total Cost: ${total:.2f}") # make sure the output is 2dp


def display_cart():
    """This funciton displays all the items the user currently has within their cart."""
    print()
    print("🛒 Your Cart:")

    if len(user_cart) == 0:
        print("You have 0 items inside your cart.")    
    else:
        total_quantity = 0 # keeps track the total amount of quesadillas the user has in cart
        for quesadilla in user_cart:
            name = quesadilla[0] # arranged in this style because it started to get super confusing.
            price = quesadilla[1]
            quantity = quesadilla[2]
            total_quantity += quantity
            print(f"(x{quantity}) {name}(s) - ${price:.2f} each")
        print(f"\nTotal Quesadillas: {total_quantity}")
        calculate_standard()


def end_program():
    """Function to end program"""
    print()
    print("Would you like to exit the program?: ")
    choice = check_response("> ")
    if choice in ["y", "yes"]:
        # clear all info before exiting
        user_cart.clear()
        user_info.clear()

        print("Thank you for choosing Queenstown Quesadillas.")
        sys.exit()
    else:
        pass


def end_or_restart_program():
    """Function to end or restart the program"""
    print()
    print("Would you like to 1) restart or 2) exit the program?: ")
    choice = check_deliver_int("> ")
    if choice == 1:
        # clear all info before restarting
        user_cart.clear()
        user_info.clear()
    
        print("Restarting...")
        main_menu()
    else:
        # clear all info before exiting
        user_cart.clear()
        user_info.clear()

        print("Thank you for choosing Queenstown Quesadillas.")
        sys.exit()
    

def cancel_order():
    """This function allows the user to cancel their order."""
    if len(user_cart) == 0:
        print("Your cart is empty. There is no order to cancel.")
    else:
        print("Are you sure you want to cancel your order? (y/n): ")
        confirm = check_response("> ")
        if confirm in ["y", "yes"]:
            user_cart.clear() # clear info 
            user_info.clear() # clear info
            print("Your order has successfully been cancelled.")
        else:
            print("Your order has not been cancelled.")


def order_summary():
    """Is a summary reciept of the user's order."""
    print()
    print("💳 Order Summary:")
    print()
    if len(user_cart) == 0:
        print()
        print(f"You have 0 quesadillas in your cart.")    
    else:
        total_quantity = 0 # keeps track the total amount of quesadillas the user has in cart
        for quesadilla in user_cart:
            name = quesadilla[0] # arranged in this style because it started to get super confusing.
            price = quesadilla[1]
            quantity = quesadilla[2]
            total_quantity += quantity
            print(f"(x{quantity}) {name}(s) - ${price:.2f} each - amount: ${price * quantity:.2f}")

        print(f"\nTotal Quesadillas: {total_quantity}")
        if len(user_info) > 2:
            print(f"Delivery fee: ${DELIVERY_FEE}")
            calculate_delivery()
            return # end here
        calculate_standard()


def checkout():
    """This function allows the user to secure their order once they are happy with all the items they have in their cart."""
    if len(user_cart) == 0:
        print()
        print("You have 0 items in your cart.")
    else:
        if "pick-up" in user_info: # pick-up
            print()
            print(f"Customer Name: {user_info[0]}")
            print()
            order_summary()
            print("Order Placed. You can expect your order ready for pickup in 10-15 minutes.")
        elif "delivery" in user_info: # delivery
            print()
            print(f"Customer Name: {user_info[0]} \nDelivery Address: {user_info[1]} \nPhone: {user_info[2]}")
            print()
            order_summary()
            print("Order Placed. We are only taking cash at this point. Your order will be delivered to you soon.")


def main_menu():
    """This function holds the main menu. It displays a range of different options the user can do in this ordering programme and executes them accordingly - by calling the other functions."""
    print("Welcome to Queenstown Quesadilla's online orders")
    print()
    input("Press enter to continue")
    pickup_or_delivery()
    while True:
        print()
        print("-- -- -- -- -- -- -- -- -- -- -- -- -- -- --") # to emphasise the menu system
        print()
        print("Select from the following options:")
        print("1. View Quesadillas Menu") 
        print("2. View Cart")
        print("3. Remove Items")
        print("4. Complete Order")
        print("5. Cancel Order")
        print("6. Restart/Exit Program")
        choice = check_menu_int("\n> ") # used a number system instead to prevent user errors.
        print()
        print("-- -- -- -- -- -- -- -- -- -- -- -- -- -- --")

        if choice == 1: 
            quesadillas_menu()
        elif choice == 2: 
            display_cart()
        elif choice == 3:
            rem_items()
        elif choice == 4: 
            checkout()
            break
        elif choice == 5:
            cancel_order()
            break
        elif choice == 6:
            end_or_restart_program()
            break
        
        response = check_response("\nBack to main menu? (y/n):\n> ")
        if response not in ["y", "yes"]:
            end_program()


if __name__ == "__main__": # python convention, anything under this is ran only inside this page.
   main_menu()