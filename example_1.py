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
       
class DotExample(Scene):
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
        
class DotCoordExample(Scene): 
    def construct(self):
        dot_dict = dict()
        for x in range(-3, 4, 3):
            for y in range(-3, 4, 3):
                dot_dict[Text(f"({x}, {y})")] = Dot(np.array([x, y, 0]))
    
        for key in dot_dict:
            dot = dot_dict[key]
            coord = key
            self.add(dot) # adding dot
            self.add(coord) 
            coord.move_to(dot.get_center())
            self.wait(0.5)
            self.remove(coord)
        
class AnnularSectorExample(Scene):
    def construct(self):
        st_angle = 0;
        N = 2
        angle = PI/N
        for i in range(2*N):
            sct = AnnularSector(inner_radius=1, outer_radius=1.2, start_angle=st_angle, angle=angle)
            self.add(sct)
            self.play(Create(sct))
            st_angle = st_angle + angle
            
class PythagoreanTheoremExample(Scene): 
    def construct(self):
        d0 = Dot()
        d1 = Dot(point = np.array([1.2, 0, 0]))
        d2 = Dot(point = np.array([0, 1.6, 0]))
        l1 = Line(d0, d1, color=GREEN)
        l2 = Line(d0, d2, color=GREEN)
        l3 = Line(d1, d2, color=BLUE)
        sq1 = Square(side_length=1.2, color=GREEN_C).next_to(l1, DOWN, buff=0.01)
        sq2 = Square(side_length=1.6, color=GREEN_C).next_to(l2, LEFT, buff=0.01)
        sq3 = Square(side_length=2.0, color=GREEN_C).next_to(l3, UR)
        Rotate(sq3, PI/2)
        

        self.add(d0)
        self.add(d1)
        self.add(d2)
        self.add(l1)
        self.add(l2)
        self.add(l3)
        self.add(sq1)
        self.add(sq2)
        self.add(sq3)
        
class TransformExample(Scene):
    def construct(self):
        circle = Circle(color=RED).set_fill(color=RED, opacity=0.3)
        square = Square(color=BLUE).set_fill(color=BLUE, opacity=0.3)
        triangle = Triangle(color=GREEN).set_fill(color=GREEN, opacity=0.3)
        
        self.play(Create(triangle))
        self.play(Transform(triangle, square))
        self.play(Transform(triangle, circle))