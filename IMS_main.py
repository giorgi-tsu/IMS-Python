# Imports

import os
import csv
from datetime import datetime
import time

# Constant variables

db_main_path = os.path.join(os.getcwd(), "dbs/main_db.csv")


# Function definitions

def input_to_int(input_prompt):
    while True:
        input_string = input(input_prompt)
        try:
            input_int = int(input_string)
            return input_int
        except:
            continue

def input_to_float(input_prompt):
    while True:
        input_string = input(input_prompt)
        try:
            input_int = float(input_string)
            return input_int
        except:
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
        print("Window: Home \nAvailable Buttons: ",
          "[quit] [search]")
        window_home_input = input("Enter button name: ").lower()
        if window_home_input == "quit":
            log.close(str(datetime.now())[:-7])
            break
        elif window_home_input == "search":
            window_search(log, db)
        else:
            continue


def window_search(log, db):
    while True:
        print("Window: Search \nAvailable Buttons: [home]",
              "[search box]")
        window_search_input = input("Enter button name: ").lower()
        if window_search_input == "home":
            break
        elif window_search_input == "search box":
            search_box(log, db)
        else:
            continue
            
def search_box(log, db):
    while True:
        print("Search Box")
        search_box_input = input("Enter text (Enter [close] "
                                 "to close Search Box): ").lower()
        if search_box_input == "close":
            break
        else:
            item = db.search(search_box_input)
            if item:
                item = Item(item)
                window_item(item)
            else:
                continue
                    
def window_item(item):
    while True:
        print(f"Window {item.name_ENG}",
              "\nAvailable Buttons: [close] [sell] "
              "[return] [add to storage]")    
        item_window_input = input("Enter button name: ")
        if item_window_input == "close":
            break
        elif item_window_input == "sell":
            window_item_sell(item)
        elif item_window_input == "return":
            print("Need to add return method")
        elif item_window_input == "add to storage":
            print("need to add add to storage method")
        else:
            continue


def window_item_sell(item):
    window_item_sell = True
    while window_item_sell:
        print(f"Window {item.name_ENG}/Sell",
              f"\nUnit: {item.item_dict["unit"]}"
              f"\nPrice per unit: {item.item_dict["price"]}"
              "\nAvailable Buttons: [close]")
        quantity = input_to_int("Enter quantity: ")
        unit_price = input_to_float("Enter unit price: ")
        while True:
            check = input("Is this correct?\n"
                        f"Name_ENG: {item.name_ENG}; "
                        f"Price per unit: {unit_price}; "
                        f"Quantity: {quantity}; "
                        f"Total Price: {quantity * unit_price}; \n"
                        "If YES: enter [Y]\n"
                        "If NO: enter [N]\n"
                        "Enter your response here: ").lower()
            if check == "y":
                item.sell(quantity, unit_price)
                window_item_sell = False
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
            self.item_dict["price"] = price
            self.item_dict["bar_code"] = bar_code
            self.item_dict["item_id"] = item_id

        else:
            self.name_ENG = input_dict["name_ENG"]
            self.name_GEO = input_dict["name_GEO"]
            self.item_dict = input_dict
    
    def sell(self, quantity, unit_price):
        
        self.item_dict["quantity"] -= quantity
        print(self.item_dict["quantity"])

class DataBase:
    
    def __init__(self, path):
        self.list= []
        try:
            with open(path, "r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    self.list.append(row)
        except:
            with open(path, "w"):
                pass

    def search(self, input_text):
        for item in self.list:
            if item["name_ENG"].lower() == input_text:
                return item
        else:
            print(f"{input_text} is not in the Storage")


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
        print("Log has been closed!")



# Main loop
create_directories()

log_main = Log(str(datetime.now())[:-7])

db_main = DataBase(db_main_path)

window_home(log=log_main, db=db_main)