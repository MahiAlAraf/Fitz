def scoreboard_Dict():
    return {
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
    }


Questions = [
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

row_review = {"moive": "AI review"}
