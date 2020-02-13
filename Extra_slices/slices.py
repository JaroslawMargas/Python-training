nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

some_nums = nums[1:5]
print(some_nums)
# [2, 3, 4, 5]

first_fine = nums[:4]
print(first_fine)
# [1, 2, 3, 4]

rev_3_val = nums[-3:]
print(rev_3_val)
# [7, 8, 9]

n_th_element = nums[::2]
print(n_th_element)
# [1, 3, 5, 7, 9]

from_1th_n_th = nums[1::2]
print(from_1th_n_th)
# [2, 4, 6, 8]

rev_n_th = nums[-2::-1]
print(rev_n_th)
# [8, 7, 6, 5, 4, 3, 2, 1]

# [start:to:step]
from_min2_to_1_reverse = nums[-2:1:-1]
print(from_min2_to_1_reverse)
# [8, 7, 6, 5, 4, 3]