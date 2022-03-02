class Solution:
    def duplicates(self, arr, n):
        # We can treat arra as a map since array only contains elements from 0 to n-1
        ans = []

        for i in range(n):
            index = arr[i] % n
            arr[index] += n

        for i in range(n):
            if(arr[i] >= 2*n):
                ans.append(i)

        return ans if len(ans) > 0 else [-1]
