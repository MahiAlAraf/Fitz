from Content_data import api_key
import tools
import requests
import chatbot


def search_fitz():
    """User typed a name: correct it, find the id, then show the review."""
    tools.clear_screen()
    user_search = input("\n Search your fitz: ").strip()
    if not user_search:
        print("Nothing typed.")
        return

    corrected = chatbot.Check_title(user_search)
    if corrected.lower() == "unknown":
        print("Sorry: title not found")
        return
    if corrected.lower() != user_search.lower():
        print(f"Loading results for {corrected}.....")

    try:
        Media_ID, Type = fetch_id(corrected)
    except ValueError:
        print("Could not find that title. Try again.")
        return

    show_review(Media_ID, Type, corrected)


def show_picked(item):
    """User picked from the list: we already know the id, so skip Gemini and fetch_id."""
    show_review(item["id"], item["type"], item["title"])


def show_review(Media_ID, Type, Title):
    key = (Type, Media_ID)
    
    records = tools.get_records()
    if key in records:
        responce = records[key]
    else:
        try:
            Age_rating, Genres, Overview, Keywords, Poster_url,Backdrop_url = fetch_details(Media_ID, Type)
        except ValueError:
            print("Failed to load details")
            return

        responce = chatbot.Unique_message(Title, Age_rating, Genres, Overview, Keywords)
        if not responce:
            print("The AI could not write a review for this title.")
            return
        tools.save_record(key, responce,Poster_url,Backdrop_url)

    tools.clear_screen()
    print(f"Ai generated responce:\n{Title}")
    print("=" * 80)
    print(responce)
    print("=" * 80)
    print("[1] Mark as watched")
    print("[enter] to return to the menu")
    tools.mark_watched(Type, Media_ID, Title)


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
        
    # --------------------------Poster and Backdrop--------------------------
    IMAGE_BASE_URL = "https://image.tmdb.org/t/p"

    Poster_path = Data.get("poster_path")
    Backdrop_path = Data.get("backdrop_path")

    if Poster_path is None:
        Poster_url = None
    else:
        Poster_url = IMAGE_BASE_URL + "/w500" + Poster_path

    if Backdrop_path is None:
        Backdrop_url = None
    else:
        Backdrop_url = IMAGE_BASE_URL + "/original" + Backdrop_path

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

    return Age_rating, Genres, Overview, Keywords, Poster_url,Backdrop_url


if __name__ == "__main__":
    search_fitz()
