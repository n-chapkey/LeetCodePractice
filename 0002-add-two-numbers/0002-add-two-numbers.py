# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = None
        head = None
        while l1 or l2:
            if l3 == None:
                l3 = ListNode(0)
                head = l3
            elif l3.next != None:
                l3 = l3.next
            else:
                l3.next = ListNode()
                l3 = l3.next
            
            val1,val2 = 0,0
            
            if(l1):
                val1 = l1.val
            
            if (l2):
                val2 = l2.val           
            
            l3.val += val1+val2
            
            temp = l3.val//10
            l3.val = l3.val % 10
            
            if(temp > 0):
                l3.next = ListNode(temp)
            if(l1):
                l1 = l1.next
            if(l2):
                l2 = l2.next
        print("broke loop")
        
        return head