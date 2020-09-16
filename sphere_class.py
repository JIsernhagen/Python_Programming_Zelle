import math

class sphere:
    def __init__(self, radius):
        self.radius = float(radius)

    def getRadius(self):
        return self.radius

    def getSurfaceArea(self):
        sphere_area = 4*math.pi*self.radius**2
        return sphere_area

    def getVolume(self):
        sphere_volume = (4 / 3) * math.pi * self.radius ** 3
        return sphere_volume

