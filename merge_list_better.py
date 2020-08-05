import heapq

class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __lt__( self, other):
    return self.value < other.value

def merge_lists(lists):
 
  temp = []  # holds minimum heap 
  resultHead = None 
 
  # initialize - take first element from every list, and put it on a temp list.
  for first_node in lists:
    if first_node is not None:
      temp.append(first_node )
  
  heapq.heapify(temp)
  
  while (temp ): 
 
    # get the node with the lowest value from the heap and
    # add it to the result.
    node = heapq.heappop(temp)
    if resultHead is None:
      resultHead = node
      resultTail = node
    else: 
      resultTail.next = node
      resultTail = resultTail.next
  
    # now push the node's next element onto temp,
    if node.next != None:
      heapq.heappush(temp, node.next) # push onto heap 
      
  return resultHead


def main():
  
  l1 = ListNode(2)
  l1.next = ListNode(6)
  l1.next.next = ListNode(8)

  l2 = ListNode(3)
  l2.next = ListNode(6)
  l2.next.next = ListNode(7)
 
  l3 = ListNode(1)
  l3.next = ListNode(3)
  l3.next.next = ListNode(4)  
 
  result = merge_lists([l1, l2, l3])

  while result is not None:
    print (result.value, " ", end='')
    result = result.next 
main()