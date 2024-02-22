# Imports

import os
import csv
from datetime import datetime
import time


# Constant variables

db_main_path = os.path.join(os.getcwd(), "dbs/main_db.csv")



# Function definitions

def input_to_int(input_prompt):
    """
    Convert user input to an integer.

    This function repeatedly prompts a user for input using 
    the given input prompt until the user enters a valid integer. 
    If the user enters an empty string, an empty string is returned.
    If the user enters a non-integer value, the function
    continues to prompt the user until a valid integer is entered.

    Parameters:
    input_prompt (str): The prompt to display to the user.

    Returns:
    int or str: The integer value entered by the user, 
    or an empty string if the user entered an empty string.
    
    """
    while True:
        input_string = input(input_prompt)
        if input_string == "":
            return ""
        try:
            input_int = int(input_string)
            return input_int
        except ValueError:
            continue


def input_to_float(input_prompt):
    """
    Convert user input to a float.

    This function repeatedly prompts the user for input using
    the given input prompt until the user enters a valid float.
    If the user enters an empty string, an empty string is returned.
    If the user enters a non-float value, the function continues 
    to prompt the user until a valid float is entered.

    Parameters:
    input_prompt (str): The prompt to display to the user.

    Returns:
    float or str: The float value entered by the user,
    or an empty string if the user entered an empty string.
    
    """
    while True:
        input_string = input(input_prompt)
        if input_string == "":
            return ""
        try:
            input_float = float(input_string)
            return input_float
        except ValueError:
            continue


def create_directories():
    if not os.path.exists("./dbs"):
        os.mkdir("./dbs")
        print("Directory dbs created.")
    else:
        print("Directory dbs already exists!")

    if not os.path.exists("./logs"):
        os.mkdir("./logs")
        print("Directory logs created.")
    else:
        print("Directory logs already exists!")


def window_home(log, db):
    while True:
        print("Window Name: Home \nAvailable Buttons: ",
          "[0. quit] [1. search]")
        window_home_input = input("Enter button name\\"
                                  "number: ").lower()
        if window_home_input == "quit" or\
        window_home_input == "0":
            log.close(str(datetime.now())[:-7])
            break
        elif window_home_input == "search" or\
            window_home_input == "1":
            window_search(log, db)
        else:
            continue


def window_search(log, db):
    while True:
        print("Window Name: Search \nAvailable Buttons: [0. home]",
              "[1. search box] [2. add new product]")
        window_search_input = input("Enter button name\\number: ")\
            .lower()
        if window_search_input == "home" or\
            window_search_input == "0":
            break
        elif window_search_input == "search box" or\
            window_search_input == "1":
            search_box(log, db)
        elif window_search_input == "add new product" or\
            window_search_input == "2":
            add_new_product(log, db)
        else:
            continue


def search_box(log, db):
    while True:
        print("Search Box")
        search_box_input = input("Enter text (Enter [0. close] "
                                 "to close Search Box): ").lower()
        if search_box_input == "close" or\
            search_box_input == "0":
            break
        else:
            item = db.search(search_box_input)
            if item:
                item = Item(item)
                window_item(item)
            else:
                continue


