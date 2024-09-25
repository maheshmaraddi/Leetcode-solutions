class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        # Check if the reshape operation is possible
        if m * n != r * c:
            return mat

        # Create the reshaped matrix
        reshaped_mat = [[0 for _ in range(c)] for _ in range(r)]

        # Fill the reshaped matrix with elements from the original matrix
        row = 0
        col = 0
        for i in range(m):
            for j in range(n):
                reshaped_mat[row][col] = mat[i][j]
                col += 1
                if col == c:
                    col = 0
                    row += 1

        return reshaped_mat