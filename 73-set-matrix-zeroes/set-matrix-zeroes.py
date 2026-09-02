class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        zero_rows = []
        zero_cols = []

        # Find zero positions
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.append(i)
                    zero_cols.append(j)

        # Make rows zero
        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0

        # Make columns zero
        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0