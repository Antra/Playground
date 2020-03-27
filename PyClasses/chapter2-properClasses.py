import random


class MSDie:
    '''
    Multi-sided die

    Instance Variables:
        current_value
        num_sides
        history

    '''

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.history = list()
        self.current_value = self.roll()

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        # a good repr makes it easier to debug with simple print statements
        return "MSDie({}): {}".format(self.num_sides, self.current_value)

    def __eq__(self, other):
        # basic equal comparison
        return self.current_value == other.current_value

    def __ne__(self, other):
        # basic not-equal comparison
        return self.current_value != other.current_value

    def __lt__(self, other):
        # basic less than comparison
        return self.current_value < other.current_value

    def __le__(self, other):
        # basic less than or equal comparison
        return self.current_value <= other.current_value

    def __gt__(self, other):
        # basic greater than comparison
        return self.current_value > other.current_value

    def __ge__(self, other):
        # basic greater than or equal comparison
        return self.current_value >= other.current_value

    def roll(self):
        self.current_value = random.randint(1, self.num_sides)
        self.history.append(self.current_value)
        return self.current_value

    def hist(self):
        return str(self.history)


my_die = MSDie(6)

for i in range(5):
    print(my_die)
    my_die.roll()

d_list = [MSDie(6), MSDie(20)]
print(d_list)
print()


shaker = [MSDie(6), MSDie(6), MSDie(6), MSDie(6), MSDie(6), MSDie(6)]

for i in range(5):
    for die in shaker:
        die.roll()

for i in range(len(shaker)):
    print(f'Die #{i+1} has rolled: {shaker[i].hist()}')
