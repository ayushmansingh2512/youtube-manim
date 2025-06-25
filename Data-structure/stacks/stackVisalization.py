from manim import *

class StackVisualization(Scene):
    def construct(self):
        grid = NumberPlane(
            x_range=[-5, 5, 1],  # X-axis range
            y_range=[-4, 4, 1],  # Y-axis range
            background_line_style={"stroke_color": BLUE_D, "stroke_width": 2, "stroke_opacity": 0.5}
        )
        # Create the stack container (open from the top)
        left_wall = Line([-2, -3, 0], [-2, 1.5, 0], color=WHITE, stroke_width=4)   # Left Side
        right_wall = Line([2, -3, 0], [2, 1.5, 0], color=WHITE, stroke_width=4) # Right Side
        bottom = Line([-2, -3, 0], [2, -3, 0], color=WHITE, stroke_width=4)     # Bottom Side
    
        line = Line([-4, 2, 0], [-1, 2, 0], color=WHITE, stroke_width=4)
        push_arrow = Arrow([-1, 2.25, 0], [-1, 0, 0], color=WHITE, stroke_width=4)  # Push arrow
        push_label = Text("ITEMS INSERTED", font_size=20).next_to(line, LEFT)
        # Animate creation

        line2 = Line([1, 2, 0], [4, 2, 0], color=WHITE, stroke_width=4).add_tip(tip_length=0.2)
        pull_arrow = Line([1, 2, 0], [1, 0.3, 0], color=WHITE, stroke_width=4)  # Push arrow
        pull_label = Text("ITEMS DELETED", font_size=20).next_to(line2, RIGHT)

        text3=Text("Figure 1: Stack Visualization").scale(0.7)
        text3.to_edge(DOWN*-1.2)

      
        self.add((left_wall),(right_wall),(bottom))
        self.add(push_arrow, push_label,line,line2,pull_arrow,pull_label)
        self.add(text3)

        self.wait(2)  # Pause for observation

        self.play(FadeOut(left_wall),FadeOut(right_wall),FadeOut(bottom),FadeOut(line),FadeOut(line2),FadeOut(push_arrow),FadeOut(push_label),FadeOut(pull_arrow),FadeOut(pull_label),FadeOut(text3),run_time=1)