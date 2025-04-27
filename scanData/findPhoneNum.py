import re
import sys
import os

def extract_PN(input_file):
    
    pattern = re.compile(r'\b\d{10}\b|\b\d{3}-\d{3}-\d{4}\b|\(\d{3}\) \d{3}-\d{4}\b')
    phone_numbers = []

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            phone_numbers.extend(pattern.findall(line))
    
    print(f"{len(phone_numbers)} Phone numbers found\n")

    
    pnFile = 'phoneList.txt'
    subDir = 'Results'
    os.makedirs(subDir, exist_ok=True)
    filePath = os.path.join(subDir,pnFile)
    with open(filePath, 'w') as file:
        for item in phone_numbers:
            file.write(f"{item}\n") 

    return phone_numbers


def writeResults(slist,fName):
     
    try:
        outfile = open(fName,'w')
    except:
        print('error opening ',fName)
        sys.exit()

    for x in slist:
         outfile.write(x + '\n')
    outfile.close()
    return True

def main():
     
     sourceFile = "fullSet.txt"
     resultFile = "PNResult.txt"
     pnList = []

     pnList = extract_PN(sourceFile)

    #writeResults(pnList, resultFile)

if __name__ == '__main__':
	main()