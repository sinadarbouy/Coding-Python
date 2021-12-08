# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

    def isPalindrome(self, head):
        rev = None
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow_next = slow.next
            slow.next = rev
            rev = slow
            slow = slow_next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
