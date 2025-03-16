import re
import sys

def find_addr(infile):
    
    addresses = []

    try:
         infile = open(infile,'r')
    except:
         print("Error opening file.")
         sys.exit()


    for line in infile:
        match = re.search(r'\b(\d+[\w\s#.’’\-,]+)\s([A-Z]{2}\s\d{5}(?:-\d{4})?)\b', line)
        if match:
            addresses.append(match.group(1).strip() + ' ' + match.group(2).strip())

    infile.close()
    return addresses



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