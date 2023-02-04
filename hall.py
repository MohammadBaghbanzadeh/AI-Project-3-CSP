
class Hall:

    def __init__(self, hall_number, hall_constraints):
        if hall_constraints is None:
            self.hall_number = hall_number
            self.hall_constraints = []

        else:
            self.hall_number = hall_number
            self.hall_constraints = []

    # @classmethod
    # def hall_number(cls):
    #     return cls

    # def hall_set_constraint(self, constraints):
    #     self.hall_constraints = constraints

    def add_constraint(self, constraint):
        self.hall_constraints.append(constraint)

    def __repr__(self):
        return f'Hall(hall_number={self.hall_number}, hall_constraints={self.hall_constraints})'
