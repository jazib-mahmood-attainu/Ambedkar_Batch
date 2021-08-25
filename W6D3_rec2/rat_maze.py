def No_of_ways(x,y,r,c,grid):
    if y==c:
        return 0

    if x==r:
        return 0

    if x == r-1 and y == c-1:
        return 1

    if grid[x][y] == 1:
        return 0

    ans  = No_of_ways(x,y+1,r,c,grid)+No_of_ways(x+1,y,r,c,grid)
    return ans


if __name__=="__main__":
    grid = [[0,0,1,1],[1,0,0,0],[1,0,0,0]]
    r = len(grid)
    c = len(grid[0])
    print(No_of_ways(0,0,r,c,grid))