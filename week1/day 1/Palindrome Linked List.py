# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinked(self,node):
        if node.next == None:
            head = node
            return head;
        head=self.reverseLinked(node.next)
        temp = ListNode()
        temp = node.next
        temp.next = node
        node.next = None
        return head
        
        
    def isPalindrome(self, head: ListNode) -> bool:
        len_ = 0
        oldhead = head
        
        currentNode = head
        while currentNode  :
            len_ +=1
            currentNode = currentNode.next
        
        if len_ <=1:
            return True
        
        secondHalf = head;

        for i in range(len_//2):
            secondHalf = secondHalf.next
        if len_ %2==1:
            secondHalf = secondHalf.next    
        x=self.reverseLinked(secondHalf)
        
        left = head 
        right = x
        for i in range(len_//2):
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
        
