
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = []
        num2 = []
        while (l1):
            num1.append(l1.val)
            l1 = l1.next
        
        while (l2):
            num2.append(l2.val)
            l2 = l2.next
        num1.reverse()
        num2.reverse()
        car1 = convert(num1)
        car2 = convert(num2)
        
        a = str(car1 + car2)[::-1]
        aws = []
        for index,x in enumerate(a):
            aws.append(ListNode(x))
        return aws
    
def convert(list):
    s = [str(i) for i in list]
    res = int(''.join(s))
    
    return res