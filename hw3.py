# === CS 115 Homework 3 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Esther Li
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.

#
# === CS 115 Homework 3 ===

def empty(m, n):
    """Creates a grid with m rows and n columns"""
    return copy([[0] * n] * m)

def copy(grid):
    """Returns a deep copy of the grid"""
    return list(map(lambda x: x[:], grid))

def increase_row(grid, y, cost):
    """Increases every element in row y by cost"""
    grid[y] = (list(map(lambda x: x + cost, grid[y])))
    
def increase_col(grid, x, cost):
    """Increases every element in column x by cost"""
    def add(y):
        y[x] = y[x] + cost
    grid = list(map(add, grid))


    
def distance_from(grid, x, y):
    """Calculates the shortest distance from a point (x,y) to (0,0)"""
    memo = {}
    def inner_distance_from(x,y):
        if(x == 0 and y == 0):
            return grid[x][y]
        
        if(not (x,y) in memo):
                
            if(x==0):
                memo[(x,y)]= grid[x][y] + inner_distance_from(x, y-1)
                
            elif(y==0):
                memo[(x,y)]= grid[x][y] + inner_distance_from(x-1, y)
            
            else: memo[(x,y)] = grid[x][y] + min(inner_distance_from(x, y-1),  inner_distance_from(x-1, y))
        return memo[(x,y)]
    return inner_distance_from(x,y)
     
    
