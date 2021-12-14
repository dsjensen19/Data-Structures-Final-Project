class BST:
    """
    First we must define this class and creat the BST.Node class
    """

    class Node:
        """
        Each node of the BST must have its own data and its own links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            We must initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
            self.data = data
            self.left = None
            self.right = None
            self.BigO = 0  # Add a global variable to calculate big O

    def __init__(self):
        """
        We also nee to initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        elif self.__contains__(data):
            do_nothing = 0
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data < node.data:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)

    def __contains__(self, data):
        """ 
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        contain = self._contains(data, self.root)
        info = [contain, self.BigO]
        return info

    def _contains(self, data, node):
        """
        This funciton will search for a node that contains
        'data'.  The current sub-tree being search is 
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        """
        if data == node.data:
            return True
        elif data < node.data:
            if node.left is None:
                return False
            else:
                self.BigO += 1 # Increase big O
                return self._contains(data, node.left)
        else:
            if node.right is None:
                return False
            else:
                self.BigO += 1 #increase big O
                return self._contains(data, node.right)
