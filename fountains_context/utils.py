from math import log, sqrt

import random


def gaussianDistance(mean, standard_deviation):
    w = 1.0

    while w >= 1.0:
        u1 = random.uniform(-1.0, 1.0)
        u2 = random.uniform(-1.0, 1.0)
        w = u1 * u1 + u2 * u2

    w = sqrt((-2.0 * log(w)) / w)

    return u1 * w * standard_deviation + mean
