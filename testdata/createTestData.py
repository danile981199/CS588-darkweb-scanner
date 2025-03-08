
import sys
import ranames
import ran_address
import ranDate
import ranSSN
import ranCCN
import ranEmail
import ranPNum


def createFullSet():
    data_item = ""
    data_item = ranames.create_names(1)[0]
    data_item += ' - '
    data_item += ran_address.genRanAddr()
    data_item += ' - '
    data_item += ranPNum.gen_pn_2()
    data_item += ' - '
    data_item += ranDate.generate_random_date()
    data_item += ' - '
    data_item += ranSSN.generate_invalid_ssn()
    data_item += ' - '
    data_item += ranCCN.genRanCCN()
    data_item += ' - '
    data_item += ranEmail.genRanEmailAddr()
    data_item += ' - '
    data_item += ranEmail.genPassword()
    return data_item

def createNameCCN():
     # Just names and Credit Card numbers
     data_item = ""
     data_item = ranames.create_names(1)[0]
     data_item += ' - '
     data_item += ranCCN.genRanCCN()
     return data_item

def createNameSSNDob():
    data_item = ""
    data_item = ranames.create_names(1)[0]
    data_item += ' - '
    data_item += ranSSN.generate_invalid_ssn()
    data_item += ' - '
    data_item += ranDate.generate_random_date()
    return data_item

def createEmalPW():
    data_item = ""
    data_item += ranEmail.genRanEmailAddr()
    data_item += ' - '
    data_item += ranEmail.genPassword()
    return data_item

def main():

    data_set = []
    m = 15
    fname = "test_data.txt"
    adrfile = open(fname,'a') 

    if len(sys.argv) > 1:
        try:
            m = int(sys.argv[1])
        except:
            print("argument must be an integer\n")
            print("using default of 5\n")

    for _ in range(m):
        #target = createFullSet()
        #target = createNameCCN()
        #target = createNameSSNDob()
        target = createEmalPW()
        print(target)
        adrfile.write(target + '\n')

    adrfile.close()


if __name__ == '__main__':
	main()

