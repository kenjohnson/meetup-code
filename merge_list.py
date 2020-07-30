import heapq

class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None


def merge_lists(lists):
 
  temp = []
  dic = {}
  result = []
 
  # initialize - take first element from every list, and put it on a temp list.
  #              The dictionary is so we can keep track of which list has which
  #              value; further down dictionary will get updated with new value
  #              every time a new value comes to the front of the list.
  for i in range(len(lists)):
    temp.append(lists[i].value)
    dic[i] = lists[i].value 
    
  heapq.heapify(temp)
  
  while (len(temp) > 0 ): 
 
    # get the lowest value from the heap and
    # and to the result.
    lowest_value = heapq.heappop(temp)
    result.append( lowest_value )
    
    # find out which list had the lowest value,
    # and get the key, that's the list we need to 
    # get our new value from and push onto the heap. 
    for key, value in dic.items():
      if lowest_value == value:
          mykey = key
          break
    
    # now push the list's next element onto temp,
    # refresh the dictionary, and increment the list pointer. 
    if lists[mykey].next != None:
      heapq.heappush(temp, lists[mykey].next.value) # push onto heap 
      dic[mykey] = lists[mykey].next.value # refresh dictionary value for this key
      lists[mykey] = lists[mykey].next # increment list pointer
     
  return result


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

  for i in range(len(result)):
    print (result[i], " ", end='')

main()