from google import genai

Model = "gemini-3.5-flash-lite"
client = genai.Client()


def Check_title(Title):
    prompt = (
        "The user typed a movie or web series name that may be misspelled.\n"
        "Reply with ONLY the correct official title, nothing else.\n"
        "If you are not sure what they mean, reply with exactly: UNKNOWN\n\n"
        f"User input: {Title}"
    )
    Response = client.models.generate_content(model=Model, contents=prompt)
    return Response.text.strip()


def Unique_message(Title, Age_rating, Genres, Overview, Keywords):
    prompt = (
        "You are a direct content advisor for movies and TV shows. Analyze the provided media details and provide a ultra-brief target audience advisory (maximum 3-4 sentences total).\n"
        "Do NOT write marketing summaries, reviews, or promotional hype.\n:"
        "Make the Response very simple and easy to understand Avoid using complex grammatical words.\n"
        "Make the answers in two para Organized in two specific sections   1.Target Audience:   2.Content & Suitability:\n"
        "Focus only on:\n"
        "1. Who will enjoy this content.\n"
        "2. Mature elements/content warnings (violence, explicit scenes, dark themes).\n"
        "3. A clear recommendation on family suitability or viewing context.\n"
        " MEDIA METADATA:"
        f"- Title: {Title}"
        f"- Age Rating: {Age_rating}"
        f" Genres: {Genres}"
        f"- Overview: {Overview}"
        f"- Keywords: {Keywords}"
    )
    Responce = client.models.generate_content(model=Model, contents=prompt)
    return Responce.text
