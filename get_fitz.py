import tools
import random   
import Data
from Content_data import get_movies_List
def get_fitz():
    scorebord = Data.scoreboard_Dict()
    random.shuffle(Data.Questions)
    for question in Data.Questions:
        tools.clear_screen()
        said_yes = tools.confirm(question["text"])
        if said_yes:
            add_points(scorebord, question["yes"])
        else:
            add_points(scorebord, question["no"])
    Movie_list = get_movies_List(top_genre(scorebord))
    if not Movie_list:
        print("No titles found for your genres.")
            
    elif Movie_list == "listFailed":
        print("Error occerd while fetching Movies")
        
    elif Movie_list == "gerneFaied":
        print("Error occerd while fetching the genres")
    else:   
        for movie in Movie_list:
                print(movie)    
     
     
def add_points(scoreboard, points):
     for genre, point in points.items():
          scoreboard[genre] += point
          
def top_genre(scoreboard):
     ranked_genres = sorted(scoreboard.items(), key=lambda x: x[1], reverse=True)
     top = []
     for genre, score in ranked_genres:
          if score> 0:
               top.append(genre)
     return top[0], top[1]
          
if __name__ == "__main__":
    tools.clear_screen()
    print("===================================")
    print(           get_fitz())
    print("===================================")