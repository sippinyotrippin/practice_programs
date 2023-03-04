class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def stringify(linkedlist, result=()):
    if linkedlist is None or (linkedlist.data is None and linkedlist.next is None):
        result = list(result)
        result.append('None')
        return ' -> '.join(result)

    else:
        result = list(result)
        result.append(str(linkedlist.data))
        if linkedlist.next is not None:
            return stringify(linkedlist.next, tuple(result))
        else:
            return stringify(Node(None), tuple(result))


linked_list = Node(1, Node(2, Node(3, Node(4))))
print(stringify(linked_list))