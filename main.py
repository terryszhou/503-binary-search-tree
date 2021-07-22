from BinaryTree import Node, BinaryTree

my_node = Node("Hello")
# print(my_node)

my_BST = BinaryTree()

my_BST.insert(10)
my_BST.insert(12)
my_BST.insert(8)
# print(f"Test! Should be 10:\n{my_BST.root}\n")
# print(f"Test! Should be 12:\n{my_BST.root.right}\n")
# print(f"Test! Should be 8:\n{my_BST.root.left}\n")
# my_BST.print()

my_BST.insert(5)
my_BST.insert(6)
my_BST.insert(7)
my_BST.insert(9)
my_BST.insert(11)
# my_BST.print()

print(my_BST.search(11))







