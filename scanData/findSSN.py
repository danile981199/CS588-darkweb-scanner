import re
import sys

def extract_SSN(input_file, output_file):
    # Define regex patterns for 9-digit numbers
    pattern1 = re.compile(r'\b\d{9}\b')  # Matches 9-digit numbers
    pattern2 = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')  # Matches nnn-nn-nnnn format
    
    found_numbers = []

    try:
        infile = open(input_file,'r')
    except:
        print('error opening ',input_file)
        sys.exit()
    
    for line in infile:
        found_numbers.extend(pattern1.findall(line))
        found_numbers.extend(pattern2.findall(line))

    infile.close()

    print(f"{len(found_numbers)} SSNs found\n")
    return found_numbers

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
     resultFile = "Results.txt"
     ssnList = []

     ssnList = extract_SSN(sourceFile,resultFile)

     writeResults(ssnList, resultFile)

if __name__ == '__main__':
	main()

