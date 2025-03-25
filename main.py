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

user_info = []
user_cart = []

# functions
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
    print()
    print("Customer Details:")
    print()
    first_name = input("First Name: ")
    print()
    address = input("Address: ")
    print()
    phone_number = input("Phone Number: ")
    user_info.append(first_name, address, phone_number)
    print()
    print("Details Saved.")

def pick_up_user_info():
    print()
    print("Customer Details:")
    print()
    first_name = input("First Name: ")
    print()
    user_info.append(first_name)
    print()
    print("Details Saved.")