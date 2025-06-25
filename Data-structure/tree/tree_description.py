from manim import *

class TreeDescription(Scene):
    def construct(self):
        # Set background to white
        self.camera.background_color = WHITE

        # Create the title
        title = Text("Tree Data Structure", font="Arial", color=BLACK)
        title.scale(1.5)
        title.to_edge(UP)
        self.add(title)
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