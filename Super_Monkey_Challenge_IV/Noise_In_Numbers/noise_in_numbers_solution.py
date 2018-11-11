"""
Problem Approach:
    Create a Fan class that records an index, team, and set of followers for every given Fan instance.
    Create a tree of Fan nodes, which begins at 'None'. Connect 'None' to all the Fans with no followers.
    Now connect all of the fans to their followers, until all fans are on the tree.
    Now execute a max() function that evaluates the maximum possible value for each branch of the tree (noting that
    the maximum can be zero, if all fans are POP fans)
    The max function will evaluate the maximum of a fan as follows:
        1. If the Fan has no child nodes, the maximum is itself, or zero (whichever is larger). (Side Note: A POP fan
        evaluates itself as -1, and an ION fan as +1, considering it has no children. The evaluation is the ION-POP
        for the node and all its childrend)
        2. If the Fan has children nodes, recursively call max() on its children nodes, and return the maximum of:
            The node's evaluation
            The sum of all of the children's maximums (Note: This will always be a non-negative number, since a node's
            max is at least zero, the case where the node shouldn't be invited.)
    Once the maximum reaches the 'None' node (the root of the tree) the max() function should execute one last time,
    resulting in the answer.

"""


class Fan:
    def __init__(self, index, team):
        self.index = index
        self.team = team
        self.evaluation = None
        self.parent = None
        self.maximum = 0
        self.children = set()

    def add_child(self, fan):
        self.children.add(fan)

    def set_parent(self, parent):
        self.parent = parent  # the compiler will never know

    def isleaf(self):
        return not self.children

    def evaluate(self):
        if self.team is None:  # Check if evaluating the root
            self.evaluation = sum(child.evaluation for child in self.children)  # Case where everyone is invited
        elif self.evaluation is None:
            self.evaluation = sum(child.evaluation for child in self.children) + int(1 if self.team is 1 else -1)
        return self.evaluation

    def get_max(self):
        if self.maximum:
            return self.maximum
        elif self.isleaf():
            self.maximum = max(0, self.evaluation)
        else:
            self.maximum = max(self.evaluation, sum(child.maximum for child in self.children))

        return self.maximum

    def __repr__(self):
        return "<Fan " + str(self.index) + ">"


root = Fan(0, None)  # The root of the tree
fan_list = [root]
for p in range(int(input())):
    following, team = [int(i) for i in input().split()]
    add_fan = Fan(p+1, team)
    parent = fan_list[following]
    add_fan.set_parent(parent)
    parent.add_child(add_fan)
    fan_list.append(add_fan)

for fan in range(len(fan_list)-1, -1, -1):  # Evaluate all nodes from the bottom of the tree up to minimize recursion
    fan_list[fan].evaluate()
    fan_list[fan].get_max()

print(root.maximum)

