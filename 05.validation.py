def get_number():

    while True:
        try:
            value = float(input("Enter value: "))
            return value

        except ValueError:
            print("Please enter a valid number.")
