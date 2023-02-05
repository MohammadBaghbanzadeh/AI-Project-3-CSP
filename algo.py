import copy
#
#
# class Algo:
#
#     def __init__(self, groupsList, constraints_list):
#         self.groupsList = groupsList
#         self.constraints_list = constraints_list
#
#     def MRV(self, hallList):
#         return sorted(hallList, key=lambda h: len(h.hall_constraints))[0]
#
#     def LCV(self, hall):
#         # Get the list of constraints for the current hall
#         domain_list = hall.hall_constraints
#
#         # Sort the list of groups whose group number is in the domain list of the hall
#         # Sort the list based on the length of the group's preferences (in descending order)
#         sorted_domain_of_groups = sorted(
#             [group for group in self.groupsList if group.group_number in domain_list],
#             key=lambda x: len(x.group_preferences),
#             reverse=True
#         )
#
#         # Return a list of group numbers sorted by the LCV heuristic
#         return [group.group_number for group in sorted_domain_of_groups]
#
#     def forward_checking(self, hall_list, assigned_hall, assigned_value):
#         # Create a list to store the conflicting halls
#         conflicts = []
#
#         # Create a deep copy of the input hall list
#         new_hall_list = copy.deepcopy(hall_list)
#
#         # Iterate over the constraints list
#         for k, p in self.constraints_list:
#             # If the assigned hall number is the first constraint, append the second constraint to conflicts list
#             if assigned_hall.hall_number == k:
#                 conflicts.append(p)
#             # If the assigned hall number is the second constraint, append the first constraint to conflicts list
#             elif assigned_hall.hall_number == p:
#                 conflicts.append(k)
#
#         # Iterate over the new hall list
#         for hall in new_hall_list:
#             # If the current hall number is in the conflict list and the assigned value is in the hall's constraints,
#             # remove the assigned value from the hall's constraints
#             if hall.hall_number in conflicts and assigned_value in hall.hall_constraints:
#                 hall.hall_constraints.remove(assigned_value)
#
#         # Return the updated hall list
#         return new_hall_list
#
#     def backtrack(self, halls_list, groups_list, constraints_list, assigned_halls=None):
#         if assigned_halls is None:
#             assigned_halls = []
#         if len(halls_list) == 0 or len(assigned_halls) == len(halls_list):
#             return [group for hall, group in assigned_halls]
#
#         next_hall = self.MRV(halls_list)
#         next_hall_domain = self.LCV(next_hall)
#         for i in next_hall_domain:
#             assigned_halls_copy = copy.deepcopy(assigned_halls)
#             assigned_halls_copy.append((next_hall.hall_number, i))
#             remaining_halls = self.forward_checking(halls_list, next_hall, i)
#             solution = self.backtrack(remaining_halls, groups_list, constraints_list, assigned_halls_copy)
#             if solution:
#                 return solution
#         return False
#

import queue

import copy
from collections import deque


