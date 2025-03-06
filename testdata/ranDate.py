import random
import sys
from datetime import datetime, timedelta

def generate_random_date():
    #Generates a random date between two specfic dates
    start_date = datetime(1700, 1, 1)
    end_date = datetime(1907, 12, 31)
    
    # Generate a random number of days between start and end dates
    random_days = random.randint(0, (end_date - start_date).days)
    
    # Calculate the random date
    random_date = start_date + timedelta(days=random_days)

    pickFormat = random.randint(0,1)
    if pickFormat == 0:
        retval = random_date.strftime("%Y-%m-%d")
    elif pickFormat == 1:
        retval = random_date.strftime("%m/%d/%Y")
    
    return retval

# Example usage:
print(generate_random_date())

def main():
    form = 'd'
    m = 5
    fname = "random_dates.txt"
    adrfile = open(fname,'a') 

    if len(sys.argv) > 1:
        try:
            m = int(sys.argv[1])
        except:
            print("argument must be an integer\n")
            print("using default of 5\n")

    for _ in range(m):
        rDate = (generate_random_date())
        print(rDate)
        adrfile.write(rDate  + '\n')
    
    adrfile.close()


if __name__ == '__main__':
	main()