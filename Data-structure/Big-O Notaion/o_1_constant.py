from manim import *

class MyScene(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#f0f0EB"

        # Title and description
        title = Text("O(1) - Constant Time", color='#C96442', font="American Typewriter").scale(0.5)
        title.to_edge(UL, buff=1)
        description = Text("O(1) means the operation takes the same time, regardless of the input size.", color=BLACK, font="American Typewriter").scale(0.3)
        description.next_to(title, DOWN, aligned_edge=LEFT)
        # self.play(Write(title), Write(description))
        self.add(title, description)
        # self.wait(1)

        # Array display
        arr_text = Text("arr = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]", color='BLACK', font="American Typewriter").scale(0.3)
        arr_text.next_to(description, DOWN, aligned_edge=LEFT)
        target_text = Text("target = arr[5]", color='BLACK', font="American Typewriter").scale(0.3)
        target_text.next_to(arr_text, DOWN, aligned_edge=LEFT)
        # self.play(Write(arr_text), Write(target_text))
        self.add(arr_text, target_text)
        #self.wait(1)

        # Array visualization
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        boxes = VGroup(*[Square(side_length=0.5, color='#C96442') for _ in arr])
        boxes.arrange(RIGHT, buff=0.2)
        boxes.next_to(target_text, DOWN, buff=1, aligned_edge=LEFT)
        labels = VGroup(*[Text(str(val), color=BLACK, font='American Typewriter', font_size=15).move_to(boxes[i]) for i, val in enumerate(arr)])
        indices = VGroup(*[Text(str(i), color=BLACK, font='American Typewriter', font_size=14).next_to(boxes[i], DOWN, buff=0.1) for i in range(len(arr))])
        #self.play(Create(boxes), Write(labels), Write(indices), run_time=3)
        self.add(boxes, labels, indices)

        # Operation counter
        op_label = Text("Operations: 1", font='American Typewriter', color=BLACK).scale(0.3)
        op_counter = DecimalNumber(0, num_decimal_places=0, color=BLACK).scale(0.3)
        op_label.next_to(boxes, DOWN, buff=1, aligned_edge=LEFT)
        op_counter.next_to(op_label, RIGHT, buff=0.2)
        # self.play(Write(op_label), Write(op_counter))
        self.add(op_label, op_counter)

        # Graph
        ax = Axes(
            x_range=[0, 10, 1], y_range=[0, 3, 1],
            x_length=6, y_length=4,
            axis_config={"color": BLACK, "include_ticks": False}
        ).scale(0.7)
        ax.to_edge(UR).shift(DOWN*2.5)
        x_label = Text("Data", color=BLACK, font="American Typewriter").scale(0.5).next_to(ax, DOWN, buff=0.2)
        y_label = Text("Time", color=BLACK, font="American Typewriter").scale(0.5).next_to(ax, LEFT, buff=0.2)
        
        # self.play(Create(ax), Write(x_label), Write(y_label))
        self.add(ax, x_label, y_label) # After drawing the graph ax

        # Animate access
       # Before finding the target in array
        pointer = Arrow(UP, DOWN, buff=0.1, color='RED', tip_length=0.15).scale(0.4)
        pointer.next_to(boxes[5], UP, buff=0.3)
        # self.wait()
        # self.play(Create(pointer))
        self.add(pointer) 
        # self.play(op_counter.animate.set_value(1), run_time=0.5)
        # self.play(boxes[5].animate.set_fill('#BCD1CA', opacity=1))
        self.add(boxes[5]) # After finding the target in array

        # Draw graph
        # self.add(graph) # Before drawing the graph
        graph = ax.plot(lambda x: 1, x_range=[0, 9], color='#D97757')
        self.wait()
        self.play(Create(graph))
        # self.add(graph) # After drawing the graph

        self.wait(2)
