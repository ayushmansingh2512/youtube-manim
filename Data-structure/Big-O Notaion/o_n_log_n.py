from manim import *
import math

class MyScene(Scene):
    def construct(self):
        self.camera.background_color = "#f0f0EB"

        title = Text("O(n log n) - Log-Linear Time", color='#C96442', font="American Typewriter").scale(0.5)
        title.to_edge(UL, buff=1)
        description = Text("A common complexity for efficient sorting algorithms like merge sort.", color=BLACK, font="American Typewriter").scale(0.3)
        description.next_to(title, DOWN, aligned_edge=LEFT)
        self.play(Write(title), Write(description))
        self.wait(1)

        arr_text = Text("arr = [ 8, 3, 1, 7, 0, 10, 2 ]", color='BLACK', font="American Typewriter").scale(0.3)
        arr_text.next_to(description, DOWN, aligned_edge=LEFT)
        self.play(Write(arr_text))
        self.wait(1)

        arr = [8, 3, 1, 7, 0, 10, 2]
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
            x_range=[0, 8, 1], y_range=[0, 20, 5],
            x_length=6, y_length=4,
            axis_config={"color": BLACK, "include_ticks": False}
        ).scale(0.7)
        ax.to_edge(UR).shift(DOWN*2.5)
        x_label = Text("Data", color=BLACK, font="American Typewriter").scale(0.5).next_to(ax, DOWN, buff=0.2)
        y_label = Text("Time", color=BLACK, font="American Typewriter").scale(0.5).next_to(ax, LEFT, buff=0.2)
        self.play(Create(ax), Write(x_label), Write(y_label))

        graph = always_redraw(lambda: ax.plot(lambda x: x * math.log2(x) if x > 1 else 0, x_range=[0, op_counter.get_value()], color='#D97757'))
        self.add(graph)

        # Simplified merge sort visualization
        def merge_sort_visualize(arr, start_index):
            if len(arr) > 1:
                mid = len(arr) // 2
                left_half = arr[:mid]
                right_half = arr[mid:]

                merge_sort_visualize(left_half, start_index)
                merge_sort_visualize(right_half, start_index + mid)

                i = j = k = 0
                while i < len(left_half) and j < len(right_half):
                    self.play(op_counter.animate.set_value(op_counter.get_value() + 1), run_time=0.1)
                    if left_half[i] < right_half[j]:
                        arr[k] = left_half[i]
                        i += 1
                    else:
                        arr[k] = right_half[j]
                        j += 1
                    k += 1

                while i < len(left_half):
                    arr[k] = left_half[i]
                    i += 1
                    k += 1

                while j < len(right_half):
                    arr[k] = right_half[j]
                    j += 1
                    k += 1
                
                new_labels = VGroup(*[Text(str(val), color=BLACK, font='American Typewriter', font_size=15).move_to(boxes[start_index + l]) for l, val in enumerate(arr)])
                self.play(Transform(labels, new_labels), run_time=0.5)

        merge_sort_visualize(arr, 0)

        self.wait(3)
