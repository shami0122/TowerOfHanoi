from Node import Node
class Stack:
    def __init__(self):
        self.size = 0
        self.top_item = None
    
    def push(self, value):
        new_item = Node(value)
        new_item.set_next_node(self.top_item)
        self.top_item = new_item
        self.size += 1
