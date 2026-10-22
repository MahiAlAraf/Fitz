import csv
import os
import re

PROFILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "profiles.csv")
PROFILE_FIELDS = ["name", "age", "email"]

MIN_AGE = 1
MAX_AGE = 120
MAX_NAME_LENGTH = 50

# Email rule: something@domain.tld
# The domain part needs at least one dot, so "a@b" is rejected.
EMAIL_PATTERN = re.compile(
    r"[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@"
    r"[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
    r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+"
)



def clear_screen():
    # Executes 'cls' on Windows, 'clear' on Linux and Mac
    os.system("cls" if os.name == "nt" else "clear")


def choice(low, high):
    """Keep asking until the user types a whole number from low to high."""
    while True:
        try:
            user_input = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if low <= user_input <= high:
            return user_input
        print(f"Please enter a number between {low} and {high}.")


def enter_to_continue(name=""):
    print()
    input(f"Press Enter to continue {name}...")


def confirm(question):
    """Ask a yes/no question. Anything except 'y' or 'yes' counts as no."""
    while True:
        print("=====================================================")
        answer = input(f"{question} [y/N]: ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Invalid input. Please enter 'y' or 'n'.")


def ask_name():
    while True:
        name = input("Enter your name: ").strip()

        if name == "":
            print("Name cannot be empty. Please try again.")
        elif len(name) > MAX_NAME_LENGTH:
            print(f"Name is too long (max {MAX_NAME_LENGTH} characters). Please try again.")
        else:
            return name


def ask_age():
    while True:
        age_text = input("Enter your age: ").strip()

        try:
            age = int(age_text)
        except ValueError:
            print("Invalid age. Please try again.")
            continue

        if MIN_AGE <= age <= MAX_AGE:
            return age
        print(f"Age must be between {MIN_AGE} and {MAX_AGE}. Please try again.")


def ask_email():
    while True:
        email = input("Enter your email: ").strip()

        if EMAIL_PATTERN.fullmatch(email):
            return email
        print("Invalid email format. Please try again.")



def save_profile(name, age, email):
    
    with open(PROFILE_PATH, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=PROFILE_FIELDS)
        writer.writeheader()
        writer.writerow({"name": name, "age": age, "email": email})


def load_profile():

    if not os.path.exists(PROFILE_PATH):
        return None

    try:
        with open(PROFILE_PATH, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            row = next(reader, None)   # None when the file has no data row
    except (OSError, UnicodeDecodeError, csv.Error):
        return None

    if row is None:
        return None

    # Every field must be present and filled in.
    for field in PROFILE_FIELDS:
        if not row.get(field):
            return None

  
    try:
        row["age"] = int(row["age"])
    except ValueError:
        return None

    return row


def delete_profile():
    if os.path.exists(PROFILE_PATH):
        os.remove(PROFILE_PATH)
