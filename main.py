import cohere
import os
from dotenv import load_dotenv

# getting API key
if os.path.exists("api.key"):
    with open("api.key", "r") as f:
        API_KEY = str(f.read().strip())
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
    Gift Suggestions: Disney princess dress, Disney-themed kid's backpack, Toy castle set, Disney coloring book
    --
    Age: 39
    Gender: non-binary
    Interest: Astrophysics
    Gift Suggestions: Telescope, NASA t-shirt, Stargazing charts, Planetarium projector
    --
    Age: 81
    Gender: female
    Interest: Gardening
    Gift Suggestions: Gardening apron, Potted plants, Garden hat, Bird feeder
    --
    Age: 19
    Gender: male
    Interest: Rock Music
    Gift Suggestions: Electric guitar, Rock music CD collection, Vinyl record player, Rock band poster
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