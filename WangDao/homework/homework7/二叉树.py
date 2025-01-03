# 作者:胡轩
# 2025年01月03日16时30分44秒
# 1733183066@qq.com

class Node:
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.queue = []

    def build_tree(self, node):
        """
        把当前结点加入树中
        """
        if not self.root:
            self.root = node
            self.queue.append(node)
        else:
            self.queue.append(node)
            if not self.queue[0].lchild:
                self.queue[0].lchild = node
            else:
                self.queue[0].rchild = node
                self.queue.pop(0)

    def pre_order(self, current_node):
        """
        前序遍历
        """
        if current_node:
            print(current_node.elem, end=' ')
            self.pre_order(current_node.lchild)
            self.pre_order(current_node.rchild)

    def in_order(self, current_node):
        """
        中序遍历
        """
        if current_node:
            self.in_order(current_node.lchild)
            print(current_node.elem, end=' ')
            self.in_order(current_node.rchild)

    def post_order(self, current_node):
        """
        后序遍历
        """
        if current_node:
            self.post_order(current_node.lchild)
            self.post_order(current_node.rchild)
            print(current_node.elem, end=' ')

    def level_order(self):
        help_queue = []
        help_queue.append(self.root)
        while help_queue:
            print(help_queue[0].elem, end='')
            if help_queue[0].lchild:
                help_queue.append(help_queue[0].lchild)
            if help_queue[0].rchild:
                help_queue.append(help_queue[0].rchild)
            help_queue.pop(0)


if __name__ == '__main__':
    T = BinaryTree()
    for i in range(1, 11):
        tnode = Node(i)
        T.build_tree(tnode)
    T.pre_order(T.root)
    print()
    T.in_order(T.root)
    print()
    T.post_order(T.root)
    print()
    T.level_order()
