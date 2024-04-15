import random
import string
from datetime import datetime
from sqlalchemy.orm import Session

def validate_email(email):
    """Validate the format of an email address."""
    # Placeholder implementation for email validation
    if "@" in email and "." in email:
        return True
    else:
        return False

def format_currency(amount):
    """Format a numeric amount as currency."""
    # Placeholder implementation for currency formatting
    return f"${amount:.2f}"

class Logger:
    """Simple logger class for logging messages to a file."""
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        """Log a message to the specified file."""
        with open(self.filename, "a") as file:
            file.write(message + "\n")


def generate_password(length=8):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def generate_game_data():
    """Generate sample game data."""
    titles = ["Game 1", "Game 2", "Game 3", "Game 4", "Game 5"]
    genres = ["Action", "Adventure", "Puzzle", "RPG", "Simulation"]
    prices = [19.99, 24.99, 29.99, 14.99, 34.99]

    games = []
    for i in range(len(titles)):
        game_data = {
            "title": titles[i],
            "genre": genres[i],
            "price": prices[i],
            "available": True  # Assuming all games are initially available
        }
        games.append(game_data)
    
    return games
