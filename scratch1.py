class Log:

    def __init__(self, start_time):
        self.start_time = start_time
        self.log_on = True
        self.log_list = []
        self.search_window_on = True
        

    def search(self, db_list, stop_search = None):
        print("Window: \"Search\" \n Available buttons: ",
              "\"home\"")
        self.search_name = input("Enter search\\button name: ").lower()

        if self.search_name == "home":
            self.search_window_on = False
            return
        else:
            self.db_list = db_list
            for index, item in enumerate(self.db_list):
                if item["name_ENG"] == self.search_name:

                    self.item = Item(item)
                    self.search_to_log(self.item)


                    while self.item.item_window_on:
                        print(f"Window: '{self.search_name}'")
                        print(f"Price: {self.item.item_dict['price']}, "
                              f"Quantity Left: {self.item.item_dict['quantity']}"
                              )
                        print(f"Available buttons: ",
                               "\"close\", \"sell\", \"return\", \"buy\"")

                        self.action_type = input("Enter button name: ")

                        if self.action_type == "close":
                            self.search_window_on = True  # back to "search" windows
                            self.item.item_window_on = False


                        elif self.action_type == "sell":
                            self.item = Item(item)
                            print("საინტერესოა შედარება: ",hex(id(self.item)))
                            self.sell_to_log(self.item)
                            self.db_list[index]["quantity"] -= self.sell_quantity

                    break
            else:
                print(f"{self.search_name} is NOT in the Storage!")
                self.search_window_on = True
        print("es satestoa")

    def sell_to_log(self, item):
        self.log_dict = item.item_dict
        print(f"Window {self.log_dict['name_ENG']}\\Sell \n",
              "Available buttons: \"close\"")

        while True:
            self.sell_price = input("Enter new price, or leave empty and press \"Enter\": ")

            if self.sell_price == "close" or self.sell_price == "":
                break
            try:
                self.sell_price = float(self.sell_price)
                break
            except:
                continue

        if self.sell_price == "close":
            return

        while True:
            self.sell_quantity = input("Enter quantity: ")

            if self.sell_quantity == "close":
                break
            try:
                self.sell_quantity = int(self.sell_quantity)
                break
            except:
                continue

        if self.sell_quantity == "close":
            return

        self.log_dict = item.item_dict
        self.log_dict["action_type"] = "sell"

        if self.sell_price == "":
            self.log_dict["sell_price"] = self.log_dict["price"]
        else:
            self.log_dict["sell_price"] = self.sell_price

        self.log_dict["sell_quantity"] = self.sell_quantity

        self.log_dict["log_time"] = str(datetime.now())[:-7] # ეს შვილობილ კლასში რომ გადავიდეს ჯობია.

        self.log_list.append(self.log_dict)



    def search_to_log(self, item):
        self.log_dict = item.item_dict
        self.log_dict["action_type"] = "search"
        self.log_dict["log_time"] = str(datetime.now())[:-7] # ეს შვილობილ კლასში რომ გადავიდეს ჯობია.
        self.log_list.append(self.log_dict)
