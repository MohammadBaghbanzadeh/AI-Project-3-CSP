from hall import *
import copy


class Algo:

    # constructor with groups list and constraints list as parameters
    def __init__(self, groupsList, constraints_list):
        self.groupsList = groupsList
        self.constraints_list = constraints_list

    # a function to find the hall with most constraints
    def MRV(self, hallList):
        # setting the first hall as the most constrained variable
        mostConstrainedVariable = Hall("0", [])
        firstRound = True
        # looping through the halls list
        for hall in hallList:
            # copying the hall to avoid changing the original hall (passed by reference)
            copiedHall = copy.deepcopy(hall)
            if not firstRound:
                # checking if the current hall has less constraints than the most constrained variable
                if len(copiedHall.hall_constraints) < len(mostConstrainedVariable.hall_constraints):
                    mostConstrainedVariable = copiedHall
            else:
                mostConstrainedVariable = copiedHall
            # setting the first round to false after first round of looping
            firstRound = False
        # returning the most constrained variable
        return mostConstrainedVariable

    # a function to find the group with least preferences in the domain of the most constrained variable
    def LCV(self, hall):
        domainList = hall.hall_constraints
        domainListToWorkOn = []
        for groupNumber in domainList:
            for group in self.groupsList:
                if group.group_number == groupNumber:
                    domainListToWorkOn.append(group)
        # sorting the domain of the most constrained variable according to the number of preferences in descending order
        sortedDomainOfGroups = sorted(domainListToWorkOn, key=lambda x: len(x.group_preferences), reverse=True)
        # returning the sorted list of groups
        return [i.group_number for i in sortedDomainOfGroups]

    # a function to remove the assigned value from the domain of the other variables
    def forward_checking(self, hallList, assignedHall, assignedValue):
        conflicts = []
        # copying the halls list to avoid changing the original halls list (passed by reference)
        newHallList = copy.deepcopy(hallList)
        hall = copy.deepcopy(assignedHall)
        # finding the halls that are connected to the assigned hall
        for k, p in self.constraints_list:
            if hall.hall_number == k:
                conflicts.append(p)
            elif hall.hall_number == p:
                conflicts.append(k)
        # removing the assigned value from the domain of the connected halls
        for hall in newHallList:
            if hall.hall_number in conflicts:
                if assignedValue in hall.hall_constraints:
                    hall.hall_constraints.remove(assignedValue)
        # returning the new halls list
        return newHallList
    
      # def backtrack(self, halls_list, groups_list, constraints_list, assigned_halls=[]):
      #
      #   if len(halls_list) == 0 or len(assigned_halls) == len(halls_list):
      #       return  [group for hall, group in assigned_halls]
      #
      #   next_hall = self.MRV(halls_list)
      #   next_hall_domain = self.LCV(next_hall)
      #   for i in next_hall_domain:
      #       assigned_halls_copy =copy.deepcopy(assigned_halls)
      #       assigned_halls_copy.append((next_hall.hall_number, i))
      #       remaining_halls = self.forward_checking(halls_list, next_hall, i)
      #       solution = self.backtrack(remaining_halls, groups_list, constraints_list, assigned_halls_copy)
      #       if solution != False:
      #           return solution
      #   return False

