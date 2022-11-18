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

    prompt=f"""This app suggests gifts based on several factors.

    Age: {age}
    Gender: {gender}
    Interests: {interest}
    Gift Suggestion:"""

    response = co.generate(prompt=prompt)
    return response.generations[0].text.split('\n')[0]

if __name__ == "__main__":
    print(suggest(25, 'Male', 'Cooking'))