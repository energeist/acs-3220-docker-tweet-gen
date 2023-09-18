from linkedlist import Node

class Queue:
    def __init__(self, items=None):
        """Initialize this queue and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        queue_str = ""
        for item in self.items():
            queue_str += f'({item}) -> '
        return queue_str

    def items(self):
        """Return a list (dynamic array) of all items in this queue."""
        items = []
        node = self.head
        while node:
            items.append(node.data)
            node = node.next
        return items

    def is_empty(self):
        """Return a boolean indicating whether this queue is empty."""
        return self.head is None

    def length(self):
        """Return the length of this queue by traversing its nodes."""
        count = 0
        if self.head:
            current_node = self.head
            count += 1
            while current_node.next:
                count += 1
                current_node = current_node.next
        return count
    
    def enqueue(self):
        """Enqueue a new item to the queue at the back (tail) end"""
        node = Node(item)
        if self.is_empty():
            self.head = node 
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        """Remove and return an item from the front (head) of the queue"""
        node = self.head
        self.delete(node)
        return node

    def find(self, matcher):
        """Return an item from this queue if it is present."""
        node = self.head
        while node:
            if matcher == node.data:
                return True
            node = node.next
        return False           

    def delete(self, item):
        """Delete the given item from this queue, or raise ValueError."""
        previous_node = None
        next_node = None
        if self.head:
            current_node = self.head
            while item not in current_node.data: # loop until data is found
                if current_node.next == None:
                    raise ValueError('Item not found: {}'.format(item))
                else:
                    previous_node = current_node
                    current_node = current_node.next
                    if current_node.next:
                        next_node = current_node.next
                    else:
                        self.tail = current_node
            if current_node == self.head: # if data is found in the head
                if current_node.next:
                    self.head = current_node.next
                else:
                    self.head = None
                    self.tail = None
                    self = None
            elif current_node.next == None: # if data is found in the tail
                self.tail = previous_node
                current_node = None
                previous_node.next = None    
            else: # data is found between head and tail
                if current_node.next:
                    previous_node.next = next_node
                else:
                    self.tail = previous_node
        else:
            raise ValueError('Item not found: {}'.format(item))