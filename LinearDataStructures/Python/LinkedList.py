class Node:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head=Node(), tail=None, length=0) -> None:
        self.head = head
        self.tail = tail
        self.length = length
    
    def print_list(self):
        curr = self.head.next
        while curr is not None:
            print(curr.val, end='')
            curr = curr.next
            if curr is not None:
                print(' -> ', end='')
        print()
        
    def add_node_at_head(self, num):
        new_node = Node(num, self.head.next)
        self.head.next = new_node
        if self.tail is None:
            self.tail = new_node
        self.length += 1
    
    def add_node_at_tail(self, num):
        new_node = Node(num, None)
        if self.head.next is None:
            self.head.next = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def remove_node(self, num):
        curr = self.head.next
        pre = self.head
        while curr is not None:
            if curr.val == num:
                pre.next = curr.next
                self.length -= 1
                return 1
            else:
                pre = curr
                curr = curr.next
        return 0

    def insert_node(self, pos, num):
        if pos < 0 or pos > self.length + 1:
            raise RuntimeError('pos参数的范围在 0 ~ length+1 之间')
        curr = self.head
        while pos > 0:
            curr = curr.next
            pos -= 1
        new_node = Node(num, curr.next)
        curr.next = new_node

if __name__ == "__main__":
    linked_list = LinkedList()

    print("头插法测试: 0~4倒序插入")
    for i in range(0, 5):
        linked_list.add_node_at_head(i)
    linked_list.print_list()

    print("尾插法测试: 5~9正序插入")
    for i in range(5, 10):
        linked_list.add_node_at_tail(i)
    linked_list.print_list()

    print("链表长度: ", linked_list.length)

    print("移除值为0的结点:")
    result = linked_list.remove_node(0)
    linked_list.print_list()

    print("在0号位置插入10:")
    linked_list.insert_node(0, 10)
    linked_list.print_list()