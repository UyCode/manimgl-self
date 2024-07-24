from manimlib import *

"""
    This is a simple example of how to use SVGMobject.
    It shows how to load a svg file and how to scale and shift it.
"""
class Map(Scene):
    def construct(self):
        map = SVGMobject("../media/map.svg", should_center=True);

        self.play(ShowCreation(map))
        self.wait()

        self.play(map.animate.scale(10))

        self.play(map.animate.shift(DOWN * 8))

        self.play(map.animate.shift(LEFT * 5))

        self.play(map.animate.scale(2))