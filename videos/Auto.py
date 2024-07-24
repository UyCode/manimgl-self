from manimlib import *

class Auto(Scene):
    def construct(self) -> None:
        # numberplane = NumberPlane()
        # self.add(numberplane)

        circle1 = Circle(start_angle=2)
        circle1.set_stroke(BLUE_E, width=4)
        self.play(ShowCreation(circle1))

        circle2 = Circle()
        circle2.set_stroke(BLUE_E, width=4)
        self.add(circle2)

        self.play(circle1.animate.shift(1.5 * LEFT))

        circle3 = Circle()
        circle3.set_stroke(BLUE_E, width=4)
        self.add(circle3)

        self.play(circle2.animate.shift(1.5 * RIGHT))

        circle4 = Circle();
        circle4.set_stroke(BLUE_E, width=4)
        self.add(circle4)

        self.play(circle4.animate.shift(3 * RIGHT))
        self.wait()

        vg = VGroup(circle1, circle2, circle3, circle4)

        self.play(vg.animate.shift(LEFT * 0.75))

        # self.embed()
        car = Text(
            """
            Beyond
            """,
            font="Eras Bold ITC", font_size=56,
            # t2c is a dict that you can choose color for different text
            t2c={"Car": ORANGE}
        )
        auto = Text(
            """
            Auto
            """,
            should_center=True,
            font="Eras Bold ITC", font_size=56,
            # t2c is a dict that you can choose color for different text
            t2c={"Auto": ORANGE}
        )

        car.next_to(auto, RIGHT, buff=0.5)
        self.play(Write(car), Write(auto))

        # self.bring_to_front(vg)
        self.play(FadeOut(car, LEFT))
        # self.wait(3)
