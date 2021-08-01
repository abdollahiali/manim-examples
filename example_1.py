from manim import *

#use the following command to preview the video
#manim example_1.py DrawCircle -p
class DrawCircle(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.play(Create(circle))
        
        text = Tex("Area of circle: $\pi\,r^2$").scale(1).next_to(circle, DOWN)
        self.add(text)       
        self.play(Create(text))

class DrawSquareCircle1(Scene):
    def construct(self):
        square = Square(color = BLUE);
        circle = Circle(color = GREEN).surround(square, buffer_factor = 1.03)
        grp = Group(square, circle)
        self.add(grp)


class DrawSquareCircle2(Scene):
    def construct(self):
        square = Square(color = BLUE);
        circle = Circle(color = GREEN).surround(square, buffer_factor = 1.03)
        self.play(Create(square))
        self.play(Create(circle))
       
class LotsOfDots(Scene):
    def construct(self):
        dot = []
        for i in range(8):
            for j in range(4):
                dot.append(Dot(point=i*LEFT+j*UP, color=BLUE))
                dot.append(Dot(point=-i*LEFT+j*UP, color=BLUE))
                dot.append(Dot(point=-i*LEFT-j*UP, color=BLUE))
                dot.append(Dot(point=i*LEFT-j*UP, color=BLUE))
        dot_org = Dot(point=ORIGIN, color=GREEN)
        for d in dot:
            self.add(d)
        self.add(dot_org)