from typing import Any


class Node(object):
    def __init__(self, value: Any) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None

    def insert(self, value: Any) -> None:
        if self.root is None:
            self.root = Node(value)
            return

        def _insert(node: Node, value: Any) -> Node:
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        _insert(self.root, value)

    def inorder(self) -> None:
        def _inorder(node: Node) -> None:
            if node is not None:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)
        _inorder(self.root)

    def search(self, value: Any) -> bool:
        def _search(node: Node, value: Any) -> bool:
            if node is None:
                return False
            if node.value == value:
                return True
            elif node.value > value:
                return _search(node.left, value)
            elif node.value < value:
                return _search(node.right, value)
        return _search(self.root, value)


if __name__ == "__main__":
    binary_tree = BinarySearchTree()
    binary_tree.insert(4)
    binary_tree.insert(1)
    print(binary_tree.root.value)
    print(binary_tree.root.value)
