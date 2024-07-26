import tqdm

from manimlib import *

"""
    This is a simple example of how to use SVGMobject.
    It shows how to load a svg file and how to scale and shift it.
"""
class Map(Scene):
    def construct(self):

        map = SVGMobject(get_manim_dir() + "/media/world-white-2.svg", should_center=True, height=13, width=13)

        self.play(ShowCreation(map))

        for i in range(100):
            random_int = random.randint(0, len(MANIM_COLORS) - 1)
            self.play(FadeToColor(map, MANIM_COLORS[random_int]), run_time=0.5)