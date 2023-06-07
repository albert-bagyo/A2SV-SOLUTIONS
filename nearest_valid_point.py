class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index = -1
        dis = 100000
        for k in range(len(points)):
            i = points[k][0]
            j = points[k][1]
            if x == i or y == j:
                newdis = (abs(x - i) + abs(y - j))
                if newdis < dis:
                    dis = newdis
                    index = k
        return index
