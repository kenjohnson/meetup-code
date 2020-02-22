"Traverse tree"

# Print the mirror image of this binary tree
# To run on windows, bring up command prompt and do
# >python tree_print_mirror.py
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
    This function gets called recursively. For each node it
    reverses the left and right legs, thus creating a mirror
    image of the node. Then it calls itself with the next node
    and does the same thing.  It keeps calling itself until it
    has traversed the whole tree.
    '''

    if not node:
        return

    # swap the left and right leg
    tmp = Node(None, None, None)
    tmp = node.get_left()
    node.set_left(node.get_right())
    node.set_right(tmp)

    #print the node value
    print(node.get_value())

    if node.get_left():
        traverse(node.get_left())

    if node.get_right():
        traverse(node.get_right())


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
    print("\ntest case - print the whole tree")
    traverse(nodes[1])

    # test None case
    print("\ntest case - print 1 node")
    nodes[1].set_left(None)
    nodes[1].set_right(None)
    traverse(nodes[1])

    # test Null case
    print("\ntest case - null ")
    traverse(None)

    print("tests completed")

if __name__ == '__main__':
    main()
    