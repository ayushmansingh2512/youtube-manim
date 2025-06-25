from manim import *
import math

class MyScene(Scene):
    def construct(self):
        # Set background color to light gray
        self.camera.background_color = "#f0f0eb"

        # Title
        text1 = Text("Types of Notations", color=BLACK, font="American Typewriter").scale(0.5)
        text1.to_edge(UL, buff=1).shift(DOWN)

        # Main content
        notations_text = """
1. O(1) – Constant time

2. O(n) – Linear time

3. O(log n) – Logarithmic time

4. O(n log n) – Quasilinear time

5. O(n^2) – Polynomial time

6. O(2^n) – Exponential time

7. O(n!) – Factorial time"""

        text2 = Text(notations_text, color=BLACK, font="American Typewriter").scale(0.3)
        text2.next_to(text1, DOWN, aligned_edge=LEFT)

        self.add(text1, text2)
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 14, 1],
            x_length=8,
            y_length=6,
            axis_config={"color": BLACK, "include_ticks": False}
        ).scale(0.6)
        ax.to_edge(UR, buff=2).shift(DOWN*0.3)

        
        # y = x line (linear growth) - O(n)
        linear_graph = ax.plot(lambda x: x, x_range=[0, 9], color=BLACK)
        linear_text = Text("O(n)", color=BLACK).scale(0.5)
        linear_text.next_to(linear_graph.get_end(), RIGHT, buff=0.2)
        
        # Constant time line - O(1)
        constant_graph = ax.plot(lambda x: 1, x_range=[0, 9], color=RED)
        constant_text = Text("O(1)", color=RED).scale(0.5)
        constant_text.next_to(constant_graph.get_end(), RIGHT, buff=0.2)
        
        o_log_n = ax.plot(lambda x: math.log(x + 1), x_range=[0, 9], color=BLUE)  # +1 to avoid log(0)
        o_log_n_text = Text("O(log n)",color=BLACK).scale(0.5)
        o_log_n_text.next_to(o_log_n.get_end(), RIGHT, buff=0.2)


        o_n_log_n = ax.plot(lambda x: x * math.log(x + 1), x_range=[0, 9],color=GREEN)
        o_n_log_n_text = Text("O(n log n)", color=ORANGE).scale(0.4)
        o_n_log_n_text.next_to(o_n_log_n.get_end(), UP + LEFT, buff=0.2)

        
        # Axis labels
        x_label = Text("Data (n)", color=BLACK, font="American Typewriter").scale(0.4)
        x_label.next_to(ax, DOWN, buff=0.2)
        y_label = Text("Time", color=BLACK, font="American Typewriter").scale(0.4)
        y_label.next_to(ax, LEFT, buff=0.2)

        

        # Add all elements
        self.add(ax)
        self.add(ax)
        self.add(constant_graph, constant_text)
        self.add(o_log_n, o_log_n_text)
        self.add(linear_graph, linear_text)
        self.add(o_n_log_n, o_n_log_n_text)
        self.add(x_label, y_label)
        
        # self.play(Create(ax))
        # self.play(Create(linear_graph))
        # self.play(Create(linear_text))
        # self.play(Create(constant_graph))
        # self.play(Create(constant_text))
        # self.play(Create(text2))
        # self.play(Create(text3))