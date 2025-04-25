import requests
import re
from bs4 import BeautifulSoup

# Tor Proxy Settings (Port 9150 confirmed working)
proxies = {
    'http': 'socks5h://127.0.0.1:9150',
    'https': 'socks5h://127.0.0.1:9150'
}

# Headers to Mimic a Real Browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# Target Dark Web URL (Replace with a real .onion site)
#url = "http://breachdbsztfykg2fdaq2gnqnxfsbj5d35byz3yzj73hazydk4vq72qd.onion/LeakedPass"  # DuckDuckGo Dark Web Search
url = "https://csectest.wordpress.com/bad-email/"

# Define Regular Expressions to Identify PII
PII_PATTERNS = {
    "Emails": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    
    "Phone Numbers": r"\+?\d[\d\s().-]{7,}",  # Covers intl & local, loose format
    
    "Credit Cards": r"\b(?:\d[ -]*?){13,16}\b",  # Visa, Mastercard, Amex etc.
    
    "Bitcoin Wallets": r"\b(?:[13][a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{39,59})\b",
    
    "Ethereum Wallets": r"\b0x[a-fA-F0-9]{40}\b",  # Add this if you want Ethereum support
    
    "IP Addresses": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    
    "Addresses": r"\d{1,5}\s\w+(?:\s\w+){0,5}(?:,)?\s\w+,\s?[A-Z]{2,}\s\d{5}",  # Looser US format
    "Social Security Numbers": r"\b(?!000|666|9\d{2})\d{3}[- ]?(?!00)\d{2}[- ]?(?!0000)\d{4}\b"
}


# Function to Extract PII from Text
def extract_pii(text):
    pii_results = {}
    for category, pattern in PII_PATTERNS.items():
        matches = re.findall(pattern, text)
        if matches:
            pii_results[category] = matches
    return pii_results

def dwScrape(url):
    # Scrape Dark Web Page
    
    try:
        response = requests.get(url, proxies=proxies, headers=headers, timeout=20)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            extracted_text = soup.get_text()

            # Extract PII from the scraped data
            pii_data = extract_pii(extracted_text)

            # Create 'Results' directory if it doesn't exist
            os.makedirs("Results", exist_ok=True)
		
            with open("./Results/rawText.txt", 'w') as rFile:
                rFile.write(extracted_text)

            if pii_data:
                print(" PII Found!")
                for category, matches in pii_data.items():
                    print(f"\n🔹 {category}:")
                    for match in matches:
                        print(f"   - {match}")

                # Save the PII data securely
                with open(os.path.join("Results", "darkweb_pii_extracted.txt"), "w", encoding="utf-8") as file:
                    for category, matches in pii_data.items():
                        file.write(f"{category}:\n")
                        for match in matches:
                            file.write(f"   - {match}\n")
                
                print(" Extracted PII saved in 'darkweb_pii_extracted.txt'")

            else:
                print(" No PII Found in the extracted content.")

        else:
            print(f" Failed to access site. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f" Error: {e}")



def simpleScrape(url):

    print("url = ", url)
    fileName = './Results/fubar.txt'
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all text
        text = soup.get_text()
        
        # Filter only ASCII characters
        ascii_text = re.sub(r'[^\x00-\x7F]+', ' ', text)
        
        # Write to a file
        with open(fileName, 'w', encoding='utf-8') as file:
            file.write(ascii_text)
        
        print(f"Text saved to {fileName}")
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")


def get_url():
    targetUrl = input("Please enter a URL to scan: ")
    return targetUrl

def create_blank_config_file(file_path):
    template_content = """[Configuration File]
[Specified Data – if not selected the field will be blank]
URL: 
Specified_Name:
Specified_Address:
Specified_Phone:
Specified_SSN:
Specified_CCN:

[Generic Data - 1 if selected, otherwise blank or 0]
Name:
Address
Phone:
SSN:
CCN:
"""
    try:
        with open(file_path, 'w') as new_file:  # 'w' mode overwrites if file exists
            new_file.write(template_content)
        print(f"Config file created (or overwritten) at: {file_path}")
    except Exception as e:
        print(f"Error: {e}")

def update_url(file_path, addition):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        if line.startswith("URL:"):
            line = line.rstrip()  # Remove trailing newline
            if line.strip() == "URL:":
                line += f" {addition}"
            else:
                line += f" {addition}"
            line += "\n"  # Re-add newline
        updated_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(updated_lines)


def main():
    
    scanTarget = get_url()
    print(scanTarget)

    create_blank_config_file("./config/configFile.txt")

    update_url("./config/ConfigFile.txt",scanTarget)

    #dwScrape(scanTarget)
    #simpleScrape(scanTarget)


if __name__ == '__main__':
	main()
