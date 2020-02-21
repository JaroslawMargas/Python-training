value = 67


# [1, 0, 0, 0, 0, 1, 1]

def check_n(val):
    i = 0
    while True:
        if 2 ** i > val:
            max_factor = i
            return max_factor - 1
        else:
            i += 1


factor = check_n(value)
bin_tab = []
sum_bin = 0
bin_tab2 = []

for x in range(factor, -1, -1):
    tmp = 2 ** x
    if sum_bin + tmp <= value:
        bin_tab.append(1)
        sum_bin += tmp
    else:
        bin_tab.append(0)
print(bin_tab)

#####

while True:
    while value > 0:
        if value % 2 == 0:
            bin_tab2.append(0)
        else:
            bin_tab2.append(1)
        value = int(value // 2)
    else:
        bin_tab2 = bin_tab2[::-1]
        print(bin_tab2)
        break
