from manim import *
import numpy as np

class StackOperation(Scene):
    def construct(self):
        # Title
        stack_op_text = Text("Stack Operations", font="Inter").scale(1.2)
        self.play(Write(stack_op_text))
        self.play(stack_op_text.animate.shift(UP * 2.5))
        self.play(stack_op_text.animate.shift(LEFT * 3))  # Shift up for spacing

        # List of stack operations with numbering
        operations = [
            "1. Push",
            "2. Pop",
            "3. Peek",
            "4. Is Empty",
            "5. Is Full"
        ]

        # Create and position operation texts
        operation_texts = VGroup(*[Text(op, font="Inter").scale(0.9) for op in operations])
        operation_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.5)  # Spacing
        operation_texts.next_to(stack_op_text, DOWN, buff=1)  # Place below the title

        # Animate writing each operation
        for text in operation_texts:
            self.play(Write(text))

        self.wait(2)  # Pause for observation

        self.play(FadeOut(stack_op_text), FadeOut(operation_texts), run_time=1)
        
