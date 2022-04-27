from token import LEFTSHIFT
from tokenize import group
from manim import *
from manim_pptx import *
from matplotlib.pyplot import title

class TitleSlide(PPTXScene):
  def construct(self):

      main_title = Tex(r"Stern-Brocot Trees - CS1800")
      main_title.shift(0.5*UP)
      authors = Tex(r"Conor Doyle, Jonah Lefkoff, and Karthik Yalala", font_size=36)
      authors.shift(1.5*DOWN)
      discrete = Tex(r"CS1800 - Spring 2022", font_size=36)
      discrete.shift(0.5*DOWN)

      title_short = Title(r"The History")

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

class History(PPTXScene):
    def construct(self):
        title_short = Title(r"The History")

        self.play(
            Write(title_short)
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

class sternBrocotTree(PPTXScene):
    def construct(self):

        f0 = MathTex(r"\frac {0}{1}")
        f1 = MathTex(r"\frac {1}{0}")
        f2 = MathTex(r"\frac {1}{1}")
        f3 = MathTex(r"\frac {1}{2}")
        f4 = MathTex(r"\frac {2}{1}")
        f5 = MathTex(r"\frac {1}{3}")
        f6 = MathTex(r"\frac {2}{3}")
        f7 = MathTex(r"\frac {3}{2}")
        f8 = MathTex(r"\frac {3}{1}")

        self.add(f0, f1)
        f0.shift(LEFT*4,UP*3)
        f1.shift(RIGHT*4,UP*3)
       
        self.play(
            Write(f0),
            Write(f1)
        )
        self.endSlide()

        l0_1=Line(f0.get_center(), f2.get_center(), buff=0.4)
        l0_2=Line(f1.get_center(), f2.get_center(), buff=0.4)

        self.play(
            FadeIn(l0_1),
            FadeIn(l0_2),
            Write(f2)
        )
        self.endSlide()

        self.play(
            f2.animate.shift(UP*2)
        )
        self.endSlide()
        
        l0_1_1=Line(f0.get_center(), f2.get_center(), buff=0.4)
        l0_2_1=Line(f1.get_center(), f2.get_center(), buff=0.4)

        self.play(
            ReplacementTransform(l0_1, l0_1_1),
            ReplacementTransform(l0_2, l0_2_1)
        )
        self.endSlide()

        f3.shift(LEFT*3)
        f4.shift(RIGHT*3)

        l1_1=Line(f2.get_center(), f3.get_center(), buff=0.4)
        l1_2=Line(f2.get_center(), f4.get_center(), buff=0.4)

        self.play(
            f2.animate.move_to(UP*2),
            FadeIn(l1_1),
            FadeIn(l1_2),
            Write(f3),
            Write(f4)
        )
        self.endSlide()

        f5.shift(LEFT*4,DOWN*2)
        f6.shift(LEFT*1.5,DOWN*2)
        f7.shift(RIGHT*1.5,DOWN*2)
        f8.shift(RIGHT*4,DOWN*2)

        l2_1 = Line(f3.get_center(), f5.get_center(), buff=0.4)
        l2_2 = Line(f3.get_center(), f6.get_center(), buff=0.4)
        l2_3 = Line(f4.get_center(), f7.get_center(), buff=0.4)
        l2_4 = Line(f4.get_center(), f8.get_center(), buff=0.4)

        self.play(
            FadeIn(l2_1),
            FadeIn(l2_2),
            FadeIn(l2_3),
            FadeIn(l2_4),
            Write(f5),
            Write(f6),
            Write(f7),
            Write(f8)
        )
        self.endSlide()

class mediantExample(PPTXScene):
    def construct(self):
        title_short = Title(r"Clock Example")
        self.add(title_short)

        mediant = MathTex(r"\frac{1}{720}=\frac{1}{10\times 8\times 9}=\frac{1}{10}\times\frac{1}{8}\times\frac{1}{9}")
        mediant.shift(RIGHT,UP*2)

        img1 = ImageMobject(r"/Users/jlefkoff/Pictures/screenshots/Screen Shot 2022-04-27 at 12.57.09 PM.png")
        img1.scale(0.5)
        img1.move_to(ORIGIN)

        img2 = ImageMobject(r"/Users/jlefkoff/Pictures/screenshots/Screen Shot 2022-04-27 at 12.57.16 PM.png")
        img2.scale(0.5)
        img2.shift(LEFT*2,DOWN*2)

        self.play(
            FadeIn(img1), run_time=2
        )
        self.endSlide()

        self.play(
            FadeOut(img1),
            Write(title_short),
            Write(mediant),
            FadeIn(img2)
        )
        self.endSlide()

class ThankYou(PPTXScene):
    def construct(self):
        main_title = Tex(r"Thank you!")
        self.add(main_title)

        self.play(
            Write(main_title)
        )
        self.endSlide()

        
# define the set of slides you want
slides = [
    TitleSlide,
    History,
    FibEx,
    SimpleSternSeq,
    sternBrocotTree,
    mediantExample,
    ThankYou
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
