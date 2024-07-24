from manimlib import *


class B(Scene):
    def construct(self) -> None:
        # To run this scene properly, you should have "Consolas" font in your computer
        # for full usage, you can see https://github.com/3b1b/manim/pull/680

        

        print("manim dir: ", get_manim_dir())

        grid = NumberPlane((-10, 10), (-5, 5))
        
        #matrix = [[1, 1], [0, 1]]

        self.play(ShowCreation(grid))
        #self.play(grid.animate.apply_matrix(matrix), run_time=3)

        difference = Text(
            """
            بۇ بىر سىناق مەزمۇن بولۇپ
            """,
            font="UKIJ Esliye", font_size=32,
        )

        difference2 = Text(
            """
            بۇ ئۇنىڭ ئىككىنچى قۇرى بولىدۇ، شۇنداقلا ئوڭدىن سولغا ماڭىدۇ.
            """,
            font="UKIJ Esliye", font_size=26,
        )

        VGroup(difference, difference2).arrange(DOWN, buff=1)

        self.play(Write(difference, reverse=True, run_time=2, stroke_color=GREEN))
        #self.play(Write(difference2, reverse=True, stroke_color=RED))

        #self.play(FadeOut(difference, shift=LEFT))
        #self.play(FadeOut(difference2, shift=RIGHT))
        self.wait(1)
        self.play(FadeTransform(difference, difference2, run_time=2))

        self.play(Uncreate(grid))

        self.remove(difference)

        fonts = Text(
            "شۇنداقلا خەتنىڭ خاسلىقىنى ئۆزگەرتىشكە بولىدۇ",
            font="UKIJ Esliye",
            font_size=26,
            t2f={"font": "UKIJ Ruqi", "words": "خاسلىقىنى"},
            t2c={"خاسلىقىنى": BLUE, "شۇنداقلا": GREEN}
        )
        # fonts.set_width(FRAME_WIDTH - 10)
        # fonts.t2f = {"font": "Microsoft Uighur", "words": "خاسلىقىنى"}
        #fonts.t2c = {"خاسلىقىنى": BLUE, "شۇنداقلا": GREEN}

        self.wait(1)
        self.play(FadeOut(difference2))
        self.play(Write(fonts, run_time=2, stroke_color=YELLOW, reverse=True))

        self.remove(difference2)

        self.wait(1)
        self.play(Uncreate(fonts, should_match_start=False))
        self.wait(1)

        # self.play(FadeIn(fonts, shift=RIGHT))
        # self.play(FadeOut(text), FadeOut(difference, shift=LEFT))
        #self.play(Write(fonts, reverse=True))
        #self.wait(2)

        map = SVGMobject(get_manim_dir() + "/media/map.svg", should_center=True, fill_color=GREEN)

        self.play(ShowCreation(map))

        self.wait()

        self.play(map.animate.scale(10))

        self.play(map.animate.shift(DOWN * 8))

        self.play(map.animate.shift(LEFT * 5))

        self.play(map.animate.scale(2))

        star = SVGMobject(get_manim_dir() + "/media/star.svg", fill_color=RED)

        self.play(ShowCreation(star))
        self.play(star.animate.shift(RIGHT * 3))
        self.play(star.animate.shift(DOWN * 1))
        self.play(star.animate.scale(0.5))

        beijing_ug = Text("بېيجىڭ", font="UKIJ Esliye", font_size=60)
        beijing_ug.set_color_by_gradient(GREEN, BLUE, RED)
        self.add(beijing_ug)
        self.play(Write(beijing_ug, reverse=True))

        self.wait(2)

        beijing = Text("北京", font="SimSun Regular", font_size=60)
        beijing_ug.set_color_by_gradient(GREEN, BLUE, RED)
        self.play(Transform(beijing_ug, beijing))

        self.remove(beijing_ug)
        self.play(Uncreate(beijing))
        self.remove(beijing)

        self.wait()

        self.play(Uncreate(star))
        self.remove(star)

        self.play(Uncreate(map))
        self.remove(map)

        return None


