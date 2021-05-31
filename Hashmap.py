from double_ll import DoubleLinkedList

class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size 
        self.array = [DoubleLinkedList() for i in range(self.array_size)]

    def hash(self, key, collisions=0):
        key_bytes = str(key).encode()
        hash_code = sum(key_bytes)
        return hash_code + collisions 

    def compressor(self, hash_code):
        return hash_code % self.array_size
    
    def setter(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]
        current_ll_head_node = current_array_value.get_head_node()

        if current_ll_head_node == None:
            current_array_value.add_to_head([key, value])
            return 
        
        if current_ll_head_node.get_value()[0] == key:
            current_array_value.add_to_tail([key, value])
            return 
        
        number_collisions = 1
        while current_ll_head_node.get_value()[0] != key:
            new_hash_code = self.hash(key ,number_collisions)
            new_array_index = self.compressor(new_hash_code)
            new_array_value = self.array[new_array_index]
            new_ll_head_node = new_array_value.get_head_node()

            if new_ll_head_node == None:
                current_array_value.add_to_head([key, value])
                return 
            
            if new_ll_head_node.get_value()[0] == key:
                new_array_value.add_to_tail([key, value])
                return 
            
            number_collisions += 1
            return 


    def retrieve(self, key):
        returns = []
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]
        current_ll_head_node = current_array_value.get_head_node()

        if current_ll_head_node == None:
            print("There is no server there! ")
            return None 
        
        if current_ll_head_node.get_value()[0] == key:
            current_node = current_ll_head_node
            while current_node:
                returns.append(current_node)
                current_node = current_node.get_link()
            
        retrieve_collisions = 1
        
        while current_ll_head_node.get_value()[0] != key:
            new_hash = self.hash(key, retrieve_collisions)
            new_array_index = self.compressor(new_hash)
            new_array_value = self.array[new_array_index]
            new_ll_head_node = new_array_value.get_head_node()

            if new_ll_head_node == None:
                print("There is no server there! ")
                return None 
            
            if new_ll_head_node.get_value()[0] == key:
                current_node = new_ll_head_node
                while new_ll_head_node:
                    returns.append(new_ll_head_node)
                    current_node = current_node.get_link()
            
            retrieve_collisions += 1
            return 
        
        return returns 

    
    def delete(self, key):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]
        current_ll_head_node = current_array_value.get_head_node()

        if current_ll_head_node == None:
            pass
        
        if current_ll_head_node.get_value()[0] == key:
            self.array[array_index] = DoubleLinkedList()
            return 
        
        del_collisions = 1
        while current_ll_head_node.get_value()[0] != key:
            new_hash_code = self.hash(key, del_collisions)
            new_array_index = self.compressor(new_hash_code)
            new_array_value = self.array[new_array_index]
            new_ll_head_node = new_array_value.get_head_node()

            if new_ll_head_node == None:
                pass 
            
            if new_ll_head_node.get_value()[0] == key:
                self.array[new_array_index] = DoubleLinkedList()
                return 
            
            del_collisions += 1
            return

    def get_array(self):
        return self.array

test = HashMap(4)

test.setter(1, 2)
test.setter(1, 3)
test.setter(3, 4)
test.delete(1)
print(test.get_array())


servers = test.retrieve(3)

for i in servers:
    print(i.get_value()[1])