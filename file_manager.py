

def save_message(message):
    """Save the message to a text file."""
    try:
        with open("user_message.txt", "w") as file:
            file.write(message)
        print("Message saved successfully.")
    except Exception as e:
        print(f"Error saving message: {e}")


def read_message():
    """Read and print the saved message."""
    try:
        with open("user_message.txt", "r") as file:
            content = file.read()
        print("Reading saved message...")
        print(content)
    except FileNotFoundError:
        print("Error: File not found. Please save a message first.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
