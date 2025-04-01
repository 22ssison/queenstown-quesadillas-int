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
            print("Invalid input. Please enter a number.")


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
    print(user_info) # test


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
    option = input("Would you like to \n1) pick up \n2) delivery\n\n> ").strip().lower()
    if option == "1":
        pick_up_user_info()
    elif option == "2":
        delivery_user_info()


def quesadillas_menu():
    """This function displays all the available quesadillas with a price and a description."""
    count = 0 # to keep count of how many elements three are in the list.
    for quesadilla in quesadillas:
        count += 1 # adds 1 to count 
        print()
        print(f"{count}) {quesadilla[0]} - ${quesadilla[2]}\n{quesadilla[1]}")
        

def main():
    pass
    # view quesadilla menu (function)
    # view bevarage menu (function)
    # add option(s) to cart: (function)


if __name__ == "__main__": # python convention, anything under this  is ran only in this page.
    quesadillas_menu() 
