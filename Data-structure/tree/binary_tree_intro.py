from manim import *

class BinaryTreeIntro(Scene):
    def construct(self):
        # Set background to white
        self.camera.background_color = WHITE

        # # Create the grid
        # grid = NumberPlane(axis_config={"color": BLACK})  # Make grid lines black
        # self.add(grid)  # Show the grid on screen

        # Create the title
        title = Text("Tree Data Structure", font="Arial", color=BLACK)  # Black text
        title.scale(1.5)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Define node positions using grid references
        root_pos = ORIGIN + UP * 2  # Center
        left_child_pos = root_pos + LEFT * 4 + DOWN * 2
        right_child_pos = root_pos + RIGHT * 4 + DOWN * 2
        child_left_pos = left_child_pos + LEFT * 2 + DOWN * 2
        child_left_pos2 = left_child_pos + RIGHT * 2 + DOWN * 2
        child_right_pos = right_child_pos + LEFT * 2 + DOWN * 2
        child_right_pos2 = right_child_pos + RIGHT * 2 + DOWN * 2

        # Create circles (nodes) with black stroke
        circle1 = Circle(radius=0.5, color=RED).move_to(root_pos)
        circle2 = Circle(radius=0.5, color=BLUE).move_to(left_child_pos)
        circle3 = Circle(radius=0.5, color=GREEN).move_to(right_child_pos)
        circle4 = Circle(radius=0.5, color=BLUE_A).move_to(child_left_pos)
        circle5 = Circle(radius=0.5, color=BLUE_B).move_to(child_left_pos2)
        circle6 = Circle(radius=0.5, color=GREEN_A).move_to(child_right_pos)
        circle7 = Circle(radius=0.5, color=GREEN_B).move_to(child_right_pos2)

        # Create lines (edges) with black color
        line1 = Line(circle1.get_bottom(), circle2.get_top(), color=BLACK)
        line2 = Line(circle1.get_bottom(), circle3.get_top(), color=BLACK)
        line3 = Line(circle2.get_bottom(), circle4.get_top(), color=BLACK)
        line4 = Line(circle2.get_bottom(), circle5.get_top(), color=BLACK)
        line5 = Line(circle3.get_bottom(), circle6.get_top(), color=BLACK)
        line6 = Line(circle3.get_bottom(), circle7.get_top(), color=BLACK)

        # Animate everything
        self.play(Create(circle1), Create(circle2), Create(circle3), 
                  Create(circle4), Create(circle5), Create(circle6), Create(circle7))
        self.play(Create(line1), Create(line2), Create(line3), Create(line4), 
                  Create(line5), Create(line6))
        self.wait(1)
        self.play(FadeOut(circle1), FadeOut(circle2), FadeOut(circle3), 
                  FadeOut(circle4), FadeOut(circle5), FadeOut(circle6), FadeOut(circle7),FadeOut(line1), FadeOut(line2), FadeOut(line3), FadeOut(line4),FadeOut(line5), FadeOut(line6))   
        
              # Set background to white
        