import sys
import os
import random
import cowsay
import tools
from search_fitz import search_fitz
from get_fitz import get_fitz

def main():
    while True:
        tools.clear_screen()
        
        if not os.path.exists("profiles.txt"):
            tools.clear_screen()
            create_profile()
        greetings()   
        if not show_manu():
            sys.exit("Exiting the program. Goodbye!")
        else:
            continue
        
def create_profile():
    print("Welcome !")
    print("==================================")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = tools.validate_email(input("Enter your email: "))
    tools.clear_screen()
    print("==================================")
    print(f"\nProfile Created:\nName: {name}\nAge: {age}\nEmail: {email}\n")
    print("==================================")
    save_profile(name, age, email)
    tools.enter_toContinue(name=name)
    
def show_manu():
    while True:
        tools.clear_screen()
        print("+--------------------------------------+")
        print("|         [1] Search your Fitz         |")
        print("|         [2] Get your Fitz            |")
        print("|         [3] Show profile             |")
        print("|         [4] Exit                     |")
        print("+--------------------------------------+")
        user_choice = tools.choice(1, 4)
        if user_choice == 1:
            print("Searching your Fitz...")
            search_fitz()
        elif user_choice == 2:
            print("Getting your Fitz...")
            get_fitz()
        elif user_choice == 3:
            if show_profile() == "pDeleted":
                return "_"
        elif user_choice == 4:
            return None
        ...
def save_profile(name, age, email):
    with open("profiles.txt", "w") as file:
        file.write(f"Name: {name}, Age: {age}, Email: {email}\n")
    
def greetings():
    with open("profiles.txt","r") as file:
        content = file.read()
        Name = content.split(",")[0].split(":")[1].strip()
        
    animals = [
    "cow", "daemon", "dragon", "fox", "ghostbusters", 
    "kitty", "meow", "miki", "octopus", "stegosaurus", 
    "stimpy", "trex", "turkey", "turtle", "tux"
    ]
    selected_animal = random.choice(animals)   
    print(cowsay.get_output_string(selected_animal, f"Hello {Name}!"))
    tools.enter_toContinue(name=Name)
            
def show_profile():
    tools.clear_screen()
    with open("profiles.txt","r") as file:
        contant = file.readline()
        print("===================================")
        print("Name", contant.split(",")[0].split(":")[1].strip())
        print("Age", contant.split(",")[1].split(":")[1].strip())
        print("Email", contant.split(",")[2].split(":")[1].strip())
        print("===================================")
        
    print("[1] to DELETE profile")
    print("enter to go back to main menu")
        
    if input() == "1":
        tools.profile_reset()
        tools.enter_toContinue()
        return "pDeleted"
    else:
         return None
        
        
        
if __name__ == "__main__":
    main()