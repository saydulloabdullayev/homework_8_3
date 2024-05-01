class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_element(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get_element_count(self, data_type):
        count = 0
        current = self.head
        while current:
            if type(current.data) == data_type:
                count += 1
            current = current.next
        return count

    def find_string(self, string):
        count = 0
        indices = []
        current = self.head
        position = 0
        while current:
            if type(current.data) == str:
                count += 1
                if current.data == string:
                    indices.append(position)
            current = current.next
            position += 1
        return count, indices

    def remove_zeros(self):
        current = self.head
        while current:
            if current.data == 0:
                if current == self.head:
                    self.head = current.next
                    current = self.head
                else:
                    previous.next = current.next
                    current = current.next
            else:
                previous = current
                current = current.next

    def to_list(self):
        element_list = []
        current = self.head
        while current:
            element_list.append(current.data)
            current = current.next
        return element_list

    def reverse_pairs(self):
        current = self.head
        while current and current.next:
            current.data, current.next.data = current.next.data, current.data
            current = current.next


# LinkedList yaratish
ll = LinkedList()

# Elementlarni qo'shish
ll.add_element(5)
ll.add_element('salom')
ll.add_element(True)
ll.add_element(3)
ll.add_element('salom')
ll.add_element([1, 2, 3])

# Har toifadagi elementlar sonini aniqlash
int_count = ll.get_element_count(int)
str_count = ll.get_element_count(str)
bool_count = ll.get_element_count(bool)
list_count = ll.get_element_count(list)

print("int elementlar soni:", int_count)
print("str elementlar soni:", str_count)
print("bool elementlar soni:", bool_count)
print("list elementlar soni:", list_count)

# Kiritilgan string linked list elementlari ichida mavjud bo'lsa necha marta
# qaysi indekslarda uchrashini aniqlash
str_occurrence, str_indices = ll.find_string('salom')
print("salom so'zi", str_occurrence, "marta uchrashdi, indekslari:", str_indices)

# Qiymati nolga teng tugunlarni o'chirish
ll.remove_zeros()

# Linked listni listga o'tkazish
ll_to_list = ll.to_list()
print("Linked listdan list:", ll_to_list)

# Yonma yon tugunlarni almashtirish
ll.reverse_pairs()
reversed_list = ll.to_list()
print("Yonma yon tugunlarni almashtirish:", reversed_list)
