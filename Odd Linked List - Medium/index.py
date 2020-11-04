class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        odd = head
        even = odd.next
        evenList = even
        
        while(even and even.next):
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
        
        odd.next = evenList
        return head