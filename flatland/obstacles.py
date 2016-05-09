
import planar
import random


DIM = 2


class RandomObstacleGen(object):

    def __init__(self, **kwargs):
        self.low = kwargs.get("low", -10)
        self.high = kwargs.get("high", 10)
        self.vlow = kwargs.get("vlow", 3)
        self.vhigh = kwargs.get("vhigh", 10)
        self.radlow = kwargs.get("radlow", 0.5)
        self.radhigh = kwargs.get("radhigh", 3)

    def set_low(self, low):
        self.low = low
        return self

    def set_high(self, high):
        self.high = high
        return self

    def set_vertex_low(self, vlow):
        self.vlow = vlow
        return self

    def set_vertex_high(self, vhigh):
        self.vhigh = vhigh
        return self

    def set_radius_low(self, radlow):
        self.radlow = radlow
        return self

    def set_radius_high(self, radhigh):
        self.radhigh = radhigh
        return self

    def generate(self, num):
        obs = list()
        for i in xrange(num):
            x = random.uniform(self.low, self.high)
            y = random.uniform(self.low, self.high)
            vcount = random.randint(self.vlow, self.vhigh)
            radius = random.uniform(self.radlow, self.radhigh)
            center = planar.Vec2(x, y)
            ob = planar.regular(vcount, radius, center=center)
            obs.append(ob)
        return obs
