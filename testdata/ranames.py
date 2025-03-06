
# Random name generator

"""
RRRR   AAA  N   N DDDD   OOO  M   M     N   N  AAA  M   M EEEEE  SSSS  
R   R A   A NN  N D   D O   O MM MM     NN  N A   A MM MM E     S      
RRRR  AAAAA N N N D   D O   O M M M     N N N AAAAA M M M EEE    SSS   
R  R  A   A N  NN D   D O   O M   M     N  NN A   A M   M E         S  
R   R A   A N   N DDDD   OOO  M   M     N   N A   A M   M EEEEE SSSS   

"""

import random
import sys
import string

def read_names():

    fnames = []
    mnames = []
    snames = []
    fileNames = ["m500.txt","f500.txt","s500.txt"]
    for fName in fileNames:
        try:
            f = open(fName,'r')
        except:
            print('error opening ',fName)
            sys.exit()
        names = f.readlines()
        names = [x.strip() for x in names]  #remove whitespace 
        if 'f' in fName:
            for x in names:
                fnames.append(x)
        elif 'm' in fName:
            for x in names:
                mnames.append(x)
        else:
            for x in names:
                snames.append(x)
        f.close()
    return mnames,fnames,snames
        
def write_names(nList):
    #write to a file

    nfile = open("full_names.txt",'a')
    for x in nList:
        nfile.write(x+'\n')

    nfile.close()

def create_names(num = 5):
    mcount = 0
    fcount = 0
    nameList = []
    middleName = ''
    middleInitial = ''
    initialList = string.ascii_uppercase

    mnames,fnames,snames = read_names()

    for x in range(0,num):
        gen = random.randint(0,1)
        if 1 == gen:
            firstnames = mnames
            #gender ='Male'
            mcount += 1
        else:
            firstnames = fnames
            #gender = 'Female'
            fcount += 1

        firstname = random.choice(firstnames)
        lname = random.choice(snames)
        middleInitial = random.choice(initialList)
        ran_name = firstname 
        
        #Add middle initial or name for one third of names
        ran = random.randint(0,3)
        if (ran == 0):
            r2 = random.randint(0,1)
            if r2 == 0:
                ran_name += ' ' + middleInitial + '.' 
            else:
                ran_name += ' ' + middleInitial
        if (ran == 1):
            ran_name += ' ' + random.choice(firstnames) 
        ran_name += ' ' +lname
        nameList.append(ran_name)
        #print('%s' % (ran_name))
        
    #print('%d males, %d females' % (mcount, fcount))
    return nameList


def main():
    
    print('starting ')
    nameNum = 10
    m = 0
    nList = []

    if len(sys.argv) > 1:
        try:
            m = int(sys.argv[1])
        except:
            print("argument must be an integer\n")
            print("using default of 10\n")
            
    if m > 0:
        nameNum = m
    else:
        if m < 0:
            print("Must be postive integer")
        print("using default of 10\n")


    nList = create_names(nameNum)
    write_names(nList)

if __name__ == '__main__':
	main()

