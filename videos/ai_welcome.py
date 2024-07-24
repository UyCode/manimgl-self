import numpy as np

from manimlib import *


class Welcome(Scene):
    def construct(self):
        # Create text objects

        manimText = Text("ManimGL", font_size=28).to_corner(RIGHT + UP)

        title = Text(
            """
            دۇنياسىغا كەلگىنىڭىزنى قارشى ئالىمىز
            """
            , font_size=28, font="ALKATIP Esliye").next_to(manimText, LEFT)
        subtitle = Text("A Modern Approach to Mathematical Animations", font_size=24).next_to(title, DOWN)

        subtitle_ug = Text("ھازىرقى زامان ماتىماتىكىلىق كارتون ماتورى", font_size=28, font="ALKATIP Esliye").next_to(
            subtitle, DOWN)

        title.set_color_by_gradient(GREEN, YELLOW, BLUE, RED)
        manimText.set_color_by_gradient(GREEN, YELLOW, BLUE, RED)

        self.play(Write(title, reverse=True, stroke_color=GREEN), Write(manimText, reverse=True, stroke_color=YELLOW))
        self.play(Write(subtitle))
        subtitle_temp = subtitle.copy()
        self.play(Transform(subtitle_temp, subtitle_ug))

        binezir = Tex("By: Binezir", font_size=32)
        binezir.set_color_by_gradient(YELLOW, GREEN, TEAL_A, TEAL_B, TEAL_C, BLUE, RED)
        self.play(ShowCreation(binezir))

        self.play(binezir.animate.scale(0.5).to_corner(LEFT + DOWN))

        self.play(FadeOut(subtitle_ug, RIGHT), FadeOut(subtitle_temp, LEFT))

        # Create a circle and add it to the scene
        circle = Circle(radius=1.0, color=BLUE)
        square = Square(side_length=2.0, color=RED)
        self.play(ShowCreation(circle), ShowCreation(square))
        # self.play(ShowCreation(square))
        self.play(circle.animate.shift(LEFT * 4 + UP * 2), square.animate.shift(RIGHT * 4 + DOWN * 2))

        self.wait(1)

        to_isolate = ["B", "C", "=", "(", ")"]

        color_map = {"A": BLUE, "B": TEAL, "C": GREEN}

        lines = VGroup(
            Tex("A^2", "+", "B^2", "=", "C^2", tex_to_color_map=color_map),
            Tex("A^2", "=", "C^2", "-", "B^2", tex_to_color_map=color_map),
            Tex("A^2 = (C + B)(C -B)", tex_to_color_map=color_map, isolate=["A^2", *to_isolate]),
            Tex("A = \\sqrt{(C + B)(C - B)}", tex_to_color_map=color_map, isolate=["A", *to_isolate]),
            Tex("")
        )

        lines.arrange(DOWN, buff=MED_LARGE_BUFF)

        self.play(ShowCreation(lines[0]))

        self.play(TransformMatchingTex(lines[0].copy(), lines[1], path_arc=90 * DEGREES, key_map={
            "A^2": "A^2",
            "B^2": "B^2",
            "C^2": "C^2"
        }).set_rate_func(smooth(1.5)), run_time=2)
        self.play(TransformMatchingTex(lines[1].copy(), lines[2], key_map={
            "C^2": "C",
            "B^2": "B",
        }).set_rate_func(exponential_decay(1.5, 0.2)), run_time=2)

        new_line2 = Tex("A^2 = (C + B)(C - B)", tex_to_color_map=color_map, isolate=["A", *to_isolate])
        new_line2.replace(lines[2])
        new_line2.match_style(lines[2])

        self.play(TransformMatchingTex(new_line2, lines[3]).set_rate_func(exponential_decay(1.5, 0.2)), run_time=2)

        self.play(FadeOut(lines[0], shift=RIGHT), FadeOut(lines[2], shift=RIGHT), FadeOut(lines[1], shift=LEFT),
                  FadeOut(lines[3], shift=LEFT))

        square2 = Square(side_length=2.0, color=RED)

        self.play(ReplacementTransform(circle, square2))

        circle2 = Circle(radius=1.0, color=BLUE)

        self.play(ReplacementTransform(square, circle2))

        self.play(FadeOut(subtitle))
        self.play(FadeOut(manimText), FadeOut(title))

        self.play(Uncreate(circle2))
        self.play(Uncreate(square2))

        objs = tuple(self.get_mobjects())


class CreateCoordinate(Scene):

    def construct(self) -> None:
        coordinate_plane = NumberPlane(
            x_range=[-10, 10],
            y_range=[-10, 10],
            axis_config={"include_numbers": True},
            background_line_style={
                "stroke_color": GREY_BROWN,
                "stroke_width": 1,
                "stroke_opacity": 0.5,
            },
        )

        self.play(ShowCreation(coordinate_plane))

        a = Line(start=coordinate_plane.get_origin(), end=((RIGHT + UP) + coordinate_plane.get_origin()))
        self.add(a)
        self.play(ShowCreation(a))


class SinAndCosFunctionPlot(Scene):
    def construct(self):
        axes = Axes((-4, 9), (-1, 4, 0.5),
                    axis_config={
                        "stroke_color": GREY_A,
                        "line_to_number_buff": LARGE_BUFF,
                        "stroke_width": 2,
                    },
                    y_axis_config={
                        "line_to_number_buff": MED_SMALL_BUFF,
                    }
                    )
        axes.add_coordinate_labels(font_size=10, num_decimal_places=1, x_tip=True, y_tip=True)

        print(axes.get_origin())

        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        #
        # t = axes.get_origin()[0] + float(((axes.get_all_ranges()[0])[1]))
        #
        # print(t)
        #
        # vec_x = VectorFrom(start=np.array([t, 0, 0]), end=np.array([t + 0.5, 0, 0]), stroke_width=2)
        # vec_x.shift(UP * axes.get_origin()[1])
        # self.add(vec_x)

        # self.play(axes.animate.shift(UP * 3))

        # Axes.get_graph will return the graph of a function
        sin_graph = axes.get_graph(
            lambda x: math.sin(x),
            color=BLUE,
        )

        cos_graph = axes.get_graph(
            lambda x: math.cos(x),
            color=GREEN,
        )

        # Axes.get_graph_label takes in either a string or a mobject.
        # If it's a string, it treats it as a LaTeX expression.  By default
        # it places the label next to the graph near the right side, and
        # has it match the color of the graph
        sin_label = axes.get_graph_label(sin_graph, "\\sin(x)")
        cos_label = axes.get_graph_label(cos_graph, "\\cos(x)")

        dot = Dot(ORIGIN, color=RED)
        self.add(dot)

        line = Line(start=axes.get_origin() + UP, end=axes.get_origin() + DOWN)
        line.shift(RIGHT * PI)
        self.add(line)

        self.play(
            ShowCreation(sin_graph),
            ShowCreation(cos_graph),
            FadeIn(sin_label, RIGHT),
            FadeIn(cos_label, RIGHT),
        )
        circle = Circle(radius=1.0, color=YELLOW, arc_center=axes.get_origin(), start_angle=PI)
        self.play(ShowCreation(circle))


class PlayAll(Scene):

    def construct(self):
        Welcome.construct(self)
        SinAndCosFunctionPlot.construct(self)
