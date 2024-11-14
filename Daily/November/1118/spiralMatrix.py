from typing import List


class Solution:
    class Position:
        def __init__(self, x, y) -> None:
            self.x = x
            self.y = y

        def __add__(self, other: "Solution.Position"):
            return Solution.Position(self.x+other.x, self.y+other.y)

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])

        direction = [self.Position(0, 1), self.Position(
            1, 0), self.Position(0, -1), self.Position(-1, 0)]
        result = []
        border = [0, m-1, n-1, 0]
        pos = self.Position(0, 0)
        d = 0
        for _ in range(n*m):
            result.append(matrix[pos.x][pos.y])
            np = pos+direction[d]
            if not (border[0] <= np.x <= border[2] and border[1] >= np.y >= border[3]):
                if d == 1 or d == 2:
                    border[d] -= 1
                else:
                    border[d] += 1
                d = (d+1) % 4
                np = pos+direction[d]
            pos = np
        return result
