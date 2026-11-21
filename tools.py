import csv
import os
import re
from Data import Cache
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROFILE_PATH = os.path.join(BASE_DIR, "profiles.csv")
PROFILE_FIELDS = ["name", "age", "email"]
RECORDS_PATH = os.path.join(BASE_DIR, "records.csv")
MARKED_PATH = os.path.join(BASE_DIR, "marked.csv")
MIN_AGE = 1
MAX_AGE = 120
MAX_NAME_LENGTH = 50
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
            print(
                f"Name is too long (max {MAX_NAME_LENGTH} characters). Please try again."
            )
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
            row = next(reader, None)  # None when the file has no data row
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
        
    
def get_records():
    records = {}
    if not os.path.exists(RECORDS_PATH):
        return records
    try:
        with open(RECORDS_PATH, "r", newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                key = (row["type"], int(row["id"]))
                records[key] = row["response"]
    except (OSError, UnicodeDecodeError, csv.Error, KeyError, ValueError):
        return {}
    return records


def save_record(key, response,posterLink,backdropLink):
    """Append ONE new review (not the whole dict)."""
    Type, Media_ID = key
    Cache[key] = response
    file_exists = os.path.exists(RECORDS_PATH)
    with open(RECORDS_PATH, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["type", "id", "response","posterLink","backdropLink"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({"type": Type, "id": Media_ID, "response": response,"posterLink":posterLink,"backdropLink":backdropLink})


def watched_content():
    """Return a set of (type, id). Empty set if nothing marked yet."""
    watched = set()
    if not os.path.exists(MARKED_PATH):
        return watched
    try:
        with open(MARKED_PATH, "r", newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                watched.add((row["type"], int(row["id"])))
    except (OSError, UnicodeDecodeError, csv.Error, KeyError, ValueError):
        pass
    return watched


def mark_watched(Type, Media_ID, Title):
    choice = input("> ").strip()
    if choice != "1":                      # string compare
        return
    if (Type, Media_ID) in watched_content():
        print("Already marked as watched.")
        return

    file_exists = os.path.exists(MARKED_PATH)
    with open(MARKED_PATH, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["type", "id", "title"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({"type": Type, "id": Media_ID, "title": Title})
    print("Marked as watched.")