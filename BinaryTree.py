class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.data}"


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        '''
        Insert(data: any) -> None:\n 
        creates a new Node from the data passed in and adds it to the tree
        If the data is already in the tree, does not insert it again
        '''
        # 1. Make a new node from input data.
        new_node = Node(data)

        # 2. If self has no root, set root to new node.
        if not self.root:
            self.root = new_node
            return 

        # 3. Set current node to root
        current_node = self.root
        #4. Begin looping over tree, starting at current node
        while current_node:
            #5a. if new node's data is SMALLER than the current node's data...
            if new_node.data < current_node.data:
                # 6a. ...and if the current node has nothing on its LEFT...
                if not current_node.left:
                    # 7a. ...then set the current node's LEFT to the new node.
                    current_node.left = new_node
                    return
                # 8a. Or if there is a node to the LEFT, go there and begin again from #4.
                else: current_node = current_node.left
            # 5b. if input data is LARGER than the current node...
            elif new_node.data > current_node.data:
                # 6b. ... and i the current node has nothing on its RIGHT
                if not current_node.right:
                    # 7b. ...then set the current node's RIGHT to the new node.
                    current_node.right = new_node
                    return
                # 8b. Or if there is a node to the RIGHT, go there and begin again from #4.
                else:
                    current_node = current_node.right

    def print(self, node=None):
        '''
        print(node=optional: Node) -> None:\n
        prints out all values recursively (in a breadth first search fashion)
        default start is at root node
        '''
        # 1. Check if this is the first recursion
        if not node: node = self.root

        # 2. Print the node
        print(node)

        # 3a. If there is a left node...
        if node.left:
            # 4a. ...recursively invoke self.print on the node
            print(f"On {node}'s' left is:")
            self.print(node.left)
        # 3b. If there is a right node...
        if node.right:
            # 4b. ...recursively invoke self.print on the node
            print(f"On {node}'s' right is:")
            self.print(node.right)

    def search(self, val):
        '''
        search(value: any) -> value or bool:\n 
        Performs depth first search
        Search the Tree for a node with the given value
        If the node exists, return it
        If the node doesn't exist, return false
        '''
        # 1. Loop through tree starting at root.
        current_node = self.root

        while current_node:
            # 2a. If input value is less than the current node...
            if val < current_node.data:
                # 3a. ...then set current node to be the left.
                current_node = current_node.left
            # 2b. Else if input value is greater than the current node...
            elif val > current_node.data:
                # 3b. ...then set current node to be the right.
                current_node = current_node.right
            # 2c. Else, return the current node.
            else:
                return current_node

        # 4. If no nodes catch...
        return False

    def size(self, node=None):
        '''
        size(node=optional: Node) -> int:\n 
        performs breadth first search
        Calculate the number of nodes in the tree, starting from the given node
        If no node is provided, we can use the root as a sensible default
        '''
        pass

    def height(self, node=None):
        '''
        height(node=optional: Node) -> int:\n 
        perform breadth first search
        Calculate the maximum amount of nodes in any one path from the given node
        If not given a specific node, default to using the root node
        '''
        pass

    def get_max(self):
        '''
        getMax() -> int:\n 
        perform depth first search
        Calculate the maximum value held in the tree
        '''
        # 1. Loop through tree starting at ROOT.
        current_node = self.root
        while current_node:

            # 2a. If there is a node to the RIGHT...
            if current_node.right:
                # 3a. ...set CURRENT node to the RIGHT
                current_node = current_node.right
            # 2b. else, return the CURRENT node
            else:
                return current_node

        # 4. If no nodes catch...
        else:
            return False

    def get_min(self):
        '''
        getMin() -> int:\n 
        perform depth first search
        Calculate the minimum value held in the tree
        '''
        # 1. Loop through tree starting at ROOT.
        current_node = self.root
        while current_node:

            # 2a. If there is a node to the LEFT...
            if current_node.left:
                # 3a. ...set CURRENT node to the LEFT
                current_node = current_node.left
            # 2b. else, return the CURRENT node
            else:
                return current_node

        # 4. If no nodes catch...
        else:
            return False
