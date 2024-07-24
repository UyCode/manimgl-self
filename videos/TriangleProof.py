from manimlib import *


class Welcome(Scene):
    def construct(self) -> None:
        text = Text("Welcome to Manim!")
        self.play(Write(text))
        self.remove(*tuple(self.get_mobjects()))


class CreateCoordinateSystem(Scene):
    def construct(self) -> None:
        x_axis_config = dict(include_numbers=True, color=BLUE)

        plan = NumberPlane([-10, 10], [-10, 10], x_axis_config=x_axis_config)

        #plan.__setattr__("origin", ORIGIN)
        print(plan.__getattribute__("origin"))
        self.play(ShowCreation(plan))


        line = Line(ORIGIN, 2 * RIGHT).set_color(RED)
        line2 = Line(RIGHT * 2, 2 * UP).set_color(RED)
        line3 = Line(2 * UP, ORIGIN).set_color(RED)

        self.play(ShowCreation(line))
        self.play(ShowCreation(line2))
        self.play(ShowCreation(line3))

        line_orignal_length = line.get_length()
        line3_orignal_length = line3.get_length()

        line_a = Text("a", color=RED).next_to(line, DOWN)
        line_c = Text("b", color=RED).next_to(line3, LEFT)
        line_b = Text("c", color=RED).next_to(line2, RIGHT)

        self.play(Write(line_a))
        self.play(Write(line_b))
        self.play(Write(line_c))

        # draw line a square
        line11 = Line(1 * DOWN, np.array([line.get_length() ** 2, -1, 0])).set_color(RED)
        self.play(Transform(line, line11))
        line_a_square = Text("a²", color=RED).next_to(line11, DOWN)
        self.play(Transform(line_a, line_a_square))

        # draw line b square
        line22 = Line(1 * DOWN, np.array([-(line3.get_length() ** 2), -1, 0])).set_color(RED)
        line_c_square = Text("b²", color=RED).next_to(line22, DOWN)
        self.play(Transform(line3, line22))
        self.play(Transform(line_c, line_c_square))

        # draw line c square

        line33 = Line(np.array([line_orignal_length ** 2, 0, 0]),
                      np.array([-(line3_orignal_length ** 2), 0, 0])).set_color(RED)
        line_b_square = Text("c²", color=RED).next_to(line33, UP)
        self.play(Transform(line2, line33))
        self.play(Transform(line_b, line_b_square))

        line_add = Line(np.array([-(line3_orignal_length ** 2), -1, 0]), np.array([line_orignal_length ** 2, -1, 0]))
        self.add(line_add)

        self.remove(line, line_a, line3, line_c)

        self.play(Transform(line_add, line33))

        # triangle = RegularPolygon(3).set_color(BLUE)

        # self.play(ShowCreation(triangle))



        self.remove(*tuple(self.get_mobjects()))


class OverAll(Scene):
    def construct(self):
        Welcome.construct(self)
        CreateCoordinateSystem.construct(self)