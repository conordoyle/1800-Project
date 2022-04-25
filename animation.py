from token import LEFTSHIFT
from tokenize import group
from manim import *
from manim_pptx import *

class TitleSlide(PPTXScene):
  def construct(self):

      main_title = Tex(r"Stern-Brocot Trees - CS1800")
      main_title.shift(0.5*UP)
      authors = Tex(r"Conor Doyle, Jonah Lefkoff, and Karthik Yalala", font_size=36)
      authors.shift(1.5*DOWN)
      discrete = Tex(r"CS1800 - Spring 2022", font_size=36)
      discrete.shift(0.5*DOWN)

      title_short = Title(r"Fibbonaci Sequence")

      self.play(
            Write(main_title),
            Write(authors),
            Write(discrete)
      )
      self.endSlide()
    
      self.play(
        Transform(main_title, title_short),
        FadeOut(authors), FadeOut(discrete)
      )
      self.endSlide()

class FibEx(PPTXScene):
    def construct(self):
        title_short = Title(r"Fibbonaci Sequence")
        self.add(title_short)

        fib_1 = Tex(r"$1$")
        fib_2 = Tex(r"$1 + 1$")
        fib_3 = Tex(r"$1 + 1 + 2$")
        fib_4 = Tex(r"$1 + 1 + 2 + \cdots$")
        
        self.play(Write(fib_1))
        self.endSlide()

        self.play(
            ReplacementTransform(fib_1, fib_2)
        )
        self.endSlide

        brace_1 = Brace(fib_2, DOWN, color=BLUE)
        b1_txt = brace_1.get_tex("=2").set_color(BLUE)

        self.play(
            GrowFromCenter(brace_1),
            Write(b1_txt) 
        )
        self.endSlide()

        group_1 = VGroup(fib_2, b1_txt)
        group_1.set_color(WHITE)

        self.play(
            FadeOut(brace_1, b1_txt),
            ReplacementTransform(fib_2, fib_3)
        )
        self.endSlide()

# define the set of slides you want
slides = [
    TitleSlide,
    FibEx,
]


class Slides(*slides):

    def setup(self):
        # setup each scene
        for s in slides:
            s.setup(self)

    def construct(self):
        # play each scene
        for s in slides:
            s.construct(self)
            # if there are any objects left at the end of the animation, remove them!
            if len(self.mobjects) >= 1:
                self.remove(*self.mobjects)
