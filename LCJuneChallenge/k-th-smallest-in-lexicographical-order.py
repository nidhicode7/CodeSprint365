'''
Leetcode 440:
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1


Constraints:

1 <= k <= n <= 109
'''

class Solution(object):
    def findKthNumber(self, n, k):
        return self.solve(0, n, k)

    def solve(self, current, n, k):
        if k == 0:
            return current // 10

        for i in range(max(current, 1), current + 10):
            count = self.numOfChildren(i, i + 1, n)
            if count >= k:
                return self.solve(i * 10, n, k - 1)
            k -= count

        return -1  

    def numOfChildren(self, current, neighbour, n):
        if neighbour > n:
            if current > n:
                return 0
            return n - current + 1
        return (neighbour - current) + self.numOfChildren(current * 10, neighbour * 10, n)
