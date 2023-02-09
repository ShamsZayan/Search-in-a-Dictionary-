import sys
class NODE:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        self.color = 'red'
        self.parent = None


class RBT:
    def __init__(self):
        self.root = None

    def create_node(self,value):
        node = NODE(value)
        return node

    def hieght(self,root):
        if root == None:
            return -1
        else:
            return max(self.hieght(root.left)+1,self.hieght(root.right)+1)

    def count(self,root):
        if root == None:
            return 0
        return 1+self.count(root.left)+self.count(root.right)

    def search(self, value, root):
        if root != None:
            if root.value == value:
                return 'YES'
            elif value < root.value:
                return self.search(value, root.left)
            else:
                return self.search(value, root.right)
        return 'NO'

    def insert_node(self,node,root):

        if self.root == None :
            node.color = 'black'
            self.root = node
        else:
            # while root != None :
            #     temp = root
            #     if node.value < root.value:
            #         root = root.left
            #     else:
            #         root = root.right
            #
            # if node.value < temp.value:
            #     temp.left = node
            #     node.parent = temp
            #     self.uncle(node)
            #
            # else:
            #     temp.right = node
            #     node.parent = temp
            #     self.uncle(node)

            if (node.value < root.value) and (root.left == None):

                root.left = node
                node.parent = root
                self.uncle(node)

            elif (node.value > root.value) and (root.right == None):
                root.right = node
                node.parent = root
                self.uncle(node)

            elif node.value < root.value:
                self.insert_node(node, root.left)
            elif node.value > root.value:
                self.insert_node(node, root.right)

    def recoloring(self, node):
        if node != None:
            if node.color == 'red':
                node.color = 'black'
            elif node.color == 'black':
                node.color = 'red'

    def rotateright(self, node):
        node.parent.parent.left = node.parent.right
        if node.parent.right != None :
            node.parent.right.parent = node.parent.parent

        node.parent.right = node.parent.parent
        node.parent.parent = node.parent.right.parent
        node.parent.right.parent = node.parent
        if node.parent.parent != None:
            if node.parent.parent.left == node.parent.right:
                node.parent.parent.left = node.parent
            else:
                node.parent.parent.right = node.parent

        if node.parent.parent == None:
            self.root = node.parent

    def rotateleft(self,node):
        node.parent.parent.right = node.parent.left
        if node.parent.left != None:
            node.parent.left.parent = node.parent.parent

        node.parent.left = node.parent.parent
        node.parent.parent = node.parent.left.parent
        node.parent.left.parent = node.parent
        if node.parent.parent != None:
            if node.parent.parent.left == node.parent.left:
                node.parent.parent.left = node.parent
            else:
                node.parent.parent.right = node.parent
        if node.parent.parent == None:
            self.root = node.parent

    def getuncle(self,node):
        if node.parent != None:
            if node.parent.left == node:

                return node.parent.right
            else:

                return node.parent.left

    def uncle(self,node):
        if node.parent.color == 'red':

            uncle = self.getuncle(node.parent)

            if uncle != None and uncle.color == 'red':

                node.parent.color = 'black'
                uncle.color = 'black'
                if node.parent.parent.color == 'black' and node.parent.parent.parent != None:
                    node.parent.parent.color = 'red'
                    self.uncle(node.parent.parent)

            elif uncle == None or uncle.color == 'black':
               if node.parent.left == node and node.parent.parent.left == node.parent:
                   self.recoloring(node.parent)
                   self.recoloring(node.parent.parent)
                   self.rotateright(node)
               elif node.parent.right == node and node.parent.parent.left == node.parent:
                   node.parent.parent.left = node
                   node.parent.right = node.left
                   if node.parent.right != None:
                       node.parent.right.parent = node.parent
                   node.left = node.parent
                   node.parent = node.left.parent
                   node.left.parent = node
                   self.recoloring(node)
                   self.recoloring(node.parent)
                   self.rotateright(node.left)
               elif node.parent.right == node and node.parent.parent.right == node.parent:

                   self.recoloring(node.parent)
                   self.recoloring(node.parent.parent)
                   self.rotateleft(node)
               elif node.parent.left == node and node.parent.parent.right == node.parent:
                   node.parent.parent.right = node
                   node.parent.left = node.right
                   if  node.parent.left!=None:
                       node.parent.left.parent = node.parent
                   node.right = node.parent
                   node.parent = node.right.parent
                   node.right.parent = node
                   self.recoloring(node)
                   self.recoloring(node.parent)
                   self.rotateleft(node.right)

    def inordertravversal(self, root):
        if root != None:
            self.inordertravversal(root.left)
            print(root.value)
            self.inordertravversal(root.right)


if __name__ == '__main__':
    tree = RBT()
    # for i in range(1, 100006):
    #     # name = input('entername: ')
    #     node = tree.create_node(i)
    #     tree.insert_node(node, tree.root)
    #
    # tree.inordertravversal(tree.root)
    # print(tree.search(2, tree.root))
    # print(tree.count(tree.root))
    # print(tree.hieght(tree.root))
    with open('EN-US-Dictionary.txt', 'r') as f:
        for line in f:
            line_strip = line.strip()
            node = tree.create_node(line_strip)
            tree.insert_node(node, tree.root)
            # print(line)
    while True:
        print(tree.count(tree.root))
        print(tree.hieght(tree.root))
        word = input('insert Word: ')
        check = tree.search(word, tree.root)
        if check == 'NO':
            node = tree.create_node(word)
            tree.insert_node(node, tree.root)
        else:
            print('ERROR:Word already in the dictionary')

        name = input('Look up a Word: ')
        print(tree.search(name, tree.root))
        print(tree.count(tree.root))
        print(tree.hieght(tree.root))






