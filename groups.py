class Groups:

    def __init__(self, group_number, group_preferences):
        if group_preferences is None:
            self.group_number = group_number
            self.group_preferences = None
        else:
            self.group_number = group_number
            self.group_preferences = group_preferences

    # def find_group(number, groups_list):
    #     for i in groups_list:
    #         if i.number == number:
    #             return i

    def set_preferences(self, preferences):
        self.group_preferences = preferences

    def __repr__(self):
        return f'Groups(group_number={self.group_number}, group_preferences={self.group_preferences})'