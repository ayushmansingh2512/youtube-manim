from manim import *
import math

class MyScene(Scene):
    def construct(self):
        # Set background color to light gray
        self.camera.background_color = "#f0f0EB"  
        text1 = Text("O(log n) - Logarithmic Time", color='#C96442', font="American Typewriter").scale(0.5)
        text1.to_edge(UL, buff=1)
        text2 = Text("O(log n) means that the time it takes to run the algorithm increases very slowly as the data size grows.", color=BLACK, font="American Typewriter").scale(0.3)
        text2.next_to(text1, DOWN, aligned_edge=LEFT)


        self.add(text1)
        self.add(text2)

        arr1 = Text("arr = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 ]", color='BLACK', font="American Typewriter").scale(0.3)
        arr1.next_to(text2, DOWN, aligned_edge=LEFT)
        target1 = Text("target = 10", color='BLACK', font="American Typewriter").scale(0.3)
        target1.next_to(arr1, DOWN, aligned_edge=LEFT)

        self.add(arr1,target1)
         
        arr = [1,2,3,4,5,6,7,8,9,10,11]
        target = 11
        
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
        self.play(Create(boxes),Write(label),Write(i_label),run_time=2)

        low_pointer = Arrow(UP, DOWN, buff=0.1, color='BLACK', tip_length=0.15).scale(0.4)
        low_text = Text('low', color='BLACK', font_size=15).next_to(low_pointer, UP, buff=0.1)
        low_group = VGroup(low_pointer, low_text)
        low_group.next_to(boxes[0], UP, buff=0.3)

        high_pointer = Arrow(UP, DOWN, buff=0.1, color='BLACK', tip_length=0.15).scale(0.4)
        high_text = Text('high', color='BLACK', font_size=15).next_to(high_pointer, UP, buff=0.1)
        high_group = VGroup(high_pointer, high_text)
        high_group.next_to(boxes[len(arr)-1], UP, buff=0.3)

        mid_pointer = Arrow(UP, DOWN, buff=0.1, color='RED', tip_length=0.15).scale(0.4)
        mid_text = Text('mid', color='RED', font_size=15).next_to(mid_pointer, UP, buff=0.1)
        mid_group = VGroup(mid_pointer, mid_text)
        
        self.play(Create(low_group), Create(high_group))

        counter = ValueTracker(0)
        
        operation_label = Text("Operations:", font='American Typewriter', color=BLACK).scale(0.3)
        operation_number = DecimalNumber(counter.get_value(), num_decimal_places=0, color=BLACK).scale(0.3)

        operation_label.next_to(boxes, DOWN, buff=1, aligned_edge=LEFT)
        operation_number.next_to(operation_label, RIGHT, buff=0.2)
        
        operation_number.add_updater(lambda m: m.set_value(counter.get_value()))         
        self.add(operation_label, operation_number)

        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 4, 1],
            x_length=6,
            y_length=4,
            axis_config={"color": BLACK, "include_ticks": False},
        ).scale(0.7)

        ax.to_edge(UR).shift(DOWN*2.5)

        text2 = Text("Data", color=BLACK, font="American Typewriter").scale(0.5)
        text3 = Text("Time", color=BLACK, font="American Typewriter").scale(0.5)

        text2.next_to(ax, DOWN, buff=0.2)
        text3.next_to(ax, LEFT, buff=0.2)

        self.play(Create(ax),Write(text2),Write(text3),run_time=3)
        
        i_tracker = ValueTracker(0)

        graph = always_redraw(lambda: ax.plot(
            lambda x: math.log2(x) if x > 0 else 0,
            x_range=[0, i_tracker.get_value()],
            color='#D97757'
        ))

        self.add(graph)

        low = 0
        high = len(arr) - 1
        
        while low <= high:
            self.play(
                counter.animate.set_value(counter.get_value() + 1),
                i_tracker.animate.set_value(i_tracker.get_value() + 1),
                run_time=0.4
            )
            mid = (low + high) // 2
            mid_group.next_to(boxes[mid], UP, buff=0.3)
            self.play(Create(mid_group))

            if arr[mid] == target:
                self.play(boxes[mid].animate.set_fill('#BCD1CA', opacity=1))
                true_text = Text('True', font='American Typewriter', color='BLACK').scale(0.3)
                true_text.next_to(i_label[mid], DOWN, buff=0.3)
                self.play(Write(true_text))
                break
            elif arr[mid] < target:
                self.play(boxes[mid].animate.set_fill('#CEC6B9', opacity=1))
                low = mid + 1
                self.play(low_group.animate.next_to(boxes[low], UP, buff=0.3))
            else:
                self.play(boxes[mid].animate.set_fill('#CEC6B9', opacity=1))
                high = mid - 1
                self.play(high_group.animate.next_to(boxes[high], UP, buff=0.3))
            
            self.play(FadeOut(mid_group))

        self.wait(2)
