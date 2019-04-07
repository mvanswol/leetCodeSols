


# write an efficient algorithm that searchs for a value in an m X n matrix with the following properties
# intergers in each row are sorted from left to right
# the first integer of each row is greater than the last integer of the previous row

# treat as one giant array and calculate with offset
# and binary search 

# o(log(mn))

class Solution:
    def searchMatrix(self, matrix, target):

        if matrix and matrix[0]:
            row_num = len(matrix)
            column_num = len(matrix[0])
            left = 0
            right = row_num * column_num - 1
            while left <= right:
                mid = (left + right) // 2
                row = mid // column_num
                column = mid % column_num
                if target > matrix[row][column]:
                    left = mid + 1
                elif target < matrix[row][column]:
                    right = mid - 1
                else:
                    return True

        return False
                

print(Solution().searchMatrix([[1,1]], 2))

        