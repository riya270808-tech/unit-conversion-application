from menu import show_menu
from conversions import convert
from validation import get_number
from output import show_result

while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Thank you for using the application!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice!")
        continue

    value = get_number()
    result = convert(choice, value)

    show_result(result)
