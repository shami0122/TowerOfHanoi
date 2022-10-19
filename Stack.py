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
    
    def pop(self):
        if self.size > 0:
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -=1
            return item_to_remove.get_value()
        return "The Stack is Empty!"
    
    def peek(self):
        if self.size > 0:
            return self.top_item
        return "The Stack is Empty!"
    
