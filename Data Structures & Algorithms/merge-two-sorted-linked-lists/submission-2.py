# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy


        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next

            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2
        return dummy.next
        #then check which is less if say l1 was then we set pointer in there and move unto next number in l1 and then next lines were if l2 was less we do same then finally out we do curr= curr.next to move pointer then after thst then the last part is if one list is through we then atttahc the remaining of leftover list either l1 or l2

























        