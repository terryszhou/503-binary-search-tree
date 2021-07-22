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
            #5. if input data is smaller than the current node...
            if new_node.data < current_node.data:
                # 6. ...and if the current node has nothing on its left...
                if not current_node.left:
                    # 7. ...then set the current node's left to the new node.
                    current_node.left = new_node
                    return
                # 8. Or if there IS a node to the left, go there and begin again from #5.
                else: current_node = current_node.left
        

    def search(self, val):
        '''
        search(value: any) -> value or bool:\n 
        Performs depth first search
        Search the Tree for a node with the given value
        If the node exists, return it
        If the node doesn't exist, return false
        '''
        pass

    def print(self, node=None):
        '''
        print(node=optional: Node) -> None:\n
        prints out all values recursively (in a breadth first search fashion)
        defualt start is at root node
        '''
        pass

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
        pass

    def get_min(self):
        '''
        getMin() -> int:\n 
        perform depth first search
        Calculate the minimum value held in the tree
        '''
        pass
