from manim import *

class TypeOfDataStructure(MovingCameraScene):
    def construct(self):
        # Set background to white
        self.camera.background_color = WHITE

        # Create the coordinate plane (graph)
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLACK},
        )

        # Create the title text and its surrounding rectangle
        title = Text("Data Structure Types", font="Arial", color=BLACK).scale(0.7).move_to(UP * 3)
        box = SurroundingRectangle(title, color=BLACK, buff=0.2)

        # Create the branching structure
        line0 = Line(plane.c2p(0, 2.5), plane.c2p(0, 2), color=RED, stroke_width=4)
        line_left = Line(plane.c2p(0, 2), plane.c2p(-3, 2), color=RED, stroke_width=4)
        line_right = Line(plane.c2p(0, 2), plane.c2p(3, 2), color=RED, stroke_width=4)
        line_left_down = Line(plane.c2p(-3, 2), plane.c2p(-3, 1.5), color=RED, stroke_width=4)
        line_right_down = Line(plane.c2p(3, 2), plane.c2p(3, 1.5), color=RED, stroke_width=4)

        # Add title, rectangle, and lines
        self.play(Write(title), Create(box))
        self.play(Create(line0), Create(line_left), Create(line_right))
        self.play(Create(line_left_down), Create(line_right_down))

        # Create the categories
        linear = Text("Linear Data Structure", font="Arial", color=BLACK).scale(0.5).next_to(line_left_down, DOWN)
        non_linear = Text("Non-linear Data Structure", font="Arial", color=BLACK).scale(0.5).next_to(line_right_down, DOWN)
        box_linear = SurroundingRectangle(linear, color=BLACK, buff=0.2)
        box_non_linear = SurroundingRectangle(non_linear, color=BLACK, buff=0.2)
        
        self.play(Write(linear), Write(non_linear))
        self.play(Create(box_linear), Create(box_non_linear))

        # Linear data structures
        line5 = Line(plane.c2p(-3, 0.7), plane.c2p(-3, -1), color=RED, stroke_width=4)
        self.play(Create(line5))
        
        linear_types = ["Stack", "Queue", "Linked List", "Arrays"]
        linear_texts = []
        linear_lines = []
        positions = [0.5, 0, -0.5, -1]
        
        for i, data_type in enumerate(linear_types):
            text = Text(data_type, font="Arial", color=BLACK).scale(0.5).move_to(plane.c2p(-5, positions[i]))
            linear_texts.append(text)
            connect_line = Line(plane.c2p(-4.5, positions[i]), plane.c2p(-3, positions[i]), color=RED, stroke_width=4)
            linear_lines.append(connect_line)
        
        self.play(*[Write(t) for t in linear_texts], *[Create(l) for l in linear_lines])

        # Non-linear data structures
        line6 = Line(plane.c2p(3, 0.7), plane.c2p(3, 0), color=RED, stroke_width=4)
        self.play(Create(line6))
        
        non_linear_types = ["Graph", "Tree"]
        non_linear_texts = []
        non_linear_lines = []
        
        for i, data_type in enumerate(non_linear_types):
            text = Text(data_type, font="Arial", color=BLACK).scale(0.5).move_to(plane.c2p(4, positions[i]))
            non_linear_texts.append(text)
            connect_line = Line(plane.c2p(3.5, positions[i]), plane.c2p(3, positions[i]), color=RED, stroke_width=4)
            non_linear_lines.append(connect_line)
        
        self.play(*[Write(t) for t in non_linear_texts], *[Create(l) for l in non_linear_lines])

        # Tree structures
        self.play(self.camera.frame.animate.set_width(7).move_to(plane.c2p(3, -1.5)))
        line7 = Line(plane.c2p(4, -0.3), plane.c2p(4, -1), color=RED, stroke_width=4)
        self.play(Create(line7))

        type_of_tree = Text("Binary Tree\nAVL Tree\nB-Tree\nBinary Search Tree\nB+ Tree\nB* Tree", font="Arial", color=BLACK).scale(0.4).next_to(line7, DOWN)
        box_tree = SurroundingRectangle(type_of_tree, color=BLACK, buff=0.2)
        self.play(Write(type_of_tree), Create(box_tree))
        self.play(self.camera.frame.animate.set_width(config.frame_width).move_to(ORIGIN))

        # Fade out elements in correct order
        self.play(FadeOut(*linear_texts), FadeOut(*linear_lines))
        self.play(FadeOut(*non_linear_texts), FadeOut(*non_linear_lines))
        
        self.play(FadeOut(line0, line_left, line_right, line_left_down, line_right_down, line5, line6, line7,
                          box, box_linear, box_non_linear, box_tree, title, linear, non_linear, type_of_tree))
