# Time Complexity :O(1)
# Space Complexity :O(1)
# Did this code successfully run on Leetcode :yes

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeked_value = None

        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peeked_value is None:
            self.peeked_value = self.iterator.next()
        return self.peeked_value
        

    def next(self):
        """
        :rtype: int
        """
        if self.peeked_value is not None:
            result = self.peeked_value
            self.peeked_value = None
            return result
        return self.iterator.next()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peeked_value is not None or self.iterator.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].