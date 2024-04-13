# utils.py

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
