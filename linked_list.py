class LinkedList:

    class Item:
        value = None
        next = None

        def init(self, value):
            self.value = value

    head:Item = None
    __count = 0

    @property
    def count(self):
        cur = self.head
        tot = 0
        while cur:
            tot += 1
            cur = cur.next
        return tot
    
    #@count.setter
    #def count(self):
    
    def append_begin(self, value):
        item = LinkedList.Item()
        item.value = value
        item.next = self.head
        self.head = item

    def append_end(self, value):
        current = self.head
        if current is None:
            self.head = LinkedList.Item()
            self.head.value = value
            return
        
        while current.next:
            current = current.next
        item = LinkedList.Item()
        item.value = value
        current.next = item
    
    
    def get_all_list(self):
        st = []
        cur = self.head
        while cur:
            st.append(cur.value)
            cur = cur.next
        return st
    
    def __str__(self):
        st = ''
        for i in self.get_all_list():
            st += f'{str(i)} '
        st = st.strip()
        return st

    def append_by_index(self, value, index):
        '''Метод всавляет значение по указанному индексу,
        оставшиеся элементы сдвигаются'''
        dl = int(self.count)
        fl = False

        if index < 0:
            if abs(index) > dl:
                raise ValueError(f'Индекс {index} находится вне длины списка')
            index = abs(index % dl)
            fl = True

        if index > dl:
            raise ValueError(f'Индекс {index} находится вне длины списка')
        
        if index == 0:
            self.append_begin(value)
            return
        
        elif index == dl:
            self.append_end(value)
            return

        current = self.head
        if fl:
            for i in range(index):
                current = current.next
        else:
            for i in range(index-1):
                current = current.next
        
        item = LinkedList.Item()
        item.value = value
        posle = current.next
        current.next = item
        item.next = posle


    def remove_first(self):
        if self.head == None:
            raise ValueError('LinkedList пуст')
        cur = self.head
        next = cur.next
        self.head = next
        
    def remove_last(self):
        cur = self.head
        if self.head == None:
            raise ValueError('LinkedList пуст')
        if self.count == 1:
            self.head = None
            return
        #for _ in range(self.len_link_list()-2):
        while cur.next.next != None:
            cur = cur.next
        cur.next = None
        
    def remove_at(self, index):
        dl = int(self.count)

        if index < 0:
            if abs(index) > dl:
                raise ValueError(f'Индекс {index} находится вне длины списка')
            index = abs(index % dl)
        
        if index > dl-1:
            raise ValueError(f'Индекс {index} находится вне длины списка')
        
        if index == 0:
            self.remove_first()
            return
        
        elif index == dl-1:
            self.remove_last()
            return      

        cur = self.head
        for _ in range(index-1):
            cur = cur.next
        
        cur.next = cur.next.next
        
    def remove_first_value(self, value):
        if value not in self.get_all_list():
            raise ValueError(f'Данного значения ({value}) нет в списке')

        cur = self.head
        tot = 0
        while cur.next != None:
            if cur.value == value:
                break
            cur = cur.next
            tot += 1
        
        self.remove_at(tot)

    def remove_last_value(self, value):

        lst = self.get_all_list()
        if value not in lst:
            raise ValueError(f'Данного значения ({value}) нет в списке')      

        tot = self.count-1
        while lst[tot] != value:
            tot -= 1
        
        self.remove_at(tot)


#Формирование списка
my_list = LinkedList()
#my_list.append_end(2)
my_list.append_end(3)
my_list.append_end(4)
my_list.append_end(5)
my_list.append_end(0)
my_list.append_by_index(1, 1)
#my_list.append_end(7)
print(my_list.__str__(), end='\n\n')

my_list.remove_at(-5)
# #Добавление по индексу
#my_list.append_by_index(33, -5)
print(my_list.__str__(), end='\n\n')

# #Удаление первого
my_list.remove_first()
print(my_list.__str__(), end='\n\n')

# #Удаление последнего
#my_list.remove_last()
print(my_list.__str__(), end='\n\n')

# #Удаление по индексу
#my_list.remove_at(5)
print(my_list.__str__(), end='\n\n')

# #Удаление первого вхождения
my_list.append_end(4)
print(my_list.__str__(), end='\n\n')
my_list.remove_first_value(4)
print(my_list.__str__(), end='\n\n')

# #Удаление последнего вхождения
my_list.append_end(33)
print(my_list.__str__(), end='\n\n')
my_list.remove_last_value(33)
print(my_list.__str__(), end='\n\n')
# # print(my_list.head.value)
# # print(my_list.head.next.value)
# # print(my_list.head.next.next.value)
# # print(my_list.head.next.next.next.value)
# # print(my_list.head.next.next.next.next.value)
# # print(my_list.head.next.next.next.next.next.value)
# # print(my_list.head.next.next.next.next.next.next.value)]