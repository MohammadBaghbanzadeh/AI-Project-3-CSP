
class Hall:

    def __init__(self, hall_number, hall_constraints):
            self.hall_number = hall_number
            self.hall_constraints = []
            if hall_constraints is not None:
                for constraint in hall_constraints:
                    self.hall_constraints.append(constraint)

    def add_constraint(self, constraint):
        self.hall_constraints.append(constraint)

    def __repr__(self):
        return f'Hall(hall_number={self.hall_number}, hall_constraints={self.hall_constraints})'
