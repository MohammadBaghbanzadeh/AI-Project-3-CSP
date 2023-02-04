from hall import *
import copy


class Algo:

    def __init__(self, groupsList, constraints_list):
        self.groupsList = groupsList
        self.constraints_list = constraints_list


    def MRV(self, hallList):
        mostConstrainedVariable = Hall("0", [])
        firstRound = True
        for hall in hallList:
            copiedHall = copy.deepcopy(hall)
            if not firstRound:
                if len(copiedHall.hall_constraints)<len(mostConstrainedVariable.hall_constraints):
                    mostConstrainedVariable = copiedHall
            else:
                mostConstrainedVariable = copiedHall
            firstRound = False

        return mostConstrainedVariable


    def LCV(self,hall):
        domainList = hall.hall_constraints
        domainListToWorkOn = []
        for groupNumber in domainList:
            for group in self.groupsList:
                if group.group_number == groupNumber:
                    domainListToWorkOn.append(group)

        sortedDomainOfGroups = sorted(domainListToWorkOn,key=lambda x: len(x.group_preferences), reverse=True)
        return [i.group_number for i in sortedDomainOfGroups]


    def forward_checking(self, hallList, assignedHall, assignedValue):
        conflicts = []
        newHallList = copy.deepcopy(hallList)
        hall = copy.deepcopy(assignedHall)
        for k, p in self.constraints_list:
            if hall.hall_number == k:
                conflicts.append(p)
            elif hall.hall_number == p:
                conflicts.append(k)
        for hall in newHallList:
            if hall.hall_number in conflicts:
                # print(assignedValue)
                if assignedValue in hall.hall_constraints:
                    hall.hall_constraints.remove(assignedValue)

        return newHallList
    
      def backtrack(self, halls_list, groups_list, constraints_list, assigned_halls=[]):
        
        if len(halls_list) == 0 or len(assigned_halls) == len(halls_list):

            hall_to_group = {hall_num: group for hall_num, group in assigned_halls}
            sorted_halls = sorted(hall_to_group.keys())
            return [hall_to_group[hall_num] for hall_num in sorted_halls]

        next_hall = self.MRV(halls_list)
        next_hall_domain = self.LCV(next_hall)
        for i in next_hall_domain:
            assigned_halls_copy =copy.deepcopy(assigned_halls)
            assigned_halls_copy.append((next_hall.hall_number, i))
            remaining_halls = self.forward_checking(halls_list, next_hall, i)
            solution = self.backtrack(remaining_halls, groups_list, constraints_list, assigned_halls_copy)
            if solution != False:
                return solution
        return False
            
