# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recursive(self,node,n):
        counter = 0
        targetNode =None
        if node == None:
            return 0,None
        counter,targetNode =self.recursive(node.next,n)
        if counter == n:
            targetNode = node
            return counter+1,targetNode
        return counter +1 , targetNode

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        counter = 0
        node = ListNode(-1,next=head) 
        _,targetNode = self.recursive(node,n)
        temp = targetNode.next.next
        targetNode.next.next = None
        targetNode.next = temp
        return node.next