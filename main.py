import cohere
import os
from dotenv import load_dotenv

# getting API key
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
    Gender: male
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
    return response.generations[0].text.split(',')[:-1]

if __name__ == "__main__":
    print(suggest(10, 'male', 'Basketball'))
    print(suggest(27, 'male', 'Cooking'))
    print(suggest(29, 'female', 'Yoga'))
    print(suggest(32, 'male', 'Marvel'))
    print(suggest(21, 'female', 'Digital Art'))
    print(suggest(69, 'male', 'History'))
    print(suggest(16, 'female', 'Books'))
    print(suggest(18, 'female', 'Rock Music'))
    print(suggest(24, 'male', 'Acting'))
    print(suggest(36, 'female', 'Beauty'))