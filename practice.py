class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self, root):
        while root:
            print(root.val, end=" ")
            root = root.next

    def sort(self, root):
        # start from head
        # check next head
        # create a loaction list
        head = ListNode(0, root)
        nextNode = head.next
        current = head
        listOfPreviousNodes = [head]
        while nextNode and nextNode.next:
            # if next is larger than previous, pass
            print(self.printList(head))
            # if nextNode.val > currentVal:
            if nextNode.val > current.val:
                listOfPreviousNodes += [nextNode]
                nextNode = nextNode.next
                current = nextNode
            else:
                # if next is smaller than previous, insert it to previous node which have a larger value than it
                print("nextNode.val", nextNode.val)
                for i, n in enumerate(listOfPreviousNodes):
                    if nextNode.val < n.val:
                        # insert the next node here at the node n
                        # previous node 0 -> 2(next), 2(next)->4(n), 4(n)->1(next.next)
                        # previousNode = listOfPreviousNodes[i - 1]
                        previousNode = listOfPreviousNodes[i - 1]
                        print("previousNode", previousNode.val)
                        print("nextNode", nextNode.val)
                        # previous node 0 -> 2(next)
                        previousNode.next = nextNode

                        # 4(n)->1(next.next)
                        dummy = nextNode.next
                        n.next = dummy

                        # 2(next)->4(n), dummy is 1 which is next to 2
                        nextNode.next = n

                        # here n is 4, n.next is 1

                        # update the listOfPreviousNodes
                        listOfPreviousNodes.insert(i, nextNode)
                        print([l.val for l in listOfPreviousNodes])
                        nextNode = n.next
                        current = n
                        # self.printList(head)
                        break

        return head.next


input = ListNode(4, ListNode(2, ListNode(1, ListNode(3, ListNode(5)))))
sorted_list = ListNode().sort(input)
ListNode().printList(sorted_list)
