from manim import *
import math as math

class Vertex():
    def __init__(self, name: str, position, color, withDistance: bool):
        # Data
        self.name: str = name
        self.position = position
        self.outgoingEdges: list = []

        # Runtime data that the dijkstra changes
        self.distance = float("inf")
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

        return vertex
    
    def UpdateDistance(self, scene: Scene, newDistance: float, liveUpdateVisuals: bool):
        self.distance = newDistance

        if not liveUpdateVisuals: return

        if len(self.visual) != 4: return
        old_text: Text = self.visual[3]
        new_text: Text = Text(str(newDistance), color=old_text[0].get_fill_color(), font_size=18).move_to(old_text)
        scene.play(
            Transform(old_text, new_text),
            run_time=1
        )
        old_text = new_text

    def UpdateDistanceAndReturnAnimation(self, scene: Scene, newDistance: float, liveUpdateVisuals: bool) -> tuple[Transform, Text, Text]:
        self.distance = newDistance

        if not liveUpdateVisuals: return

        if len(self.visual) != 4: return
        old_text: Text = self.visual[3]
        new_text: Text = Text(str(newDistance), color=old_text[0].get_fill_color(), font_size=18).move_to(old_text)

        return (Transform(old_text, new_text), old_text, new_text)
    
    def ResetDistance(self, scene: Scene) -> Transform:
        self.distance = float("inf")

        old_text: Text = self.visual[3]
        new_text: Text = Text("∞", color=old_text[0].get_fill_color(), font_size=18).move_to(old_text)

        return Transform(old_text, new_text)