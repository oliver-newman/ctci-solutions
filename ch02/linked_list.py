class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '{0} ->{1}'.format(self.val, ' ' if self.next else '')

    __repr__ = __str__


class LinkedList:
    def __init__(self, items=None):
        self.head = self.tail = None
        if items:
            for item in items:
                self.add_to_tail(item)

    def __len__(self):
        curr = self.head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        return length

    def __eq__(self, other):
        self_curr = self.head
        other_curr = other.head
        while self_curr and other_curr:
            if self_curr.val != other_curr.val:
                return False
            self_curr = self_curr.next
            other_curr = other_curr.next
        return self_curr is other_curr is None

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def __repr__(self):
        return ''.join(str(node) for node in self)

    def add_to_head(self, val):
        self.head = LinkedListNode(val, self.head)

    def add_to_tail(self, val):
        new_tail = LinkedListNode(val)
        if self.tail:
            self.tail.next = new_tail
        else:
            self.head = new_tail
        self.tail = new_tail

    __str__ = __repr__