class Algo:

    def __init__(self, groupsList, constraints_list):
        self.groupsList = groupsList
        self.constraints_list = constraints_list

    def MRV(self, hallList):
        return sorted(hallList, key=lambda h: len(h.hall_constraints))[0]

    def LCV(self, hall):
        # Get the list of constraints for the current hall
        domain_list = hall.hall_constraints

        # Sort the list of groups whose group number is in the domain list of the hall
        # Sort the list based on the length of the group's preferences (in descending order)
        sorted_domain_of_groups = sorted(
            [group for group in self.groupsList if group.group_number in domain_list],
            key=lambda x: len(x.group_preferences),
            reverse=True
        )

        # Return a list of group numbers sorted by the LCV heuristic
        return [group.group_number for group in sorted_domain_of_groups]

    def forward_checking(self, hall_list, assigned_hall, assigned_value):
        # Create a list to store the conflicting halls
        conflicts = []

        # Create a deep copy of the input hall list
        new_hall_list = copy.deepcopy(hall_list)

        # Iterate over the constraints list
        for k, p in self.constraints_list:
            # If the assigned hall number is the first constraint, append the second constraint to conflicts list
            if assigned_hall.hall_number == k:
                conflicts.append(p)
            # If the assigned hall number is the second constraint, append the first constraint to conflicts list
            elif assigned_hall.hall_number == p:
                conflicts.append(k)

        # Iterate over the new hall list
        for hall in new_hall_list:
            # If the current hall number is in the conflict list and the assigned value is in the hall's constraints,
            # remove the assigned value from the hall's constraints
            if hall.hall_number in conflicts and assigned_value in hall.hall_constraints:
                hall.hall_constraints.remove(assigned_value)

        # Return the updated hall list
        return new_hall_list

    def is_valid(self, hall, group_number, assigned_halls):
        for assigned_hall, assigned_group in assigned_halls:
            if (hall, assigned_hall) in self.constraints_list or (assigned_hall, hall) in self.constraints_list:
                if group_number == assigned_group:
                    return False
        return True

    # def backtrack(self, halls_list, groups_list, constraints_list, assigned_halls=None):
    #     print(f"in BT halls_list is: {halls_list} and group_list is: {groups_list} and constraints is: {constraints_list}")
    #     if assigned_halls is None:
    #         assigned_halls = []
    #     if len(halls_list) == 0 or len(assigned_halls) == len(halls_list):
    #         return [group for hall, group in assigned_halls]
    #
    #     next_hall = self.MRV(halls_list)
    #     for i in self.LCV(next_hall):
    #         assigned_halls_copy = copy.deepcopy(assigned_halls)
    #         assigned_halls_copy.append((next_hall.hall_number, i))
    #         remaining_halls = self.forward_checking(halls_list, next_hall, i)
    #         solution = self.backtrack(remaining_halls, groups_list, constraints_list, assigned_halls_copy)
    #         print(f"solution: ", solution)
    #         if solution:
    #             return solution
    #     return False

    def backtrack(self, halls_list, assigned_halls=None):
        if assigned_halls is None:
            assigned_halls = {}

        # If all halls have been assigned a group, return the assigned_halls dictionary
        if len(assigned_halls) == len(halls_list):
            return assigned_halls

        # Choose an unassigned hall using MRV (Minimum Remaining Values) heuristic
        unassigned_hall = self.MRV([hall for hall in halls_list if hall.hall_number not in assigned_halls])

        # Get the list of groups that are available for the chosen hall using LCV (Least Constraining Value) heuristic
        group_domain = self.LCV(unassigned_hall)

        for group in group_domain:
            # Make a deep copy of the assigned_halls dictionary
            assigned_halls_copy = copy.deepcopy(assigned_halls)

            # Assign the current group to the chosen hall
            assigned_halls_copy[unassigned_hall.hall_number] = group

            # Use forward checking to eliminate invalid values from the domains of other unassigned halls
            updated_halls_list = self.forward_checking(halls_list, unassigned_hall, group)

            # Recursively call the backtrack function with the updated halls list and assigned_halls dictionary
            solution = self.backtrack(updated_halls_list, assigned_halls_copy)

            # If a solution is found, return it
            if solution:
                return solution

        # If no solution is found, return False
        return False

    def AC3(self, halls_list, assigned_halls=None):
        if assigned_halls is None:
            assigned_halls = []
        queue = deque([(xi, xj) for xi in halls_list for xj in halls_list if xi != xj and xj in xi.hall_constraints])
        while queue:
            xi, xj = queue.popleft()
            if self.revise(xi, xj, assigned_halls):
                if len(xi.hall_constraints) == 0:
                    return False
                for xk in halls_list:
                    if xk != xi and xk != xj:
                        queue.append((xk, xi))
        return True

    def revise(self, xi, xj, assigned_halls):
        revised = False
        for x in xi.hall_constraints:
            if not any(self.is_valid(x, y, assigned_halls) for y in xj.hall_constraints):
                xi.hall_constraints.remove(x)
                revised = True
        return revised