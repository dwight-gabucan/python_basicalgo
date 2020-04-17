
# the Node class

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_data(self):
        return self.value

    def set_data(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

# the Linked list class
class LinkedList(object):
    def __init__(self,head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, value):
        item = self.head
        while item is not None:
            if item.get_data() == value:
                return item
            else:
                item = item.get_next()
        return None
    
    def deleteAt(self, idx):
        if idx > self.count-1:
            print ("idx > count -1 ")
            return

        if idx == 0:
            self.head = self.head.get_next()
        else:
            tempIndex = 0
            node = self.head
            while tempIndex < idx - 1:
                node = node.get_next()
                tempIndex += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self):
        tempnode = self.head
        while tempnode is not None:
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()


# test out the List
itemList = LinkedList()
itemList.insert(38)
itemList.insert(49)
# itemList.insert(13)
# itemList.insert(15)
itemList.dump_list()

#exercise
# print("Item count: ", itemList.get_count())
# print("Finding item: ", itemList.find(13).get_data())
# print("Finding item: ", itemList.find(78))

itemList.deleteAt(1)
itemList.dump_list()