class LinkedList:

    class Item:
        value = None
        next = None

        def init(self, value):
            self.value = value

    head:Item = None

    def __len__(self):
        cur = self.head
        tot = 0
        while cur:
            tot += 1
            cur = cur.next
        return tot
    
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
        st = []
        cur = self.head
        while cur:
            st.append(str(cur.value))
            cur = cur.next
        return ''.join(st)

    def append_by_index(self, value, index):
        '''Метод всавляет значение по указанному индексу,
        оставшиеся элементы сдвигаются'''
        dl = len(self)
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
        if len(self) == 1:
            self.head = None
            return
        #for _ in range(self.len_link_list()-2):
        while cur.next.next != None:
            cur = cur.next
        cur.next = None
        
    def remove_at(self, index):
        dl = len(self)

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

        cur = self.head
        count_value = 0

        if self.head == None:
            raise ValueError("Список пуст")
        
        elif self.head.value == value:
            if self.head.next == None:
                self.head = None
            else:
                self.head = cur.next
            return

        while cur.next != None:
            if cur.next.value == value:
                if cur.next.next == None:
                    cur.next = None
                    count_value += 1
                    return
                else:
                    cur.next = cur.next.next
                    count_value += 1
                    return
                
            cur = cur.next

        if count_value == 0:
            raise ValueError(f'Данного значения ({value}) нет в списке')

    def remove_last_value(self, value):

        cur = self.head
        count_value = 0

        while cur != None:
            if cur.value == value:
                count_value += 1
            cur = cur.next

        if count_value == 0:
            raise ValueError(f'Данного значения ({value}) нет в списке')      
        
        cur_2 = self.head
        tot = 0

        while cur_2.next != None:
            if cur_2.next.value == value and count_value == tot+1:
                if cur_2.next.next == None:
                    cur_2.next = None
                    break
                else:
                    cur_2.next = cur_2.next.next
                    break
            elif cur_2.value == value:
                tot += 1
            cur_2 = cur_2.next
        else:
            self.head = None
