from manim import *
import math as math

class Vertex():
    def __init__(self, name: str, position, color, withDistance: bool):
        self.name: str = name
        self.position = position
        self.distance = float("inf")
        self.visited: bool = False
        self.outgoingEdges: list = []

        self.visual: Group = self.GetVisual(color, withDistance)

    def GetVisual(self, color, withDistance: bool) -> Group:
        # Circle for the vertex
        visual: Circle = Circle(radius=0.75, color=color).move_to(self.position)
    
        # Vertex name text
        text: Text = Text(self.name, color=color, font_size=55)
        text.move_to(visual.get_center())  # center on circle
        if withDistance: text.shift(UP * 0.1)               # shift a bit upward

        # Group them together
        vertex: Group = Group(
            visual,
            text,
        ).scale(0.5)

        return vertex