import re
import sys
import os 

def extract_emailAddr(input_file):
    pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    email_addresses = []

    try:
        infile = open(input_file,'r')
    except:
        print('error opening ',input_file)
        sys.exit()

    for line in infile:
        email_addresses.extend(pattern.findall(line))

    infile.close()

    emFile = 'emList.txt'
    subDir = 'Results'
    filePath = os.path.join(subDir,empwFile)
    with open(filePath, 'w') as file:
        for item in email_addresses:
            file.write(f"{item}\n")

    return email_addresses

def extract_email_PW(input_file):
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    password_pattern = re.compile(r'[\w!@#$%^&*.-]{8,}')  # Includes letters, digits, and special characters
    results = []

    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                email_matches = list(email_pattern.finditer(line))  # Find email matches with positions
                
                for email_match in email_matches:
                    email = email_match.group()
                    email_end = email_match.end()  # Position where email ends
                    
                    # Search for the first valid password-like string *after* the email
                    password_matches = password_pattern.finditer(line, email_end)  
                    for password_match in password_matches:
                        results.append(f"{email} {password_match.group()}")
                        break  # Stop at the first valid match

    except Exception as e:
        print(f"Error opening {input_file}: {e}")
        sys.exit()

    empwFile = 'empwList.txt'
    subDir = 'Results'
    filePath = os.path.join(subDir,empwFile)
    with open(filePath, 'w') as file:
        for item in results:
            file.write(f"{item}\n")

    return results


def main():
     
     #sourceFile = "Test1.txt"
     sourceFile = "rawText.txt"
     resultFile = "emResults.txt"
     emList = []
     both = []

     emList = extract_emailAddr(sourceFile)

     print(f"{len(emList)} email addresses found\n")
     
     both = extract_email_PW(sourceFile)
     for x in both:
         print(x+"\n")

if __name__ == '__main__':
	main()
