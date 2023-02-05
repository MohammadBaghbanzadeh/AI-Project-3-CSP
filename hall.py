
class Hall:

    # # constructor with hall number and constraints as parameters
    def __init__(self, hall_number, hall_constraints):
            self.hall_number = hall_number
            self.hall_constraints = []
            if hall_constraints is not None:
                for constraint in hall_constraints:
                    self.hall_constraints.append(constraint)

    # a function to add constraints to halls
    def add_constraint(self, constraint):
        self.hall_constraints.append(constraint)

    # a function to show the constraints and the number of halls
    def __repr__(self):
        return f'Hall(hall_number={self.hall_number}, hall_constraints={self.hall_constraints})'
