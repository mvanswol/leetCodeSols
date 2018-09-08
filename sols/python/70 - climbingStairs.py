#
#
# Created By : Mitchell Van Swol
# Date : 9/7/2018
#

# step problem
class Solution(object):
    def climbStairs(self, n):

        if n == 0:
            return 1
        if n == 1:
            return 1
        paths = [0 for i in range(n)]
        paths[0] = 1
        paths[1] = 1

        for i in range(2, n):
            paths[i] = paths[i-1] + paths[i-2]

        return paths[-1]