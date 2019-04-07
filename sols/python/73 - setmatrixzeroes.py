


# give an entire matrix, if an element is zero set its entire row and oclumn to 0


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        columns = set([])
        rows = set([])

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not matrix[i][j]:
                    columns.add(j)
                    rows.add(i)


        for col in columns:
            for i in range(len(matrix)):
                matrix[i][col] = 0


        for row in rows:
            for j in range(len(matrix[row])):
                matrix[row][j] = 0