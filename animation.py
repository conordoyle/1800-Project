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

class TOC(PPTXScene):
    def construct(self):
        title_short = Title(r"Fibbonaci Sequence")
        self.add(title_short)

        fib_start = Tex(r"$1 + 1 + 2 + \cdots$")
        self.add(fib_start)

        self.play(FadeIn(fib_start))
        self.endSlide()

class SquareToCircle(PPTXScene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * PI / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.endSlide()
        self.play(Transform(square, circle))
        self.endSlide()
        self.play(FadeOut(square))
        self.endSlide()
# define the set of slides you want
slides = [
    TitleSlide,
    TOC,
    SquareToCircle
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
