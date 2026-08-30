class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and ((i, j)) not in visited:
                    # new island
                    islands += 1
                    visited.add((i, j))

                    # run bfs on island
                    q = collections.deque()
                    q.append((i, j))

                    while q:
                        r, c = q.popleft()

                        directions = [(0,1), (1,0), (-1, 0), (0, -1)]

                        for dir in directions:
                            curr_row = r + dir[0]
                            curr_col = c + dir[1]

                            if curr_row >= 0 and curr_row < rows and curr_col >= 0 and curr_col < cols and grid[curr_row][curr_col] == "1" and (curr_row, curr_col) not in visited:
                                q.append((curr_row, curr_col))
                                visited.add((curr_row, curr_col))



        return islands
        