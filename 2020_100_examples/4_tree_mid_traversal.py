#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论QQ群630011153 144081101
# CreateDate: 2020-1-14

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the Tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print( self.data),
        if self.right:
            self.right.print_tree()

# Inorder traversal
# Left -> Root -> Right
    def mid_traversal(self, root):
        res = []
        if root:
            res = self.mid_traversal(root.left)
            res.append(root.data)
            res = res + self.mid_traversal(root.right)
        return res
    
    # Inorder traversal
    # Left -> Root -> Right
    def mid_traversal_stack(self, root):
        stack = []
        result = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.data)
                node = node.right
        return result    
            
            

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.mid_traversal(root))
print(root.mid_traversal_stack(root))