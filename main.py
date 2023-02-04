from groups import Groups
from hall import *
from algo import *


def find_hall(number, halls_list):
    for hall in halls_list:
        if hall.hall_number == number:
            return hall


halls, groups = input().split(" ")
halls = int(halls)
groups = int(groups)
preferences_list = []


for i in range(0, groups):
    preferences_list.append(input())

No_constraints = int(input())

constraints_list = []


for i in range(0, No_constraints):
    constraints_list.append(tuple([int(i) for i in input().split()]))

halls_constraints = {}

new_list = []

for i in preferences_list:
    new_list.append(i.split(" "))

halls_list = []

for i in range(1, halls + 1):
    halls_list.append(Hall(i, None))

# print(halls_list)

groups_list = []

for i in range(1, groups + 1):
    groups_list.append(Groups(i, None))

preferences_list_int = []

# print(groups_list)

for i in new_list:
        int_list = [int(x) for x in i]
        preferences_list_int.append(int_list)


# print(preferences_list_int)


for i in range(len(groups_list)):
    the_group = groups_list[i]
    the_preference = preferences_list_int[i]
    the_group.set_preferences(the_preference)
    for preference in the_preference:
        the_hall = find_hall(preference, halls_list)
        the_hall.add_constraint(the_group.group_number)


# print(preferences_list)
# # print(new_list)
# # print(constraints_list)
# print(halls_list[1].hall_constraints)
# print(halls_list[2].hall_number)
# print(halls_list)
# print(groups_list)
[print("domain of hall", i.hall_number, ":", i.hall_constraints) for i in halls_list]
x = Algo(groups_list,constraints_list)
# MRV returns the most constrained variable
mostConstrainedHall = x.MRV(halls_list)
print(mostConstrainedHall.hall_number)
# LCV returns a sorted list of groups according to the number of their preferences in descending order
LCVOutput = x.LCV(mostConstrainedHall)
print(LCVOutput)

print(constraints_list)
# give the ith LCVOutput as the assigned value
newHallsList = x.forward_checking(halls_list, mostConstrainedHall, LCVOutput[0])
solution = x.backtrack(halls_list, groups_list, constraints_list)
if solution == False:
    print("No")
else:
    print(solution)


[print("domain of hall", i.hall_number, ":", i.hall_constraints) for i in newHallsList]



""""
6 3
1 4 6
1 2 3 5 6
3 4 5
5
1 2
2 3
3 4
3 5
3 6
"""

"""
7 5
2 3 1 5
2 7 4 5
4 6 2
3 2 1
4 5 6
8
7 4
7 5
3 4
2 7
6 5
5 2
1 7
6 3
1 5
"""

# if __name__ == '__main__':
