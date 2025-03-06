import random
import sys

def generate_quad():
    return f"{random.randint(0, 9999):04d}"

def gen_xDate():
     m = f"{random.randint(1,12):1d}"
     y = f"{random.randint(29,35)}"

     return m+'/'+y

def genAMEX_CCnum():
     # Amex is 14 digits with a four digit CVC

    f1 = generate_quad()
    f2 = generate_quad()
    f3 = generate_quad()
    f4 = f"{random.randint(0,99):02d}"

    first = f"{random.randint(1,9):01d}"
    next = f"{random.randint(0,999):03d}"
    cvc = first + next

    return (f1+f2+f3+f4+' '+cvc + ' ' + gen_xDate())
    

def genMCV_CCnum():
    # Generates a random MasterCard/Visa format credit card Number.
    # MC/Visa is 16 digit (four groups of four) with a three digit CVC
    
    # Date Format is mm/yy

    q1 = generate_quad()
    q2 = generate_quad()
    q3 = generate_quad()
    q4 = generate_quad()
    mcvNum = q1+q2+q3+q4

    first = f"{random.randint(1,9):01d}"
    next = f"{random.randint(0,99):02d}"
    cvc = first + next

    return (mcvNum + ' ' + cvc + ' ' + gen_xDate())

def genRanCCN():
     
     x = random.randint(0,3)
     if x > 0:
          retVal = genMCV_CCnum() + ' ' + gen_xDate()
     else:
          retVal = genAMEX_CCnum() + ' ' + gen_xDate()
     return retVal

def main():
    form = 'd'
    m = 1
    fname = 'ccNums.txt'
    #ssnfile = open(fname,'a') 

    if len(sys.argv) > 1:
        try:
            m = int(sys.argv[1])
        except:
            print("argument must be an integer\n")
            print("using default of 5\n")

    #print(genMCV_CCnum())
    #print(genAMEX_CCnum())
    #print(gen_xDate())
    print()

    '''
    for _ in range(m):
        ssn = (generate_invalid_ssn(form))
        print(ssn)
        ssnfile.write(ssn + '\n')
    '''
    #ccnfile.close()


if __name__ == '__main__':
	main()
