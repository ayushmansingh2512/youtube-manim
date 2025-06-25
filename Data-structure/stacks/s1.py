from manim import *

class S1(Scene):
    def construct(self):
        text = Text("stack", font_size=144)
        self.play(Write(text))
   
        self.play(text.animate.shift(UP*3).scale(0.5), run_time=1)

        text2=Text("Description",line_spacing=2).scale(0.7)
        self.play(Write(text2)) 
        self.play(text2.animate.shift(LEFT*4.9), run_time=1)
        self.play(text2.animate.shift(UP*1.5), run_time=1)
        text3=Text("A stack can be defined as ordered collection of items into which items\n"
                   "may be added or deleted at one end only,called the top of the stack",
                   line_spacing=1.5).scale(0.6)
        self.play(Write(text3))
        self.wait(1)
        self.play(FadeOut(text3),FadeOut(text2),FadeOut(text),run_time=1)
        text4=Text("We can ilustrate stack as follows - " ,font= "Inter").scale(0.7)
        self.play(Write(text4))
        self.play(text4.animate.shift(LEFT*3), run_time=1)
        self.play(text4.animate.shift(UP*3), run_time=1)
        grid = NumberPlane(
            x_range=[-5, 5, 1],  # X-axis range
            y_range=[-4, 4, 1],  # Y-axis range
            background_line_style={"stroke_color": BLUE_D, "stroke_width": 2, "stroke_opacity": 0.5}
        )

        # Create the stack container (open from the top)
        left_wall = Line([-2, -3, 0], [-2, 1.5, 0], color=WHITE, stroke_width=4)   # Left Side
        right_wall = Line([2, -3, 0], [2, 1.5, 0], color=WHITE, stroke_width=4)    # Right Side
        bottom = Line([-2, -3, 0], [2, -3, 0], color=WHITE, stroke_width=4)        # Bottom Side

        # Push arrow and label
        line = Line([-4, 2, 0], [-1, 2, 0], color=WHITE, stroke_width=4)
        push_arrow = Arrow([-1, 2.25, 0], [-1, 0, 0], color=WHITE, stroke_width=4)  # Push arrow
        push_label = Text("ITEMS INSERTED", font_size=20).next_to(line, LEFT)

        # Pull arrow and label
        line2 = Line([1, 2, 0], [4, 2, 0], color=WHITE, stroke_width=4).add_tip(tip_length=0.2)
        pull_arrow = Line([1, 2, 0], [1, 0.3, 0], color=WHITE, stroke_width=4)  # Pull arrow
        pull_label = Text("ITEMS DELETED", font_size=20).next_to(line2, RIGHT)
        text3=Text("LIFO:Last in First Outt").scale(0.7)
        text3.to_edge(DOWN)
        # Animate everything using self.play(Create(...))
        # self.play(Create(grid))
        self.play(Create(left_wall), Create(right_wall), Create(bottom))
        self.play(Create(line), Create(push_arrow), Write(push_label))
        self.play(Create(line2), Create(pull_arrow), Write(pull_label))
        self.play(Write(text3))
        self.wait(2)  # Pause for observation

        self.play(FadeOut(left_wall),FadeOut(right_wall),FadeOut(bottom),FadeOut(line),FadeOut(line2),FadeOut(push_arrow),FadeOut(push_label),FadeOut(pull_arrow),FadeOut(pull_label),FadeOut(text4),FadeOut(text3),run_time=1)
        
   
      
        left_wall2 = Line([-2, -3, 0], [-2, 1, 0], color=WHITE, stroke_width=4)   # Left Side
        right_wall2 = Line([2, -3, 0], [2, 1, 0], color=WHITE, stroke_width=4) # Right Side
        
        #stack operation -----------------

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
        


        #Push ---------------------------

        text_push = Text("Push",font="Inter")
        text_push.to_edge(UP)
        self.play(Write(text_push))
        rectangle = Rectangle(height=1, width=4, color=WHITE, fill_opacity=0.5)
        rectangle.move_to(UP*1.5 + LEFT*5)
        rectangle2 = Rectangle(height=1, width=4, color=RED, fill_opacity=0.5)
        rectangle2.move_to(UP*1.5 + LEFT*5)
        rectangle3 = Rectangle(height=1, width=4, color=WHITE, fill_opacity=0.5)
        rectangle3.move_to(UP*1.5 + LEFT*5)
        
        textPushFunctiom=Text("Push() add a item into stack").scale(0.7)
        textPushFunctiom.to_edge(DOWN)

        self.play(Create(left_wall2),Create(right_wall2),Create(bottom))
        
        self.add(rectangle)
        self.play(rectangle.animate.shift(RIGHT*5), run_time=1)
        self.play(rectangle.animate.shift(DOWN*4), run_time=1)
        self.play(FadeIn(rectangle2), run_time=1)
        self.play(rectangle2.animate.shift(RIGHT*5), run_time=1)
        self.play(rectangle2.animate.shift(DOWN*3), run_time=1)
        self.play(FadeIn(rectangle3), run_time=1)
        self.play(rectangle3.animate.shift(RIGHT*5), run_time=1)
        self.play(rectangle3.animate.shift(DOWN*2), run_time=1)
        self.play(Write(textPushFunctiom), run_time=1)
        self.wait(2)
        self.play(FadeOut(left_wall2), FadeOut(right_wall2), FadeOut(bottom), FadeOut(rectangle), FadeOut(rectangle2), FadeOut(rectangle3), FadeOut(textPushFunctiom), FadeOut(text_push), run_time=1)

        #  Pop ---------------------------

        text_pop = Text("Pop()",font="Inter")
        text_pop.to_edge(UP)

        rectanglePop = Rectangle(height=1, width=4, color=WHITE, fill_opacity=0.5)
        rectanglePop.move_to(DOWN*2.5)
        rectanglePop2 = Rectangle(height=1, width=4, color=RED, fill_opacity=0.5)
        rectanglePop2.move_to(DOWN*1.5 )
        rectanglePop3 = Rectangle(height=1, width=4, color=WHITE, fill_opacity=0.5)
        rectanglePop3.move_to(DOWN*.5)

        text_pop_description = Text("Pop(): removes the top item from the stack", font="Inter").scale(0.7)
        text_pop_description.to_edge(DOWN)


        self.play(Create(left_wall2),Create(right_wall2),Create(bottom))
        self.play(Write(text_pop))
        self.add(rectanglePop,rectanglePop2,rectanglePop3)
       
        self.play(rectanglePop3.animate.shift(UP*2), run_time=1)
        self.play(rectanglePop3.animate.shift(RIGHT*4.5), run_time=1)
      
        self.play(rectanglePop2.animate.shift(UP*3), run_time=1)
        self.play(rectanglePop2.animate.shift(RIGHT*4.5), run_time=1)
      
        self.play(rectanglePop.animate.shift(UP*4), run_time=1)
        self.play(rectanglePop.animate.shift(RIGHT*4.5), run_time=1)
        self.play(Write(text_pop_description), run_time=1)
        self.wait(2)

        self.play(FadeOut(left_wall2), FadeOut(right_wall2), FadeOut(bottom), FadeOut(rectanglePop), FadeOut(rectanglePop2), FadeOut(rectanglePop3), FadeOut(text_pop_description), FadeOut(text_pop), run_time=1)