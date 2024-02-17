def input_to_int(input_prompt):
    while True:
        input_string = input(input_prompt)
        try:
            input_int = int(input_string)
            return input_int
        except:
            continue

quantity = input_to_int("Enter quantity: ")

print(quantity)