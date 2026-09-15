class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Merge both arrays
        l1 = nums1 + nums2
        # Sort the merged array
        l = sorted(l1)
        # Get length
        leng = len(l)
        # If odd length, return middle element
        if leng % 2 != 0:
            ans = (leng // 2)
            return l[ans] 
        # If even length, return average of two middle elements
        elif leng % 2 == 0:
            ans = (l[leng // 2] + l[(leng // 2) - 1]) / 2.0
            return ans  
            
            
        