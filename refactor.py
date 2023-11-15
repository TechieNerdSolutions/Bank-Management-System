import os
from datetime import date

# Backend python functions code starts:

def is_valid(customer_account_number):
    try:
        customer_database = open("./database/Customer/customerDatabase.txt")
    except FileNotFoundError:
        os.makedirs("./database/Customer/customerDatabase.txt", exist_ok=True)
        print(
            "# Customer database doesn't exist!\n# New Customer database created automatically."
        )
        customer_database = open("./database/Customer/customerDatabase.txt", "a")
    else:
        if check_credentials(customer_account_number, "DO_NOT_CHECK", 2, True):
            return False
        else:
            return True
    finally:
        customer_database.close()

def check_leap(year):
    return ((int(year) % 4 == 0) and
            (int(year) % 100 != 0)) or (int(year) % 400 == 0)

def check_date(date_str):
    days_in_months = [
        "31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"
    ]
    days_in_months_in_leap_year = [
        "31", "29", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"
    ]

    if date_str == "":
        return False

    date_elements = date_str.split("/")
    day, month, year = map(int, date_elements)

    if (year > 2021 or year < 0) or (month > 12 or month < 1):
        return False
    else:
        if check_leap(year):
            num_of_days = days_in_months_in_leap_year[month - 1]
        else:
            num_of_days = days_in_months[month - 1]
        return int(num_of_days) >= day >= 1

def is_valid_mobile(mobile_number):
    if len(mobile_number) == 10 and mobile_number.isnumeric():
        return True
    else:
        return False

# Other backend functions remain the same.

# Backend python functions code ends.

# Example usage:
customer_account_number = input("Enter customer account number: ")
if is_valid(customer_account_number):
    print("Valid account number.")
else:
    print("Invalid account number.")
