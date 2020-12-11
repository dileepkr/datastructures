class BinaryHeap:
    def __init__(self):
        """
        Binary heap Abstract data structure
        """
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, element):
        self.heap_list.append(element)
        self.current_size += 1
        self.percolate_up(self.current_size)
    
    def percolate_up(self, nth_elem):
        while nth_elem // 2 > 0:
            if self.heap_list[nth_elem] < self.heap_list[nth_elem // 2]:
                self.heap_list[nth_elem], self.heap_list[nth_elem // 2] = self.heap_list[nth_elem // 2], self.heap_list[nth_elem]
            nth_elem = nth_elem // 2

    def del_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.heap_list.pop()
        self.percolate_down(1)
        return retval
    
    def percolate_down(self, element_index):
        while element_index * 2 < self.current_size:
            min_child_idx = self.min_child(element_index)
            if self.heap_list[element_index] > self.heap_list[min_child_idx]:
                self.heap_list[element_index], self.heap_list[min_child_idx] = self.heap_list[min_child_idx], self.heap_list[element_index]
            element_index = min_child_idx

    def min_child(self, element_idx):
        if 2*element_idx+1 > self.current_size:
            return 2*element_idx
        else:
            if self.heap_list[2*element_idx] < self.heap_list[2*element_idx+1]:
                return 2*element_idx
            else:
                return 2*element_idx+1
    
    def build_heap(self, input_list):
        mid_pt = len(input_list) // 2
        self.current_size = len(input_list)
        self.heap_list = [0] + input_list[:]
        while mid_pt > 0:
            self.percolate_down(mid_pt)
            mid_pt = mid_pt - 1


if __name__ == "__main__":

    b1 = BinaryHeap()
    b1.build_heap([9,3,7,4,2,6,1,89])
    print(b1.heap_list)
    b1.insert(5)
    print(b1.heap_list)