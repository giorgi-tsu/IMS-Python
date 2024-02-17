# Importing Libraries

import os
import csv
from datetime import datetime
import time

# Setting up a directory structure

# If the program is running for the first time, it creates all
# necessary directories.

# This folder contains all database files.

# There is one main database "db_main" that keeps the stock of items.

try:
    os.mkdir(r".\dbs")
except:
    print("Directory dbs already exists!")

# This folder contains all log files.

try:
    os.mkdir(r".\logs")
except:
    print("Directory logs already exists!")

# Declaring necessary classes

class Item:

    fieldnames = ["name_ENG", "name_GEO", "unit", "quantity",
                  "price", "bar_code", "item_id"]
    
    def __init__(self, input_dict="", name_ENG="", name_GEO="", 
                 unit="", quantity="", price="", bar_code="",
                 item_id=""):

        if input_dict == "":
            self.item_dict = {}
            self.item_dict["name_ENG"] = name_ENG
            self.item_dict["name_GEO"] = name_GEO
            self.item_dict["unit"] = unit
            self.item_dict["quantity"] = quantity
            self.item_dict["price"] = price
            self.item_dict["bar_code"] = bar_code
            self.item_dict["item_id"] = item_id

        else:
            self.name_ENG = input_dict["name_ENG"]
            self.name_GEO = input_dict["name_GEO"]
            self.item_dict = input_dict
    
    # def add_to_db(self):
    #     if (any(list(self.item_dict.values()))):
    #         db.append(self.item_dict)
    #     else:
    #         self.item_dict["name_ENG"] = input("name_ENG: ")
    #         self.item_dict["name_GEO"] = input("name_GEO: ")
    #         self.item_dict["unit"] = input("unit: ")
    #         self.item_dict["quantity"] = input("quantity: ")
    #         self.item_dict["price"] = input("price: ")
    #         self.item_dict["bar_code"] = input("bar_code: ")
    #         self.item_dict["item_id"] = input("item_id: ")
    #         db.append(self.item_dict)

# Declaring DataBase class

class DataBase:
    
    def __init__(self, path):
        self.list= []
        try:
            with open(path, "r") as csv_file:
                csv_reader = csv.DictReader(csv_file)

                for row in csv_reader:
                    self.list.append(row)
        except:
            with open(path, "w") as csv_file:
                pass

    def search(self, input_text):
        for item in self.list:
            if item["name_ENG"].lower() == input_text:
                return item
        else:
            print(f"{input_text} is not in the Storage")
            
# Declaring Log class

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

# Loading the database

# with open(r".\dbs\main_db.csv", "w", newline="") as csv_file:
#     csv_writer = csv.DictWriter(csv_file, fieldnames=Item.fieldnames)
#     csv_writer.writeheader()
#     csv_writer.writerows(db)


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
                window_item(item)
            else:
                continue
                    
def window_item(item):
    while True:
        print(f"Window {item.name_ENG}",
              "\nAvailable Buttons: [close] [sell]"
              "[return] [add to storage]")    
        item_window_input = input("Enter button name: ")
        if item_window_input == "close":
            break
        elif item_window_input == "sell":
            print("Need to add sell method")
        elif item_window_input == "return":
            print("Need to add return method")
        elif item_window_input == "add to storage":
            print("need to add add to storage method")
        else:
            continue

# Main loop

log_main = Log(str(datetime.now())[:-7])
db_main_path = os.path.join(os.getcwd(), "dbs\main_db.csv")
db_main = DataBase(db_main_path)

window_home(log=log_main, db=db_main)