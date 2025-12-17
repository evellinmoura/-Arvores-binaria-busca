

RED = True
BLACK = False


class RBNode:
    def __init__(self, key, color=RED):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


def rotate_left(root, x):
    y = x.right
    x.right = y.left
    if y.left:
        y.left.parent = x

    y.parent = x.parent

    if not x.parent:
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y

    y.left = x
    x.parent = y
    return root


def rotate_right(root, y):
    x = y.left
    y.left = x.right
    if x.right:
        x.right.parent = y

    x.parent = y.parent

    if not y.parent:
        root = x
    elif y == y.parent.right:
        y.parent.right = x
    else:
        y.parent.left = x

    x.right = y
    y.parent = x
    return root


def fix_insert(root, z):
    while z.parent and z.parent.color == RED:
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            if y and y.color == RED:
                z.parent.color = BLACK
                y.color = BLACK
                z.parent.parent.color = RED
                z = z.parent.parent
            else:
                if z == z.parent.right:
                    z = z.parent
                    root = rotate_left(root, z)
                z.parent.color = BLACK
                z.parent.parent.color = RED
                root = rotate_right(root, z.parent.parent)
        else:
            y = z.parent.parent.left
            if y and y.color == RED:
                z.parent.color = BLACK
                y.color = BLACK
                z.parent.parent.color = RED
                z = z.parent.parent
            else:
                if z == z.parent.left:
                    z = z.parent
                    root = rotate_right(root, z)
                z.parent.color = BLACK
                z.parent.parent.color = RED
                root = rotate_left(root, z.parent.parent)

    root.color = BLACK
    return root


def insert(root, key):
    node = RBNode(key)
    y = None
    x = root

    while x:
        y = x
        if key < x.key:
            x = x.left
        else:
            x = x.right

    node.parent = y
    if not y:
        root = node
    elif key < y.key:
        y.left = node
    else:
        y.right = node

    return fix_insert(root, node)


# TESTE 
if __name__ == "__main__":
    root = None
    for k in [5, 16, 22, 45, 2, 10, 18, 30, 50, 12, 1]:
        root = insert(root, k)
    print("Red-Black Tree criada com sucesso.")
#Outro teste
def is_red(node):
    return node and node.color == RED

def check_red_property(node):
    if not node:
        return True
    if is_red(node):
        if is_red(node.left) or is_red(node.right):
            return False
    return check_red_property(node.left) and check_red_property(node.right)

print("Raiz é preta?", root.color == BLACK)
print("Sem vermelho consecutivo?", check_red_property(root))
