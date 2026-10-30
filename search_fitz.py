from Content_data import api_key
from Data import raw_review
import tools
import requests
import chatbot


def search_fitz(user_search=""):

    tools.clear_screen()
    if not user_search:
        user_search = input("\n Search you fitz :").strip()
    corrected = chatbot.Check_title(user_search).lower()
    if corrected == "unknown":
        return "_"  # title not foud my ai
    if user_search != corrected:
        print(f"showing results for {corrected}")

    if not corrected in raw_review:
        responce = Ai_responce(corrected)
        if responce == "error":
            print("Could not find that title. Try again.")
            return "error"
        raw_review[corrected] = responce
    else:
        responce = raw_review[corrected]
    tools.clear_screen()
    print(f"Ai generated responce:            \n{corrected.title()}")
    print("================================================================================")
    print(responce)
    print( "==================================================================================")


def Ai_responce(Title):
    try:
        Media_ID, Type = fetch_id(Title)
    except ValueError:
        return "error"
    try:
        Age_rating, Genres, Overview, Keywords = fetch_details(Media_ID, Type)
    except ValueError:
        return "error"

    # TEMPORARY: shows the real data until Gemini is connected
    return chatbot.Unique_message(Title, Age_rating, Genres, Overview, Keywords)


def fetch_id(Title):
    url = "https://api.themoviedb.org/3/search/multi"
    params = {"query": Title, "api_key": api_key}  # requests encodes spaces for us

    try:
        responce = requests.get(url, params=params, timeout=10)
        responce.raise_for_status()  # errors on 401, 404, 500...
    except requests.exceptions.RequestException:
        raise ValueError("Network or TMDB error in fetch_id")

    data = responce.json()

    for item in data["results"]:
        if item["media_type"] == "movie" or item["media_type"] == "tv":
            return item["id"], item["media_type"]

    raise ValueError("No movie or series found")


def fetch_details(ID, Type):
    if Type == "tv":
        rating_section = "content_ratings"
        path = "results"
    else:
        rating_section = "release_dates"
        path = "keywords"
    url = f"https://api.themoviedb.org/3/{Type}/{ID}"
    params = {"api_key": api_key, "append_to_response": f"keywords,{rating_section}"}

    try:
        responce = requests.get(url, params=params, timeout=10)
        responce.raise_for_status()
    except requests.exceptions.RequestException:
        raise ValueError("Network or TMDB error in fetch_details")

    # ---------------------------Overview---------------------------------
    Data = responce.json()
    Overview = Data.get("overview", "")
    if Overview == "":
        Overview = "No overview available"

    # ---------------------------get genre------------------
    Genres = []
    for genre in Data.get("genres", []):
        Genres.append(genre["name"])

    # ---------- Keywords: list of dicts -> list of names ---------
    Keywords = []

    keyword_list = Data.get("keywords", {}).get(path, [])
    for keyword in keyword_list:
        Keywords.append(keyword["name"])

    # ---------- Age rating ----------
    Age_rating = "Unknown"  # default value
    rating_list = Data.get(rating_section, {}).get("results", [])

    for country in rating_list:
        if country["iso_3166_1"] != "US":
            continue  # not the US entry, check the next country

        if Type == "tv":
            # TV: the rating sits directly on the country entry
            if country["rating"] != "":
                Age_rating = country["rating"]
        else:
            # Movie: one level deeper, a list of releases
            for release in country["release_dates"]:
                if release["certification"] != "":
                    Age_rating = release["certification"]
                    break  # first non-empty certification is enough
        break  # US found, stop looking at other countries

    return Age_rating, Genres, Overview, Keywords


if __name__ == "__main__":
    search_fitz()
