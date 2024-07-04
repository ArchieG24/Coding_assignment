class Node:
  def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

class BinaryTree:
  def __init__(self):
      self.root = None

  def insert(self, value):
      if self.root is None:
          self.root = Node(value)
      else:
          self._insert_rec(self.root, value)

  def _insert_rec(self, current_node, value):
      if value < current_node.value:
          if current_node.left is None:
              current_node.left = Node(value)
          else:
              self._insert_rec(current_node.left, value)
      else:
          if current_node.right is None:
              current_node.right = Node(value)
          else:
              self._insert_rec(current_node.right, value)

  def calculate_depth(self):
      if self.root is None:
          return 0
      return self.calculate_depth_rec(self.root)

  def calculate_depth_rec(self, current_node):
      if current_node is None:
          return 0
      left_depth = self.calculate_depth_rec(current_node.left)
      right_depth = self.calculate_depth_rec(current_node.right)
      return 1 + max(left_depth, right_depth)

# Example usage
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(2)
tree.insert(10)
tree.insert(11)

depth = tree.calculate_depth()
print("Depth of the tree:", depth)  # Output: Depth of the tree: 3
