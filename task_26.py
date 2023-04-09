"""
https://www.codewars.com/kata/56a1c63f3bc6827e13000006
How many are smaller than me II?
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data, kol):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return 0
        if new_node.data <= self.head.data:
            new_node.next = self.head
            self.head = new_node
            return 0
        elif new_node.data > self.tail.data:
            self.tail.next = new_node
            self.tail = new_node
            return kol
        else:
            ind = 1
            current_node = self.head
            while current_node.next and current_node.next.data < new_node.data:
                current_node = current_node.next
                ind += 1
            new_node.next = current_node.next
            current_node.next = new_node
            return ind

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


def smaller(arr):
    lst = [0]
    linked_list = LinkedList()
    kol = 0
    linked_list.append(arr[-1], kol)
    for x in range(len(arr)-2, -1, -1):
        kol += 1
        lst.append(linked_list.append(arr[x], kol))
    return lst[::-1]


print(smaller([5, 4, 3, 2, 1]), "___", [4, 3, 2, 1, 0])
print(smaller([1, 2, 3]), "___", [0, 0, 0])
print(smaller([1, 2, 0]), "___", [1, 1, 0])
print(smaller([1, 2, 1]), "___", [0, 1, 0])
print(smaller([1, 1, -1, 0, 0]), "___", [3, 3, 0, 0, 0])
print(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]), "___", [4, 1, 5, 5, 0, 0, 0, 0, 0])
print(smaller([5, 4, 7, 9, 2, 4, 1, 4, 5, 6]), "___", [5, 2, 6, 6, 1, 1, 0, 0, 0, 0])
