from manim import *

class TreeStructure(MovingCameraScene):
    def construct(self):
        # Set background color
        self.camera.background_color = WHITE
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
        
       