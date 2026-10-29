import os
import sys
import requests

api_key = os.environ.get("TMDB_API_KEY")


def create_gernes_id():
    try:
        gernes_id_responce = requests.get(
            f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}",
            timeout=10,
        )
    except requests.exceptions.RequestException:
        return "gerneFaied"

    gernes_id = {}
    data = gernes_id_responce.json()
    for genre in data.get("genres", []):
        gernes_id[genre["name"]] = genre["id"]
    return gernes_id


def get_movies_List(genres_Tuple):

    genres_idDict = create_gernes_id()
    if genres_idDict == "gerneFaied":
        return "gerneFaied"
    top_genre, second_genre = genres_Tuple
    top_genre_id = genres_idDict.get(top_genre)
    second_genre_id = genres_idDict.get(second_genre)
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={top_genre_id},{second_genre_id}&sort_by=popularity.desc&vote_count.gte=200"
    try:
        movies_responce = requests.get(url, timeout=10)
    except requests.exceptions.RequestException:
        return "listFailed"

    movies_List = []
    Movies_data = movies_responce.json()
    for movies in Movies_data.get("results", []):
        movies_List.append(movies["title"])
    return movies_List


def main():
    for gernes, id in create_gernes_id().items():
        print(f"{gernes}: {id}")
    List = get_movies_List()
    for item in List:
        print(item)


if __name__ == "__main__":
    main()
