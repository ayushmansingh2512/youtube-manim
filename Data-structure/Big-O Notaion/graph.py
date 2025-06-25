from manim import *
import math

class MyScene(Scene):
    def construct(self):
        # Set background color to light gray
        self.camera.background_color = "#f0f0eb"
        
        # Title
        title = Text("Big O Notation Complexity Classes", color=BLACK, font="American Typewriter").scale(0.6)
        title.to_edge(UP, buff=0.5)
        
        # Create a comprehensive comparison chart
        ax = Axes(
            x_range=[1, 15, 1],
            y_range=[0, 100, 10],
            x_length=6,
            y_length=4,
            axis_config={
                "color": BLACK,
                "include_ticks": True,
                "tick_size": 0.05,
                "numbers_to_exclude": []
            }
        )
        ax.center().shift(DOWN * 0.5)
        
        # Add grid for better readability
        grid = NumberPlane(
            x_range=[1, 15, 1],
            y_range=[0, 100, 10],
            x_length=10,
            y_length=6,
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 0.5,
                "stroke_opacity": 0.3,
            }
        )
        grid.center().shift(DOWN * 0.5)
        
        # Define complexity functions with appropriate ranges
        # O(1) - Constant
        const_func = ax.plot(lambda x: 1, x_range=[1, 15], color=RED, stroke_width=3)
        
        # O(log n) - Logarithmic  
        log_func = ax.plot(lambda x: 3 * math.log2(x), x_range=[1, 15], color=BLUE, stroke_width=3)
        
        # O(n) - Linear
        linear_func = ax.plot(lambda x: x, x_range=[1, 15], color=GREEN, stroke_width=3)
        
        # O(n log n) - Linearithmic
        nlogn_func = ax.plot(lambda x: x * math.log2(x) / 2, x_range=[1, 15], color=ORANGE, stroke_width=3)
        
        # O(n²) - Quadratic
        quad_func = ax.plot(lambda x: x**2 / 4, x_range=[1, 12], color=PURPLE, stroke_width=3)
        
        # O(2^n) - Exponential (limited range)
        exp_func = ax.plot(lambda x: 2**(x-5), x_range=[1, 11], color=MAROON, stroke_width=3)
        
        # O(n!) - Factorial (very limited range)

        
        
        # Create legend
        legend_items = [
            ("O(1) - Constant", RED),
            ("O(log n) - Logarithmic", BLUE),
            ("O(n) - Linear", GREEN),
            ("O(n log n) - Linearithmic", ORANGE),
            ("O(n^2) - Quadratic", PURPLE),
            ("O(2^n) - Exponential", MAROON),
      
        ]
        
        legend = VGroup()
        for i, (text, color) in enumerate(legend_items):
            line = Line(ORIGIN, RIGHT * 0.5, color=color, stroke_width=4)
            label = Text(text, color=BLACK, font="American Typewriter").scale(0.35)
            item = VGroup(line, label.next_to(line, RIGHT, buff=0.1))
            legend.add(item)
        
        legend.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        legend.to_edge(UR, buff=0.5).shift(DOWN * 1.5)
        
        # Axis labels
        x_label = Text("Input Size (n)", color=BLACK, font="American Typewriter").scale(0.5)
        x_label.next_to(ax.x_axis, DOWN)
        
        y_label = Text("Time Complexity", color=BLACK, font="American Typewriter").scale(0.5)
        y_label.next_to(ax, LEFT,buff=-1).rotate(PI/2)
        
        # Performance comparison table
        comparison_data = [
        ]
        
        table = VGroup()
        for i, row in enumerate(comparison_data):
            row_group = VGroup()
            for j, cell in enumerate(row):
                cell_text = Text(cell, color=BLACK, font="American Typewriter").scale(0.25)
                
                # Color code the algorithm names
                if j == 0 and i > 0:
                    colors = [RED, BLUE, GREEN, ORANGE, PURPLE, MAROON, BLACK]
                    cell_text.set_color(colors[i-1])
                
                row_group.add(cell_text)
            
            row_group.arrange(RIGHT, buff=0.4)
            table.add(row_group)
        
        table.arrange(DOWN, buff=0.1)
        table.to_edge(DL, buff=0.5).shift(UP * 0.5)
        
        # Add efficiency note
        efficiency_note = Text(
            "Efficiency Ranking (Best to Worst):\nO(1) > O(log n) > O(n) > O(n log n) > O(n^2) > O(2^n) > O(n!)",
            color=BLACK,
            font="American Typewriter"
        ).scale(0.3)
        efficiency_note.to_edge(UP, buff=0.3).shift(DOWN)
        
        #Add all elements to scene
        self.add(title)
        self.add(grid)
        self.add(ax)
        self.add(const_func, log_func, linear_func, nlogn_func, quad_func, exp_func)
        self.add(legend)
        self.add(x_label, y_label)
        self.add(table)
        self.add(efficiency_note)


        # Optional: Animation sequence
        # self.play(Write(title))
        # self.play(Create(ax), Create(grid))
        # self.play(Create(const_func), run_time=0.5)
        # self.play(Create(log_func), run_time=0.5)
        # self.play(Create(linear_func), run_time=0.5)
        # self.play(Create(nlogn_func), run_time=0.5)
        # self.play(Create(quad_func), run_time=0.5)
        # self.play(Create(exp_func), run_time=0.5)
        # # self.play(Create(fact_func), run_time=0.5)
        # self.play(Write(legend))
        # self.play(Write(x_label), Write(y_label))
        # self.play(Write(table))
        # self.play(Write(efficiency_note))
        # self.wait(2)
        # 