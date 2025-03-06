import random
import sys

def generate_invalid_ssn():
    # Generates a random invalid U.S. Social Security Number.
    '''
    https://secure.ssa.gov/poms.nsf/lnx/0110201035
    A SSN is invalid if:
        1. All zeros in any section
        2. First three digits "000," "666,” or in the 900 series
        3. Any nonnumeric character besides a dash in the format xxx-yy-zzzz
        4. Number of numeric digits are not equal to 9
    '''
    invalid_patterns = [
        (0, random.randint(1, 99), random.randint(1, 9999)),  # 000-XX-XXXX
        (random.randint(1, 899), 0, random.randint(1, 9999)),  # XXX-00-XXXX
        (random.randint(1, 899), random.randint(1, 99), 0),  # XXX-XX-0000
        (666, random.randint(1, 99), random.randint(1, 9999)),  # 666-XX-XXXX
        (random.randint(900, 999), random.randint(1, 99), random.randint(1, 9999)),  # 900-999-XX-XXXX
    ]
    
    area, group, serial = random.choice(invalid_patterns)
    form = random.randint(0,1)
    if form == 0:
        return f"{area:03d}-{group:02d}-{serial:04d}"
    else:
        return f"{area:03d}{group:02d}{serial:04d}"


def main():
    #form = 'd'
    m = 5
    fname = 'ssNums.txt'
    ssnfile = open(fname,'a') 

    if len(sys.argv) > 1:
        try:
            m = int(sys.argv[1])
        except:
            print("argument must be an integer\n")
            print("using default of 5\n")

    for _ in range(m):
        ssn = (generate_invalid_ssn())
        print(ssn)
        ssnfile.write(ssn + '\n')

    ssnfile.close()


if __name__ == '__main__':
	main()
