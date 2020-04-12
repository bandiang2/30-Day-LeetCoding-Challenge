# Day 12

# Last Stone Weight

# We have a collection of stones, each stone has a positive integer weight.

# Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have #weights x and y with x <= y.  The result of this smash is:

# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

# Example;
#	Input: [2,7,4,1,8,1]
#	Output: 1
#	Explanation: 
#	We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
#	we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
#	we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
#	we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

# My Solution 


class MaxHeap:
    def __init__(self, items=[]):
        self.heap = []
        for item in items:
            self.heap.append(item)
            self.heapify(len(self.heap)-1)
            
    def empty(self):
        return self.heap == []
    def size(self):
        return len(self.heap)
            
    def getLc(self, node):
        return 2*node + 1
    def getRc(self, node):
        return 2*node + 2
    def getPa(self, node):
        return (node-1)//2
    
    def hasLc(self, node):
        return self.getLc(node) < len(self.heap)
    def hasRc(self, node):
        return self.getRc(node) < len(self.heap)
    def hasPa(self, node):
        return self.getPa(node) >= 0
    def swap(self, i , j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def heapify(self, node):
        while self.hasPa(node) and self.heap[node] > self.heap[self.getPa(node)]:
            self.swap(node, self.getPa(node))
            node = self.getPa(node)
            
    def insert(self, item):
        self.heap.append(item)
        self.heapify(len(self.heap)-1)

    def delete(self, root):
        removed_node = self.heap[root]
        self.heap[root] = self.heap[-1]
        if not self.empty():
            _= self.heap.pop(-1)
        self.heapifyDown(root)
        return removed_node
        
    def heapifyDown(self, node):
        largest = node
        if self.hasLc(node) and self.heap[largest] < self.heap[self.getLc(node)]:
            largest = self.getLc(node)
        if self.hasRc(node) and self.heap[largest] < self.heap[self.getRc(node)]:
            largest = self.getRc(node)
            
        if largest != node:
            self.swap(node, largest)
            self.heapifyDown(largest)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        mheap = MaxHeap(stones)
        while mheap.size() > 1:
            y = mheap.delete(0)
            x = mheap.delete(0)
            if x != y:
                mheap.insert(y-x)
        if mheap.empty():
            return 0
        else:
            return mheap.heap[0]


