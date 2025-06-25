from manim import *

class constantSearchLineGraph(Scene):
    def construct(self):
        self.camera.background_color = "#ffffff00"
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=6,
            y_length=4,
            axis_config={"color": BLACK, "include_ticks": False}
        )
        
        # y = x line (linear growth) - O(n)
        linear_graph = ax.plot(lambda x: x, x_range=[0, 9], color=BLACK)
        linear_text = Text("O(n)", color=BLACK).scale(0.5)
        linear_text.next_to(linear_graph.get_end(), RIGHT, buff=0.2)
        
        # Constant time line - O(1)
        constant_graph = ax.plot(lambda x: 2, x_range=[0, 9], color=RED)
        constant_text = Text("O(1)", color=RED).scale(0.5)
        constant_text.next_to(constant_graph.get_end(), RIGHT, buff=0.2)
        
        # Axis labels
        text2 = Text("Data", color=BLACK, font="American Typewriter").scale(0.5)
        text2.next_to(ax, DOWN, buff=0.2)
        text3 = Text("Time", color=BLACK, font="American Typewriter").scale(0.5)
        text3.next_to(ax, LEFT, buff=0.2)
        
#        Add all elements
        self.add(ax)
        self.add(linear_graph)
        self.add(linear_text)
        self.add(constant_graph)
        self.add(constant_text)
        self.add(text2)
        self.add(text3)


        # self.play(Create(ax))
        # self.play(Create(linear_graph))
        # self.play(Create(linear_text))
        # self.play(Create(constant_graph))
        # self.play(Create(constant_text))
        # self.play(Create(text2))
        # self.play(Create(text3))