def add_new_product(log, db):
    window_add_new_product = True
    while window_add_new_product:
        print(f"Window Name: Add New Product\n" 
              "Enter Product Details Below "
              "Enter [0. close] to close window ") 
        while True:
            print("Entering New Product Details (Enter [0. close] "
                  "to go back to search window...)")
            new_item = {}
            new_item["name_ENG"] = input("Enter name_ENG: ")
            if new_item["name_ENG"] == "close" or\
                new_item["name_ENG"] == "0":
                window_add_new_product = False
                break
            new_item["name_GEO"] = input("Enter name_GEO: ")
            if new_item["name_GEO"] == "close" or\
                new_item["name_GEO"] == "0":
                window_add_new_product = False
                break
            new_item["unit"] = input("Enter unit: ")
            if new_item["unit"] == "close" or\
                new_item["unit"] == "0":
                window_add_new_product = False
                break
            while True:
                new_item["quantity"] = input_to_int("Enter "
                                                    "quantity: ")
                if new_item["quantity"] != "":
                    break
                else:
                    continue
            while True:
                new_item["price"] = input_to_float("Enter price: ")
                if new_item["price"] !="":
                    break
                else:
                    continue
            new_item["bar_code"] = input("Enter bar code: ")
            if new_item["bar_code"] == "close" or\
                new_item["bar_code"] == "0":
                window_add_new_product = False
                break
            new_item["item_id"] = input("Enter item_id: ")
            if new_item["bar_code"] == "close" or\
                new_item["bar_code"] == "0":
                window_add_new_product = False
                break
            check = input("Is this correct?\n"
                        f"Name_ENG: {new_item["name_ENG"]}; "
                        f"Name_GEO: {new_item["name_GEO"]}; "
                        f"Unit: {new_item["unit"]}; "
                        f"Quantity: {new_item["quantity"]}; "
                        f"Price per unit: {new_item["price"]}; "
                        f"Bar Code: {new_item["bar_code"]}; "
                        f"Item ID: {new_item["item_id"]}; \n"
                        "If YES: enter [Y]\n"
                        "If NO: enter [N]\n"
                        "Enter your response here: ").lower()
            if check == "y":
                db.db_list.append(new_item)
                print(f"{new_item["name_ENG"]}"
                    " has been added to the database!")         
                break
            elif check == "n":
                continue
            else:
                continue

                    
def window_item(item):
    while True:
        print(f"Window Name: {item.name_ENG}",
              f"\nUnit: {item.item_dict["unit"]}"
              f"\nAvailable Quantity: {item.item_dict["quantity"]}"
              f"\nPrice per unit: {item.item_dict["price"]}"
              "\nAvailable Buttons: [0. close] [1. sell] "
              "[2. refill] ")    
        item_window_input = input("Enter button name\\number: ")
        if item_window_input == "close" or\
            item_window_input == "0":
            break
        elif item_window_input == "sell" or\
            item_window_input == "1":
            window_item_sell(item)
        elif item_window_input == "refill" or\
            item_window_input == "2":
            window_item_refill(item)
        else:
            continue


def window_item_sell(item):
    window_item_sell = True
    
    while window_item_sell:
        print(f"Window Name: {item.name_ENG}/Sell",
              f"\nName_GEO: {item.name_ENG}"
              f"\nUnit: {item.item_dict["unit"]}"
              f"\nAvailable Quantity: {item.item_dict["quantity"]}"
              f"\nPrice per unit: {item.item_dict["price"]}"
              "\nAvailable Buttons: [close]")
        while True:
            quantity = input_to_int("Enter quantity: ")
            if quantity != "":
                break
        unit_price = input_to_float("Enter new price "
                    "or press [Enter]: ")
        if unit_price == "":
            unit_price = item.item_dict["price"]
    
        while True:
            check = input("Is this correct?\n"
                        f"Name_ENG: {item.name_ENG}; "
                        f"Name_GEO: {item.name_GEO}; "
                        f"Price per unit: {unit_price}; "
                        f"Quantity: {quantity}; "
                        f"Total Price: {quantity * unit_price}; \n"
                        "If YES: enter [Y]\n"
                        "If NO: enter [N]\n"
                        "Enter your response here: ").lower()
            if check == "y":
                result = item.sell(quantity, unit_price)
                if result == "sold":
                    window_item_sell = False
                break
            elif check == "n":
                break
            else:
                continue


def window_item_refill(item):
    window_item_refill = True
    
    while window_item_refill:
        print(f"Window Name: {item.name_ENG}/Refill",
              f"\nName_GEO: {item.name_ENG}"
              f"\nUnit: {item.item_dict["unit"]}"
              f"\nAvailable Quantity: {item.item_dict["quantity"]}"
              f"\nPrice per unit: {item.item_dict["price"]}"
              "\nAvailable Buttons: [close]")
        while True:
            quantity = input_to_int("Enter quantity: ")
            if quantity != "":
                break
        unit_price = input_to_float("Enter new price "
                    "or press [Enter]: ")
        if unit_price == "":
            unit_price = item.item_dict["price"]
    
        while True:
            check = input("Is this correct?\n"
                        f"Name_ENG: {item.name_ENG}; "
                        f"Name_GEO: {item.name_GEO}; "
                        f"Price per unit: {unit_price}; "
                        f"Quantity: {quantity}; \n"
                        "If YES: enter [Y]\n"
                        "If NO: enter [N]\n"
                        "Enter your response here: ").lower()
            if check == "y":
                result = item.refill(quantity, unit_price)
                if result == "refilled":
                    window_item_refill = False
                break
            elif check == "n":
                break
            else:
                continue

