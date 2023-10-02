class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insertion_sort(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        current = head

        while current.next:
            if current.next.val < current.val:
                # If the next node's value is smaller, we need to find its correct position
                prev = dummy
                while prev.next.val < current.next.val:
                    prev = prev.next

                temp = current.next
                current.next = temp.next
                temp.next = prev.next
                prev.next = temp
            else:
                current = current.next

        return dummy.next

    def print_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result


# Example usage:
input_list = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
sorted_list = ListNode().insertion_sort(input_list)
print(ListNode().print_list(sorted_list))  # Output: [1, 2, 3, 4]
