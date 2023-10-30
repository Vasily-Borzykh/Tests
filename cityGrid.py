import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from collections import deque
from queue import PriorityQueue

class CityGrid :
    
    def __init__(self, n, m, r, obstacles_probability = 0.1):
        self.n = n
        self.m = m
        self.r = r
        self.grid = [[0 for _ in range(m)] for _ in range(n)]
        self.obstacles = set()
        for i in range(n):
            for j in range(m):
                if random.random() < obstacles_probability:
                    self.grid[i][j] = 1
                    self.obstacles.add((i, j))

    def visualize_grid(self):
        bounds = [0, 1, 2, 3, 4]
        colors = ['#FFFFFF', '#808080', '#FFA500', '#40E0D0', '#00FFFF']
        cmap = matplotlib.colors.ListedColormap(colors)
        norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)
        grid_data = np.array(self.grid)
        plt.imshow(grid_data, cmap=cmap, norm=norm, interpolation='nearest', extent=[0, self.m, 0, self.n], origin='lower')
        plt.show()

    def place_tower(self, towers = None):
        self.counts = set()
        if (towers):
            count_towers = 0
            while towers > count_towers:
                count_towers += 1
                min_count = 0
                self.counts.clear()
                for i in range(self.n):
                    for j in range(self.m):
                        if(self.grid[i][j] == 0):
                            count = 0
                            for k in range(max(0, i - self.r + 1), min(self.n, i + self.r)):
                                for c in range(max(0, j - self.r + 1), min(self.m, j + self.r)):
                                    if self.grid[k][c] == 0:
                                        count += 1
                            self.counts.add((i, j, count)) 
                for item in self.counts:
                    i, j, count1 = item
                    if count1 > min_count:
                        min_count = count1
                        max_i = i
                        max_j = j
                CityGrid.radar_around_tower(self, max_i, max_j)
        else:
            while CityGrid.exist(self):
                min_count = 0
                self.counts.clear()
                for i in range(self.n):
                    for j in range(self.m):
                        if(self.grid[i][j] == 0):
                            count = 0
                            for k in range(max(0, i - self.r + 1), min(self.n, i + self.r)):
                                for c in range(max(0, j - self.r + 1), min(self.m, j + self.r)):
                                    if self.grid[k][c] == 0:
                                        count += 1
                            self.counts.add((i, j, count)) 
                for item in self.counts:
                    i, j, count1 = item
                    if count1 > min_count:
                        min_count = count1
                        max_i = i
                        max_j = j
                CityGrid.radar_around_tower(self, max_i, max_j)

                                                
    def exist(self):
        check = False
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == 0:
                    check = True
                    break
            if check:
                break
        return check            
                
    def radar_around_tower(self, x, y):
        for i in range(max(0, x - 1), min(self.n, x + 2)):
            for j in range(max(0, y - 1), min(self.m, y + 2)):
                if self.grid[i][j] == 0:
                    self.grid[i][j] = 3
        self.grid[x][y] = 2
        
n, m = 10, 10
r = 2
towers = 5
city = CityGrid(n, m, r)
city.visualize_grid()
city.place_tower(towers)
city.visualize_grid()