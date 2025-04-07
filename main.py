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


def get_int(txt):
    """This function is to check each integer user input to control the input types and prevent the program from crashing"""
    while True:
        try:
            x = int(input(txt))
            return x
        except ValueError:
            print("Invalid Input. Please enter a number.")
            print()

# fix
def check_string(txt):
    """This function checks each user string input and prevents the user from not entering anything and the program saving nothing."""
    while True:
        try: 
            x = input(txt)
            if len(x) > 0:
                return x
        except ValueError:
            print("Please make sure that you have entered something in.")
            print()

# fix
def phone_characters(txt):
    """This function checks the number of characters entered in when the user has entered their phone number, and provides a barrier of how many characters they should enter in."""
    while True:
        try:
            x = int(input(txt))
            if len(x) >= 9 and len(x) <= 10:
                return x
        except ValueError:
            print("Please make sure it is 9-10 characters long.")


def delivery_user_info():
    """This function saves the user's info which is specific for the delivery option."""
    print()
    print("-- -- -- -- Customer Details -- -- -- --")
    print()
    first_name = input("First Name: ").lower().strip()
    address = input("Address: ").lower().strip()
    phone_number = input("Phone Number: ").lower().strip()
    user_info.extend([first_name.capitalize(), address, phone_number]) # "extend" + square brackets = another way to append more than one value into the user's list. 
    print()
    print("Details Saved.")


def pick_up_user_info():
    """This function saves the user's info which is specific for the pick up option."""
    print()
    print("-- -- -- -- Customer Detail -- -- -- --")
    first_name = input("First Name: ").lower().strip()
    user_info.append(first_name.capitalize())
    print()
    print("Detail Saved.")


def pickup_or_delivery():
    """This funciton asks the user to choose whether they want to pick up the food or get it delivered. It also determines what information is asked of them."""
    print()
    option = get_int("Please select from the following options: \n1) Pick up \n2) Delivery\n> ")
    if option == 1:
        pick_up_user_info()
    elif option == 2:
        delivery_user_info()


def quesadillas_menu():
    """This function displays all the available quesadillas with a price and a description."""
    count = 0 # to keep count of how many elements three are in the list.
    for quesadilla in quesadillas:
        count += 1 # adds 1 to count 
        print()
        print(f"{count}) {quesadilla[0]} - ${quesadilla[2]}\n{quesadilla[1]}")

# fix
# should i not make this a separate function anymore? just put this option in the display menu option?
def add_to_cart():
    """This function allows the user to add different items to their cart, which saves the information in a list on the main scope"""
    print()
    user_quesadilla = get_int("Which quesadilla would you like?: ")
    if user_quesadilla == 1:
        user_cart.append(quesadillas[0]) # selects the specific quesadilla the user wants and adds the information for that quesadilla into the user's cart which is saved as another list.
        print(f"{quesadillas[0][0]} added to cart.")
    elif user_quesadilla == 2:
        user_cart.append(quesadillas[1])
        print(f"{quesadillas[1][0]} added to cart.")
    elif user_quesadilla == 3:
        user_cart.append(quesadillas[2])
        print(f"{quesadillas[2][0]} added to cart.")
    elif user_quesadilla == 4:
        user_cart.append(quesadillas[3])
        print(f"{quesadillas[3][0]} added to cart.")
    elif user_quesadilla == 5:
        user_cart.append(quesadillas[4])
        print(f"{quesadillas[4][0]} added to cart.")
    elif user_quesadilla == 6:
        user_cart.append(quesadillas[5])
        print(f"{quesadillas[5][0]} added to cart.")
    elif user_quesadilla == 7:
        user_cart.append(quesadillas[6])
        print(f"{quesadillas[6][0]} added to cart.")
    elif user_quesadilla == 8:
        user_cart.append(quesadillas[7])
        print(f"{quesadillas[7][0]} added to cart.")

# test + fix after creating working menu system
def calculate():
    for item in user_cart:
        total = sum(item[2])
        print(f"Total: ${total:.2f}")

def cart_menu():
    """This function holds the cart menu for the user, which allows them to add additional items into their cart, remove items into their cart or simply view the items in their cart. """
    pass # add while loop, so that it asks the user again and again if they want to add more or they are ready to check out.

def display_cart():
    print()
    print("🛒 Your Cart:")
    count = 0 # to keep count of how many elements three are in the list.     
    for quesadilla in user_cart:
        count += 1
        print()
        print(f"{count}) {quesadilla[0]} - ${quesadilla[2]}")
    print()
    calculate()

#fix
def checkout():
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
    """This function holds the main menu. It displays a range of different options the user can do in this ordering programme and executes them accordingly - by calling hte other function"""
    print("Welcome to Queenstown Quesadilla's online orders")
    print()
    input("Press enter to continue")
    pickup_or_delivery()
    while True:
        print()
        print("-- -- -- -- -- -- -- -- -- -- -- -- -- -- --") # to emphasise the menu system
        print("Select from the following options:")
        print()
        print("1. View Quesadillas Menu") 
        print()
        print("2. Add Quesadillas to Cart")
        print()
        print("3. View Cart")
        print()
        print("4. Checkout")
        print()
        choice = get_int("\n> ") #prevents the user from putting in an unexpected input
        print()
        print("-- -- -- -- -- -- -- -- -- -- -- -- -- -- --")

        if choice == 1: 
            quesadillas_menu()
        elif choice == 2: 
            add_to_cart()
        elif choice == 3: 
            display_cart()
        elif choice == 4: 
            checkout()
        
        response = input("\nChoose again? (y/n):\n> ").lower().strip()
        print()
        if response not in ["y", "yes"]:
            break

if __name__ == "__main__": # python convention, anything under this  is ran only in this page.
    main_menu()

"""
tweaks:
- tell them how many items they have in the cart when they click view cart details or sum
- what if the user has nothing int their cart? (change this so that it tells them they have 0 items in the cart)
- in the check out box, capitalise the first letter of the user's name + address + add a maximum phone number

- check each and evefy integer input and do not allow any inputs to be a negative integer/float/etc


"""