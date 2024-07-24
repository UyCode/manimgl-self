from manimlib import *

import arabic_reshaper

class ArabicText(Scene):
    def construct(self):

        test = "ياخشىمۇ سىز"

        print("flag 0: ", test)

        f = arabic_reshaper.reshape(test)

        print("flag 1.5: ", f)
        fc = f[::-1]

        print(fc)

        #print("flag 1: ", get_tex_config())
        tex = Text(test + "\n", font="ALKATIP Gezit", font_size=96, disable_ligatures=False, t2c={'سىز': YELLOW})

        self.play(Write(tex, reverse=True))
        self.wait(2)
        # self.play(ShowSubmobjectsOneByOne(tex, run_time=4))
        # self.play(FadeOut(tex))