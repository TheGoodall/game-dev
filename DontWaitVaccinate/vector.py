import math


def subtract(vec1, vec2):
    return map(lambda x: x[0]-x[1], zip(vec1, vec2))


def add(vec1, vec2):
    return map(lambda x: x[0]+x[1], zip(vec1, vec2))


def length(vec):
    return math.sqrt(sum(map(lambda x: x**2, vec)))


def normalise(vec):
    mag = vec_length(vec)
    if mag != 0:
        return map(lambda x: x/mag, vec)
    else:
        return map(lambda _: 0, vec)
