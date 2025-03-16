import re

def find_addr(infile):
    address_pattern = re.compile(r"""
        (\d+\s+                         # Building number
        [\w\s]+                         # Street name
        (?:\s+(?:Apt|Suite|#)\s*\w+)?   # Optional apartment/suite number
        ,?\s*                             # Optional comma separator before city
        [A-Za-z\s]+                      # City name
        \s+                               # Space before state
        [A-Z]{2}                          # State abbreviation
        \s+                               # Space before ZIP code
        \d{5}(?:-\d{4})?)                # ZIP code (5 or 5+4 format)
    """, re.VERBOSE)
    
    addresses = []
    with open(infile, 'r', encoding='utf-8') as file:
        for line in file:
            matches = address_pattern.findall(line)
            addresses.extend(matches)
    
    return addresses


def main():
     
     sourceFile = "t1.txt"
     resultFile = "addResults.txt"
     adList = []
 
     adList = find_addr(sourceFile)

     

if __name__ == '__main__':
	main()