def celsius_to_fahrenheit(c):
    """Convert a Celsius temperature to Fahrenheit."""
    if not isinstance(c, (int, float)) or isinstance(c, bool):
        raise TypeError("Temperature must be a number.")
    return (c * 9 / 5) + 32


def line_total(price, qty):
    """Return the total cost by multiplying price by quantity."""
    if not isinstance(price, (int, float)) or isinstance(price, bool):
        raise TypeError("Price must be a number.")
    if not isinstance(qty, (int, float)) or isinstance(qty, bool):
        raise TypeError("Quantity must be a number.")
    if qty < 0:
        raise ValueError("Quantity cannot be negative.")
    return price * qty


def initials(full_name):
    """Return the initials from a person's full name."""
    if not isinstance(full_name, str):
        raise TypeError("Name must be a string.")

    name = full_name.strip()

    if not name:
        return ""

    parts = name.split()
    return "".join(part[0].upper() for part in parts)


def is_valid_url(text):
    """Return True when text looks like a valid HTTP or HTTPS URL."""
    if not isinstance(text, str):
        return False

    text = text.strip()

    if not text:
        return False

    return text.startswith("http://") or text.startswith("https://")


def truncate(text, limit=20):
    """Shorten text to the given limit and add an ellipsis if needed."""
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")

    if not isinstance(limit, int) or isinstance(limit, bool):
        raise TypeError("Limit must be an integer.")

    if limit < 0:
        raise ValueError("Limit cannot be negative.")

    if len(text) <= limit:
        return text

    if limit == 0:
        return "..."

    return text[:limit] + "..."


def safe_filename(text):
    """Convert text into a filename without spaces, slashes, or quotes."""
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")

    filename = text.strip()

    for character in [" ", "/", "\\", '"', "'"]:
        filename = filename.replace(character, "_")

    return filename
