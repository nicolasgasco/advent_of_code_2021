# First part

def list_from_file(file):
    """Create a list from a file"""
    bins_list = []
    with open(file) as f:
        bins = f.readlines()

    for bin in bins:
        bins_list.append(bin.strip())
    f.close()
    return bins_list


def bin_to_dec(string):
    """Convert from string to 0s and 1s to decimal number"""
    result = 0
    mult = 1
    for i in range(1, len(string) + 1):
        result += int(string[-i]) * mult
        mult = 2**(i)
    return result


gamma = ""
epsilon = ""

bins = list_from_file("day_3_input")
len_bin = len(bins)
for i in range(len(bins[0])):
    sum = 0
    for bin in bins:
        sum += int(bin[i])
    if sum > (len_bin / 2):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"


output = open("day_3_output_part_1", "w")
output.write(str(bin_to_dec(gamma) * bin_to_dec(epsilon)))
output.close()

# Part 2

# Find oxigen
def filter_list(ref, most, least):
    """Filter list till you have only one element"""
    lst = ref.copy()
    while (len(lst) != 1):
        for i in range(len(lst[0])):
            sum = 0
            for bin in lst:
                sum += int(bin[i])
            if sum >= (len(lst) / 2):
                bit_criteria = most
            else:
                bit_criteria = least
            lst = [bin for bin in lst if bin[i] == bit_criteria]
            if len(lst) == 1:
                return bin_to_dec(lst[0])


oxygen = filter_list(bins.copy(), "1", "0")
co2 = filter_list(bins, '0', '1')

output = open("day_3_output_part_2", "w")
output.write(str(co2 * oxygen))
output.close()