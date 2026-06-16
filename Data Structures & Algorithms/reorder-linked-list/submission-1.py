# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#grabbing front back alternatively

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow = head 
        fast = head

       

        while fast and fast.next:#need to have first and the second thing sth to jump to
            slow = slow.next
            fast = fast.next.next 

       
        prev = None
        curr = slow.next
        slow.next = None
        

        while curr:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        first = head
        second = prev
        
        #save ,point then move
        while first and second:
            first_next = first.next
            second_next = second.next #we will be picking alternatively from each need to save where each is going

            first.next = second
            second.next = first_next #point to first list

            first = first_next
            second = second_next #moving through to the next iteration
            
            