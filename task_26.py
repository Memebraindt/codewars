"""
https://www.codewars.com/kata/56a1c63f3bc6827e13000006
How many are smaller than me II?
"""


# Node class for creating nodes of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = data

    def append(self, data):
        new_node = Node(data)
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # def print_list(self):
    #     current_node = self.head
    #     while current_node:
    #         print(current_node.data)
    #         current_node = current_node.next

    # def sort_list(self):
    #     # Convert linked list to list for sorting
    #     current_node = self.head
    #     elements = []
    #     while current_node:
    #         elements.append(current_node.data)
    #         current_node = current_node.next
    #     # Sort the list using the built-in sorted function
    #     elements = sorted(elements)
    #     # Rebuild the linked list with sorted elements
    #     self.head = None
    #     for element in elements:
    #         self.append(element)


# linked_list = LinkedList()
# linked_list.append(3)
# linked_list.append(1)
# linked_list.append(4)
# linked_list.append(2)

def smaller(arr):
    linked_list = LinkedList(arr[-1])
    print(linked_list.head)

    # lst = []
    # x0 = Node(arr[-1])
    # for x in range(len(arr) - 1, 0, -1):
    #     while linked_list.head.data > arr[x]:
    #         print(linked_list.head.data)
    #
    #     else:
    #         pass
    return linked_list


print(smaller([5, 4, 3, 2, 1]), "___", [4, 3, 2, 1, 0])
print(smaller([1, 2, 3]), "___", [0, 0, 0])
print(smaller([1, 2, 0]), "___", [1, 1, 0])
print(smaller([1, 2, 1]), "___", [0, 1, 0])
print(smaller([1, 1, -1, 0, 0]), "___", [3, 3, 0, 0, 0])
print(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]), "___", [4, 1, 5, 5, 0, 0, 0, 0, 0])
print(smaller([5, 4, 7, 9, 2, 4, 1, 4, 5, 6]), "___", [5, 2, 6, 6, 1, 1, 0, 0, 0, 0])

# print("Original linked list:")
# linked_list.print_list()
#
# linked_list.sort_list()
#
# print("Sorted linked list:")
# linked_list.print_list()
