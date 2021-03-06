class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_data(self, data):
        self.data = data

    def getHeight(self, node):
        if node is None:
            return 0
        else:
            lheight = self.getHeight(node.left)
            rheight = self.getHeight(node.right)

            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def getHeight2(self, node):
        if node is None:
            return 0
        return max(self.getHeight2(node.left), self.getHeight2(node.right)) + 1
    
    def get_data(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.left = self.left
            self.left = temp

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.right = self.right
            self.right = temp


def preorderRecursive(root):
    '''
    先序遍历递归法
    '''

    def helper(root, result):
        if not root:
            return
        result.append(root.data)
        helper(root.left, result)
        helper(root.right, result)

    result = []
    helper(root, result)
    return result


def levelOrder(root):
    '''
    二叉树的层次遍历
    '''
    if not root:
        return []

    result = [[root.data]]  # 存储层次遍历的结果
    current = [root]  # 存储当前层次内的节点，在循环里面更新

    while True:
        node_list = []  # 临时存储节点
        for node in current:  # 循环内遍历
            if node.left:
                node_list.append(node.left)
            if node.right:
                node_list.append(node.right)
        if node_list == []:
            break
        vals = [node.data for node in node_list]  # 拿出当前层次的节点的值
        result.append(vals)
        current = node_list  # 更新层次
    return result


'''
递归方式层次遍历二叉树
'''


def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)


def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data)
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)


def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


root = BinaryTree(11)

root.insertLeft(1)
root.insertRight(2)
root.insertLeft(3)

print('height is: %d' % root.getHeight2(root))

print(levelOrder(root))

print(preorderRecursive(root))

printLevelOrder(root)
