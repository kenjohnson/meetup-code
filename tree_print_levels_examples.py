"Traverse binary tree, play around with levels"

# This is my core code used to show how to use parameters in the 
# traverse function. In this case, I use level . 
# This code shows examples of playing around with levels.
# For example, print all the values between two levels, 
# print values on even levels, print values on a certain
# level where the node has some specific value. 
# I can't run all examples at once, so I leave all but
# one example commented out.  Just uncomment the one
# you want to look at.  Make up your own example too. 
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


def traverse(node,level):
    '''
    This function gets called recursively. It
    visits each node, plays around with levels. Then it checks to see if
    it has a left leg, and if so, it traverses down the
    left leg. If it has no left leg or it finishes its left
    leg traversal, then it traverses down the right side.
    Finally it return to the root node, and then returns to
    the calling program.
    '''
    
    #print values between these two levels
    '''if level > 0 and level < 3:
        print("value is ", node.get_value(), " level is ", level)'''

    #print values on even levels
    '''if level % 2 == 0:
        print("value is ", node.get_value(), " level is ", level)'''

    #print values on level 2 where the values are even
    if level == 2 and node.get_value() % 2 == 0:
        print("value is ", node.get_value(), " level is ", level)

    if node.get_left():
        traverse(node.get_left(), level + 1)

    if node.get_right():
        traverse(node.get_right(), level + 1)

def main():
    ''' Creates the tree and runs the test cases'''
    
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
    
    # run the test
    traverse(ARR[1], 0)
    
    # test None case
    print()
    ARR[1].set_left(None)
    ARR[1].set_right(None)
    traverse(ARR[1],0)

if __name__ == '__main__':
   main()