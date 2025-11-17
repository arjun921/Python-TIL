# https://www.educative.io/courses/ds-and-algorithms-in-python/introduction-qAlJqORgZLG
# Linked lists


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        # inserts element to the END of the LinkedList
        new_node = Node(data)
        if (
            self.head == None
        ):  # if there is no elements in the linkedlist, just insert as first element
            self.head = new_node
            return
        last_node = self.head
        while (
            last_node.next
        ):  # while there is next element, iterate and find last node for appending after that node.
            last_node = last_node.next
        # exits the loop when last_node is indeed the last node, and there .next is None. that way next line gets executed after
        # iteration through all nodes to APPEND the new node at the end
        last_node.next = new_node
        return

    def print_list(self):
        curr_node = self.head
        while curr_node.next:
            print(curr_node.data)
            curr_node = curr_node.next

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_data_node(self, data, after):

        curr_node = self.head
        while curr_node.data != after:
            curr_node = curr_node.next
        new_node = Node(data)
        new_node.next = curr_node.next
        curr_node.next = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Prev node not found")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


linked_list = LinkedList()

linked_list.append("A")
linked_list.append("B")
linked_list.append("C")
linked_list.append("D")

linked_list.print_list()

print("prepending 0")

linked_list.prepend("0")

linked_list.print_list()

# summary
# - linkedlists Introduction and insertion completed.
# - next up https://www.educative.io/courses/ds-and-algorithms-in-python/deletion-by-value
