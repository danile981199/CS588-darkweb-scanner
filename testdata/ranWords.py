import random
import requests

def generate_random_words(output_file, num_words=500):
    """Fetches a list of random English words and writes them to a file with CR/LF separation."""
    try:
        # Fetch a list of words from an online source
        response = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
        words = response.text.splitlines()

        # Select random words
        selected_words = random.sample(words, min(num_words, len(words)))

        # Write words to the output file with CR/LF formatting
        with open(output_file, "w") as file:
            file.write("\r\n".join(selected_words))

        print(f"Successfully wrote {len(selected_words)} words to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
generate_random_words("random_words.txt")

