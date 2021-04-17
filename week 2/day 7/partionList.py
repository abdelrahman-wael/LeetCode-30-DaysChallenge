class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        partion1 = ListNode()
        partion2 = ListNode()
        p1 = partion1
        p2 = partion2
        current = head
        while current != None:
            if current.val < x:
                p1.next = current
                current = current.next
                p1=p1.next
                p1.next = None
            else:
                p2.next = current
                current = current.next
                p2=p2.next
                p2.next = None
            
        
        p1.next = partion2.next    
        return partion1.next
