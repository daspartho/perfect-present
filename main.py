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

    prompt=f"""This app suggests gifts based on several factors.

    Age: 6
    Gender: female
    Interests: Disney
    Gift Suggestions: Disney princess dress, Disney Frozen toy, A trip to Disney World
    --
    Age: 25
    Gender: male
    Interests: Cooking
    Gift Suggestions: A nice set of kitchen knives, A subscription to a cooking magazine, A cooking apron
    --
    Age: 81
    Gender: female
    Interests: Gardening
    Gift Suggestions: A gardening apron or gloves, A book on gardening, a gift certificate to a local nursery or garden shop
    --
    Age: 17
    Gender: male
    Interests: Anime
    Gift Suggestions: A gift card to an anime or manga store, A DVD or Blu-ray set of an Anime show, an Anime t-shirt or hoodie, a Funko Pop figure of an Anime character
    --
    Age: {age}
    Gender: {gender}
    Interests: {interest}
    Gift Suggestions:"""

    response = co.generate(prompt=prompt)
    return response.generations[0].text

if __name__ == "__main__":
    print(suggest(10, 'male', 'Basketball'))
