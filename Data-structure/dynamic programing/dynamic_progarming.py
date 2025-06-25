from manim import *

# Set background color
config.background_color = "#f2f3f5"

# 🔷 Custom class for the screen border
class ScreenBorder(RoundedRectangle):
    def __init__(self, color="#0a4ca8", stroke_width=3, corner_radius=0.4, **kwargs):
        super().__init__(
            width=config.frame_width * 0.91,
            height=config.frame_height * 0.91,
            corner_radius=corner_radius,
            stroke_color=color,
            stroke_width=stroke_width,
            fill_opacity=0,
            **kwargs
        )
        self.move_to(ORIGIN)

# 🔷 Main scene class
class DefineDynamicProgramming(Scene):
    def construct(self):
        # Text with custom font and gradient
        text = Text(
            "Dynamic Programming",
            font="Rejouice Headline",
            font_size=34
        )
        text.set_color_by_gradient(BLACK, "#0a4ca8")
        text.move_to(ORIGIN)

        # Add the custom border
        border = ScreenBorder()
        self.play(Create(border) , Write(text))
      #  self.add(border,text)
        


class ShrinkAndMoveText(Scene):
    def construct(self):
        # Recreate the text (must match exactly)
        text = Text(
            "Dynamic Programming",
            font="Rejouice Headline",
            font_size=34
        )
        text.set_color_by_gradient(BLACK, "#0a4ca8")
        text.move_to(ORIGIN)

        border = ScreenBorder()

        self.add(border, text)

        # Animate shrinking and moving the text
        self.play(
            text.animate.scale(0.5).to_edge(UP).shift(DOWN * 0.3),
            run_time=1.5
        )
        self.wait()



class DefineDPExplanation(Scene):
    def construct(self):
        # Header text (shrunk and positioned at the top)
        heading = Text(
            "Dynamic Programming",
            font="Rejouice Headline",
            font_size=34
        )
        heading.set_color_by_gradient(BLACK, "#0a4ca8")
        heading.scale(0.5).to_edge(UP).shift(DOWN * 0.3)

        # Definition with colored keywords
        definition = (
            "Dynamic Programming is a method for solving complex problems by\n"
            "breaking them down into simpler <span fgcolor=\"#689ded\">sub-problems</span>\n"
            "and storing the results to avoid redundant computation. This is called\n"
            "<span fgcolor=\"#689ded\">memoization</span>."
        )
        # Create the paragraph and color key terms
        para = MarkupText(
            definition,
            font="Poppins",
            font_size=28,
            color=BLACK,
            line_spacing=1.5
        )
        para.set_opacity(0.85)
        para.set_width(config.frame_width * 0.7)
        para.next_to(heading, DOWN, buff=0.8)
        para.scale(1.1)

        # Color the key terms
      

        border = ScreenBorder()

        self.add(border, heading)
        self.play(Write(para), run_time=5)
        self.play(FadeOut(para))
        self.wait()
        



class CoinSwitch(Scene):
    def construct(self):
        # Header text
        heading = Text(
            "Dynamic Programming",
            font="Rejouice Headline",
            font_size=34
        )
        heading.set_color_by_gradient(BLACK, "#0a4ca8")
        heading.scale(0.5).to_edge(UP).shift(DOWN * 0.3)

        # Sub-header text
        q = Text(
            "Coin Switch",
            font="Rejouice Headline",
            font_size=34
        )
        q.set_color_by_gradient(BLACK, "#0a4ca8")
        q.scale(0.5).to_edge(UL).shift(DOWN * 0.8).shift(LEFT * -0.4)

        # Problem definition
        definition = (
            "You are given an integer array <span fgcolor=\"#689ded\">coins</span> representing coins of different denominations and "
            "an integer amount representing a total <span fgcolor=\"#689ded\">amount</span> of money.\n"
            "\nReturn the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return <span fgcolor=\"#689ded\">-1</span>.\n"
            "\nYou may assume that you have an infinite number of each kind of coin."
        )

        para = MarkupText(
            definition,
            font="Poppins",
            font_size=28,
            color=BLACK,
            line_spacing=2
        )
        para.set_opacity(0.85)
        para.set_width(config.frame_width * 0.7)
        para.next_to(heading, DOWN, buff=0.8)
        para.scale(1.1)

        # Remove this or update keywords if necessary
        # para.set_color_by_text_to_color_map({
        #     "memoization": "#689ded",
        #     "sub-problems": "#689ded"
        # })

        border = ScreenBorder()

        self.add(border, heading)
        self.play(Write(q))
        self.play(Write(para), run_time=7)
        self.wait(1)
        
        
        code_string = (
            "class <span fgcolor=\"#689ded\">Soluton</span>\n"
            "\n def coinChange (self , coins ,amount)\n"
            "\n     dp[0] = 0\n"
            "\n       for i in range(1,amount+1):\n"
            "\n            for c in coins:\n"
            "\n                if (i-c) >= 0:\n"
            "\n                    dp[i] = min(dp[i],1+ dp[i -c])\n"
            "\n     return dp[amount] if (dp[amount] != amount+1) else -1\n"
            "\nprint(coinChange([1, 2, 5], 11))  # Output: 3 (5 + 5 + 1)\n"
        
          )

        code = MarkupText(
                code_string,
                tab_width=4,
                color=BLACK, 
                font="Fira Code",
                line_spacing=2,
                font_size=28
              )
        code.set_opacity(0.85)
        code.scale(0.4)  # Scale first!
        code.to_edge(RIGHT, buff=1)  # Then move to edge
        code.shift(DOWN * 0.4)


        self.play(Write(code), run_time=3)
        self.wait(1)
      #  self.add(code)

        boxes = VGroup()  # Group to store all boxes

        for i in range(12):  # Create 12 boxes
            # Create a rounded rectangle box
            box = RoundedRectangle(
                corner_radius=0.6,
                height=0.6,
                width=0.6,
                stroke_color="#689ded",
                stroke_width=2,
                fill_color=WHITE,
                fill_opacity=1
            )

            # Text inside the box (value)
            number_text = Text("12", font_size=16, color=BLACK)
            number_text.move_to(box.get_center())

            # Index text at the top of box
            index_text = Text(str(i), font_size=16, color=BLACK)
            index_text.next_to(box, UP, buff=0.1)

            # Group box and texts
            single_box = VGroup(box, number_text, index_text)

            # Position horizontally
            single_box.shift(RIGHT * i * 1.4)  # Adjust spacing

            boxes.add(single_box)

        # Center and scale if needed
        boxes.arrange(RIGHT, buff=0.4).to_edge(DOWN)

        self.play(FadeIn(boxes, lag_ratio=0.1), run_time=5)
        self.wait()     
        self.play(FadeOut(boxes))
        self.wait(2)


