from manim import *

class MyScene(Scene):
    def construct(self):
        # Set background color to light gray
        self.camera.background_color = "#f0f0eb"  # light gray
        
        # Create headings with proper syntax
        heading = Text("Big O Notation", color=BLACK, font="American Typewriter").scale(0.3)
        heading2 = Text("Time Complexities", color=BLACK, font="American Typewriter").scale(0.3)
        
        # Fixed syntax errors: Text() not text(), proper string formatting
        q1 = Text("What is Big-O notation?", color=BLACK, font="American Typewriter").scale(0.3)
        
        # For multi-line text, use proper line breaks
        a1 = Text(
            "Time complexity is important because it tells us how efficient a program is and how it performs as the amount of data grows"
            ,color=BLACK, 
            font="American Typewriter"
        ).scale(0.3)
        
        # Position elements
        heading.to_edge(UP)  # Move to top with buffer
        heading2.next_to(heading, DOWN )  # Position below first heading
        q1.to_edge(UL, buff=1).shift(DOWN)  # Position in upper left, below heading2
        a1.next_to(q1, DOWN, aligned_edge=LEFT)  # Position answer below question, left-aligned

                # Add all elements to scene
        self.add(heading)
        self.add(heading2)
        self.add(q1)  # Fixed: was q2, should be q1
        self.add(a1)

        ar1 = Text('arr = [2,4,5,6,8,0,1]' ,color=BLACK , font='American Typewriter' ).scale(0.3)
        t1 = Text('target = 1' ,color=BLACK , font='American Typewriter').scale(0.3)
        ar1.next_to(a1, DOWN*2, aligned_edge=LEFT)
        t1.next_to(ar1, DOWN, aligned_edge=LEFT)
        # self.wait()
        # self.play(Create(ar1))
        # self.play(Create(t1))
        # self.wait(3)
        self.add(ar1)
        self.add(t1)
        arr = [2,4,5,6,8,0,1]
        target = 1
        
        

        boxes = VGroup(*[
            Square(side_length=0.7, color=BLACK).shift(RIGHT * i)
            for i in range(len(arr))
        ])

        # Arrange them horizontally with spacing
           
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
        self.wait(1)

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
                          run_time=3)

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

