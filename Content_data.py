import os
import requests

api_key = os.environ.get("TMDB_API_KEY")

add_limit = 10


def create_gernes_id(TYPE):

    gernes_id = {}
    url = f"https://api.themoviedb.org/3/genre/{TYPE}/list?api_key={api_key}"
    data = responce(URL=url)
    if not data:
        return "gerneFaied"

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
    url_2 = f"https://api.themoviedb.org/3/discover/{Type}?api_key={api_key}&with_genres={top_genre_id}|{second_genre_id}&sort_by=popularity.desc&vote_count.gte=200"

    # url 1 works if both genres must be present
    # url 2 works if any grenes are present

    content_data = responce(URL=url)  # AND query first
    if content_data is None:
        return "listFailed"

    extra_data = None
    if len(content_data.get("results", [])) < 5:  # includes 0 results
        extra_data = responce(URL=url_2)  # OR query; stays None if it failed

    return ContentList_Dict(content_data, Type, extra_data)

def get_title(item, TYPE):
    if TYPE == "tv":
        return item["name"]
    return item["title"]


def ContentList_Dict(Main_data_package, TYPE, Sub_Package=None):
    content_info = {}
    seen_ids = set()  # ids already in the list
    slot = 1  # next free number in the list

    # 1) best matches first: titles that have BOTH genres
    for item in Main_data_package.get("results", []):
        if slot > add_limit:
            break
        content_info[slot] = {
            "id": item["id"],
            "type": TYPE,
            "title": get_title(item, TYPE),
        }
        seen_ids.add(item["id"])
        slot += 1

    # 2) fill the remaining slots from the OR results, skipping duplicates
    if Sub_Package:
        for item in Sub_Package.get("results", []):
            if slot > add_limit:
                break
            if item["id"] in seen_ids:
                continue  # already listed, do not use a slot
            content_info[slot] = {
                "id": item["id"],
                "type": TYPE,
                "title": get_title(item, TYPE),
            }
            seen_ids.add(item["id"])
            slot += 1

    return content_info


def responce(URL):
    try:
        content_responce = requests.get(URL, timeout=10)
        return content_responce.json()
    except (requests.exceptions.RequestException, ValueError):
        return None  # network error OR response was not valid JSON


def main():
    for gernes, id in create_gernes_id().items():
        print(f"{gernes}: {id}")
    List = get_content_List()
    for item in List:
        print(item)


if __name__ == "__main__":
    main()
