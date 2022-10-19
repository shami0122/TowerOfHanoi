from Node import Node
class Stack:
    def __init__(self, name):
        self.size = 0
        self.top_item = None
        # Need the name variable for the game speicifically
        self.name = name
    
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
    
    #Helper methods
    def peek(self):
        if self.size > 0:
            return self.top_item
        return "The Stack is Empty!"

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size
    
    def print_items(self):
        item_to_print = self.top_item
        list_to_print = []
        while(item_to_print):
            list_to_print.append(item_to_print)
            item_to_print = item_to_print.get_next_node()
        list_to_print.reverse
        print("{0} Stack: {1}".format(self.get_name(), list_to_print))