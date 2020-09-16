import math

class cube:
    def __init__(self, edge):
        self.edge = float(edge)

    def getEdge(self):
        return self.edge

    def getSurfaceArea(self):
        cube_surface_area = 6 * self.edge**2
        return cube_surface_area

    def getVolume(self):
        cube_volume = self.edge ** 3
        return cube_volume
