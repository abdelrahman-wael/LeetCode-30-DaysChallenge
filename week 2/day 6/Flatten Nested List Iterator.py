# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list_ = self.flatten(nestedList)
        print(self.list_)
        self.next_ = 0
        
    def flatten(self,list_):
        merged = []
        for element in list_:
            if element.isInteger():
                merged += [element.getInteger()]
            else:
                merged += self.flatten(element.getList())
        return merged
    
    def next(self) -> int:
        if self.hasNext():
            value = self.list_[self.next_]
            self.next_ +=1
            return value
        return False
        
    
    def hasNext(self) -> bool:
         return self.next_ < len(self.list_)
            

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
