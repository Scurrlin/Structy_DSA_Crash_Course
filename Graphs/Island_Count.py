# Write a function, island_count, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the number of islands on the grid. An island is a vertically or horizontally connected region of land.

def island_count(grid):

    visited = set()
    count = 0
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited) == True:
                count += 1
            
    return count

def explore(grid, r, c, visited):

    row_inbounds = 0 <= r < len(grid)
    column_inbounds = 0 <= c < len(grid[0])
    
    if not row_inbounds or not column_inbounds:
        return False
    
    if grid[r][c] == 'W':
        return False
    
    pos = (r,c)
    if pos in visited:
        return False
    
    visited.add(pos)
    explore(grid, r - 1, c, visited)
    explore(grid, r + 1, c, visited)  
    explore(grid, r, c - 1, visited)
    explore(grid, r, c + 1, visited)
    
    return True

# Time Complexity: O(n)
# Space Complexity: O(n)