class Node:
    value = ""
    leftChild = None
    rightChild = None

    def __init__(self, parent):
        self.parent = parent

    def isLeaf(self):
        if (self.leftChild == None and self.rightChild == None):
            return True
        else:
            return False


def convertTreeAux(node, newick):
    if node.isLeaf():
        newick.append(node.value)
    if node.leftChild != None:
        newick.append("(")
        convertTreeAux(node.leftChild, newick)
        newick.append(",")
    if node.rightChild != None:
        convertTreeAux(node.rightChild, newick)
        newick.append(")")


tree = Node()
tree.leftChild.value1= "A"
# tree.leftChild = Node(tree)
tree.leftChild.value2= "B"
tree.rightChild = Node(tree)
tree.rightChild.value = "E"
tree.rightChild.leftChild = Node(tree.rightChild)
tree.rightChild.leftChild.value = "C"
tree.rightChild.rightChild = Node(tree.rightChild)
tree.rightChild.rightChild.value = "D"

newick = []
convertTreeAux(tree, newick)

print(''.join(newick))