import re
import sys
import os

def find_addr(data_file):
    
    addresses = []

    try:
         infile = open(data_file,'r')
    except:
         print("Error opening file.")
         sys.exit()


    for line in infile:
        match = re.search(r'\b(\d+[\w\s#.’’\-,]+)\s([A-Z]{2}\s\d{5}(?:-\d{4})?)\b', line)
        if match:
            addresses.append(match.group(1).strip() + ' ' + match.group(2).strip())

    infile.close()

    addrFile = 'addressList.txt'
    subDir = 'Results'
    filePath = os.path.join(subDir,addrFile)
    with open(filePath, 'w') as file:
        for item in addresses:
            file.write(f"{item}\n") 

    return addresses

def find_names(data_file):
    names = []

    try:
         infile = open(data_file,'r')
    except:
         print("Error opening file.")
         sys.exit()

    for line in infile:
        match = re.search(r'([A-Z][a-z]+(?:\s[A-Z][a-z]+)*(?:\sO\s[A-Z][a-z]+)?)', line)
        if match:
            names.append(match.group(1).strip())

    infile.close()

    nameFile = 'nameList.txt'
    subDir = 'Results'
    filePath = os.path.join(subDir,nameFile)
    with open(filePath, 'w') as file:
        for item in names:
            file.write(f"{item}\n")

    return names



def main():
     
     sourceFile = "fullSet.txt"
     resultFile = "addResults.txt"

     adList = []

     outFile = open(resultFile,'w')
     adList = find_addr(sourceFile)
     for x in adList:
          print(x)
          outFile.write(x + '\n')
     outFile.close()
    


if __name__ == '__main__':
	main()