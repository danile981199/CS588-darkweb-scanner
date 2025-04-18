# Generate a rando US based phone number
import random
import sys

def generate_us_phone_number(form):
    area_codes = [201, 202, 203, 205, 206, 207, 208, 209, 210, 212, 213, 214, 215, 216, 217, 218, 219, 220, 223, 224, 225, 227, 228, 229, 231, 234, 239, 240, 248, 251, 252, 253, 254, 256, 260, 262, 267, 269, 270, 272, 274, 276, 281, 301, 302, 303, 304, 305, 307, 308, 309, 310, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 323, 325, 327, 330, 331, 332, 334, 336, 337, 339, 346, 351, 352, 360, 361, 364, 380, 385, 386, 401, 402, 404, 405, 406, 407, 408, 409, 410, 412, 413, 414, 415, 417, 419, 423, 425, 430, 432, 434, 435, 440, 442, 443, 458, 463, 464, 469, 470, 475, 478, 479, 480, 484, 501, 502, 503, 504, 505, 507, 508, 509, 510, 512, 513, 515, 516, 517, 518, 520, 530, 531, 534, 539, 540, 541, 551, 559, 561, 562, 563, 564, 567, 570, 571, 573, 574, 575, 580, 585, 586, 601, 602, 603, 605, 606, 607, 608, 609, 610, 612, 614, 615, 616, 617, 618, 619, 620, 623, 626, 628, 629, 630, 631, 636, 641, 646, 650, 651, 657, 660, 661, 662, 667, 669, 678, 681, 682, 701, 702, 703, 704, 706, 707, 708, 712, 713, 714, 715, 716, 717, 718, 719, 720, 724, 725, 727, 731, 732, 734, 737, 740, 743, 747, 754, 757, 760, 762, 763, 765, 769, 770, 772, 773, 774, 775, 779, 781, 785, 786, 801, 802, 803, 804, 805, 806, 808, 810, 812, 813, 814, 815, 816, 817, 818, 828, 830, 831, 832, 843, 845, 847, 848, 850, 854, 856, 857, 858, 859, 860, 862, 863, 864, 865, 870, 872, 878, 901, 903, 904, 906, 907, 908, 909, 910, 912, 913, 914, 915, 916, 917, 918, 919, 920, 925, 928, 929, 930, 931, 934, 936, 937, 938, 940, 941, 945, 947, 949, 951, 952, 954, 956, 959, 970, 971, 972, 973, 978, 979, 980, 984, 985, 986, 989]

    area_code = random.choice(area_codes)
    co_code = random.randint(200, 999)  # Cannot start with 0 or 1
    s_number = random.randint(1000, 9999)

    form = form.lower()
    if (form != 'd') and (form != 'p') and (form != 'n'):
        form = 'p'

    if 'p' == form:
        return f"({area_code}) {co_code}-{s_number}"
    elif 'd' == form:
        return f"{area_code}-{co_code}-{s_number}"
    else:
        return f"{area_code}{co_code}{s_number}"

def gen_pn_2():
    choice = random.randint(0,3)
    if 0 == choice:
        return generate_us_phone_number('d')
    elif 1 == choice:
        return generate_us_phone_number('p')
    else:
        return generate_us_phone_number('n')

def main():
    # Generate and print  random US phone numbers

    m = 10
    # 'p' will format the area code with parens by default. use 'd' for all dashes and no spaces
    # 'n' will list number with no special characters and no spaces, just a 10 digit number
    format = 'p' 
    if len(sys.argv) > 1:
        try:
            m = int(sys.argv[1])
        except:
            print("argument must be an integer\n")
            print("using default of 10\n")

    fname = 'phoneNums.txt'
    pnfile = open(fname,'a')

    for _ in range(m):
        pn = generate_us_phone_number(format)
        print(pn)
        pnfile.write(pn + '\n')

    pnfile.close()

if __name__ == '__main__':
	main()
