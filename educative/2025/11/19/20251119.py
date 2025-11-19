# https://www.educative.io/courses/ds-and-algorithms-in-python/node-swap
# Linked lists - Node Swap


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
        print(curr_node.data)

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

    def delete_node(self, data):
        # if node is head
        if self.head.data == data:
            self.head = self.head.next
            return
        # if node is not head
        curr_node = self.head
        prev_node = None
        while curr_node.data != data:
            prev_node = curr_node
            curr_node = curr_node.next
        # data found, delete it
        prev_node.next = curr_node.next
        return

    def delete_node_at_position(self, index):
        if self.head:  # check that linkedlist isnt empty
            curr_node = self.head
            # if node is at position 0
            if index == 0:
                self.head = curr_node.next
                curr_node = None  # delete curr_node variable since no longer needed
                return

            prev = None
            current_position = 0
            # if node is not at position 0
            while current_position != index:
                prev = curr_node
                curr_node = curr_node.next
                current_position += 1

            if curr_node is None:  # index greater than linkedlist length
                return

            prev.next = curr_node.next
            curr_node = None

    def length(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    def recursive_length(self, node):
        if node is None:
            return 0
        return 1 + self.recursive_length(node.next)

    def swap_nodes(self, data_1, data_2):

        if data_1 == data_2:
            return  # return as is since both are same and swapping makes no difference

        # find both nodes
        data_1_prev_node = None
        data_1_node = self.head
        while data_1_node.data != data_1:
            data_1_prev_node = data_1_node
            data_1_node = data_1_node.next
        data_2_prev_node = None
        data_2_node = self.head
        while data_2_node.data != data_2:
            data_2_prev_node = data_2_node
            data_2_node = data_2_node.next

        # swap the nodes
        if data_1_prev_node:
            # only if this is not first element, do the swap since the while loop never runs if element was found in first index
            data_1_prev_node.next = data_2_node
        else:
            self.head = data_2_node

        if data_2_prev_node:
            # only if this is not first element, do the swap since the while loop never runs if element was found in first index
            data_2_prev_node.next = data_1_node
        else:
            self.head = data_1_node
        data_1_node.next, data_2_node.next = data_2_node.next, data_1_node.next


linked_list = LinkedList()

print("appending A,B,C,D")

linked_list.append("A")
linked_list.append("B")
linked_list.append("C")
linked_list.append("D")

linked_list.print_list()
print(f"length = {linked_list.length()}")
print("-" * 100)

print("prepending 0")
linked_list.prepend("0")
linked_list.print_list()
print(f"length = {linked_list.length()}")
print("-" * 100)


print("deleting 0")
linked_list.delete_node("0")
linked_list.print_list()
print(f"length = {linked_list.length()}")
print("-" * 100)

print("Swapping A and C")
linked_list.swap_nodes("A", "C")
linked_list.print_list()
print(f"length = {linked_list.length()}")
print("-" * 100)

print("Swapping C and B")
linked_list.swap_nodes("C", "B")
linked_list.print_list()
print(f"length = {linked_list.length()}")
print("-" * 100)


print("Swapping A and D")
linked_list.swap_nodes("A", "D")
linked_list.print_list()
print(f"length = {linked_list.length()}")
print("-" * 100)

# summary (X minutes today)
# - wrapped up
# Up next: Linkedlist reverse
# https://www.educative.io/courses/ds-and-algorithms-in-python/reverse-7X4AY7MVXwG
