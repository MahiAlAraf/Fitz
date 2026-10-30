import tools
import random
import Data
from Content_data import get_content_List, add_limit
from search_fitz import show_picked


def get_fitz():
    scoreboard = Data.scoreboard()
    Type = choose_type()
    # ------------------------------------for movies questions---------------------------------
    if Type == "movie":
        random.shuffle(Data.Questions_movie)
        for question in Data.Questions_movie:
            tools.clear_screen()
            said_yes = tools.confirm(question["text"])
            if said_yes:
                add_points(scoreboard, question["yes"])
            else:
                add_points(scoreboard, question["no"])
    # -------------------------------------for tv series---------------------------------------
    else:
        random.shuffle(Data.Questions_tv)
        for question in Data.Questions_tv:
            tools.clear_screen()
            said_yes = tools.confirm(question["text"])
            if said_yes:
                add_points(scoreboard, question["yes"])
            else:
                add_points(scoreboard, question["no"])

    content_list = get_content_List(top_genre(scoreboard), Type)

    if not content_list:
        print("No titles found for your genres.")

    elif content_list == "listFailed":
        print("Error occerd while fetching Movies")

    elif content_list == "gerneFaied":
        print("Error occerd while fetching the genres")
    else:
        while True:
            tools.clear_screen()
            for serial, content in content_list.items():
                print(f"[{serial}] {content['title']}")

            print("-------------------------------------------")
            print("To get Details \n Enter the Serial number")
            print("Or Press Enter to return:")
            details = see_details(content_list)
            if details is None:
                break
            show_picked(details)
            tools.enter_to_continue()


def choose_type():
    tools.clear_screen()
    print("+================+")
    print("| [1] Web series | ")
    print("| [2] Movie      |")
    print("+================+")
    choice = tools.choice(low=1, high=2)
    if choice == 1:
        return "tv"
    return "movie"


def see_details(content_dict):
    while True:
        choice = input("-> ").strip()
        if not choice:
            return None  # Enter = go back

        if not choice.isdigit():
            print("Invalid input: enter a number.")
            continue

        choice = int(choice)
        if choice in content_dict:  # keys are 1..N, however many results came back
            return content_dict[choice]  # the whole item: id, type, title

        print(f"Invalid input: enter a number from 1 to {len(content_dict)}.")


def add_points(scoreboard, points):
    for genre, point in points.items():
        scoreboard[genre] += point


def top_genre(scoreboard):
    ranked_genres = sorted(scoreboard.items(), key=lambda x: x[1], reverse=True)
    top = []
    for genre, score in ranked_genres:
        if score > 0:
            top.append(genre)
    return top[0], top[1]


if __name__ == "__main__":
    tools.clear_screen()
    print("===================================")
    print(get_fitz())
    print("===================================")
