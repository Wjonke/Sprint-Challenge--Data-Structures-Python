from doubly_linked_list import DoublyLinkedList

'''
uses a Queue
when new data comes in after max if reached, oldest gets dropped, FIFO method
append = add plus remove last if length max reached
get should return not None 
get sets up the method used to see whats in the dll not append
Append will be used in get, we are creating a custom append method

 RingBuffer has two methods, append and get.  
 The get method, which is provided, returns all of the elements in the buffer in a list in their given order. 
 It should not return any None values in the list even if they are present in the ring buffer.



'''
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if the length of current storage is less than capacity, adds to the tail(back of queue)
        # and sets itself as the head
        if self.storage.length < self.capacity :
            self.storage.add_to_tail(item)
            self.current = self.storage.head

        # if storage = capacity then it is full
        elif  self.storage.length == self.capacity :
            # sets current value to item passed in
            self.current.value = item
            # replace the oldest value(head) with new item
            if self.current == self.storage.tail :
                self.current = self.storage.head

            else:
                self.current = self.current.next


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # set head to a var
        current_item = self.storage.head

        while current_item is not None: # while var is not None its going to run
            # adds current item to list using custom append method
            list_buffer_contents.append(current_item.value)
            # iterates current
            current_item = current_item.next

        return list_buffer_contents










# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
