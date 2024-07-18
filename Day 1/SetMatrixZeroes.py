class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        C0 = False

        for i in range(m):
            if matrix[0][i] == 0:
                C0 = True
                break

        for i in range(1, n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    continue

        for i in range(1,n):
            if matrix[i][0] == 0:
                for j in range(m):
                    matrix[i][j] = 0

        for j in range(m):
            if matrix[0][j] == 0:
                for i in range(n):
                    matrix[i][j] = 0

        if C0:
            for j in range(m):
                matrix[0][j] = 0
