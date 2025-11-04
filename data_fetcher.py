import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the API key from environment
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.api-ninjas.com/v1/animals?name="

def fetch_data(animal_name):
    """
    Fetches data for the given 'animal_name' from API Ninja Animals API.
    Returns a list of animals. Each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {...},
        'locations': [...],
        'characteristics': {...}
    }
    """
    if not API_KEY:
        print("Error: API_KEY not found in .env")
        return []

    response = requests.get(
        f"{BASE_URL}{animal_name}",
        headers={"X-Api-Key": API_KEY}
    )

    if response.status_code == 200:
        data = response.json()
        # If no animal found, return empty list
        return data if data else []
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []

