import tools
import random
import Data
from Content_data import get_content_List, add_limit
from search_fitz import search_fitz


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
                print(f"[{serial}] {content}")

            print("-------------------------------------------")
            print("To get Details \n Enter the Serial number")
            print("Or Press Enter to return:")
            decision = see_details(content_list)
            if not decision:
                break
            if search_fitz(user_search=decision):
                print(
                    " Sorry: title not found"
                )  # ---> search fitz only returns a vlaue if a title is not found
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


def see_details(movie_dict):
    while True:
        choice = input("-> ")
        if not choice:
            return False
        choice = int(choice)
        if 1 <= choice <= add_limit:  # from content_data
            break
        print("Invalid input: try again.. ")
    for serial, content in movie_dict.items():
        if choice == int(serial):
            return content.lower()


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
