class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def stringify(linkedlist, result=()):
    if linkedlist is None or linkedlist.data is None:
        result = list(result)
        result.append('None')
        return ' -> '.join(result)

    else:
        result = list(result)
        result.append(str(linkedlist.data))
        return stringify(linkedlist.next, tuple(result))


linked_list1 = Node(None)
linked_list2 = Node(1, None)
linked_list3 = Node(1, Node(2, Node(3, Node(4))))
print(stringify(linked_list1))
print(stringify(linked_list2))
print(stringify(linked_list3))
