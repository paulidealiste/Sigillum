import re
import random
import svgwrite


def get_attr_values(attr_dict):
    '''Reads width and height as ints from svg baseElement attr dict'''
    pattern = re.compile('\d+')
    w = int(re.findall(pattern, attr_dict['width'])[0])
    h = int(re.findall(pattern, attr_dict['height'])[0])
    return ({'w': w, 'h': h})


def point_dict(point, wh):
    '''Creates point starter dict - origin and radius'''
    cx = int(random.uniform(0, wh['w']))
    cy = int(random.uniform(0, wh['h']))
    dx = (wh['w'] - cx) * 0.5
    dy = (wh['h'] - cy) * 0.5
    r = int(random.uniform(dx, dy))
    return ({'cx': cx, 'cy': cy, 'r': r})


def rcol():
    '''Returns random rgb color'''
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    return svgwrite.utils.rgb(r, g, b)
