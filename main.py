from groups import Groups
from hall import *
from algo import *

halls, groups = map(int, input().split(" "))
preferences_list = [list(map(int, input().split(" "))) for i in range(groups)]
No_constraints = int(input())
constraints_list = [tuple(map(int, input().split(" "))) for i in range(No_constraints)]

halls_dict = {i: Hall(i) for i in range(1, halls + 1)}
groups_list = [Groups(i, None) for i in range(1, groups + 1)]

for i in range(len(groups_list)):
    groups_list[i].set_preferences(preferences_list[i])
    for preference in preferences_list[i]:
        the_hall = halls_dict[preference]
        the_hall.add_constraint(groups_list[i].group_number)

halls_list = [halls_dict[i] for i in range(1, halls + 1)]
for i in halls_list:
    print("domain of hall", i.hall_number, ":", i.hall_constraints)
x = Algo(groups_list, constraints_list)

# MRV returns the most constrained variable
mostConstrainedHall = x.MRV(halls_list)
print("-" * 10, "\nMost Constrained Hall is: ")
print(mostConstrainedHall.hall_number, "\n", "-" * 10)

# LCV returns a sorted list of groups according to the number of their preferences in descending order
LCVOutput = x.LCV(mostConstrainedHall)
print("lcv output: ")
print(LCVOutput)
print("-" * 10)

print("constraints list is: \n", constraints_list)
print("-" * 10)

# give the ith LCVOutput as the assigned value
# new_halls_list = x.forward_checking(halls_list, mostConstrainedHall, LCVOutput[0])
# solution = x.backtrack(halls_list)
#
# if not solution:
#     print("No")
# else:
#     print(f"backtracking solurion is: ", solution)

# for hall in new_halls_list:
#     print(f"domain of hall {hall.hall_number}: {hall.hall_constraints}")

# Call the AC3 method on the instance
if x.AC3(halls_list):
    # Call the backtrack method on the instance
    solution = x.backtrack(halls_list)
    keys = sorted(solution.keys())
    for key in keys:
        print(solution[key], end= ' ')
else:
    print("No solution found")

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
