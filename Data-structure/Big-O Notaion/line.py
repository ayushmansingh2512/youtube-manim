from manim import *

class LinearSearchLineGraph(Scene):
    def construct(self):
        self.camera.background_color = "#ffffff00"

        ax = Axes(
            x_range=[0, 10,1 ],
            y_range=[0, 10,1],
            x_length=6,
            y_length=4,
            axis_config={"color": BLACK,   "include_ticks": False, }
            )

        # y = x line (linear growth)
        graph = ax.plot(lambda x: x, x_range=[0, 9], color=BLACK)
        text =  Text("O(n)", color=BLACK).scale(0.5)
        text.next_to(graph.get_end(),RIGHT,buff=0.2)
        text2 = Text("Data", color=BLACK,font="American Typewriter").scale(0.5)
        text2.next_to(ax,DOWN,buff=0.2)
        text3 = Text("Time", color=BLACK,font="American Typewriter").scale(0.5)
        text3.next_to(ax,LEFT,buff=0.2)
         

        self.add(ax)
        self.add(text)
        self.add(text2)
        self.add(text3)
        self.add(graph) 

        
