class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:  # found a new island!
                    islands += 1

                    q = deque()
                    q.append((i, j))

                    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                    while q:
                        curr = q.popleft()
                        r = curr[0]
                        c = curr[1]

                        for dir in directions:
                            if (
                                r + dir[0] >= 0
                                and r + dir[0] < rows
                                and c + dir[1] >= 0
                                and c + dir[1] < cols
                                and grid[r + dir[0]][c + dir[1]] == "1"
                                and ((r + dir[0]),(c + dir[1])) not in visited
                            ):
                                q.append((dir[0] + r, dir[1] + c))
                                visited.add((dir[0] + r, dir[1] + c))

        return islands
