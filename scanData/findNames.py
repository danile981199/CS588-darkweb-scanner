import re
import sys



def find_names(data_file):
    names = []

    try:
         infile = open(data_file,'r')
    except:
         print("Error opening file.")
         sys.exit()

    for line in infile:
        match = re.search(r'([A-Z][a-z]+(?:\s[A-Z](?:\.|[a-z]+))?(?:\s[A-Z][a-z]+)+)', line)
        if match:
            names.append(match.group(1).strip())

    infile.close()
    return names



def main():
     
     sourceFile = "fullSet.txt"
     r2File = "nameResults.txt"
     adList = []
     nameList=[]
     
     out2File = open(r2File,'w')
     nameList = find_names(sourceFile)
     for x in nameList:
          print(x)
     out2File.close()

if __name__ == '__main__':
	main()