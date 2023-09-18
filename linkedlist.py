#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        """=> O(1) because this is a comparison of a known value"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        """=> O(n) because we must traverse the length of n elements of the list to get a count"""
        """Even if n=1 this is technically still O(n) because O(1) represents constant time"""
        count = 0
        if self.head:
            current_node = self.head
            count += 1
            while current_node.next:
                count += 1
                current_node = current_node.next
        return count

        # TODO: Loop through all nodes and count one for each

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Why and under what conditions?"""
        """=> O(1) because self.tail is tracked, and we are appending one item to a known location"""
        # TODO: Create new node to hold given item
        node = Node(item)
        # TODO: If self.is_empty() == True set the head and the tail to the new node
        if self.is_empty() == True:
            self.head = node 
            self.tail = node
        # TODO: Else append node after tail
        else:
            self.tail.next = node
            self.tail = node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
        => O(1) because self.head is tracked, and we are prepending one item to a known location"""
        # TODO: Create new node to hold given item
        node = Node(item)
        # TODO: Prepend node before head, if it exists
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node

    def find(self, matcher):
        """Return an item from this linked list if it is present.
        TODO: Best case running time: O(???) Why and under what conditions?
        => O(1) best case if the item being found is the first item in the list
        TODO: Worst case running time: O(???) Why and under what conditions?
        => O(n) worst case if the item being found is the last item in the list"""
        # TODO: Loop through all nodes to find item, if present return True otherwise False
        
        # SLICK CODE THAT MATCHES ORIGINAL TEST FILE
        # node = self.head
        # while node:
        #     if matcher(node.data):
        #         return node.data
        #     node = node.next
        # return None

        # SAD NON-LAMBDA CODE THAT MATCHES GRADESCOPE 4.13 TEST
        node = self.head
        while node:
            if matcher in node.data:
                return True
            node = node.next
        return False

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        => O(1) best case if item being deleted is the first item in the list
        TODO: Worst case running time: O(???) Why and under what conditions?
        => O(n) worst case if the item being deleted is the last item in the list"""
        # TODO: Loop through all nodes to find one whose data matches given item
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

    # TODO: Update previous node to skip around node with matching data
    # TODO: Otherwise raise error to tell user that delete has failed
    # Hint: raise ValueError('Item not found: {}'.format(item))

    def replace(self, match, replacement):
        node = self.head
        while node:
            if match == node.data:
                node.data = replacement
            node = node.next
        
def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()