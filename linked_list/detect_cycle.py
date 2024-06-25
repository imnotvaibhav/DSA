# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head):
        # fast and slow
        slow, fast = head, head.next
        while fast:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
    
# Creating the first linked list: 1 -> 2 -> 3 -> 4 -> 1
l_node4 = ListNode(4)
l_node3 = ListNode(3, l_node4)
l_node2 = ListNode(2, l_node3)
l_node1 = ListNode(1, l_node2)
l_node4.next = l_node1
l_head = l_node1


sol = Solution()

print(sol.hasCycle(l_head))