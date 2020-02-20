"Traverse tree"

# Print the sum of the nodes on this binary tree.
# To run on windows, bring up command prompt and do
# >python tree_print_count.py
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


def traverse(node):
    '''
    This function gets called recursively. It
    visits each node, and prints the value. Then it checks to see if
    it has a left leg, and if so, it traverses down the
    left leg. If it has no left leg or it finishes its left
    leg traversal, then it traverses down the right side.
    At the end of this function it adds the value returned
    from the left side traversal and the value returned from
    the right side traversal, and adds a value of 1 to it.
    This is how it counts the number of nodes in the tree.
    '''

    left = 0
    right = 0

    if not node:
        return 0

    print(node.get_value())

    if node.get_left():
        left = traverse(node.get_left())

    if node.get_right():
        right = traverse(node.get_right())

    return left + right + 1


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

    # run the test
    print("\ntest case - whole tree, print nodes and count of nodes")
    total = traverse(nodes[1])
    print("\nNumber of nodes is: ", total)

    # test None case
    print("\ntest case - 1 node, print node and count")
    nodes[1].set_left(None)
    nodes[1].set_right(None)
    total = traverse(nodes[1])
    print("\nNumber of nodes is: ", total)

    print("tests completed")

if __name__ == '__main__':
    main()
    