from manim import *
import math as math

class Vertex():
    def __init__(self, name, position, color):
        self.name = name
        self.position = position
        self.visual = self.GetVisual(color)
        self.distance = float("inf")
        self.visited = False
        self.outgoingEdges: list = []

    def GetVisual(self, color) -> Group:
        visual: Circle = Circle(radius=0.75, color=color).move_to(self.position)
        text: Text = Text(self.name, color=color, font_size=75)

        # Center the text on the circle
        text.move_to(visual.get_center())

        # Group them
        vertex: Group = Group(
            visual,
            text
        ).scale(0.5)

        return vertex