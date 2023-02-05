
class Groups:

    # constructor with group number and preferences as parameters
    def __init__(self, group_number, group_preferences):
        if group_preferences is None:
            self.group_number = group_number
            self.group_preferences = None
        else:
            self.group_number = group_number
            self.group_preferences = group_preferences

    # a function to set the preferences of groups
    def set_preferences(self, preferences):
        self.group_preferences = preferences

    # a function to show the preferences and the number of groups
    def __repr__(self):
        return f'Groups(group_number={self.group_number}, group_preferences={self.group_preferences})'
