import random

from utils import gaussianDistance


class Particle:

    def __init__(
        self, fountain, ejection_size=2.0, shade_variation=0.03, speed_mean=7.0,
        speed_variation=0.2, transparency_mean=0.3, transparency_variation=0.1,
        ):

        self.ejection_size = ejection_size
        self.shade_variation = shade_variation
        self.speed_mean = speed_mean
        self.speed_variation = speed_variation
        self.transparency_mean = transparency_mean
        self.transparency_variation = transparency_variation

        self.x = fountain.x + random.uniform(-self.ejection_size, self.ejection_size)
        self.y = 0.0
        self.z = fountain.y + random.uniform(-self.ejection_size, self.ejection_size)

        self.vx = 0.0
        self.vy = gaussianDistance(self.speed_mean, self.speed_variation)
        self.vz = 0.0
        
        self.r = gaussianDistance(fountain.r, self.shade_variation)
        self.g = gaussianDistance(fountain.g, self.shade_variation)
        self.b = gaussianDistance(fountain.b, self.shade_variation)
        self.a = gaussianDistance(self.transparency_mean, self.transparency_variation)
