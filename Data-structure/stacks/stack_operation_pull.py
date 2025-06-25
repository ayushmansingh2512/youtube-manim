from manim import *
import numpy as np

class StackOperationPull(Scene):
    def construct(self):
        grid = NumberPlane(
            x_range=[-5, 5, 1],  # X-axis range
            y_range=[-4, 4, 1],  # Y-axis range
            background_line_style={"stroke_color": BLUE_D, "stroke_width": 2, "stroke_opacity": 0.5}
        )
        # Create the stack container (open from the top)
        
        left_wall = Line([-2, -3, 0], [-2, 1, 0], color=WHITE, stroke_width=4)   # Left Side
        right_wall = Line([2, -3, 0], [2, 1, 0], color=WHITE, stroke_width=4) # Right Side
        bottom = Line([-2, -3, 0], [2, -3, 0], color=WHITE, stroke_width=4)     # Bottom Side

        text_pop = Text("Pop()",font="Inter")
        text_pop.to_edge(UP)

        rectanglePop = Rectangle(height=1, width=4, color=WHITE, fill_opacity=0.5)
        rectanglePop.move_to(DOWN*2.5)
        rectanglePop2 = Rectangle(height=1, width=4, color=RED, fill_opacity=0.5)
        rectanglePop2.move_to(DOWN*1.5 )
        rectanglePop3 = Rectangle(height=1, width=4, color=WHITE, fill_opacity=0.5)
        rectanglePop3.move_to(DOWN*.5)

        text_pop_description = Text("Pop(): removes the top item from the stack", font="Inter").scale(0.7)
        text_pop_description.to_edge(DOWN)

        self.add(grid)
        self.add((left_wall),(right_wall),(bottom))
        self.add(text_pop)
        self.add(rectanglePop,rectanglePop2,rectanglePop3)
       
        self.play(rectanglePop3.animate.shift(UP*2), run_time=1)
        self.play(rectanglePop3.animate.shift(RIGHT*4.5), run_time=1)
      
        self.play(rectanglePop2.animate.shift(UP*3), run_time=1)
        self.play(rectanglePop2.animate.shift(RIGHT*4.5), run_time=1)
      
        self.play(rectanglePop.animate.shift(UP*4), run_time=1)
        self.play(rectanglePop.animate.shift(RIGHT*4.5), run_time=1)
        self.play(Write(text_pop_description), run_time=1)