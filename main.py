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

# integer
def check_quantity(txt):
    """This function is specific to how many quesadillas the user wants. It sets bounderies to deal with unexpected inputs."""
    while True:
        try:
            x = int(input(txt)) # checks if this is an integer
            if x >= 1 and x <= 10:
                return x
            else:
                print("Invalid quantity. You can only order 1-10 quesadillas at a time.")
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
    """This function is specific to checking the user's input for the pickup or delivery prompt."""
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
            if x >= 1 and x <= 4: 
                return x
            else:
                print("Please enter either a number between 1 and 4.")
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
    user_info.append([first_name.capitalize(), address, phone_number])
    print()
    print("Details Saved.")


def pick_up_user_info():
    """This function saves the user's info which is specific for the pick up option."""
    print()
    print("-- -- -- -- Customer Detail -- -- -- --")
    print()
    first_name = check_string("First Name: ").lower().strip()
    user_info.append(first_name.capitalize()) # puts it into the user info list with the first letter of the name capitalised
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
    quantity = check_quantity(f"Quantity?: ") # fix by making another check funciton and have barriers of a min and max ammount.
    if user_quesadilla == 1:
        user_cart.append(quesadillas[0]) # selects the specific quesadilla the user wants and adds the information for that quesadilla into the user's cart which is saved as another list.
        user_cart[0].append(quantity)  # adds another element (index 3) in the list withint the list which will account for the quantity the user wants
        print(f"x{quantity} {quesadillas[0][0]}(s) added to cart.")
    elif user_quesadilla == 2:
        user_cart.append(quesadillas[1])
        user_cart[0].append(quantity)
        print(f"x{quantity} {quesadillas[1][0]}(s) added to cart.")
    elif user_quesadilla == 3:
        user_cart.append(quesadillas[2])
        user_cart[0].append(quantity)
        print(f"x{quantity} {quesadillas[2][0]}(s) added to cart.")
    elif user_quesadilla == 4:
        user_cart.append(quesadillas[3])
        user_cart[0].append(quantity)
        print(f"x{quantity} {quesadillas[3][0]}(s) added to cart.")
    elif user_quesadilla == 5:
        user_cart.append(quesadillas[4])
        user_cart[0].append(quantity)
        print(f"x{quantity} {quesadillas[4][0]}(s) added to cart.")
    elif user_quesadilla == 6:
        user_cart.append(quesadillas[5])
        user_cart[0].append(quantity)
        print(f"x{quantity} {quesadillas[5][0]}(s) added to cart.")
    elif user_quesadilla == 7:
        user_cart.append(quesadillas[6])
        user_cart[0].append(quantity)
        print(f"x{quantity} {quesadillas[6][0]}(s) added to cart.")
    elif user_quesadilla == 8:
        user_cart.append(quesadillas[7])
        user_cart[0].append(quantity)
        print(f"x{quantity} {quesadillas[7][0]}(s) added to cart.")


def quesadillas_menu():
    """This function displays all the available quesadillas with a price and a description."""
    count = 0 # to keep count of how many elements three are in the list.
    for quesadilla in quesadillas:
        count += 1 # adds 1 to count 
        print()
        print(f"{count}) {quesadilla[0]} - ${quesadilla[2]}\n{quesadilla[1]}")
    print()
    print("Would you like to add items into your cart? (y/n):")
    order = check_response("> ")
    if order in ["y", "yes"]:
        add_to_cart()


def calculate():
    """This function calculates the total cost of the user's items."""
    for quesadilla in user_cart:
        total = sum(quesadilla[2])
        print(f"Total Cost: ${total:.2f}") # make sure the output is 2dp

# fix
def cart_menu():
    """This function holds the cart menu for the user, which allows them to add additional items into their cart, remove items into their cart or simply view the items in their cart. """
    pass # add while loop, so that it asks the user again and again if they want to add more or they are ready to check out.


def display_cart():
    """This funciton displays all the items the user currently has within their cart."""
    print()
    print("🛒 Your Cart:")
    count = 0 # to keep count of how many elements three are in the list.
    if len(user_cart) == 0:
        print("You have 0 items inside your cart.")    
    else:
        for quesadilla in user_cart:
            count += 1
            total_quantity = sum(quesadilla[3])
            print()
            print(f"{count}) {quesadilla[0]} - ${quesadilla[2]}")
        print()
        print(f"You ordered {total_quantity} quesadillas.")
        calculate()

#fix
def checkout():
    """This function allows the user to secure their order once they are happy with all the items they have in their cart."""
    if len(user_cart) == 0:
        print()
        print("You have 0 items in your cart.")
    else:
        for info in user_info:
            if len(user_info) == 1:
                print()
                print(f"Customer Name: {info[0]}")
            elif len(user_info) > 1:
                print()
                print(f"Customer Name: {info[0]} \nDelivery Address: {info[1]} \nPhone: {info[2]}")


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
        print("3. Checkout")
        choice = check_menu_int("\n> ") # used a number system instead to prevent user errors.
        print()
        print("-- -- -- -- -- -- -- -- -- -- -- -- -- -- --")

        if choice == 1: 
            quesadillas_menu()
        elif choice == 2: 
            display_cart()
        elif choice == 3: 
            checkout()
        
        response = check_response("\nBack to main menu? (y/n):\n> ")
        if response not in ["y", "yes"]:
            break


if __name__ == "__main__": # python convention, anything under this is ran only inside this page.
   main_menu()

"""
tweaks:
- tell them how many items they have in the cart when they click view cart details or sum
- what if the user has nothing int their cart? (change this so that it tells them they have 0 items in the cart)
- in the check out box, capitalise the first letter of the user's name + address + add a maximum phone number

- check each and evefy integer input and do not allow any inputs to be a negative integer/float/etc
"""