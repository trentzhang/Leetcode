class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self, root):
        res = []
        while root:
            res.append(root.val)
            root = root.next
        return res

    def sort(self, root):
        # start from head
        # check next head
        # create a loaction list
        head = ListNode(0, root)
        nextNode = head.next
        current = head
        previousNode = None
        # listOfPreviousNodes = [head]
        while current.next:
            # if next is larger than previous, pass
            print("head", self.printList(head))
            print("current.next", self.printList(current.next))
            print("current", self.printList(current))
            print("previousNode", self.printList(previousNode))
            # if nextNode.val > currentVal:
            if current.next.val > current.val:
                current = current.next
            else:
                # if next is smaller than previous, insert it to previous node which have a larger value than it

                previousNode = head
                while current.next.val > previousNode.next.val:
                    previousNode = previousNode.next

                nextNode = current.next
                print("nextNode", self.printList(nextNode))

                current.next = nextNode.next

                nextNode.next = previousNode.next

                previousNode.next = nextNode

        return head.next


input = ListNode(2, ListNode(4, ListNode(1, ListNode(3, ListNode(5)))))
sorted_list = ListNode().sort(input)
print(ListNode().printList(sorted_list))
