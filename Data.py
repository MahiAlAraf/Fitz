def scoreboard ()
    return {
    # ---- movie genres (unchanged) ----
    "Comedy": 0,
    "Romance": 0,
    "Horror": 0,
    "Fantasy": 0,
    "Action": 0,
    "Adventure": 0,
    "Animation": 0,
    "Crime": 0,
    "Documentary": 0,
    "Drama": 0,
    "History": 0,
    "Mystery": 0,
    "Science Fiction": 0,
    "Thriller": 0,
    # ---- TV-only genres (names must match TMDB's TV genre list exactly) ----
    "Action & Adventure": 0,
    "Sci-Fi & Fantasy": 0,
    "War & Politics": 0,
    "Family": 0,
    "Reality": 0,
    "Soap": 0,
    "Western": 0,
}


Questions_movie = [
    {  # 1. Mood
        "text": "Do you want to feel happy and light-hearted right now?",
        "yes": {
            "Comedy": 3,
            "Animation": 2,
            "Romance": 1,
            "Adventure": 1,
            "Fantasy": 1,
        },
        "no": {"Drama": 1, "Thriller": 1, "Crime": 1, "Horror": 1},
    },
    {  # 2. Energy
        "text": "Do you have lots of energy and want fast, exciting scenes?",
        "yes": {"Action": 3, "Adventure": 2, "Thriller": 1, "Science Fiction": 1},
        "no": {"Drama": 1, "Romance": 1, "Documentary": 1, "Mystery": 1},
    },
    {  # 3. Fear tolerance
        "text": "Are you okay with feeling scared or tense?",
        "yes": {"Horror": 4, "Thriller": 2, "Mystery": 1, "Crime": 1},
        "no": {"Comedy": 1, "Animation": 1, "Romance": 1, "Fantasy": 1},
    },
    {  # 4. Reality vs imagination
        "text": "Do you prefer stories that feel real, not imaginary?",
        "yes": {"Documentary": 3, "Drama": 1, "Crime": 2, "History": 2},
        "no": {"Fantasy": 3, "Science Fiction": 2, "Animation": 2, "Adventure": 2},
    },
    {  # 5. Thinking effort
        "text": "Do you enjoy puzzling things out and guessing the twist?",
        "yes": {"Mystery": 3, "Crime": 2, "Thriller": 2, "Science Fiction": 1},
        "no": {"Comedy": 1, "Romance": 1, "Action": 1, "Animation": 1},
    },
    {  # 6. Emotional depth
        "text": "Are you okay with a sad, emotional story that might make you cry?",
        "yes": {"Drama": 3, "Romance": 2, "History": 1},
        "no": {"Comedy": 1, "Action": 1, "Adventure": 1, "Horror": 1},
    },
    {  # 7. Time setting
        "text": "Do you like stories set in the past (history, old times)?",
        "yes": {"History": 3, "Crime": 1, "Documentary": 1},
        "no": {"Science Fiction": 2, "Action": 1, "Thriller": 1, "Fantasy": 1},
    },
]
Questions_tv = [
    {  # 1. Mood
        "text": "Do you want to feel happy and light-hearted right now?",
        "yes": {
            "Comedy": 3,
            "Animation": 2,
            "Family": 1,
            "Action & Adventure": 1,
            "Sci-Fi & Fantasy": 1,
        },
        "no": {"Drama": 1, "Crime": 1, "Mystery": 1, "War & Politics": 1},
    },
    {  # 2. Energy
        "text": "Do you have lots of energy and want fast, exciting scenes?",
        "yes": {
            "Action & Adventure": 3,
            "Sci-Fi & Fantasy": 2,
            "Crime": 1,
            "Western": 1,
        },
        "no": {"Drama": 1, "Soap": 1, "Documentary": 1, "Mystery": 1},
    },
    {  # 3. Fear tolerance
        "text": "Are you okay with feeling scared or tense?",
        "yes": {"Mystery": 3, "Crime": 2, "Sci-Fi & Fantasy": 2, "Drama": 1},
        "no": {"Comedy": 1, "Animation": 1, "Family": 1, "Soap": 1},
    },
    {  # 4. Reality vs imagination
        "text": "Do you prefer stories that feel real, not imaginary?",
        "yes": {"Documentary": 3, "Reality": 2, "Crime": 2, "War & Politics": 2},
        "no": {
            "Sci-Fi & Fantasy": 3,
            "Animation": 2,
            "Action & Adventure": 2,
            "Family": 1,
        },
    },
    {  # 5. Thinking effort
        "text": "Do you enjoy puzzling things out and guessing the twist?",
        "yes": {"Mystery": 3, "Crime": 2, "Sci-Fi & Fantasy": 1, "Drama": 1},
        "no": {"Comedy": 1, "Reality": 1, "Soap": 1, "Action & Adventure": 1},
    },
    {  # 6. Emotional depth
        "text": "Are you okay with a sad, emotional story that might make you cry?",
        "yes": {"Drama": 3, "Soap": 2, "War & Politics": 1},
        "no": {"Comedy": 1, "Action & Adventure": 1, "Reality": 1, "Animation": 1},
    },
    {  # 7. Time setting
        "text": "Do you like stories set in the past (history, old times)?",
        "yes": {"War & Politics": 3, "Western": 2, "Drama": 1, "Documentary": 1},
        "no": {
            "Sci-Fi & Fantasy": 2,
            "Action & Adventure": 1,
            "Reality": 1,
            "Crime": 1,
        },
    },
]

raw_review = {"moive": "AI review"}