from manim import *

class CoinSwitch2(Scene):
    def construct(self):
        # Header
        heading = Text("Dynamic Programming", font="Rejouice Headline", font_size=34)
        heading.set_color_by_gradient(BLACK, "#0a4ca8")
        heading.scale(0.5).to_edge(UP).shift(DOWN * 0.3)

        # Sub-header
        q = Text("Coin Switch", font="Rejouice Headline", font_size=34)
        q.set_color_by_gradient(BLACK, "#0a4ca8")
        q.scale(0.5).to_edge(UL).shift(DOWN * 0.8).shift(LEFT * -0.4)

        # Problem text
        definition = (
            "You are given an integer array <span fgcolor=\"#689ded\">coins</span> representing coins of different denominations and "
            "an integer amount representing a total <span fgcolor=\"#689ded\">amount</span> of money.\n"
            "\nReturn the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return <span fgcolor=\"#689ded\">-1</span>.\n"
            "\nYou may assume that you have an infinite number of each kind of coin."
        )
        para = MarkupText(definition, font="Poppins", font_size=28, color=BLACK, line_spacing=2)
        para.set_opacity(0.85)
        para.set_width(config.frame_width * 0.7)
        para.next_to(heading, DOWN, buff=0.8)
        para.scale(1.1)

        # Code (static)
        code_string = (
            "class <span fgcolor=\"#689ded\">Soluton</span>\n"
            "\n def coinChange (self , coins ,amount)\n"
            "\n     dp[0] = 0\n"
            "\n       for i in range(1,amount+1):\n"
            "\n            for c in coins:\n"
            "\n                if (i-c) >= 0:\n"
            "\n                    dp[i] = min(dp[i],1+ dp[i -c])\n"
            "\n     return dp[amount] if (dp[amount] != amount+1) else -1\n"
            "\nprint(coinChange([1, 2, 5], 11))  # Output: 3 (5 + 5 + 1)\n"
        
          )
        code = MarkupText(code_string, color=BLACK, font="Fira Code", font_size=28, line_spacing=2)
        code.set_opacity(0.85)
        code.scale(0.4)
        code.to_edge(RIGHT, buff=1).shift(DOWN * 0.4)

        self.add(ScreenBorder(), heading, q, para, code)

        # 🧮 Logic to compute dp array
        def coinChange(coins, amount):
            dp = [amount + 1] * (amount + 1)
            dp[0] = 0
            for i in range(1, amount + 1):
                for c in coins:
                    if i - c >= 0:
                        dp[i] = min(dp[i], 1 + dp[i - c])
            return dp

        coins = [1, 2, 5]
        amount = 11
        dp = coinChange(coins, amount)

        # Draw boxes with dp[i] values
        boxes = VGroup()
        for i in range(amount + 1):
            box = RoundedRectangle(
                corner_radius=0.6,
                height=0.6,
                width=0.6,
                stroke_color="#689ded",
                stroke_width=2,
                fill_color=WHITE,
                fill_opacity=1
            )
            value_text = Text(str(dp[i]), font_size=16, color=BLACK).move_to(box.get_center())
            index_text = Text(str(i), font_size=16, color=BLACK).next_to(box, UP, buff=0.1)

            single_box = VGroup(box, value_text, index_text)
            single_box.shift(RIGHT * i * 1.2)
            boxes.add(single_box)

        boxes.arrange(RIGHT, buff=0.4).to_edge(DOWN)
        self.play(FadeIn(boxes, lag_ratio=0.1), run_time=3)
        self.wait(2)



