

class TreeNode:
    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None


class TreeMap:
    def __init__(self):
        self.root = None
        self.size = 0

    def _subtree_search(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self._subtree_search(node.left, key)
        else:
            return self._subtree_search(node.right, key)

    def __setitem__(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
            self.size = 1
            return

        parent = None
        curr = self.root

        while curr:
            parent = curr
            if key == curr.key:
                curr.value = value
                return
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        node = TreeNode(key, value, parent)
        if key < parent.key:
            parent.left = node
        else:
            parent.right = node

        self.size += 1

    def __getitem__(self, key):
        node = self._subtree_search(self.root, key)
        if node is None:
            raise KeyError(key)
        return node.value

    def _minimum(self, node):
        while node.left:
            node = node.left
        return node

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def __delitem__(self, key):
        node = self._subtree_search(self.root, key)
        if node is None:
            raise KeyError(key)

        if node.left is None:
            self._transplant(node, node.right)
        elif node.right is None:
            self._transplant(node, node.left)
        else:
            succ = self._minimum(node.right)
            if succ.parent != node:
                self._transplant(succ, succ.right)
                succ.right = node.right
                succ.right.parent = succ
            self._transplant(node, succ)
            succ.left = node.left
            succ.left.parent = succ

        self.size -= 1


# TESTE 
if __name__ == "__main__":
    t = TreeMap()
    for k in [30, 40, 24, 58, 48, 26, 11, 13]:
        t[k] = k
    print("BST criada com sucesso.")
def inorder(node):
    if node:
        inorder(node.left)
        print(node.key, end=" ")
        inorder(node.right)

print("\nInorder traversal:")
inorder(t.root)
