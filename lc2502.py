

class Allocator:
    def __init__(self, n: int):
        self.mem = [0] * n
        self.free_chunks = {0:n} # index of chunk, size of chunk
        self.all_chunks = {}

    def allocate(self, size: int, mID: int) -> int:
        temp_chunks = {}
        res = -1
        for chunk, s in sorted(self.free_chunks.items()):
            if s >= size:
                self.mem[chunk:chunk + size] = [mID] * size
                self.all_chunks[mID] = chunk + size
                if chunk + s not in self.free_chunks:
                    temp_chunks[chunk + size] = s - size
                res = chunk
            else:
                temp_chunks[chunk] = s
        self.free_chunks = temp_chunks
        return res

    def freeMemory(self, mID: int) -> int:
        pass

# Your Allocator object will be instantiated and called as such:
obj = Allocator(8)
param_1 = obj.allocate(1,4)
param_1 = obj.allocate(2,2)
param_1 = obj.allocate(4,4)