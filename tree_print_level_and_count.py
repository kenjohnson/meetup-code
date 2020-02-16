"Traverse tree, count the nodes at a given level"

# This code will count the nodes at a given level. 
# You can also, modify it to count the values at a
# certain level. 
# To run on windows, bring up command prompt and do
# >python tree_print_level.py
class Node():
    '''This class defines a node on the tree'''

    def __init__(self, left, right, value):
        self.__left = None
        self.__right = None
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


def traverse(node,level, k):
    '''
    This function gets called recursively. On each
    call it visits a new node on the tree. 
    level - the level parameter is used to keep track
            of the level as we traverse the tree
    k - is constant. It is the desired level. We want
        to sum the number of nodes at this desired level
        (or sum of the values of the nodes at this level).
    '''

    #print value and level 
    print("value is ", node.get_value(), " level is ", level)
    
    left = 0
    right = 0

    if node.get_left():
        left = traverse(node.get_left(), level + 1, k)
        
    if node.get_right():
        right = traverse(node.get_right(), level + 1, k)
    
    if level == k:    
        return left + right + 1
        #return left + right + node.get_value()
    else:
        return left + right

def main():
    
    # create tree for testing

    ARR = []

    for i in range(0, 10):
        ARR.append(Node(None, None, i))

    # add the legs
    ARR[6].set_left(ARR[8])
    ARR[6].set_right(ARR[9])
    ARR[3].set_left(ARR[6])
    ARR[4].set_left(ARR[7])
    ARR[2].set_left(ARR[4])
    ARR[2].set_right(ARR[5])
    ARR[1].set_left(ARR[2])
    ARR[1].set_right(ARR[3])
    
    
    k = 2   # the desired level 
    
    # run the test
    sum = traverse(ARR[1], 0, k)
    print("sum is ", sum)

    # test None case
    print()
    ARR[1].set_left(None)
    ARR[1].set_right(None)
    traverse(ARR[1],0, k)

if __name__ == '__main__':
   main()