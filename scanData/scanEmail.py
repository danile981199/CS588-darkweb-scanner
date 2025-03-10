import re

def extract_emailAddr(input_file):
    pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    email_addresses = []

    with open(input_file, 'r', encoding='ascii', errors='ignore') as file:
        for line in file:
            email_addresses.extend(pattern.findall(line))

    return email_addresses

# Example usage:
# emails = extract_email_addresses('sample.txt')
# print(emails)

def main():
     
     sourceFile = "Test1.txt"
     resultFile = "emResults.txt"
     emList = []

     emList = extract_emailAddr(sourceFile)

     print(f"{len(emList)} email addresses found\n")

if __name__ == '__main__':
	main()
