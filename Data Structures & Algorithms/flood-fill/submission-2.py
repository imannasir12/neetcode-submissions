class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:    
        q = collections.deque()
        q.append((sr, sc))
        original = image[sr][sc]

        seen = set()
        seen.add((sr, sc))

        while q:
            curr = q.popleft()

            r, c = curr[0], curr[1]

            image[r][c] = color

            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            for dir in directions:
                curr_row = r + dir[0]
                curr_col = c + dir[1]
                if (
                    curr_row >= 0
                    and curr_row < len(image)
                    and curr_col >= 0
                    and curr_col < len(image[0])
                    and image[curr_row][curr_col] == original
                    and (curr_row, curr_col) not in seen
                ):
                    q.append((curr_row, curr_col))
                    seen.add((curr_row, curr_col))

        return image
