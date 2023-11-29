import math
class Cylinder:
    def __innit__(self, height, radius=1):
        self.height = height
        self.radius = radius
        self.surface_area = self.get_surface_area()
        self.volume = self.get_volume()
    def get_surface_area(self):
        surface_area = 2 * math.pi * self.radius * self.height + 2 * math.pi *self.radius**2
        self.surface_area = surface_area
        return round(surface_area, 2)
    def get_volume(self):
        volume = math.pi * self.radius**2 * self.height
        self.volume = volume
        return round(volume, 2)
cylinder = Cylinder(10, 5)
print(f"Surface area: {cylinder.surface_area} square units")
print(f"Volume: {cylinder.volume} cubic units")