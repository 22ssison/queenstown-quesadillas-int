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
            print()
            print("Invalid Input. Please enter a number.")


def delivery_user_info():
    """This function saves the user's info which is specific for the delivery option."""
    print()
    print("Customer Details:")
    print()
    first_name = input("First Name: ").lower().strip()
    print()
    address = input("Address: ").lower().strip()
    print()
    phone_number = input("Phone Number: ").lower().strip()
    user_info.append(first_name, address, phone_number)
    print()
    print("Details Saved.")


def pick_up_user_info():
    """This function saves the user's info which is specific for the pick up option."""
    print()
    print("Customer Details:")
    print()
    first_name = input("First Name: ").lower().strip()
    print()
    user_info.append(first_name)
    print()
    print("Details Saved.")


def pickup_or_delivery():
    """This funciton asks the user to choose whether they want to pick up the food or get it delivered. It also determines what information is asked of them."""
    option = get_int("Would you like to: \n1) pick up \n2) delivery\n\n> ").strip().lower()
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
    user_quesadilla = input("Which quesadilla would you like?: ")
    if user_quesadilla == 1:
        user_cart.append(quesadillas[0])
    elif user_quesadilla == 2:
        user_cart.append(quesadillas[1])
    elif user_quesadilla == 3:
        user_cart.append(quesadillas[1])


def calculate():
    pass


def cart_menu():
    """This function holds the cart menu for the user, which allows them to add additional items into their cart, remove items into their cart or simply view the items in their cart. """
    pass # add while loop, so that it asks the user again and again if they want to add more or they are ready to check out.

def main_menu():
    """This function holds the main menu. It displays a range of different options the user can do in this ordering programme and executes them accordingly - by calling hte other function"""
    print("Welcome to Queenstown Quesadilla's online orders")
    # view quesadilla menu (function)
    # view bevarage menu (function)
    # add option(s) to cart: (function)


if __name__ == "__main__": # python convention, anything under this  is ran only in this page.
    quesadillas_menu() 
