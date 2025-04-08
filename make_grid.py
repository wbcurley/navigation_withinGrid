import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.mplot3d as axes3d

'''
Use this file to generate a 3 dimensional mesh-grid that can be used as a single frame.
A grid will be "drawn" which includes a known position, a target destination, and known barriers around the points.
Then use vectorizations to determine a "path" between the two points, then use external input equation of state to determine how to manipulate drive system to travel from known point to the target.
Each time the target position is reached, move to generate a new frame.
'''



#cleanup item
class Vector:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.magnitude = 0

#cleanup item
class Point:
    def __init__(self, x_position, y_position, z_position):
        self.x = x_position
        self.y = y_position
        self.z = z_position

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

#pass an array of Point objects to generate a "barrier"
class Barrier:
    def __init__(self, *points: Point):
        Barrier.points = points

#defines a numpy meshgrid of linear spacing across x y and z coordinates
class Grid:
    def __init__(self, x_size, y_size, z_size):
        argdict = {arg: locals()[arg] 
                   for arg in 
                   }
        self.X, self.Y, self.Z = np.meshgrid(np.linspace(-x_size, x_size, 2*x_size), np.linspace(-y_size, y_size, 2*y_size), np.linspace(0, z_size, z_size))
        self.xresolution = 

    #define a target position to navigate to
    def set_target(self, x_position, y_position, z_position):
        self.target = Point(x_position, y_position, z_position)

    #define a current position
    def set_start(self, x_position, y_position, z_position):
        self.start = Point(x_position, y_position, z_position)

    def set_barriers(self, Barrier):
        for i in Barrier:
            self.invalid = Point(Barrier[i].x_position, Barrier[i].y_position, Barrier[i].z_position)

    def check_isTarget(self):
        return(self.target=self.start)

    def check_isInBarrier(self):
        for i in self.invalid:
            if(self.start = self.invalid[i]):
                return True

    #visualize current grid frame
    def visualize_3D_grid(self):
        fig = plt.figure()
        ax = fig.add_subplot(11, projection='3d')

        ax.scatter(self.X, self.Y, self.Z, color = 'b', alpha = 0.1)
        if self.start:
            ax.scatter(self.start.x, self.start.y, self.start.z, color = 'g', label = 'start')
        if self.target:
            ax.scatter(self.target.x, self.target.y, self.target.z, color = 'r', label = 'target')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()

        plt.show()

    #returns x y and z distance between start and target
    def set_distance_to_target(self):
        self.distance = Vector() #initialize the pseudo-vector item
        self.distance.x = self.target.x - self.start.x
        self.distance.y = self.target.y - self.start.y
        self.distance.z = self.target.z - self.start.z

        self.distance.magnitude = math.sqrt(self.distance.x^2 + self.distance.y^2 + self.distance.z^2)
    
    def clean_points(self, *points: Point):
        for point in points:
            