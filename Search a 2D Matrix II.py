class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        print(matrix)
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])
        minl = min(m, n)
        stopDiagonalIndex = -1
        # search from the diagonal
        for i in range(minl):
            if target == matrix[i][i]:
                return True
            if target < matrix[i][i]:
                stopDiagonalIndex = i
                break
        # case1: i<minl-1, split matrix in to 3 sub matrix
        print(stopDiagonalIndex)
        if stopDiagonalIndex != -1:
            leftMatrix = [row[:i] for row in matrix[i:]]
            upperMatrix = [row[i:] for row in matrix[:i]]
            return self.searchMatrix(leftMatrix, target) or self.searchMatrix(
                upperMatrix, target
            )
        # case2 i=minl-1, return submatrix, apply same algorithm
        else:
            subMatrix = (
                [row[i + 1 :] for row in matrix] if m == i + 1 else matrix[i + 1 :]
            )
            return self.searchMatrix(subMatrix, target)


matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]
target = 15
print(Solution().searchMatrix(matrix, target))
