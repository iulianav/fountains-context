import random

try:
    from OpenGL.GL import *
except:
    print "OpenGL wrapper for python not found"

from particle import Particle
from utils import gaussianDistance


class Fountain:
 
    def __init__(
        self, context, alive=0, color_mean=0.003, color_variation=0.007,
        context_ejection_size=400.0, dir_mean=0.0, dir_variation=0.02,
        ejection_size=2.0, total=300, life=1000.0, life_variation=100.0,
        speed_mean=7.0, speed_variation=0.1, transparency_lifetime=0.00001,
        ejection_y=120.0, lifetime=0.3, 
        ):

        self.alive = alive
        self.color_mean = color_mean
        self.color_variation = color_variation
        self.context_ejection_size = context_ejection_size
        self.dir_mean = dir_mean
        self.dir_variation = dir_variation
        self.ejection_size = ejection_size
        self.total = total
        self.life = life + random.uniform(-life_variation, life_variation)
        self.mass = context.mass
        self.gravity = context.gravity
        self.speed_mean = speed_mean
        self.speed_variation = speed_variation
        self.transparency_lifetime = transparency_lifetime
        self.ejection_y = ejection_y
        self.lifetime = lifetime

        self.r = random.uniform(0, 1)
        self.g = random.uniform(0, 1)
        self.b = random.uniform(0, 1)

        self.x = random.uniform(-self.context_ejection_size, self.context_ejection_size)
        self.y = 0.0
        self.z = random.uniform(-self.context_ejection_size, self.context_ejection_size)

        self.particles = [Particle(self) for i in range(self.total)]

    def init(self):
       for i in range(self.alive, self.total):
            self.particles[i] = Particle(self)
            self.alive += 1

    def update(self):
        for i in range(self.alive):
            if ((self.r - self.particles[i].r > self.lifetime) and
                (self.g - self.particles[i].g > self.lifetime) and
                (self.b - self.particles[i].b > self.lifetime) or
                (self.particles[i].a < self.transparency_lifetime)):
                self.particles[i] = self.particles[self.alive - 1]
                self.alive -= 1
            else:
                self.particles[i].x += self.particles[i].vx
                self.particles[i].y += self.particles[i].vy
                self.particles[i].z += self.particles[i].vz

                if self.particles[i].y < self.ejection_y:
                    self.particles[i].y = self.ejection_y

                self.particles[i].vx  += gaussianDistance(self.dir_mean, self.dir_variation);
                self.particles[i].vy += self.mass * self.gravity;
                self.particles[i].vz +=gaussianDistance(self.dir_mean, self.dir_variation);

                decrease_amount = 0.0001
                shadeChange = gaussianDistance(self.color_mean, self.color_variation)

                self.particles[i].r -= shadeChange;
                self.particles[i].g -= shadeChange;
                self.particles[i].b -= shadeChange;
                self.particles[i].a -= decrease_amount;

                self.draw(i)

                if self.life <= 0:
                    self.life = 1000.0 + random.uniform(-100.0, 100.0)
                    self.x = random.uniform(-self.context_ejection_size, self.context_ejection_size)
                    self.z = random.uniform(-self.context_ejection_size, self.context_ejection_size)
                    self.r = random.uniform(0, 1)
                    self.g = random.uniform(0, 1)
                    self.b = random.uniform(0, 1)

    def draw(self, i):
        glPointSize(7.0);
        glBegin(GL_POINTS)
        glColor3f(self.particles[i].r,
          self.particles[i].g,
          self.particles[i].b)
        glVertex3f(self.particles[i].x,
          self.particles[i].y,
          self.particles[i].z)
        glEnd()
