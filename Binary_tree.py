class Node:
  def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      
class BinaryTree:

    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, value, node=None):
        if node is None:
            node = self.root
        if value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert(value, node.right)
        elif value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert(value, node.left)
        return node

    def find_maximum(self, node=None):
        if node is None:
            node = self.root
        if node.right is None:
            return node.value
        else:
            return self.find_maximum(node.right)

    def calculate_depth(self, node=None, depth=0):
        if node is None:
           node = self.root
        if node.left is None and node.right is None:
              return depth + 1
        else:
            left_depth = self.calculate_depth(node.left, depth + 1)
            
            right_depth = self.calculate_depth(node.right, depth + 1)
        
            return max(left_depth, right_depth)
            
# Constructing the binary tree
tree = BinaryTree(5)
tree.insert(3)
tree.insert(22)
tree.insert(10)
tree.insert(11)

# Finding the maximum value
max_value = tree.find_maximum()
print(f"Maximum Value: {max_value}")

# Calculating the tree depth
depths = tree.calculate_depth()
print(f"Depth of the Tree: {depths}")
