from vertex import *

class Edge():
    def __init__(self, start: Vertex, to: Vertex, weight: float, color):
        self.start = start
        self.to = to
        self.weight = weight
        self.visual = self.GetVisual(color)

        # Add this edge as a connected Edge to the vertices
        start.outgoingEdges.append(self)
    
    # -- AI GENERATED METHOD! -- and a bit of me : )
    def GetVisual(self, color) -> VGroup:
        circle1 = self.start.visual[0]
        circle2 = self.to.visual[0]

        # Get actual scaled radius
        radius1 = circle1.width / 2
        radius2 = circle2.width / 2

        # Vector from circle1 to circle2
        direction = circle2.get_center() - circle1.get_center()
        distance = np.linalg.norm(direction)
        direction_norm = direction / distance

        # Start and end points exactly at the edge of the scaled circles
        start = circle1.get_center() + direction_norm * radius1
        end = circle2.get_center() - direction_norm * radius2

        # Create arrow
        arrow = Arrow(
            start=start,
            end=end,
            buff=0,       # no extra padding
            tip_length=0.2,  # optional, adjust tip size
            color=color
        )

        # Create weight text
        mid_point = (start + end) / 2
        perp = np.array([-direction_norm[1], direction_norm[0], 0])  # perpendicular
        offset = perp * 0.2
        weight_text = Text(str(self.weight), font_size=24).move_to(mid_point + offset)

        return VGroup(arrow, weight_text)