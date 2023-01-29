# -

from ctypes import Union


set_list =[[],[],[],[],[],[],[],[]]

prime_set = [2,3,5,7,11,13,17,19]

it = 0
for i in prime_set:
    for j in range(2,1001,1):
        if j % i == 0:
            set_list[it].append(j)
    it += 1

set3 = set(set_list[0])
set5 = set(set_list[1])
set7 = set(set_list[2])
set11 = set(set_list[3])
set13 = set(set_list[4])
set17 = set(set_list[5])
set19 = set(set_list[6])

#final_set = set()
final_set = set().union(set3,set5,set7,set11,set13,set17,set19)
print("the length of final set is : ", len(final_set), "\n the set is : \n", final_set)

    