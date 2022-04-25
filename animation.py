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

        fib = MathTex(r"1",r"+",r"1",r"+",r"2",r"+",r"5",r"+",r"\cdots")
        
        self.play(Write(fib[0]))
        self.endSlide()

        self.play(
            Write(fib[1:3])
        )
        self.endSlide

        brace_1 = Brace(fib[0:3], DOWN, color=BLUE)
        b1_txt = brace_1.get_tex("=2").set_color(BLUE)

        self.play(
            GrowFromCenter(brace_1),
            Write(b1_txt) 
        )
        self.endSlide()

        self.play(
            FadeOut(brace_1, b1_txt),
            Write(fib[3:5])
        )
        self.endSlide

        brace_2 = Brace(fib[2:5], DOWN, color=BLUE)
        b2_txt = brace_2.get_tex("=3").set_color(BLUE)

        self.play(
            GrowFromCenter(brace_2),
            Write(b2_txt)
        )
        self.endSlide()

        self.play(
            FadeOut(brace_2, b2_txt),
            Write(fib[5:9])
        )
        self.endSlide()

class SimpleSternSeq(PPTXScene):
    def construct(self):
        title_short = Title(r"Stern-Brocot Sequence")
        self.add(title_short)

        brocot_seq = MathTex()

        n = 15
        BrocotSequence = [1,1]

        #loop to generate the stern brocot sequence
        #see https://www.youtube.com/watch?v=DpwUVExX27E
        for i in range(1,  n):
            
            considered_element = BrocotSequence[i]
            precedent = BrocotSequence[i-1]
    
            # adding sum of considered element and its precedent
            BrocotSequence.append(considered_element + precedent)
            
            # adding next considered element
            BrocotSequence.append(considered_element)

        #convert the ints to strings
        for i in range(0, len(BrocotSequence)):
            BrocotSequence[i] = str(BrocotSequence[i])

        #add '+' between each element
        for i in range(0, len(BrocotSequence)):
            if i == 0:
                BrocotSequence[i] = "1"
            elif i % 2 == 0:
                brocot_seq.add(MathTex(r"+"))
            else:
                brocot_seq.add(MathTex(BrocotSequence[i]))
        
    
        brocot_seq.add(MathTex(r"\cdots"))
        
        self.play(
            brocot_seq.animate.arrange_submobjects(RIGHT, buff=0.1),
        )
        self.endSlide()

        brocot_frac = MathTex()

        for i in range(0, (len(BrocotSequence)//2)):
            brocot_frac.add(MathTex(r"\frac {" +str(BrocotSequence[i])+ r"} {" +str(BrocotSequence[i+1])+ r"}"))
            brocot_frac.add(MathTex(r"+"))
            i += 1
        
        brocot_seq.move_to(UP)
        brocot_frac.next_to(brocot_seq, DOWN, buff=1.5)

        self.play(
            brocot_frac.animate.arrange_submobjects(RIGHT, buff=0.1),
        )
        self.endSlide()

class mediantExample(PPTXScene):
    def construct(self):
        number_plane = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        )

        self.add(number_plane)

        p1 = [10,10,0]
        mediant_line = Line(ORIGIN,p1)

        self.add(mediant_line)

        self.play(
            Create(number_plane),
            Create(mediant_line)
        )
        self.endSlide()

        
# define the set of slides you want
slides = [
    TitleSlide,
    FibEx,
    SimpleSternSeq,
    mediantExample
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
