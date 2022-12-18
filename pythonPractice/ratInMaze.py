def isLegal(maze,x,y):
    if x>=0 and x <=N-1  and y>=0 and y<=N-1 and maze[x][y]==1:
        return True
    return False

def solve(maze,x,y,sol):

    if x == N-1 and y == N-1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True

    if isLegal(maze, x , y) == True:         #check if rat can be moved to x,y position
        sol[x][y]=1
        if solve(maze,x+1,y,sol):            #move in x directon
            return True
        if solve(maze,x,y+1,sol):            #move in y direction
            return True
        sol[x][y]=0                          #if both the above conditions do not satisfy, then backtrack.
        return False

maze = [ [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]
sol=[[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]
N=4
solve(maze,0,0,sol)
print(sol)
