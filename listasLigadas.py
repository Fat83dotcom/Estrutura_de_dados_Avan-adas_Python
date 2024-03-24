from random import randint


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.__last_item_cache = None

    def pop(self):
        if self.head:
            pop_item: Node = self.head
            previous_item: Node = None
            while pop_item.next:
                previous_item = pop_item
                pop_item = pop_item.next
            if not previous_item:
                self.__last_item_cache = self.head = None
                self.size -= 1
                return pop_item.data
            previous_item.next = None
            self.__last_item_cache = previous_item
            self.size -= 1
            return pop_item.data
        return None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.__last_item_cache = self.head = new_node
            self.size += 1
            return
        pointer = self.__last_item_cache
        self.__last_item_cache = pointer.next = new_node
        self.size += 1

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        if key > (self.size - 1):
            raise IndexError('Index out of range')
        if key < 0:
            raise IndexError('Index must be greater than or equal to zero')
        pointer = self.head
        for i in range(key):
            if pointer.next:
                pointer = pointer.next

        return pointer.data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    linked_list = LinkedList()
    for n in range(100000):
        linked_list.append(randint(0, 1000))
    print(len(linked_list))

    print(linked_list.pop())
    print(linked_list.pop())
    print(linked_list.pop())
    print(linked_list.pop())
    print(linked_list.pop())

    print(len(linked_list))

    linked_list.append(666)
    linked_list.append(666)

    print(len(linked_list))

    for i in linked_list:
        print(i)

    print(len(linked_list))

    print(linked_list[854])
    # li = []
    # for n in range(10000):
    #     li.append(randint(0, 1000))
    # print(len(li))
