from manim import *

class LinearSearchGraph(Scene):
    def construct(self):
        self.camera.background_color = "#f0f0f0"  # Light gray background

        # Array and target setup
        arr = [2, 4, 6, 8, 10, 12]
        target = 12


        # Create boxes for array elements
        boxes = VGroup(*[
            Square(side_length=0.5, color=BLACK).shift(RIGHT * i)
            for i in range(len(arr))
        ])

        # Arrange them horizontally with spacing
        boxes.arrange(RIGHT, buff=0.5)  # Increase buff for more gap
        boxes.move_to(DOWN * 1.5)

        # Labels inside boxes
        labels = VGroup(*[
            Text(str(val), color=BLACK, font_size=24).move_to(boxes[i])
            for i, val in enumerate(arr)
        ])

        # Index labels below each box
        index_labels = VGroup(*[
            Text(str(i), font_size=20, color=GRAY).next_to(boxes[i], DOWN, buff=0.1)
            for i in range(len(arr))
        ])

        self.play(Create(boxes), Write(labels), Write(index_labels))
        self.wait(0.5)

        # Pointer Arrow
        pointer = Arrow(UP, DOWN, buff=0.1, color=BLUE).next_to(boxes[0], UP)
        pointer_text = Text("i", font_size=20, color=BLUE).next_to(pointer, UP, buff=0.1)
        self.play(GrowArrow(pointer), FadeIn(pointer_text))

        # Search animation
        found = False
        for i, val in enumerate(arr):
            if i > 0:
                self.play(pointer.animate.next_to(boxes[i], UP),
                          pointer_text.animate.next_to(boxes[i], UP, buff=0.1),
                          run_time=0.5)

            if val == target:
                # Highlight found element
                self.play(boxes[i].animate.set_fill(GREEN, opacity=0.5))
                found_text = Text(f"Found {target} at index {i}", color=GREEN, font_size=28).next_to(boxes, DOWN, buff=1)
                self.play(Write(found_text))
                found = True
                break
            else:
                self.play(boxes[i].animate.set_fill(RED, opacity=0.3), run_time=0.3)

        if not found:
            not_found = Text(f"{target} not found", color=RED, font_size=28).next_to(boxes, DOWN, buff=1)
            self.play(Write(not_found))

        self.wait(2)
        
