# exemple 1:
#     '10'
#    /    \
# '5'     '15'


# exemple 2:
#      '+'
#    /     \
#  'a'      '*'
#          /   \
#        'b'    '-'
#              /    \
#            '/'    'e'
#           /   \
#         'c'   'd'

# (a + (b * ((c/d) - e)))


# define the tree node


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# # return results as a string

    def __str__(self):
        return str(self.data)

# Define tree structure


class Tree:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    # percurso em ordem simetrica
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root

        if node.left:
            print('(', end='')

            self.simetric_traversal(node.left)
            # o end= no final do print serve para o python nao pular linha no print
        print(node, end="")

        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')


if __name__ == "__main__":
    tree = Tree()

    n1 = Node("a")
    n2 = Node("+")
    n3 = Node("*")
    n4 = Node("b")
    n5 = Node("-")
    n6 = Node("/")
    n7 = Node("c")
    n8 = Node("d")
    n9 = Node("e")

    n6.left = n7
    n6.right = n8

    n5.left = n6
    n5.right = n9

    n3.left = n4
    n3.right = n5

    n2.left = n1
    n2.right = n3

    tree.root = n2
    tree.simetric_traversal()
    print('')
    # tree = Tree(10)
    # tree.root.left = Node(5)
    # tree.root.right = Node(15)

    # print(tree.root, 'Root')
    # print(tree.root.left, 'Left')
    # print(tree.root.right, 'Right')


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

