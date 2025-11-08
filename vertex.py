from manim import *
import math as math
from math import isinf, isnan

class Vertex():
    def __init__(self, name: str, position, color, withDistance: bool):
        # Data
        self.name: str = name
        self.position = position
        self.outgoingEdges: list = []

        # Runtime data that the dijkstra changes
        self.distance = float("inf")
        self.distanceTracker = ValueTracker(float("inf"))
        self.visited: bool = False
        self.previousVertex: Vertex = None

        # Visual (can be ignored)
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

        if (withDistance):
            vertex.add(
                always_redraw(
                    lambda: Text(
                        "∞" if isinf(self.distanceTracker.get_value())
                        else str(round(self.distanceTracker.get_value()))
                        , color=RED
                        , font_size=20 if isinf(self.distanceTracker.get_value())
                        else 16
                    ).move_to(visual.get_center() + DOWN * 0.25, aligned_edge=DOWN)
                )
            )

        return vertex
    
    def UpdateDistance(self, scene: Scene, newDistance: float, liveUpdateVisuals: bool):
        self.distance = newDistance

        if not liveUpdateVisuals: return

        self.distanceTracker.set_value(self.distance)

        return

    def UpdateDistanceAndReturnAnimation(self, newDistance: float, liveUpdateVisuals: bool) -> ValueTracker:
        self.distance = newDistance

        if not liveUpdateVisuals: return None

        return self.distanceTracker
    
    def ResetDistance(self) -> ValueTracker:
        self.distance = float("inf")
        self.previousVertex = None
        self.visited = False

        return self.distanceTracker
