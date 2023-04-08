class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        # Find the correct position to insert the new node
        if new_node.data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        while current_node.next and current_node.next.data < new_node.data:
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

# Example usage
linked_list = LinkedList()
linked_list.append(3)
linked_list.append(1)
linked_list.append(4)
linked_list.append(2)

print("Original linked list:")
linked_list.print_list()
