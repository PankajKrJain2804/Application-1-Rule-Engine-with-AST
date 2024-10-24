class ASTNode:
    def __init__(self, node_type, value=None):
        self.node_type = node_type  # "operator" or "operand"
        self.value = value  # Value for operand nodes
        self.left = None  # Left child
        self.right = None  # Right child
