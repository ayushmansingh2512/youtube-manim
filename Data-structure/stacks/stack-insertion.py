from manim import *
import numpy as np

class StackInsertion(Scene):
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

        text_push = Text("Push",font="Inter")
        text_push.to_edge(UP)

        rectangle = Rectangle(height=1, width=4, color=WHITE, fill_opacity=0.5)
        rectangle.move_to(UP*1.5 + LEFT*5)
        rectangle2 = Rectangle(height=1, width=4, color=RED, fill_opacity=0.5)
        rectangle2.move_to(UP*1.5 + LEFT*5)
        rectangle3 = Rectangle(height=1, width=4, color=WHITE, fill_opacity=0.5)
        rectangle3.move_to(UP*1.5 + LEFT*5)
        self.add(grid)
        self.add((left_wall),(right_wall),(bottom))
        self.add(text_push)
        self.add(rectangle)
        self.play(rectangle.animate.shift(RIGHT*5), run_time=1)
        self.play(rectangle.animate.shift(DOWN*4), run_time=1)
        self.play(FadeIn(rectangle2), run_time=1)
        self.play(rectangle2.animate.shift(RIGHT*5), run_time=1)
        self.play(rectangle2.animate.shift(DOWN*3), run_time=1)
        self.play(FadeIn(rectangle3), run_time=1)
        self.play(rectangle3.animate.shift(RIGHT*5), run_time=1)
        self.play(rectangle3.animate.shift(DOWN*2), run_time=1)