import numpy as np
import matplotlib.pyplot as plt


class Grid:
    def __init__(self, x_size, y_size, z_size):
        self.X, self.Y, self.Z = np.meshgrid(np.linspace(0, x_size, x_size), np.linspace(0, y_size, y_size), np.linspace(0, z_size, z_size))

    def __target__(self, x_pos, y_pos, z_pos):
        self.targetx = x_pos
        self.targety = y_pos
        self.targetz = z_pos

    def __start__(self, x_pos, y_pos, z_pos):
        self.startx = x_pos
        self.starty = y_pos
        self.startz = z_pos

    def visualize_3D_grid(self):
        fig = plt.figure()
        ax = fig.add_subplot(11, projection='3d')

        ax.scatter(self.X, self.Y, self.Z, color = 'b', alpha = 0.1)
        ax.scatter(self.startx, self.starty, self.startz, color = 'g', label = 'start')
        ax.scatter(self.targetx, self.targety, self.targetz, color = 'r', label = 'target')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()

        plt.show()

