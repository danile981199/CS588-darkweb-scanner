import re
import sys

def extract_PN(input_file):
    
    pattern = re.compile(r'\b\d{10}\b|\b\d{3}-\d{3}-\d{4}\b|\(\d{3}\) \d{3}-\d{4}\b')
    phone_numbers = []

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            phone_numbers.extend(pattern.findall(line))
    
    print(f"{len(phone_numbers)} Phone numbers found\n")
    return phone_numbers
    '''
    try:
        infile = open(input_file,'r')
    except:
        print('error opening ',input_file)
        sys.exit()
    
    for line in infile:
        found_numbers.extend(pattern1.findall(line))
        found_numbers.extend(pattern2.findall(line))
        found_numbers.extend(pattern3.findall(line))

    infile.close()

    print(f"{len(found_numbers)} SSNs found\n")
    return found_numbers'
    '''

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
     
     sourceFile = "Test1.txt"
     resultFile = "PNResult.txt"
     pnList = []

     pnList = extract_PN(sourceFile)

     writeResults(pnList, resultFile)

if __name__ == '__main__':
	main()