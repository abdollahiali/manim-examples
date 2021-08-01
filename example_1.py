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