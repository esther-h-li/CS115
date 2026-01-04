"""
Name: Esther Li
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
"""


def parse_file(filename):
    """
Stores the file information in a grid
"""
    file = open(filename, "r")
    columns = 0
    rows = 0
    grid = []
    for i, line in enumerate(file):
        
        line = line.rstrip()
        toGrid = line.split(" ")
        for j in toGrid:
            if not j.isdigit():
                print("This isn't a number!")
                file.close()
                raise ValueError
            
        toGrid = list(map(lambda x: int(x), toGrid))
        
        if i==0:
            if len(toGrid) != 2:
                print("Make sure you input dimensions!")
                file.close()
                raise ValueError
            else:
                columns = int(toGrid[0])
                rows = int(toGrid[1])
        else:
            if len(toGrid) > columns:
                print("Make sure your columns are accurate!")
                file.close()
                raise ValueError
            if i > rows:
                print("Make sure your rows are accurate!")
                file.close()
                raise ValueError
            if len(toGrid) < columns:
                print("Make sure your columns are accurate!")
                file.close()
                raise ValueError
            grid.append(toGrid)
    if len(grid) != rows:
        print("Make sure your rows are accurate!")
        file.close()
        raise ValueError
    
    file.close()
    return grid


            
            

def distances_from(grid):
    """
    Taking in a grid of costs, returns a 2d array of the shortest distances from each block in the grid
    """
    dist = []
    for i, line in enumerate(grid):
        row = []
        for j, num in enumerate(line):
            if(i == 0 and j == 0):
                row.append(num)
            elif i == 0:
                row.append(num + row[j-1])
            elif j == 0:
                row.append(num + dist[i-1][j])
            else:
                row.append(num + min(dist[i-1][j], row[j-1]))
        dist.append(row)
    return dist

def shortest_path(dists, point):
    """Returns a list of points that is the shortest path from an inputted point"""
    path = []
    while True:
        path.append(point)
        x = point[0]
        y = point[1]
        if(point == (0,0)):
            break;
        elif (x == 0):
            point = (x, y-1)
        elif y == 0:
            point = (x-1, y)
        else:
            if dists[y][x-1] < dists[y-1][x]:
                point = (x-1, y)
            else:
                point = (x,y-1)
    return path
            
    

