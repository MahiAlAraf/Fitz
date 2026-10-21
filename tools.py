
import os
import re
def clear_screen(): 
    # Executes 'cls' on Windows, 'clear' on Linux and Mac
    os.system('cls' if os.name == 'nt' else 'clear')
    
def choice(min, max):
    while True:
        try:
            user_input = int(input("Enter your choice: "))
            if min <= user_input <= max:
                return user_input
            else:
                print(f"Please enter a number between {min} and {max}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def validate_email(email):
    pattertn =(
        r"^[a-zA-Z0-9.!#\$%&'*+\/=?^_`{|}~-]+@"
        r"[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
        r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
    )
    if re.match(pattertn, email):
        return email
    else:
        print("Invalid email format. Please try again.")
        return validate_email(input("Enter your email: "))
    
def enter_toContinue(name=""):
    print()
    input(f"Press Enter to continue {name}...")
def profile_reset():
    if os.path.exists("profiles.txt"):
        os.remove("profiles.txt")