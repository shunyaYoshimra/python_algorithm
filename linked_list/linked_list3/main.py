from __future__ import annotations
from typing import Any, Optional


class Node(object):
    def __init__(self, data: Any, next_node: Node = None, previous_node: Node = None) -> None:
        self.data = data
        self.next = next_node
        self.previous = previous_node


class DoublyLinkedList(object):
    def __init__(self, head: Node = None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.previous = current_node

    def insert(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: Any) -> Node:
        current_node = self.head
        if current_node and current_node.data == data:
            if current_node.next is None:
                current_node = None
                self.head = None
                return
            else:
                next_node = current_node.next
                next_node.previous = None
                current_node = None
                self.head = next_node
                return

        while current_node and current_node.data != data:
            current_node = current_node.next

        if current_node is None:
            return

        if current_node.next is None:
            previous_node = current_node.previous
            previous_node.next = None
            current_node = None
            return
        else:
            next_node = current_node.next
            previous_node = current_node.previous
            previous_node.next = next_node
            next_node.previous = previous_node
            current_node = None
            return

    def reverse_iterative(self) -> None:
        previous_node = None
        current_node = self.head
        while current_node:
            previous_node = current_node.previous
            current_node.previous = current_node.next
            current_node.next = previous_node

            current_node = current_node.previous
        if previous_node:
            self.head = previous_node.previous

    def reverse_recursive(self) -> None:
        def _reverse_recursive(current_node: Node) -> Optional[Node]:
            if not current_node:
                return None

            previos_node = current_node.previous
            current_node.previous = current_node.next
            current_node.next = previos_node

            if current_node.previous is None:
                return current_node

            return _reverse_recursive(current_node.previous)

        self.head = _reverse_recursive(self.head)


if __name__ == "__main__":
    d = DoublyLinkedList()
    d.append(0)
    d.append(1)
    d.append(2)
    d.append(3)
    d.reverse_recursive()
    d.print()