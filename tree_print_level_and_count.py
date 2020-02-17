"Traverse tree, count the nodes at a given level"

# This code will count the nodes at a given level.
# You can also, modify it to count the values at a
# certain level.
# To run on windows, bring up command prompt and do
# >python tree_print_level.py
class Node():
    '''This class defines a node on the tree'''

    def __init__(self, left, right, value):
        self.__left = left
        self.__right = right
        self.__value = value

    def get_left(self):
        '''Return the left leg of the node.'''
        return self.__left

    def set_left(self, left):
        '''Set the left leg of the node.'''
        self.__left = left

    def get_right(self):
        '''Return the right leg of the node'''
        return self.__right

    def set_right(self, right):
        '''Set the right leg of the node.'''
        self.__right = right

    def get_value(self):
        '''Get the value of the node.'''
        return self.__value

    def set_value(self, value):
        '''Set the value of the node.'''
        self.__value = value


def traverse(node, level, desired_level):
    '''
    This function gets called recursively. On each
    call it visits a new node on the tree.
    level - the level parameter is used to keep track
            of the level as we traverse the tree
    k - is constant. It is the desired level. We want
        to sum the number of nodes at this desired level
        (or sum of the values of the nodes at this level).
    '''

    left = 0
    right = 0

    if not node:
        return 0

    #print value and level - use for troubleshooting
    #print("value is ", node.get_value(), " level is ", level)

    if node.get_left():
        left = traverse(node.get_left(), level + 1, desired_level)

    if node.get_right():
        right = traverse(node.get_right(), level + 1, desired_level)


    # If you are at the desired level increment count
    # NOTE: it would be more efficient to check for this
    # above and return there, but to keep more clear on
    # what this exercise is, I just put it all here.

    if level == desired_level:
        #return left + right + 1
        return left + right + node.get_value()

    return left + right

def main():
    '''main creates tree, and runs tests'''

    # create tree for testing

    nodes = []

    for i in range(0, 10):
        nodes.append(Node(None, None, i))

    # add the legs
    nodes[6].set_left(nodes[8])
    nodes[6].set_right(nodes[9])
    nodes[3].set_left(nodes[6])
    nodes[4].set_left(nodes[7])
    nodes[2].set_left(nodes[4])
    nodes[2].set_right(nodes[5])
    nodes[1].set_left(nodes[2])
    nodes[1].set_right(nodes[3])

    # add desired level
    k = 2

    # run the test
    print("\nbasic functional test - level 2\n")
    total = traverse(nodes[1], 0, k)
    print("total is ", total)

    print("\nbasic functional test - level 3\n")
    k = 3
    total = traverse(nodes[1], 0, k)
    print("total is ", total)

    print("\nbasic functional test - level 1\n")
    k = 1
    total = traverse(nodes[1], 0, k)
    print("total is ", total)

    # test 1 node case
    print("\n\ntest case - one node in tree\n")
    nodes[1].set_left(None)
    nodes[1].set_right(None)
    k = 0
    total = traverse(nodes[1], 0, k)
    print("total is ", total)

    # test null case
    print("\n\ntest null case\n")
    traverse(None, 0, k)
    print("test complete")

if __name__ == '__main__':
    main()
   