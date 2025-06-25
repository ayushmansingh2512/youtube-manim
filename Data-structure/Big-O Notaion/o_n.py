from manim import *

class MyScene(Scene):
    def construct(self):
        # Set background color to light gray
        self.camera.background_color = "#f0f0EB"  
        text1 = Text("O(n) - Linear time", color='#C96442', font="American Typewriter").scale(0.5)
        text1.to_edge(UL, buff=1)
        text2 = Text("O(n) is linear time that means time increases as the size of the data will increase", color=BLACK, font="American Typewriter").scale(0.3)
        text2.next_to(text1, DOWN, aligned_edge=LEFT)


        self.add(text1)
        self.add(text2)

        arr1 = Text("arr = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]", color='BLACK', font="American Typewriter").scale(0.3)
        arr1.next_to(text2, DOWN, aligned_edge=LEFT)
        target1 = Text("target = 6", color='BLACK', font="American Typewriter").scale(0.3)
        target1.next_to(arr1, DOWN, aligned_edge=LEFT)

        # self.play(Write(arr1))
        # self.play(Write(target1))
        # self.wait()

        self.add(arr1,target1)
         

        arr = [1,2,3,4,5,6,7,8,9]
        target = 6 
        
   

        boxes = VGroup(*[
            Square(side_length=0.5,color='#C96442').shift(RIGHT*i)
            for i in range(len(arr))
            ])
        boxes.arrange(RIGHT,buff=0.2)
        boxes.next_to(target1,DOWN,buff=2,aligned_edge=LEFT)
        
        label = VGroup(*[
            Text(str(val),color=BLACK,font='American Typewriter', font_size=15).move_to(boxes[i])
            for i , val in enumerate(arr)
            ])

        i_label = VGroup(*[
                Text(str(i), color=BLACK , font='American Typewriter' , font_size=14).next_to(boxes[i],DOWN,buff=0.1)
                for i in range(len(arr))
                ]) 
        # self.add(boxes , label, i_label)
        self.play(Create(boxes),Write(label),Write(i_label),run_time=2)

        pointer = Arrow(UP, DOWN, buff=0.1, color='BLACK', tip_length=0.15).scale(0.4)
        pointer_text = Text('6', color='BLACK', font_size=15).next_to(pointer, UP, buff=0.1)

        pointer_group = VGroup(pointer, pointer_text)
        pointer_group.next_to(boxes[0], UP, buff=0.3)
        # self.add(pointer_group)
        # boxes[5].set_fill('#BCD1CA',opacity=1)
        # for i in range(4+1):
        #     boxes[i].set_fill('#CEC6B9',opacity=1)

        # ValueTracker for counting operations
        counter = ValueTracker(0)
        
        # Create a number display
        operation_label = Text("Operations:", font='American Typewriter', color=BLACK).scale(0.3)
        operation_number = DecimalNumber(counter.get_value(), num_decimal_places=0, color=BLACK).scale(0.3)
        # operation_number = Text('6' , color=BLACK).scale(0.3)


        # Positioning the counter display
        operation_label.next_to(boxes, DOWN, buff=1, aligned_edge=LEFT)
        operation_number.next_to(operation_label, RIGHT, buff=0.2)
        
        # Add updater to reflect changing counter value
        operation_number.add_updater(lambda m: m.set_value(counter.get_value()))         
        self.add(operation_label, operation_number)





        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=6,
            y_length=4,
            axis_config={"color": BLACK, "include_ticks": False},
        ).scale(0.7)

        ax.to_edge(UR).shift(DOWN*2.5)

        # Labels
        text = Text("O(n)", color=BLACK).scale(0.5)
        text2 = Text("Data", color=BLACK, font="American Typewriter").scale(0.5)
        text3 = Text("Time", color=BLACK, font="American Typewriter").scale(0.5)

        text2.next_to(ax, DOWN, buff=0.2)
        text3.next_to(ax, LEFT, buff=0.2)

        # Add base elements
        # self.add(ax, text2, text3)
        self.play(Create(ax),Write(text2),Write(text3),run_time=3)
        # ValueTracker for progressive drawing
        i_tracker = ValueTracker(0)

        # Function line (y = x), dynamically updated
        graph = always_redraw(lambda: ax.plot(
            lambda x: x,
            x_range=[0, i_tracker.get_value()],
            # x_range=[0,6],
            color='#D97757'
        ))

        self.add(graph)

         

        found = False
        for i, val in enumerate(arr):
            self.play(
                counter.animate.set_value(i + 1),
                i_tracker.animate.set_value(i + 1),
                run_time=0.4
            )

        
            if i > 0:
                self.play(pointer_group.animate.next_to(boxes[i], UP, buff=0.3), run_time=1)
        
            if val == target:
                self.play(boxes[i].animate.set_fill('#BCD1CA', opacity=1))
                true_text = Text('True', font='American Typewriter', color='BLACK').scale(0.3)
                true_text.next_to(i_label, DOWN, buff=0.3, aligned_edge=LEFT)
                self.play(Write(true_text))
                break
            else:
                self.play(boxes[i].animate.set_fill('#CEC6B9', opacity=1))
        

        self.wait(2)


        target2 = Text("target = 9", color='BLACK', font="American Typewriter").scale(0.3)
        target2.next_to(arr1, DOWN, aligned_edge=LEFT)
        targetk = 9

        self.play(ReplacementTransform(target1,target2)) 

        pointer2 = Arrow(UP, DOWN, buff=0.1, color='BLACK', tip_length=0.15).scale(0.4)
        pointer_text2 = Text('9', color='BLACK', font_size=15).next_to(pointer2, UP, buff=0.1)

        pointer_group2 = VGroup(pointer2, pointer_text2)
        pointer_group2.next_to(boxes[5], UP, buff=0.3)

        self.play(ReplacementTransform(pointer_group,pointer_group2))
        self.wait(3)
        found = False
        for i, val in enumerate(arr[5:], start=5):

            self.play(
                counter.animate.set_value(i + 1),
                i_tracker.animate.set_value(i + 1),
                run_time=0.4
            )
             
            if i > 0:
                self.play(pointer_group2.animate.next_to(boxes[i], UP, buff=0.3), run_time=1)
        
            if val == targetk:
                self.play(boxes[i].animate.set_fill('#BCD1CA', opacity=1))
                true_text = Text('True', font='American Typewriter', color='BLACK').scale(0.3)
                true_text.next_to(i_label, DOWN, buff=0.3, aligned_edge=LEFT)
                self.play(Write(true_text))
                break
            else:
                self.play(boxes[i].animate.set_fill('#CEC6B9', opacity=1))
        

        self.wait(2)
        
