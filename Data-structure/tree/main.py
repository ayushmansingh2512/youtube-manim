from manim import *

class Main(MovingCameraScene):
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
   

        # Create the title
       
        self.play(title.animate.scale(0.6).set_color(BLACK))

        # Create the tree description text
        tree_definition = Text("Description of Tree Data Structure", font="Arial", color=BLACK)
        self.play(Write(tree_definition))

        # Move tree_definition left and then up
        self.play(tree_definition.animate.scale(0.6).shift(LEFT * 3))
        self.play(tree_definition.animate.shift(UP * 2))

        # Create definition text

        definition = Text(
            "A tree is a non-linear hierarchical data structure\n"
            "where data is stored in nodes.",
            font="Arial",
            color=BLACK,
            line_spacing=1.5
        )

        definition.scale(0.7)

        # Place it below `tree_definition` after all shifts
        definition.next_to(tree_definition, DOWN*2)
        definition.shift(RIGHT * 2.5)

        # Write definition on screen
        self.play(Write(definition))

        self.play(FadeOut(definition), FadeOut(tree_definition), FadeOut(title))

    
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

                # Create the grid
        plane = NumberPlane(
            x_range=[-7, 7, 1],  # X-axis from -5 to 5
            y_range=[-5, 5, 1],  # Y-axis from -3 to 3
            axis_config={"color": BLACK},  # Make axes black
        )
        # self.play(Create(plane))
        # Node positions
        root_pos = ORIGIN + UP * 2
        left_pos = root_pos + LEFT * 3 + DOWN * 2
        right_pos = root_pos + RIGHT * 3 + DOWN * 2
        left_left_pos = left_pos + LEFT * 2 + DOWN * 2
        left_right_pos = left_pos + RIGHT * 2 + DOWN * 2
        right_left_pos = right_pos + LEFT * 2 + DOWN * 2
        right_right_pos = right_pos + RIGHT * 2 + DOWN * 2
        
        # Create circles (nodes)
        root = Circle(radius=0.5, color=BLACK, fill_opacity=0.1).move_to(root_pos)
        left = Circle(radius=0.5, color=BLACK, fill_opacity=0.1).move_to(left_pos)
        right = Circle(radius=0.5, color=BLACK, fill_opacity=0.1).move_to(right_pos)
        left_left = Circle(radius=0.5, color=BLACK, fill_opacity=0.1).move_to(left_left_pos)
        left_right = Circle(radius=0.5, color=BLACK, fill_opacity=0.1).move_to(left_right_pos)
        right_left = Circle(radius=0.5, color=BLACK, fill_opacity=0.1).move_to(right_left_pos)
        right_right = Circle(radius=0.5, color=BLACK, fill_opacity=0.1).move_to(right_right_pos)
        
        # Node values (optional - you can add numbers or text inside circles)
        root_value = Text("1", font="Arial", color=BLACK).scale(0.6).move_to(root.get_center())
        left_value = Text("2", font="Arial", color=BLACK).scale(0.6).move_to(left.get_center())
        right_value = Text("3", font="Arial", color=BLACK).scale(0.6).move_to(right.get_center())
        left_left_value = Text("4", font="Arial", color=BLACK).scale(0.6).move_to(left_left.get_center())
        left_right_value = Text("5", font="Arial", color=BLACK).scale(0.6).move_to(left_right.get_center())
        right_left_value = Text("6", font="Arial", color=BLACK).scale(0.6).move_to(right_left.get_center())
        right_right_value = Text("7", font="Arial", color=BLACK).scale(0.6).move_to(right_right.get_center())
        
        node_values = [root_value, left_value, right_value, left_left_value, left_right_value, right_left_value, right_right_value]
        
        # Create lines (edges between nodes in the tree structure)
        edges = [
            Line(root.get_bottom(), left.get_top(), color=BLACK),
            Line(root.get_bottom(), right.get_top(), color=BLACK),
            Line(left.get_bottom(), left_left.get_top(), color=BLACK),
            Line(left.get_bottom(), left_right.get_top(), color=BLACK),
            Line(right.get_bottom(), right_left.get_top(), color=BLACK),
            Line(right.get_bottom(), right_right.get_top(), color=BLACK)
        ]
        
        # Create labels - root and internal nodes to the right, leaf nodes below
        root_label = Text("Root", font="Arial", color=BLACK).scale(0.5).move_to(root.get_center() + RIGHT * 1.5)
        left_label = Text("Left Child", font="Arial", color=BLACK).scale(0.5).move_to(left.get_center() + RIGHT * 1.5)
        right_label = Text("Right Child", font="Arial", color=BLACK).scale(0.5).move_to(right.get_center() + RIGHT * 1.5)
        
        # Leaf labels positioned BELOW the leaf nodes
        left_left_label = Text("Left-Left Leaf", font="Arial", color=BLACK).scale(0.45).move_to(left_left.get_center() + DOWN * 1.0)
        left_right_label = Text("Left-Right Leaf", font="Arial", color=BLACK).scale(0.45).move_to(left_right.get_center() + DOWN * 1.0)
        right_left_label = Text("Right-Left Leaf", font="Arial", color=BLACK).scale(0.45).move_to(right_left.get_center() + DOWN * 1.0)
        right_right_label = Text("Right-Right Leaf", font="Arial", color=BLACK).scale(0.45).move_to(right_right.get_center() + DOWN * 1.0)

        labels = [root_label, left_label, right_label, left_left_label, left_right_label, right_left_label, right_right_label]

        # Create label lines - connecting to the right for root and internal nodes, connecting to bottom for leaf nodes
        label_lines = [
            Line(root.get_right(), root_label.get_left(), color=BLACK),
            Line(left.get_right(), left_label.get_left(), color=BLACK),
            
            Line(right.get_right(), right_label.get_left(), color=BLACK),
            # Bottom connections for leaf nodes
            Line(left_left.get_bottom(), left_left_label.get_top(), color=BLACK),
            Line(left_right.get_bottom(), left_right_label.get_top(), color=BLACK),
            Line(right_left.get_bottom(), right_left_label.get_top(), color=BLACK),
            Line(right_right.get_bottom(), right_right_label.get_top(), color=BLACK)
        ]
        
        # Create title
        title = Text("Binary Tree Structure", font="Arial", color=BLACK).scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Animate creation of nodes and edges step by step with improved animation
        
        # Root node animation
        self.play(Create(root))
        self.play(root.animate.scale(1.3), run_time=0.5)
        self.play(root.animate.scale(1/1.3), run_time=0.5)
        self.play(Write(root_value))
        self.play(Create(label_lines[0]), Write(labels[0]))
        self.wait(0.5)

        # Level 1 nodes animation
        self.play(
            Create(left),
            Create(right),
        )
        self.play(
            left.animate.scale(1.3),
            right.animate.scale(1.3),
            run_time=0.5
        )
        self.play(
            left.animate.scale(1/1.3),
            right.animate.scale(1/1.3),
            run_time=0.5
        )
        self.play(
            Write(left_value),
            Write(right_value),
        )
        
        # Create edges connecting root to level 1
        self.play(
            Create(edges[0]), 
            Create(edges[1])
        )
        
        # Create labels for level 1
        self.play(
            Create(label_lines[1]), Write(labels[1]),
            Create(label_lines[2]), Write(labels[2]),
        )
        self.wait(0.5)

        # Level 2 nodes animation
        self.play(
            Create(left_left),
            Create(left_right),
            Create(right_left),
            Create(right_right),
        )
        self.play(
            left_left.animate.scale(1.3),
            left_right.animate.scale(1.3),
            right_left.animate.scale(1.3),
            right_right.animate.scale(1.3),
            run_time=0.5
        )
        self.play(
            left_left.animate.scale(1/1.3),
            left_right.animate.scale(1/1.3),
            right_left.animate.scale(1/1.3),
            right_right.animate.scale(1/1.3),
            run_time=0.5
        )
        self.play(
            Write(left_left_value),
            Write(left_right_value),
            Write(right_left_value),
            Write(right_right_value),
        )
        
        # Create edges connecting level 1 to level 2
        self.play(
            Create(edges[2]),
            Create(edges[3]),
            Create(edges[4]),
            Create(edges[5]),
        )
        
        # Create labels for level 2 (leaf nodes)
        self.play(
            Create(label_lines[3]), Write(labels[3]),
            Create(label_lines[4]), Write(labels[4]),
            Create(label_lines[5]), Write(labels[5]),
            Create(label_lines[6]), Write(labels[6]),
        )
        
        # Final pause to see the complete structure
        self.wait(2)
        
        # Add a highlight animation at the end
        highlight_sequence = [
            root, left, right, 
            left_left, left_right, 
            right_left, right_right
        ]

        
        self.play(
        self.camera.frame.animate.set_width(8).move_to(plane.c2p(-3,-1.5))
        )
           
        parent_label = Text("Parent node", font="Arial", color=BLACK).scale(0.5).move_to(left.get_center() + RIGHT * 1.5)
        self.play(ReplacementTransform(left_label,parent_label))
        self.wait(2)
        # Traverse and highlight each node in sequence
        self.play(self.camera.frame.animate.set_width(config.frame_width).move_to(ORIGIN))
        for node in highlight_sequence:
            self.play(
                node.animate.set_fill(YELLOW, opacity=0.5).scale(1.2),
                run_time=0.5
            )
            self.play(
                node.animate.set_fill(WHITE, opacity=0.1).scale(1/1.2),
                run_time=0.5
            )
            
        self.wait(1)
        
        # End with a fade out of all elements
        all_objects = [
            root, left, right, left_left, left_right, right_left, right_right,
            *node_values, *edges, *label_lines, *labels, title,parent_label
        ]
        self.play(FadeOut(*all_objects))
        
       
