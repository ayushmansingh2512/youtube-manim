from manim import *

class MyScene(Scene):
    def construct(self):
        # Set background color to light gray
        self.camera.ackground_color = "#f0f0f0"  # light gray
        code = '''
        
        # Linear Search
        class solution():
        def linearSearch(self,nums, k):
            for i in nums:
                if i == k:
                    return True
            return False
    s = solution()
    a = [1,2,3,4,5,6,7,8,9]
    print(s.linearSearch(a,9))
'''

        rendered_code = Code(
            code_string=code,
            language="python",
            background="window",
            background_config={"stroke_color": "white"},
            formatter_style="emacs",



        )
        self.add(rendered_code)