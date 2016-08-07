def InsertNth(head, data, position):
    dummy = Node()
    dummy.next = head
    runner = dummy

    for i in range(0, position):
        runner = runner.next

    new_node = Node()
    new_node.data = data
    new_node.next = runner.next
    runner.next = new_node
    return dummy.next

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

llist = Node()
llist = InsertNth(llist, 1, 0)
llist = InsertNth(llist, 2, 0)
type(llist.next)

llist = InsertNth(llist, 3, 1)
print llist.data
