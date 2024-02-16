# Importing Libraries

import os
import csv
from datetime import datetime
import time

# Setting up a directory structure

# If the program is running for the first time, it creates all
# necessary directories.

# This folder contains all database files.

# There is one main database "main_db" that keeps the stock of items.

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

        self.item_window_on = True

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
            self.item_dict = {}
            for key in input_dict.keys():
                self.item_dict[key] = input_dict[key]
    
    def add_to_db(self):
        if (any(list(self.item_dict.values()))):
            db.append(self.item_dict)
        else:
            self.item_dict["name_ENG"] = input("name_ENG: ")
            self.item_dict["name_GEO"] = input("name_GEO: ")
            self.item_dict["unit"] = input("unit: ")
            self.item_dict["quantity"] = input("quantity: ")
            self.item_dict["price"] = input("price: ")
            self.item_dict["bar_code"] = input("bar_code: ")
            self.item_dict["item_id"] = input("item_id: ")
            db.append(self.item_dict)

# Declaring Log class

class Log:

    def __init__(self, date_time):
        print("Log has been opened!")
        self.start_date = date_time.split()[0]
        self.start_time = "-".join(date_time.split()[1].split(":"))
        self.on = True
        self.list = []
        self.search_window_on = True
    
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
    
try:
    print("try:")
    db = []
    with open(r".\dbs\main_db.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            db.append(row)
except:
    print("except:")
    db = []
    with open(r".\dbs\main_db.csv", "w") as csv_file:
        pass


for item in db:
    print(item)

# with open(r".\dbs\main_db.csv", "w", newline="") as csv_file:
#     csv_writer = csv.DictWriter(csv_file, fieldnames=Item.fieldnames)
#     csv_writer.writeheader()
#     csv_writer.writerows(db)

log = Log(str(datetime.now())[:-7])


while log.on:
    print("Window: Home \nAvailable Buttons: ",
          "[quit] [search]")
    home_window_input = input("Enter button name: ").lower()
    if home_window_input == "quit":
        log.close(str(datetime.now())[:-7])
    
    elif home_window_input == "search":
        search_window_on = True
        while search_window_on:
            print("Window: Search \nAvailable Buttons: [home]",
              "[search box]")
            search_window_input = \
                input("Enter button name: ").lower()
            if search_window_input == "home":
                search_window_on = False
            
            elif search_window_input == "search box":
                search_box_on = True
                while search_box_on:
                    print("Search Box")
                
                    search_box_input = input("Enter text: ")
                    if search_box_input == "stop":
                        search_box_on = False
        else:
            continue
    else:
        continue
        
        
        

    # elif home_window == "search":
    #     log.search_window_on = True

    #     while log.search_window_on:
    #         log.search(db_list)

    #     log.end_time = str(datetime.now())[:-7]

    # else:
    #     continue

    # print("log loop is complete")


# Saving Log to a csv file.






