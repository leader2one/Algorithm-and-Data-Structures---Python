class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ans = ListNode(0)
        ans.next = head
        
        first = ans
        second = ans
        
        for i in range(1, n + 2):
            first = first.next
        
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        
        return ans.next