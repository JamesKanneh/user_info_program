

def validate_input(user_input):
    """Check if user input is not empty and is a string."""
    if  isinstance(user_input, str) and user_input.strip() !="":
        return True
    return False


def convert_to_binary(text):
    """Convert text or number into binary."""
    if isinstance(text, (int, float)) or (isinstance(text, str) and text.isdigit()):
        # Convert to integer then to binary
        return bin(int(text))
    elif isinstance(text, str):
        # Convert each character to 8-bit binary
        return " ".join(format(ord(char), "08b") for char in text)
    else:
        raise TypeError("Input must be a string or number.")


def create_message(name, age, name_binary, age_binary):
    """Combine all information into a final message."""
    message = (
        f"Hello {name}, you are {age} years old!\n"
        f"Name in binary: {name_binary}\n"
        f"Age in binary: {age_binary}"
    )
    return message
