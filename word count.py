# python Word Counter Program

def get_user_input():
    """
    Prompts user to enter a sentence or paragraph.
    """
    user_input = input("Please enter a sentence or paragraph: ")
    return user_input

def count_words(input_text):
    """
    Counts the number of words in the input text.
    """
    # Remove leading/trailing whitespace and split text into words
    words = input_text.strip().split()
    
    # Return word count
    return len(words)

def display_output(word_count):
    """
    Displays the word count to the console.
    """
    print(f"Word count: {word_count}")

def handle_error(input_text):
    """
    Checks for potential errors (e.g., empty input).
    """
    if not input_text.strip():
        print("Error: Input cannot be empty.")
        return True
    return False

def main():
    # Get user input
    user_input = get_user_input()
    
    # Check for errors
    if handle_error(user_input):
        return
    
    # Count words
    word_count = count_words(user_input)
    
    # Display output
    display_output(word_count)

if __name__ == "__main__":
    main()

