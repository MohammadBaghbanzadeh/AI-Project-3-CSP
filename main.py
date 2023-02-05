from datetime import datetime
from groups import Groups
from hall import Hall
from algo import Algo


def return_solution(sol: dict) -> list:
    keys = sorted(sol.keys())
    arr = [sol[key] for key in keys]
    return arr


halls, groups = map(int, input().split())
preferences_list = [list(map(int, input().split())) for _ in range(groups)]
no_constraints = int(input())
constraints_list = [tuple(map(int, input().split())) for _ in range(no_constraints)]

halls_dict = {i: Hall(i) for i in range(1, halls + 1)}
groups_list = [Groups(i, None) for i in range(1, groups + 1)]

for i in range(len(groups_list)):
    groups_list[i].set_preferences(preferences_list[i])
    for preference in preferences_list[i]:
        the_hall = halls_dict[preference]
        the_hall.add_constraint(groups_list[i].group_number)

halls_list = [halls_dict[i] for i in range(1, halls + 1)]

x = Algo(groups_list, constraints_list)
most_constrained_hall = x.MRV(halls_list)
LCV_output = x.LCV(most_constrained_hall)

ans = input("Would you like to calculate with backtracking(b) or AC-3 algorithm(a), (b/a): ").lower()

if ans == 'b':
    new_halls_list = x.forward_checking(halls_list, most_constrained_hall, LCV_output[0])
    start = datetime.now()
    solution = x.backtrack(halls_list)
    end = datetime.now()
    if not solution:
        print("No")
    else:
        print(f"Backtracking solution is: {return_solution(solution)} and it takes: {end - start} seconds")
elif ans == 'a':
    if x.AC3(halls_list):
        start = datetime.now()
        solution = x.backtrack(halls_list)
        end = datetime.now()
        print(f"AC-3 solution is: {return_solution(solution)} and it takes: {end - start} seconds")
    else:
        print("No")

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
