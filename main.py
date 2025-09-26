import os
from manim import *
from matplotlib import font_manager

def setup():
    register_font(os.path.join("./", "assets", "fonts", "SUSEMono-VariableFont_wght.ttf"))

class HelloWorld(Scene):
    def construct(self):
        # text with custom font VIBGYOR
        setup()    
        font_path = "assets/fonts/SUSEMono-VariableFont_wght.ttf"
        font_name = font_manager.FontProperties(fname=font_path).get_name()
        text = Text("HELLO EVERYNYAN !!!",color=PURPLE,  gradient=(PURPLE, BLUE, GREEN, YELLOW, ORANGE, RED), font=font_name)
        image = ImageMobject(os.path.join("./", "assets", "images", "hello_everynyan.jpg")).scale(5)
        image.to_edge(UP)
        text.next_to(image, DOWN)
        self.add_sound("assets/audio/azumanga-daioh-hello-everynyan.mp3")
        self.play(FadeIn(image), Write(text))
        self.wait(2)