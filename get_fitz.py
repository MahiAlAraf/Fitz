import tools
def make_scoreboard():
    return {
        "Comedy": 0,
        "Romance": 0,
        "Horror": 0,
        "Fantasy": 0,
    }
def get_fitz():
     scorebord = make_scoreboard()
     for question in Questions:
          said_yes = tools.confirm(question["text"])
          if said_yes:
               add_points(scorebord, question["yes"])
               ...
          else:
               add_points(scorebord, question["no"])
     return top_genre(scorebord)
     
     
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
          
Questions = [
    {
        "text": "Do you want to laugh tonight?",
        "yes": {"Comedy": 3, "Romance": 1},
        "no":  {"Horror": 1},
    },
    {
        "text": "Are you okay with scary scenes?",
        "yes": {"Horror": 3},
        "no":  {"Comedy": 1, "Romance": 1},
    },
    {
        "text": "Do you like magic or other worlds?",
        "yes": {"Fantasy": 3},
        "no":  {"Romance": 1},
    },
]
if __name__ == "__main__":
    print( get_fitz())