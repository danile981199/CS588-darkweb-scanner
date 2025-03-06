import random

def select_random_names(input_file, output_file, num_names=500):
    """Reads names from input_file, selects random unique names, and writes them to output_file."""
    try:
        # Read names from the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            names = list(set(line.strip() for line in file if line.strip()))  # Remove duplicates & empty lines
        
        if not names:
            print("No valid names found in the file.")
            return

        # Select random names without replacement
        selected_names = random.sample(names, min(num_names, len(names)))
        selected_names = sorted(selected_names)

        # Write selected names to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("\n".join(selected_names))

        print(f"Successfully wrote {len(selected_names)} names to {output_file}")

    except FileNotFoundError:
        print("Error: The input file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# select_random_names("names.txt", "selected_names.txt")

infile = "mnames.txt"
outfile = "m500.txt"
select_random_names(infile,outfile)

