#  Time Complexity : O(1) for insert, and O(n) for remove and contains
#  Space Complexity : O(n)
#  Did this code successfully run on Leetcode : YES
#  Any problem you faced while coding this :


#  Your code here along with comments explaining your approach
class MyHashSet:

    # HashSet is an array of arrays lenght 10000. Constraint 0 <= key <= 10^6
    def __init__(self):
        self.n = 10000
        self.arr = [[] for _ in range(self.n)]

    # Hash function is mod of the length of the array 10000
    # to find the array index in which a key will go, we will mod the key by 10000
    # then check if the key already exist in the array at the given index and insert
    # Complexity: O(1)
    def add(self, key: int) -> None:
        index = key % self.n
        if key not in self.arr[index]:
            self.arr[index].append(key)

    # find the array index in which the key could be
    # if present in the array, remove it
    # Complexity: O(n)
    def remove(self, key: int) -> None:
        index = key % self.n
        if key in self.arr[index]:
            self.arr[index].remove(key)

    # Complexity: O(n)
    def contains(self, key: int) -> bool:
        index = key % self.n
        return key in self.arr[index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)