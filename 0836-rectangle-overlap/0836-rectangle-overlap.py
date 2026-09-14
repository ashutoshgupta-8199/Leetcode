class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        h=rec1[0]<rec2[2] and rec2[0]<rec1[2]
        v=rec1[1] < rec2[3] and rec2 [1] <rec1[3]
        return h and v 
        