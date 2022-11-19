import cohere
import os
from dotenv import load_dotenv

# getting API key
if os.path.exists("api.key"):
    with open("api.key", "r") as f:
        API_KEY = str(f.read())
else:
    load_dotenv()
    API_KEY=os.getenv('API_KEY')

# Setting up the cohere client
co = cohere.Client(API_KEY)

# Main function for suggesting gifts
def suggest(
    age, 
    gender, 
    interest,
    ):

    prompt=f"""
    This app suggests gifts based on several factors.

    Age: 6
    Gender: female
    Interest: Disney
    Gift Suggestions: Disney princess dress, Disney-themed coloring book, Toy castle, set of Disney figurines
    --
    Age: 39
    Gender: non-binary
    Interest: Astrophysics
    Gift Suggestions: Telescope, NASA t-shirt, constellation charts, Space-themed coffee mug
    --
    Age: 81
    Gender: female
    Interest: Gardening
    Gift Suggestions: Gardening apron, Potted plants, Garden hat, set of gardening tools
    --
    Age: 19
    Gender: male
    Interest: Anime
    Gift Suggestions: DVD set of an Anime show, video game based on popular anime, Funko Pop figure of an Anime character, Manga collection
    --
    Age: {age}
    Gender: {gender}
    Interest: {interest}
    Gift Suggestions:"""

    response = co.generate(
        model='xlarge',
        prompt=prompt,
        stop_sequences=["--"],
        )
    suggestions = response.generations[0].text.split(',')[:-1] # list of suggestions
    return list(map(str.strip, suggestions)) # removing extra space and return