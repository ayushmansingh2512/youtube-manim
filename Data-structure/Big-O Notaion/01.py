from manim import *

class MyScene(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#f0f0EB"

        front = Text(
            '''
      ██████╗     ██╗
     ██╔═══██╗   ███║
     ██║   ██║   ╚██║
     ██║   ██║    ██║
     ╚██████╔╝    ██║
      ╚═════╝     ╚═╝
''',
            color='#C96442',
            font="Courier New"
        )  
        self.wait()
        self.play(Write(front), run_time=5)
        self.wait(3)