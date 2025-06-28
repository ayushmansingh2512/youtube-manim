from manim import *

class MyScene(Scene):
    def construct(self):
        self.camera.background_color = "#f0f0EB"

        title = Text("O(n^2) - Quadratic Time", color='#C96442', font="American Typewriter").scale(0.5)
        title.to_edge(UL, buff=1)
        description = Text("Time grows quadratically with the input size, common in nested loop algorithms.", color=BLACK, font="American Typewriter").scale(0.3)
        description.next_to(title, DOWN, aligned_edge=LEFT)
        self.play(Write(title), Write(description))
        self.wait(1)

        arr_text = Text("arr = [ 8, 2, 6, 4, 5 ]", color='BLACK', font="American Typewriter").scale(0.3)
        arr_text.next_to(description, DOWN, aligned_edge=LEFT)
        self.play(Write(arr_text))
        self.wait(1)

        arr = [8, 2, 6, 4, 5]
        boxes = VGroup(*[Square(side_length=0.5, color='#C96442') for _ in arr])
        boxes.arrange(RIGHT, buff=0.2)
        boxes.next_to(arr_text, DOWN, buff=1, aligned_edge=LEFT)
        labels = VGroup(*[Text(str(val), color=BLACK, font='American Typewriter', font_size=15).move_to(boxes[i]) for i, val in enumerate(arr)])
        self.play(Create(boxes), Write(labels))

        op_label = Text("Operations:", font='American Typewriter', color=BLACK).scale(0.3)
        op_counter = DecimalNumber(0, num_decimal_places=0, color=BLACK).scale(0.3)
        op_label.next_to(boxes, DOWN, buff=1, aligned_edge=LEFT)
        op_counter.next_to(op_label, RIGHT, buff=0.2)
        self.play(Write(op_label), Write(op_counter))

        ax = Axes(
            x_range=[0, 6, 1], y_range=[0, 30, 5],
            x_length=6, y_length=4,
            axis_config={"color": BLACK, "include_ticks": False}
        ).scale(0.7)
        ax.to_edge(UR).shift(DOWN*2.5)
        x_label = Text("Data", color=BLACK, font="American Typewriter").scale(0.5).next_to(ax, DOWN, buff=0.2)
        y_label = Text("Time", color=BLACK, font="American Typewriter").scale(0.5).next_to(ax, LEFT, buff=0.2)
        self.play(Create(ax), Write(x_label), Write(y_label))

        graph = always_redraw(lambda: ax.plot(lambda x: x**2, x_range=[0, op_counter.get_value()], color='#D97757'))
        self.add(graph)

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                self.play(op_counter.animate.set_value(op_counter.get_value() + 1), run_time=0.2)
                self.play(boxes[i].animate.set_fill('#A8DADC', opacity=1), boxes[j].animate.set_fill('#A8DADC', opacity=1), run_time=0.3)
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    new_labels = VGroup(*[Text(str(val), color=BLACK, font='American Typewriter', font_size=15).move_to(boxes[k]) for k, val in enumerate(arr)])
                    self.play(Transform(labels, new_labels), run_time=0.5)
                self.play(boxes[i].animate.set_fill('#C96442', opacity=1), boxes[j].animate.set_fill('#C96442', opacity=1), run_time=0.3)

        self.wait(3)
 