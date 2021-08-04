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
        a = 1
        b = 2
        c = np.sqrt(a**2 + b**2)
        
        d0 = Dot()
        d1 = Dot(point = np.array([a, 0, 0]))
        d2 = Dot(point = np.array([0, b, 0]))
        l1 = Line(d0, d1, color=BLUE)
        l2 = Line(d0, d2, color=GREEN)
        l3 = Line(d1, d2, color=RED)
        sq1 = Square(side_length=a, color=BLUE).next_to(l1, DOWN, buff=0.01)
        sq2 = Square(side_length=b, color=GREEN).next_to(l2, LEFT, buff=0.01)
        sq3 = Square(side_length=c, color=RED)
        
        self.add(d0, d1, d2)
        
        self.add(l1)
        self.play(Create(l1))
        self.add(MathTex('a').scale(0.7).next_to(l1, DOWN, buff=0.05))

        self.add(l2)
        self.play(Create(l2))
        self.add(MathTex('b').scale(0.7).next_to(l2, LEFT, buff=0.05))
       
        self.wait(0.2)
        self.play(Create(l3))
        self.add(MathTex('c').scale(0.7).move_to([2*b/5-0.05*b, c/2-0.05*c, 0]))
        
        sq1.set_fill(color=BLUE, opacity=0.3)
        self.wait(0.2)
        self.play(Create(sq1))
        txt_a2 = MathTex('a^2').scale(0.7).move_to(sq1)
        self.add(txt_a2)
        
        sq2.set_fill(color=GREEN, opacity=0.3)
        self.wait(0.2)
        self.play(Create(sq2))
        txt_b2 = MathTex('b^2').scale(0.7).move_to(sq2)
        self.add(txt_b2)
        
        sq3.rotate(np.arctan(a/b))
        x = a + c/2*np.sqrt(2)*np.sin(np.pi/4-np.arctan(a/b))
        y = c/2*np.sqrt(2)*np.cos(np.pi/4-np.arctan(a/b))
        sq3.move_to([x, y, 0])
        sq3.set_fill(color=RED, opacity=0.3)
        self.wait(0.2)
        self.play(Create(sq3))
        txt_c2 = MathTex('c^2').scale(0.7).move_to(sq3)
        self.add(txt_c2)
        
        txt_a2.generate_target()
        txt_a2.target.move_to([2*a, -a/2, 0])
        self.play(MoveToTarget(txt_a2))
        
        self.add(MathTex('+').scale(0.7).move_to([2*a+0.5, -a/2, 0]))
        
        txt_b2.generate_target()
        txt_b2.target.move_to([2*a+1, -a/2, 0])
        self.play(MoveToTarget(txt_b2))
        
        self.add(MathTex('=').scale(0.7).move_to([2*a+1.5, -a/2, 0]))
        
        txt_c2.generate_target()
        txt_c2.target.move_to([2*a+2, -a/2, 0])
        self.play(MoveToTarget(txt_c2))
        self.wait(0.1)
        
class TransformExample(Scene):
    def construct(self):
        circle = Circle(color=RED).set_fill(color=RED, opacity=0.3)
        square = Square(color=BLUE).set_fill(color=BLUE, opacity=0.3)
        triangle = Triangle(color=GREEN).set_fill(color=GREEN, opacity=0.3)
        
        self.play(Create(triangle))
        self.play(Transform(triangle, square))
        self.play(Transform(triangle, circle))
        
class ShapesExample(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        self.add(circle, square, triangle)
        for i in range(20):
            circle.shift(0.1*LEFT)
            square.shift(0.1*UP)
            triangle.shift(0.1*RIGHT)
            self.wait(0.05)
        self.wait()
        for i in range(20):
            circle.shift(0.1*RIGHT)
            square.shift(0.1*DOWN)
            triangle.shift(0.1*LEFT)
            self.wait(0.05)