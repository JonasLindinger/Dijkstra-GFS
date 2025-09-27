from manim import *

class DijkstraIntro(Scene):
    def construct(self):
        text = Text("Dijkstra's Algorithm")
        self.play(Write(text))