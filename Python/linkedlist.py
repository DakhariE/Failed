class Node:
  def __init__(self,data,next=None):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  def print(self):
    temp = self.head
    while temp is not None:
      print(temp.data)
      temp = temp.next

elem1 = LinkedList()
elem1.head = Node(1)
elem2 = Node(2)
elem3 = Node(3)

elem1.head.next = elem2
elem2next = elem3

LinkedList.print(elem1)