# Class definitions

class Item:
    fieldnames = ["name_ENG", "name_GEO", "unit", "quantity",
                  "price", "bar_code", "item_id"]
    
    def __init__(self, input_dict="", name_ENG="", name_GEO="", 
                 unit="", quantity="", price="", bar_code="",
                 item_id=""):

        if input_dict == "":
            self.name_ENG = name_ENG
            self.name_GEO = name_GEO
            self.item_dict = {}
            self.item_dict["name_ENG"] = name_ENG
            self.item_dict["name_GEO"] = name_GEO
            self.item_dict["unit"] = unit
            self.item_dict["quantity"] = int(quantity)
            self.item_dict["price"] = float(price)
            self.item_dict["bar_code"] = bar_code
            self.item_dict["item_id"] = item_id

        else:
            self.name_ENG = input_dict["name_ENG"]
            self.name_GEO = input_dict["name_GEO"]
            self.item_dict = input_dict
            self.item_dict["quantity"] =\
                int(self.item_dict["quantity"])
            self.item_dict["price"] =\
                float(self.item_dict["price"])
    

    def sell(self, quantity, unit_price):
        if quantity > self.item_dict["quantity"]:
            print("Quantity is not available!")
            return
        else:
            self.item_dict["quantity"] -= quantity
            return "sold"
    

    def refill(self, quantity, unit_price):
        self.item_dict["quantity"] += quantity
        return "refilled"

    
    def print(self):
        for key in self.item_dict:
            print(f"{key}: {self.item_dict[key]}")


class DataBase:
    
    """
    A simple database class for managing data stored in a CSV
    file.

    Parameters:
    - path (str): The file path to the CSV file.

    Attributes:
    - db_list (list): A list to store the data read from 
    the CSV file.
    - path (str): The file path to the CSV file.

    Methods:
    - __init()__(path): Initializes the database by reading data
    from the CSV file specified by the path.
    - search(input_text): Searches for a dictionary in the database
    where the "name_ENG" key mathces the input_text.
    - dump_to_csv(): Writes the contents (list of dictionaries
    referenced by db_list attribute) to the CSV file
    specified by the path. 
    """
    
    def __init__(self, path):
        self.db_list= []
        self.path = path
        try:
            with open(self.path, "r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    self.db_list.append(row)
        except:
            with open(self.path, "w"):
                pass


    def search(self, input_text):
        # item is a dictionary and the search methods
        # looks for the dictionary whose key (name_ENG)
        # has the desired value(input_text)
        for item in self.db_list:
            if item["name_ENG"].lower() == input_text:
                return item
        else:
            # If no item matches with input text, the method
            # returns None and prints the message below.
            print(f"{input_text} is not in the Storage")


    def add_to_db(self, input_dict):
        self.db_list.append(input_dict)


    def dump_to_csv(self):
        with open(self.path, "w", newline="") as csv_file:
            fieldnames = self.db_list[0].keys()
            csv_writer = csv.DictWriter(csv_file, fieldnames)

            csv_writer.writeheader()
            csv_writer.writerows(self.db_list)



class Log:

    def __init__(self, date_time):
        print("Log has been opened!")
        self.start_date = date_time.split()[0]
        self.start_time = "-".join(date_time.split()[1].split(":"))
        self.on = True
        self.list = []

    def close(self, date_time):
        self.on = False
        self.end_date = date_time.split()[0]
        self.end_time = "-".join(date_time.split()[1].split(":"))
        self.name = os.path.join(os.getcwd(),
        f"logs\log_{self.start_date}-{self.start_time}"
        f"_{self.end_date}-{self.end_time}")
        with open(self.name + ".csv", "w", newline="") as csv_file:
            fieldnames = []
            csv_writer = csv.DictWriter(csv_file, fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(self.list)
        db_main.dump_to_csv()
        print("Log has been closed!")



# Main loop
create_directories()

log_main = Log(str(datetime.now())[:-7])

db_main = DataBase(db_main_path)

window_home(log=log_main, db=db_main)