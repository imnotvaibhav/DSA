# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        temp = dummy

        while l1 and l2:
            if l1.val<l2.val:
                temp.next = l1
                l1 = l1.next
            elif l2.val<=l2.val:
                temp.next = l2
                l2 = l2.next
            temp = temp.next

        if l1:
            temp.next = l1
        elif l2:
            temp.next = l2
        return dummy.next
    
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Creating the first linked list: 1 -> 2 -> 3
l1_node3 = ListNode(3)
l1_node2 = ListNode(2, l1_node3)
l1_node1 = ListNode(1, l1_node2)
l1_head = l1_node1

# Creating the second linked list: 1 -> 2 -> 4
l2_node3 = ListNode(4)
l2_node2 = ListNode(2, l2_node3)
l2_node1 = ListNode(1, l2_node2)
l2_head = l2_node1

# Creating an instance of the Solution class
sol = Solution()

# Merging the two lists
merged_head = sol.mergeTwoLists(l1_head, l2_head)

# Printing the merged linked list
print("Merged Linked List:")
printLinkedList(merged_head)