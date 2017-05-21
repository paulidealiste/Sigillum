import svgwrite
from renderers.rendererutils import get_attr_values, point_dict, rcol
import math
import random


class SvgRenderer(object):
    '''Generates output svg based on the letter-number links

    Attributes:
    '''

    def __init__(self, file_name, linked_object):
        self._linked = linked_object
        self._svg = svgwrite.Drawing(
            filename=file_name, size=("800px", "600px"))

    def output_svg(self):
        '''Outputs rendered svg'''
        starter = self.get_polygon_starter()
        polycoord = self.calc_poly_coords(starter)
        for po in polycoord:
            rc = rcol()
            self._svg.add(self._svg.polygon(
                points=po,
                stroke_width="0",
                fill=rc,
                opacity=random.random()
            ))
        self._svg.save()

    def get_polygon_starter(self):
        '''Returns list of polygon blueprints - origin and radius coords'''
        wh = get_attr_values(self._svg.attribs)
        return list(map(
            lambda x: point_dict(x, wh), self._linked.letter_list))

    def calc_poly_coords(self, starter):
        '''Calculates list of polygon point coordinates.'''
        pc = []
        for i, link in enumerate(self._linked.substitute_zip):
            pc.append(self.poly(link, starter[i]))
        return pc

    def poly(self, l, s):
        '''Calculates pairs of polygon coordinates for one link.'''
        ip = []
        angle = 2 * math.pi / l[1]
        for i in range(l[1]):
            x = int(s['cx'] + s['r'] * math.sin(i * angle))
            y = int(s['cy'] + s['r'] * math.cos(i * angle))
            ip.append((x, y))
        return ip
