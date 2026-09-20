class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        INF = float('inf')
        n= len(arr)
        best = [INF]*n
        left = 0
        shortest = INF
        answer = INF
        currentSum=0
        for i in range(n):

            currentSum = currentSum+arr[i]
            while currentSum>target:
                currentSum-=arr[left]
                left+=1

            if currentSum==target:
                length = i -left+1
                if left>0:
                    answer = min(answer,best[left-1]+length)
                shortest = min(shortest,length)
            best[i]=shortest
        print(best)
        if answer==INF:
            return -1
        else:
            return answer



            
        