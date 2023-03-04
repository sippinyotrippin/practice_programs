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


linked_list = Node(None)
print(stringify(linked_list))
