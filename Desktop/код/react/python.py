class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isIslandsConverter(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == "0":
                return
            else:
                grid[i][j] = "0"
                isIslandsConverter(i+1,j)
                isIslandsConverter(i-1,j)
                isIslandsConverter(i,j+1)
                isIslandsConverter(i,j-1)
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    counter += 1
                    isIslandsConverter(i, j)
        return counter