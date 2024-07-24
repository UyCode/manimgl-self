from manimlib import *


class TexDemo(Scene):

    def construct(self):
        tex = Tex(r"Welcome to the LaTeX ")
        math = Tex("\\frac{1}{2} + \\frac{1}{2} = 1")

        tex.set_color_by_gradient(BLUE, GREEN, YELLOW, PURPLE, BLUE, GREEN, RED, YELLOW, )
        math.set_color_by_gradient(BLUE, GREEN, RED, YELLOW, PURPLE)

        VGroup(tex, math).arrange(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(tex))
        self.play(Write(math))
