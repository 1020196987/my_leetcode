class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # print(list(zip(*[(2, 1), (2, 1), (2, 1)])))
        # a = [2, 2, 2]
        # b = [1, 1, 1]
        # print(list(zip(a, b)))  # 打包
        # # [(2, 1), (2, 1), (2, 1)]
        # print(list(zip(*zip(a, b))))  # 解压
        # # [(2, 2, 2), (1, 1, 1)]
        # # matrix[:] = zip(*matrix[::-1])
        # print(matrix)
        # print(list(zip(matrix)))
        # print(matrix[::-1])
        matrix[:] = [[j[i] for j in matrix] for i in range(len(matrix[0]))]
        return matrix


s = Solution()
res = s.rotate([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(res)
