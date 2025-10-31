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
        with open("user_message.txt", "r", encoding="utf-8") as file:
            content = file.read()
            print("\nSaved Message:\n")
            print(content)
    except FileNotFoundError:
        print("Error: No saved message found. Please save one first.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")