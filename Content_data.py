import os
import sys
import requests

api_key = os.environ.get("TMDB_API_KEY")

add_limit = 10


def create_gernes_id(TYPE):
    try:
        gernes_id_responce = requests.get(
            f"https://api.themoviedb.org/3/genre/{TYPE}/list?api_key={api_key}",
            timeout=10,
        )
    except requests.exceptions.RequestException:
        return "gerneFaied"

    gernes_id = {}
    data = gernes_id_responce.json()
    for genre in data.get("genres", []):
        gernes_id[genre["name"]] = genre["id"]
    return gernes_id


def get_content_List(genres_Tuple, Type):

    genres_idDict = create_gernes_id(TYPE=Type)
    if genres_idDict == "gerneFaied":
        return "gerneFaied"
    top_genre, second_genre = genres_Tuple
    top_genre_id = genres_idDict.get(top_genre)
    second_genre_id = genres_idDict.get(second_genre)
    url = f"https://api.themoviedb.org/3/discover/{Type}?api_key={api_key}&with_genres={top_genre_id},{second_genre_id}&sort_by=popularity.desc&vote_count.gte=200"
    try:
        movies_responce = requests.get(url, timeout=10)
    except requests.exceptions.RequestException:
        return "listFailed"

    moviesList_Dict = {}
    Movies_data = movies_responce.json()

    i = 1  # for listing.....
    for movies in Movies_data.get("results", []):
        if Type == "tv":
            moviesList_Dict[i] = movies["name"]
        else:
            moviesList_Dict[i] = movies["title"]
        if i == add_limit:
            break  # -----------------> add limit maximum responce 20 byt TMDB
        i += 1
    return moviesList_Dict


def main():
    for gernes, id in create_gernes_id().items():
        print(f"{gernes}: {id}")
    List = get_content_List()
    for item in List:
        print(item)


if __name__ == "__main__":
    main()
