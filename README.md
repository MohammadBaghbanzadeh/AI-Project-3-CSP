# Project: Hall Allocation Problem
## Introduction

This project implements a solution to a Hall Allocation problem. The problem is to allocate a group of students to different halls of residency based on their preferences. This project solves the problem using two different algorithms: Backtracking and AC-3 (Arc Consistency Algorithm).
File Descriptions
## groups.py

This file contains the implementation of the Groups class. The Groups class represents a group of students and contains information about their group number and their preferences for different halls of residency. The class has the following methods:

    set_preferences(self, preferences): This method sets the preferences of a group of students.
    get_preferences(self): This method returns the preferences of a group of students.

## hall.py

This file contains the implementation of the Hall class. The Hall class represents a hall of residency and contains information about the hall number and the groups assigned to the hall. The class has the following methods:

    add_constraint(self, group_number): This method adds a constraint to a hall of residency, i.e. it adds a group of students to the hall.
    get_constraints(self): This method returns the constraints of a hall of residency, i.e. it returns the groups assigned to the hall.

## algo.py

This file contains the implementation of the Algo class. The Algo class implements the algorithms (Backtracking and AC-3) to solve the Hall Allocation problem. The class has the following methods:

    MRV(self, halls_list): This method implements the Minimum Remaining Value heuristic which returns the hall with the minimum number of remaining values.
    LCV(self, hall): This method implements the Least Constraining Value heuristic which returns the hall with the least number of constraining values.
    forward_checking(self, halls_list, most_constrained_hall, LCV_output): This method implements the forward checking algorithm which updates the domains of the halls.
    backtrack(self, halls_list): This method implements the backtracking algorithm which finds the solution to the Hall Allocation problem.
    AC3(self, halls_list): This method implements the AC-3 algorithm which checks the consistency of the halls.

## main.py

This file is the main file which uses the classes implemented in the previous files to solve the Hall Allocation problem. The file first takes the input of the number of halls and the number of groups, followed by the preferences of the groups and the constraints on the halls. The file then asks the user if they want to solve the problem using the Backtracking algorithm or the AC-3 algorithm. Based on the user's choice, the corresponding algorithm is implemented and the solution is displayed along with the time taken to find the solution. The file also has a helper function return_solution(sol) which formats the solution in a readable manner.
## Conclusion

This project provides a solution to the Hall Allocation problem using two different algorithms, Backtracking and AC-3. The solution takes into account the preferences of the groups and the constraints on the halls to find the optimal allocation. The project can be further improved by implementing more advanced algorithms to solve the problem.
