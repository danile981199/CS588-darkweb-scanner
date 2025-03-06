import random
import sys
import string

def read_file(fName):

    nList = []

    try:
        f = open(fName,'r')
    except:
        print('error opening ',fName)
        sys.exit()
    names = f.readlines()
    names = [x.strip() for x in names]  #remove whitespace 

    for x in names:
        nList.append(x)

    f.close()
    return nList

def genUserName():
    #generate a random user names
    
    uNames =[]
    t = []
    nfiles = ["m500.txt","f500.txt","s500.txt"]
    for x in nfiles:
        t = read_file(x)
    for y in t:
        uNames.append(y)

    rWord = read_file("random_words.txt")

    retVal = random.choice(uNames) + random.choice(rWord) + str(random.randint(1,999))
    retVal = retVal.replace(" ","")
    retVal = retVal.replace("'","")
    retVal = retVal.replace(".","")
    return retVal

def genRanEmailAddr():
    # Generates a email random address.
    uName = genUserName()
    providers = read_file("emailProviders.txt")
    
    retVal = uName + "@" + random.choice(providers)
    return retVal

def genPassword():
    #generate a ranodom password

    rWord = read_file("random_words.txt")
    specChar = ["#","%","-","+","%","-"]
    pWord = random.choice(rWord) + random.choice(rWord) + random.choice(rWord) + random.choice(specChar) + str(random.randint(0,999))

    return pWord

def main():
    form = 'd'
    m = 15
    fname = "random_email.txt"
    adrfile = open(fname,'a') 

    if len(sys.argv) > 1:
        try:
            m = int(sys.argv[1])
        except:
            print("argument must be an integer\n")
            print("using default of 5\n")

    for _ in range(m):
        addr = (genRanEmailAddr())
        print(addr)
        adrfile.write(addr + '\n')
    
    adrfile.close()


if __name__ == '__main__':
	main()
