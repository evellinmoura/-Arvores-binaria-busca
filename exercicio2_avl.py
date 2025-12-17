

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    return node.height if node else 0


def balance(node):
    return height(node.left) - height(node.right)


def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


def insert(node, key):
    if not node:
        return AVLNode(key)

    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node

    node.height = 1 + max(height(node.left), height(node.right))
    bf = balance(node)

    # LL
    if bf > 1 and key < node.left.key:
        return rotate_right(node)

    # RR
    if bf < -1 and key > node.right.key:
        return rotate_left(node)

    # LR
    if bf > 1 and key > node.left.key:
        node.left = rotate_left(node.left)
        return rotate_right(node)

    # RL
    if bf < -1 and key < node.right.key:
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node


# TESTE 
if __name__ == "__main__":
    root = None
    for k in [30, 40, 24, 58, 48, 26, 11, 13]:
        root = insert(root, k)
    print("AVL criada com sucesso.")
#Outro teste
def check_balance(node):
    if not node:
        return True
    bf = balance(node)
    if bf < -1 or bf > 1:
        return False
    return check_balance(node.left) and check_balance(node.right)

print("AVL balanceada?", check_balance(root))
