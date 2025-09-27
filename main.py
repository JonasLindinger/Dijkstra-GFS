from manim import *

class DijkstraIntro(Scene):
    def construct(self):
        # Show topic
        title = Text("Dijkstra Algorithmus").scale(1.5)
        self.play(Write(title, run_time=2))
        
        titleAnimation = AnimationGroup(
            title.animate
            .scale(0.7)
            .move_to([-3.2, 3, 0]),
        )

        self.play(titleAnimation)

        underline = Underline(title, buff=0)

        self.play(Write(underline, run_time=.5))

        # Show content
        first = Text("1. Was macht der Dijkstra Algorithmus?").scale(.5).move_to([-3.2, 2, 0])

        contentGroup = AnimationGroup(
            Write(first, run_time=1),
        )

        self.play(contentGroup)
        self.wait(5)